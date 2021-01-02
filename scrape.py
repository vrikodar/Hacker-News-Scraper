#By SxNade
#https://github.com/SxNade/Hacker-News-Scraper

import requests
from termcolor import colored
from bs4 import BeautifulSoup
import pprint
from tqdm import tqdm
import time
import os

hn = '''
 _   _ _   _      ____   ____ ____      _    ____  _____ ____  
| | | | \ | |    / ___| / ___|  _ \    / \  |  _ \| ____|  _ \ 
| |_| |  \| |____\___ \| |   | |_) |  / _ \ | |_) |  _| | |_) |
|  _  | |\  |_____|__) | |___|  _ <  / ___ \|  __/| |___|  _ < 
|_| |_|_| \_|    |____/ \____|_| \_\/_/   \_\_|   |_____|_| \_\
                                                               
'''
print(hn)

#tqdm for a little animation of loading..

for i in tqdm(range(10)):
	time.sleep(0.1)
time.sleep(2)
os.system('clear')

print(colored('[+]Loading Stories Now.......', 'green', attrs=['bold']))

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(colored(res.text, 'green'))

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

#function which sorts stories according to the number of votes
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 50:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

#print statement to print the stories in the Terminal
pprint.pprint(create_custom_hn(mega_links, mega_subtext))
