import entities as ent


class Notifier:
    """
    Base class- implements all to notify condition check.
    New notifier conditions can be added here to all notifiers that inherit from Notifier class.
    To ignore checks, we'll need to implement it individually in our derived notifier class.
    """

    def __init__(self, entity_obj, original_entity_obj, entity_type):
        self.entity_obj = entity_obj
        self.original_entity_obj = original_entity_obj
        self.entity_type = entity_type
        self.set_notify_entity()

    # New object
    def check_new_entity(self):
        if self.original_entity_obj is None:
            return True
        return False

    # Physically deleted object
    def check_deleted_entity(self):
        if self.entity_obj is None:
            return True
        return False

    # Check is_deleted parameter
    def check_is_deleted(self):
        if self.original_entity_obj.is_deleted != self.entity_obj.is_deleted:
            return True
        return False

    # Check is_blacklisted parameter
    def check_if_blacklisted(self):
        if self.entity_obj.is_blacklisted != self.original_entity_obj.is_blacklisted:
            return True
        return False

    # Check crawling status
    def check_crawling_status(self):
        if self.original_entity_obj.crawling_status != self.entity_obj.crawling_status \
                and (
                self.original_entity_obj.crawling_status == ent.CRAWLING_STATUSES.TEXT_ANALYZED or
                self.original_entity_obj.crawling_status == ent.CRAWLING_STATUSES.TEXT_UPLOADED):
            return True
        return False

    # Entity to be notified on
    def set_notify_entity(self):
        if self.entity_obj is not None:
            self.notified_entity_name = self.entity_obj.name
        else:
            self.notified_entity_name = self.original_entity_obj.name

    # Getter for notified entity name
    def notified_entity(self):
        return self.notified_entity_name

    # Main function to calculate notify conditions
    def notify(self):
        notify = False
        if self.check_new_entity():
            notify = True
        elif self.check_deleted_entity():
            notify = True
        elif self.check_is_deleted() or self.check_if_blacklisted() or self.check_crawling_status():
            notify = True

        if notify:
            print(f"Notify On {self.notified_entity()}")

    notified_entity_name = ""


# For Company
class CompanyNotifier(Notifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # No need to check
    def check_if_blacklisted(self):
        return False


# For Event
class EventNotifier(Notifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# For Webinar
class WebinarNotifier(Notifier):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# For ContentItem
class ContentItemNotifier(Notifier):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Content Item company needs to be notified
    def set_notify_entity(self):
        if self.entity_obj is not None:
            self.notified_entity_name = self.entity_obj.company.name
        else:
            self.notified_entity_name = self.original_entity_obj.company.name


# For CompanyForEvent
class CompanyForEventNotifier(Notifier):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Company For Event's event needs to be notified
    def set_notify_entity(self):
        if self.entity_obj is not None:
            self.notified_entity_name = self.entity_obj.event.name
        else:
            self.notified_entity_name = self.original_entity_obj.event.name

    # No need to check
    def check_crawling_status(self):
        return False


# For CompanyCompetitor
class CompanyCompetitorNotifier(Notifier):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Company Competitor's company needs to be notified
    def set_notify_entity(self):
        if self.entity_obj is not None:
            self.notified_entity_name = self.entity_obj.company.name
        else:
            self.notified_entity_name = self.original_entity_obj.company.name

    # No need to check
    def check_crawling_status(self):
        return False

    # No need to check
    def check_if_blacklisted(self):
        return False


# For CompanyForWebinar
class CompanyForWebinarNotifier(Notifier):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Company For Webinar's webinar needs to be notified
    def set_notify_entity(self):
        if self.entity_obj is not None:
            self.notified_entity_name = self.entity_obj.webinar.name
        else:
            self.notified_entity_name = self.original_entity_obj.webinar.name

    # No need to check
    def check_crawling_status(self):
        return False
