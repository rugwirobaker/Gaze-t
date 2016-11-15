
from spider import Spider
from general import*
from domain import*

#python has no built-in constants but by Python convention
#variables that are not going to change through the program articles
#have capitalised letters:
PROJECT_NAME = "The Newtimes"
HOMEPAGE = "http://www.newtimes.co.rw/"
DATABASE_NAME ="news"
DOMAIN_NAME = DOMAIN_NAME = get_domain_name(HOMEPAGE)
COLLECTION_NAME = "the_new_times"
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
Spider( PROJECT_NAME, DOMAIN_NAME, HOMEPAGE, DATABASE_NAME , COLLECTION_NAME)

for link in file_to_set(QUEUE_FILE):
    url = link
    Spider.crawl_page(url)
