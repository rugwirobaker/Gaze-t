#specific links pattern matching
import re

def match_domain(string):
    pattern = re.compile(r'http://www\.newtimes\.co\.rw/.*')
    if pattern.match(string):
        answer = True
    else:
        answer = False
    return answer

def match_relative_url(string):
    pattern = pattern =  re.compile(r'^/section/.')
    if pattern.match(string):
        answer = True
    else:
        answer = False
    return answer

def match_article(string):
    pattern = re.compile(r'.*/section/article/20\d\d-\d\d-\d\d/\d*/.*')
    if pattern.match(string):
        answer = True
    else:
        answer = False
    return answers
