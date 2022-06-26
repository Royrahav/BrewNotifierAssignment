import entities as ent
import notifier as noti
from datetime import datetime

# date time to use in tests
custom_date_time = datetime(2022, 6, 25)
google_company = ent.Company(link="link", name="Google", employees_min=50, employees_max=1000)
apple_company = ent.Company(link="link", name="Apple", employees_min=50, employees_max=1000)
comiccon_event = ent.Event(link="link", name="Comic-con", start_date=custom_date_time)
webinar_ent = ent.Webinar(link="link", name="Webinar of All Webinars", start_date=custom_date_time)


def test(entity, entity_name, functionality, expect, notify_on):
    print("-----------------------------------")
    print(f"We test entity: {entity.entity_type}")
    print(f"Notified entity's name: {entity_name}")
    print(f"Checking functionality: {functionality}")
    print(f"We expect that: {expect}")
    print(f"Should notify on: {notify_on}")
    print("\n\n")
    print("Result: \n")
    entity.notify()
    separate_test()


def separate_test():
    print("-----------------------------------")
    print("\n\n\n")


def print_astrix(text):
    print(
        f"**************************************************** {text} ****************************************************")


def test_company():
    ''' Test Company: Constructor: self, *, link, name, crawling_status=CRAWLING_STATUSES.NOT_CRAWLED,
    is_deleted=False, is_blacklisted=False, last_crawled=None, employees_min, employees_max
    '''
    print_astrix("Now testing Company")
    company1 = ent.Company(link="link", name="Microsoft", employees_min=50, employees_max=100)
    company2 = ent.Company(link="link", name="Microsoft", employees_min=50, employees_max=100)
    company_notifier_new_obj = noti.CompanyNotifier(entity_obj=company1, original_entity_obj=None,
                                                    entity_type="Company")
    company_notifier_deleted_obj = noti.CompanyNotifier(entity_obj=None, original_entity_obj=company2,
                                                        entity_type="Company")
    company_notifier_obj = noti.CompanyNotifier(entity_obj=company1, original_entity_obj=company2,
                                                entity_type="Company")

    # Test new object notify
    test(company_notifier_new_obj, "Microsoft", "new object", "To notify on", "itself")

    # Test deleted object notify
    test(company_notifier_deleted_obj, "Microsoft", "deleted object", "To notify on", "itself")

    # Test no change in object
    test(company_notifier_obj, "Microsoft", "no change in object", "Empty result (no notify)", "itself")

    # Test is_deleted object notify
    company2.is_deleted = True
    test(company_notifier_obj, "Microsoft", "update is_deleted", "To notify on", "itself")
    company2.is_deleted = False

    # Test change crawl status object notify TEXT_UPLOADED
    company2.crawling_status = ent.CRAWLING_STATUSES.TEXT_UPLOADED
    test(company_notifier_obj, "Microsoft", "update crawling_status to TEXT_UPLOADED", "To notify on", "itself")
    company2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change crawl status object notify TEXT_ANALYZED
    company2.crawling_status = ent.CRAWLING_STATUSES.TEXT_ANALYZED
    test(company_notifier_obj, "Microsoft", "update crawling_status to TEXT_ANALYZED", "To notify on", "itself")
    company2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change is_blacklisted object notify
    company2.is_blacklisted = True
    test(company_notifier_obj, "Microsoft", "update is_black_listed", "Empty result (no notify)", "itself")
    company2.is_blacklisted = False
    print_astrix("End of testing company")
    print("\n\n\n")


def test_event():
    ''' Test event: Constructor: self, *, link, name, crawling_status=CRAWLING_STATUSES.NOT_CRAWLED,
    is_deleted=False, is_blacklisted=False, last_crawled=None, start_date, description=None, location=None,
    end_date=None, **kwargs
    '''
    print_astrix("Now testing Event")
    event1 = ent.Event(link="link", name="Hackathon", start_date=custom_date_time)
    event2 = ent.Event(link="link", name="Hackathon", start_date=custom_date_time)
    event_notifier_new_obj = noti.EventNotifier(entity_obj=event1, original_entity_obj=None,
                                                entity_type="Event")
    event_notifier_deleted_obj = noti.EventNotifier(entity_obj=None, original_entity_obj=event2,
                                                    entity_type="Event")
    event_notifier_obj = noti.EventNotifier(entity_obj=event1, original_entity_obj=event2,
                                            entity_type="Event")

    # Test new object notify
    test(event_notifier_new_obj, "Hackathon", "new object", "To notify on", "itself")

    # Test deleted object notify
    test(event_notifier_deleted_obj, "Hackathon", "deleted object", "To notify on", "itself")

    # Test no change in object
    test(event_notifier_obj, "Hackathon", "no change in object", "Empty result (no notify)", "itself")

    # Test is_deleted object notify
    event2.is_deleted = True
    test(event_notifier_obj, "Hackathon", "update is_deleted", "To notify on", "itself")
    event2.is_deleted = False

    # Test change crawl status object notify TEXT_UPLOADED
    event2.crawling_status = ent.CRAWLING_STATUSES.TEXT_UPLOADED
    test(event_notifier_obj, "Hackathon", "update crawling_status to TEXT_UPLOADED", "To notify on", "itself")
    event2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change crawl status object notify TEXT_ANALYZED
    event2.crawling_status = ent.CRAWLING_STATUSES.TEXT_ANALYZED
    test(event_notifier_obj, "Hackathon", "update crawling_status to TEXT_ANALYZED", "To notify on", "itself")
    event2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change is_blacklisted object notify
    event2.is_blacklisted = True
    test(event_notifier_obj, "Hackathon", "update is_black_listed", "To notify on", "itself")
    event2.is_blacklisted = False
    print_astrix("End of testing Event")
    print("\n\n\n")


def test_webinar():
    ''' Test test_webinar: Constructor: self, *, link, name, crawling_status=CRAWLING_STATUSES.NOT_CRAWLED,
    is_deleted=False, is_blacklisted=False, last_crawled=None, start_date, description=None, language="en", **kwargs
    '''
    print_astrix("Now testing Webinar")
    webinar1 = ent.Webinar(link="link", name="Webinar World", start_date=custom_date_time)
    webinar2 = ent.Webinar(link="link", name="Webinar World", start_date=custom_date_time)
    webinar_notifier_new_obj = noti.WebinarNotifier(entity_obj=webinar1, original_entity_obj=None,
                                                    entity_type="Webinar")
    webinar_notifier_deleted_obj = noti.WebinarNotifier(entity_obj=None, original_entity_obj=webinar2,
                                                        entity_type="Webinar")
    webinar_notifier_obj = noti.WebinarNotifier(entity_obj=webinar1, original_entity_obj=webinar2,
                                                entity_type="Webinar")

    # Test new object notify
    test(webinar_notifier_new_obj, "Webinar World", "new object", "To notify on", "itself")

    # Test deleted object notify
    test(webinar_notifier_deleted_obj, "Webinar World", "deleted object", "To notify on", "itself")

    # Test no change in object
    test(webinar_notifier_obj, "Webinar World", "no change in object", "Empty result (no notify)", "itself")

    # Test is_deleted object notify
    webinar2.is_deleted = True
    test(webinar_notifier_new_obj, "Webinar World", "update is_deleted", "To notify on", "itself")
    webinar2.is_deleted = False

    # Test change crawl status object notify TEXT_UPLOADED
    webinar2.crawling_status = ent.CRAWLING_STATUSES.TEXT_UPLOADED
    test(webinar_notifier_new_obj, "Webinar World", "update crawling_status to TEXT_UPLOADED", "To notify on", "itself")
    webinar2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change crawl status object notify TEXT_ANALYZED
    webinar2.crawling_status = ent.CRAWLING_STATUSES.TEXT_ANALYZED
    test(webinar_notifier_new_obj, "Webinar World", "update crawling_status to TEXT_ANALYZED", "To notify on", "itself")
    webinar2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change is_blacklisted object notify
    webinar2.is_blacklisted = True
    test(webinar_notifier_new_obj, "Webinar World", "update is_black_listed", "To notify on", "itself")
    webinar2.is_blacklisted = False
    print_astrix("End of testing Webinar")
    print("\n\n\n")


def test_content_item():
    ''' Test test_content_item: Constructor: self, *, link, name, crawling_status=CRAWLING_STATUSES.NOT_CRAWLED,
    is_deleted=False, is_blacklisted=False, last_crawled=None, company, snippet=None, **kwargs
    '''
    print_astrix("Now testing Content Item")
    content_item1 = ent.ContentItem(link="link", name="Google's Content", company=google_company)
    content_item2 = ent.ContentItem(link="link", name="Google's Content", company=google_company)
    content_item_notifier_new_obj = noti.ContentItemNotifier(entity_obj=content_item1, original_entity_obj=None,
                                                             entity_type="ContentItem")
    content_item_notifier_deleted_obj = noti.ContentItemNotifier(entity_obj=None, original_entity_obj=content_item2,
                                                                 entity_type="ContentItem")
    content_item_notifier_obj = noti.ContentItemNotifier(entity_obj=content_item1, original_entity_obj=content_item2,
                                                         entity_type="ContentItem")

    # Test new object notify
    test(content_item_notifier_new_obj, "Google", "new object", "To notify on", "Company's name")

    # Test deleted object notify
    test(content_item_notifier_deleted_obj, "Google", "deleted object", "To notify on", "Company's name")

    # Test no change in object
    test(content_item_notifier_obj, "Google", "no change in object", "Empty result (no notify)", "Company's name")

    # Test is_deleted object notify
    content_item2.is_deleted = True
    test(content_item_notifier_obj, "Google", "update is_deleted", "To notify on", "Company's name")
    content_item2.is_deleted = False

    # Test change crawl status object notify TEXT_UPLOADED
    content_item2.crawling_status = ent.CRAWLING_STATUSES.TEXT_UPLOADED
    test(content_item_notifier_obj, "Google", "update crawling_status to TEXT_UPLOADED", "To notify on",
         "Company's name")
    content_item2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change crawl status object notify TEXT_ANALYZED
    content_item2.crawling_status = ent.CRAWLING_STATUSES.TEXT_ANALYZED
    test(content_item_notifier_obj, "Google", "update crawling_status to TEXT_ANALYZED", "To notify on",
         "Company's name")
    content_item2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change is_blacklisted object notify
    content_item2.is_blacklisted = True
    test(content_item_notifier_obj, "Google", "update is_black_listed", "To notify on", "Company's name")
    content_item2.is_blacklisted = False
    print_astrix("End of testing Content Item")
    print("\n\n\n")


def test_company_for_event():
    ''' Test test_company_for_event: Constructor: event, company, is_deleted=False, is_blacklisted=False
    '''
    print_astrix("Now testing Company For Event")
    company_for_event1 = ent.CompanyForEvent(company=google_company,
                                             event=comiccon_event)
    company_for_event2 = ent.CompanyForEvent(company=google_company,
                                             event=comiccon_event)
    company_for_event_notifier_new_obj = noti.CompanyForEventNotifier(entity_obj=company_for_event1,
                                                                      original_entity_obj=None,
                                                                      entity_type="CompanyForEvent")
    company_for_event_notifier_deleted_obj = noti.CompanyForEventNotifier(entity_obj=None,
                                                                          original_entity_obj=company_for_event2,
                                                                          entity_type="CompanyForEvent")
    company_for_event_notifier_obj = noti.CompanyForEventNotifier(entity_obj=company_for_event1,
                                                                  original_entity_obj=company_for_event2,
                                                                  entity_type="CompanyForEvent")

    # Test new object notify
    test(company_for_event_notifier_new_obj, "Comic-con", "new object", "To notify on", "Event's name")

    # Test deleted object notify
    test(company_for_event_notifier_deleted_obj, "Comic-con", "deleted object", "To notify on", "Event's name")

    # Test no change in object
    test(company_for_event_notifier_obj, "Comic-con", "no change in object", "Empty result (no notify)", "Event's name")

    # Test is_deleted object notify
    company_for_event2.is_deleted = True
    test(company_for_event_notifier_obj, "Comic-con", "update is_deleted", "To notify on", "Event's name")
    company_for_event2.is_deleted = False

    # Test change crawl status object notify TEXT_UPLOADED
    company_for_event2.crawling_status = ent.CRAWLING_STATUSES.TEXT_UPLOADED
    test(company_for_event_notifier_obj, "Comic-con", "update crawling_status to TEXT_UPLOADED", "Empty result (no "
                                                                                                 "notify)",
         "Event's name")
    company_for_event2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change crawl status object notify TEXT_ANALYZED
    company_for_event2.crawling_status = ent.CRAWLING_STATUSES.TEXT_ANALYZED
    test(company_for_event_notifier_obj, "Comic-con", "update crawling_status to TEXT_ANALYZED", "Empty result (no "
                                                                                                 "notify)",
         "Event's name")
    company_for_event2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change is_blacklisted object notify
    company_for_event2.is_blacklisted = True
    test(company_for_event_notifier_obj, "Comic-con", "update is_black_listed", "To notify on", "Event's name")
    company_for_event2.is_blacklisted = False
    print_astrix("End of testing Company For Event")
    print("\n\n\n")


def test_company_competitor():
    ''' Test test_company_competitor: Constructor: company, competitor, is_deleted=False
    '''
    print_astrix("Now testing Company Competitor")
    company_competitor1 = ent.CompanyCompetitor(competitor=apple_company,
                                                company=google_company)
    company_competitor2 = ent.CompanyCompetitor(competitor=apple_company,
                                                company=google_company)
    company_competitor_notifier_new_obj = noti.CompanyCompetitorNotifier(entity_obj=company_competitor1,
                                                                         original_entity_obj=None,
                                                                         entity_type="CompanyCompetitor")
    company_competitor_notifier_deleted_obj = noti.CompanyCompetitorNotifier(entity_obj=None,
                                                                             original_entity_obj=company_competitor2,
                                                                             entity_type="CompanyCompetitor")
    company_competitor_notifier_obj = noti.CompanyCompetitorNotifier(entity_obj=company_competitor1,
                                                                     original_entity_obj=company_competitor2,
                                                                     entity_type="CompanyCompetitor")

    # Test new object notify
    test(company_competitor_notifier_new_obj, "Google", "new object", "To notify on", "Company's name")

    # Test deleted object notify
    test(company_competitor_notifier_deleted_obj, "Google", "deleted object", "To notify on", "Company's name")

    # Test no change in object
    test(company_competitor_notifier_obj, "Google", "no change in object", "Empty result (no notify)", "Company's name")

    # Test is_deleted object notify
    company_competitor2.is_deleted = True
    test(company_competitor_notifier_obj, "Google", "update is_deleted", "To notify on", "Company's name")
    company_competitor2.is_deleted = False

    # Test change crawl status object notify TEXT_UPLOADED
    company_competitor2.crawling_status = ent.CRAWLING_STATUSES.TEXT_UPLOADED
    test(company_competitor_notifier_obj, "Google", "update crawling_status to TEXT_UPLOADED", "Empty result (no "
                                                                                               "notify)",
         "Company's name")
    company_competitor2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change crawl status object notify TEXT_ANALYZED
    company_competitor2.crawling_status = ent.CRAWLING_STATUSES.TEXT_ANALYZED
    test(company_competitor_notifier_obj, "Google", "update crawling_status to TEXT_ANALYZED", "Empty result (no "
                                                                                               "notify)",
         "Company's name")
    company_competitor2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change is_blacklisted object notify
    company_competitor2.is_blacklisted = True
    test(company_competitor_notifier_obj, "Google", "update is_black_listed", "Empty result (no notify)",
         "Company's name")
    company_competitor2.is_blacklisted = False
    print_astrix("End of testing Company Competitor")
    print("\n\n\n")


def test_company_for_webinar():
    ''' Test test_company_for_webinar: Constructor: webinar, company, is_deleted=False, is_blacklisted=False
    '''
    print_astrix("Now testing Company For Webinar")
    company_for_webinar1 = ent.CompanyForWebinar(webinar=webinar_ent,
                                                 company=google_company)
    company_for_webinar2 = ent.CompanyForWebinar(webinar=webinar_ent,
                                                 company=google_company)
    company_for_webinar_notifier_new_obj = noti.CompanyForWebinarNotifier(entity_obj=company_for_webinar1,
                                                                         original_entity_obj=None,
                                                                         entity_type="CompanyForWebinar")
    company_for_webinar_notifier_deleted_obj = noti.CompanyForWebinarNotifier(entity_obj=None,
                                                                             original_entity_obj=company_for_webinar2,
                                                                             entity_type="CompanyForWebinar")
    company_for_webinar_notifier_obj = noti.CompanyForWebinarNotifier(entity_obj=company_for_webinar1,
                                                                     original_entity_obj=company_for_webinar2,
                                                                     entity_type="CompanyForWebinar")

    # Test new object notify
    test(company_for_webinar_notifier_new_obj, "Webinar of All Webinars", "new object", "To notify on", "Webinar's name")

    # Test deleted object notify
    test(company_for_webinar_notifier_deleted_obj, "Webinar of All Webinars", "deleted object", "To notify on", "Weninar's name")

    # Test no change in object
    test(company_for_webinar_notifier_obj, "Webinar of All Webinars", "no change in object", "Empty result (no notify)", "Weninar's name")

    # Test is_deleted object notify
    company_for_webinar2.is_deleted = True
    test(company_for_webinar_notifier_obj, "Webinar of All Webinars", "update is_deleted", "To notify on", "Weninar's name")
    company_for_webinar2.is_deleted = False

    # Test change crawl status object notify TEXT_UPLOADED
    company_for_webinar2.crawling_status = ent.CRAWLING_STATUSES.TEXT_UPLOADED
    test(company_for_webinar_notifier_obj, "Webinar of All Webinars", "update crawling_status to TEXT_UPLOADED", "Empty result (no "
                                                                                               "notify)",
         "Weninar's name")
    company_for_webinar2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change crawl status object notify TEXT_ANALYZED
    company_for_webinar2.crawling_status = ent.CRAWLING_STATUSES.TEXT_ANALYZED
    test(company_for_webinar_notifier_obj, "Webinar of All Webinars", "update crawling_status to TEXT_ANALYZED", "Empty result (no "
                                                                                               "notify)",
         "Weninar's name")
    company_for_webinar2.crawling_status = ent.CRAWLING_STATUSES.NOT_CRAWLED

    # Test change is_blacklisted object notify
    company_for_webinar2.is_blacklisted = True
    test(company_for_webinar_notifier_obj, "Webinar of All Webinars", "update is_black_listed", "To notify on",
         "Weninar's name")
    company_for_webinar2.is_blacklisted = False
    print_astrix("End of testing Company For Webinar")
    print("\n\n\n")


test_company()
test_event()
test_webinar()
test_content_item()
test_company_for_event()
test_company_competitor()
test_company_for_webinar()
