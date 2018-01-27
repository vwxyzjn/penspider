from bs4 import BeautifulSoup
import urllib.request
import time
import logging
import datetime
import gmail
import os

def server():
    with urllib.request.urlopen('http://gregminuskin.com/') as url:  # open the site
        r = url.read()
    soup = BeautifulSoup(r, 'html.parser')
    pen_list_html = soup.findAll('h2', attrs={'class' : 'entry-title'})  # get tag with class : entry-title
    pen_list = []
    for item in pen_list_html:
        pen_list += [item.find('a').string]         # get strings in the tag
    return pen_list


if __name__ == "__main__":
    logging.basicConfig(filename='record.log',level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    temp_list = server()
    pen_list = temp_list
    gmail.send(gmail.create_message('Shengyi Huang <vwxyzjn@gmail.com>','shengyi.huang@furman.edu', 'Program runs', str(pen_list)))
    while True:
        temp_list = server()
        if temp_list != pen_list:  # if the website has new pen 
            pen_list = temp_list
            for item in pen_list:  # and the said new pen is unsold
                if "SOLD" not in item:
                    if "wahl" in item.lower():
                        gmail.send(gmail.create_message('Shengyi Huang <vwxyzjn@gmail.com>','shengyi.huang@furman.edu', 'Fountain pen found', str(pen_list[:2])))  # if there is unsold item, send me an email
                        break
        logger.info(datetime.datetime.now())
        logger.info(str(pen_list[:1]))
        time.sleep(300)  # run the program every 5 mins
    
        
            


