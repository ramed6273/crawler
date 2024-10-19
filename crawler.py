from os import mkdir, remove
import requests
import re

sites_file = open('websites.txt', 'r')

error_links = []
titles = []
links_array = []
crawled_links = []

def isXMLLInk(site):
    return site.find('.xml') == -1


def crawl(site):

    # for site in file_link:
        
    if isXMLLInk(site):
        site = site.replace("\n","").strip("/") + '/sitemap.xml'

    try:
        response = requests.get(url=site).text
    except Exception:
        error_links.append(site)
        return 1
    
    pattern = re.compile(r'<loc>(.*?)<\/loc>', re.DOTALL)

    links = pattern.findall(response)

    for link in links:
        if not isXMLLInk(link):
            links_array.append(link)
        else:
            title = (link.split('/')[-2]).replace('-', ' ')
            titles.append(title)
    return 0


for link in sites_file:
    links_array.append(link)

for link in links_array:
    if link in crawled_links:
        continue
    crawled_links.append(link)
    crawl(link)

title_file = open(f'titles.txt', 'a')

for item in titles:
    title_file.write(f'{item}\n')

title_file.close()
# print(titles)
# print(links_array)
# print(error_links)


# for site in sites_file:
#     try:
#         mkdir(site.split('.')[0][8:])
#     except FileExistsError:
#         pass

#     if site.find('.xml') == -1:
#         site = site.replace("\n","").strip("/") + '/sitemap.xml'
#         print(site)

#     response = requests.get(url=site).text
#     pattern = re.compile(r'<loc>(.*?)<\/loc>', re.DOTALL)

#     links = pattern.findall(response)

#     print(links)

#     site = site.split('.')[0][8:]

#     links_file = open(f'{site}/links.txt', 'w')
#     title_file = open(f'{site}/titles.txt', 'w')



#     for link in links:
#         links_file.write(f'{link}\n')
#         if link.find('.xml') == -1:
#             link = (link.split('/')[-2]).replace('-', ' ')
#             title_file.write(f'{link}\n')      

# links_file.close()
# title_file.close()
sites_file.close()

#TODO append - make dic and write - loop through xml - take file by argument - check in title before adding