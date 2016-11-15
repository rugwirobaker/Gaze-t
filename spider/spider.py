from urllib import urlopen
from general import*
from Parser import*
from api import*
from pattern import*

class Spider:
    #class variables
    project_name = "" #str
    db_name = ""
    collection_name = "" #str
    base_url = ""
    domain_name = ""
    queue_file = "" #str
    crawled_file = "" #str
    queue = set()
    crawled = set()
    page_info = dict()

    def __init__(self, project_name, domain_name, base_url, db_name, collection_name):
        Spider.project_name = project_name
        Spider.domain_name = domain_name
        Spider.base_url = base_url
        Spider.db_name = db_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.collection_name = collection_name
        self.boot()

    def boot(self):
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        try:
            Spider.db_client = DatabaseClient(Spider.db_name)
        except:
            print "Database Error"

    @staticmethod
    def crawl_page(page_url):
        if page_url not in Spider.crawled:
            print(" Spider now crawling: " + page_url)
            print("Queue " + str(len(Spider.queue))+ '| Crawled' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.crawled.add(page_url)
            Spider.update_files()
            if match_article(page_url) == True:
                    Spider.page_info = Spider.gather_page_info(page)
                    Spider.page_info["link"] = page_url
                    create_new_article(Spider.page_info)
            if len(Spider.queue) != 0:
                Spider.queue.remove(page_url)
    @staticmethod
    def gather_links(page_url):
        try:
            response = urlopen(page_url)
            #check if response is html
            if check_content_type (response)==True:
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8', 'ignore')
                link_finder = LinkFinder(html_string, Spider.base_url)
        except:
            print("Error: can not crawl page")
            return set()
        return link_finder.page_links()

    @staticmethod
    def gather_page_info(page_url):
        try:
            response = urlopen(page_url)
            if check_encoding(response) ==True:
                html_string = html_bytes.decode('utf-8', 'ignore')
                page_parser = PageParser(html_string)
        except:
            print ("Error: can not gather information from this page")
            return dict()
        return PageParser.page_data()


    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if match_domain(Spider.domain_name) != True:
                continue
            Spider.queue.add(url)
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)

    @staticmethod
    def update_database(data):
        create_new_article(data)
