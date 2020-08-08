from bs4 import BeautifulSoup
import requests
import csv
import regex as re
from FnF import FileNotFound

URL = 'https://allpoetry.com/'


def get_me_my_stuff(ep):
    source= requests.get(f"{URL}{ep}").text
    soup= BeautifulSoup(source,'lxml')
    reg_text= re.compile('orig_.*')


    if soup.find_all('h2',{'class':'error'}):
        raise FileNotFound('No poets with the given username')
    else:
        with open('composition.txt','w') as f:
            for i in soup.find_all('div',{"class" : 'fonted'}):
                f.write(f"{i.a.text.upper()}\n")
                f.write(i.find('div',{"class" : reg_text}).text)
                f.write('\n\n++++++++++++\n\n\n')
        
    


if __name__ == "__main__":
    get_me_my_stuff('FernZpy')
