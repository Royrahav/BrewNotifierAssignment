import entities as ent


class Notifier:
    def __init__(self, entity_obj, original_entity_obj, entity_type):
        self.entity_obj = entity_obj
        self.original_entity_obj = original_entity_obj
        self.entity_type = entity_type
        self.set_notify_entity()

    def check_new_entity(self):
        if self.original_entity_obj is None:
            return True
        return False

    def check_deleted_entity(self):
        if self.entity_obj is None:
            return True
        return False

    def check_is_deleted(self):
        if self.original_entity_obj.is_deleted != self.entity_obj.is_deleted:
            return True
        return False

    def check_if_blacklisted(self):
        if self.entity_obj.is_blacklisted != self.original_entity_obj.is_blacklisted:
            return True
        return False

    def check_crawling_status(self):
        if self.original_entity_obj.crawling_status != self.entity_obj.crawling_status \
                and (
                self.original_entity_obj.crawling_status == ent.CRAWLING_STATUSES.TEXT_ANALYZED or
                self.original_entity_obj.crawling_status == ent.CRAWLING_STATUSES.TEXT_UPLOADED):
            return True
        return False

    def set_notify_entity(self):
        if self.entity_obj is not None:
            self.notified_entity_name = self.entity_obj.name
        else:
            self.notified_entity_name = self.original_entity_obj.name

    def notified_entity(self):
        return self.notified_entity_name

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


class CompanyNotifier(Notifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def check_if_blacklisted(self):
        return False


class EventNotifier(Notifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WebinarNotifier(Notifier):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ContentItemNotifier(Notifier):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_notify_entity(self):
        if self.entity_obj is not None:
            self.notified_entity_name = self.entity_obj.company.name
        else:
            self.notified_entity_name = self.original_entity_obj.company.name


class CompanyForEventNotifier(Notifier):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_notify_entity(self):
        if self.entity_obj is not None:
            self.notified_entity_name = self.entity_obj.event.name
        else:
            self.notified_entity_name = self.original_entity_obj.event.name

    def check_crawling_status(self):
        return False


class CompanyCompetitorNotifier(Notifier):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_notify_entity(self):
        if self.entity_obj is not None:
            self.notified_entity_name = self.entity_obj.company.name
        else:
            self.notified_entity_name = self.original_entity_obj.company.name

    def check_crawling_status(self):
        return False

    def check_if_blacklisted(self):
        return False


class CompanyForWebinarNotifier(Notifier):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def set_notify_entity(self):
        if self.entity_obj is not None:
            self.notified_entity_name = self.entity_obj.webinar.name
        else:
            self.notified_entity_name = self.original_entity_obj.webinar.name

    def check_crawling_status(self):
        return False
