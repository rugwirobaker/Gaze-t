

import os

#create folder for the new times articles
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating project: ' + directory)
		os.makedirs(directory)

def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close


def append_to_file(path, data):
	with open(path,'a') as f:
		f.write(data +'\n')

def delete_file_contents(path):
	with open(path, 'w'):
		pass

# we major problem here
def file_to_set(file_name):
	results = set()
	with open(file_name,'r') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results

def set_to_file(links, file_name):
	delete_file_contents(file_name)
	for link in sorted(links):
		append_to_file(file_name, link)

# the function has already been migrated
def package_data():
	pass



def check_content_type(content):
    if content.info().getheader("Content-Type") =="text/html":
        check = True
    else:
        check = False
    return check
