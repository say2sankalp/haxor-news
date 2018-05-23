
"""
Created by Sankalp Yadav
mail: say2sankalp90@gmail.com
April, 2018

"""


from bs4 import BeautifulSoup
import requests
from scrape_url import ScrapeUrl
import re



def google_scrape_id(word, month, year, class_name, section):
    scrape_url = ScrapeUrl(word2search= word, month_name= month, year= year)
    if(scrape_url.validation()):
        page = requests.get(scrape_url.hn_url)
        page_html = BeautifulSoup(page.text,"html.parser")
        # print page_html

    if(page.status_code is 200) :

        try:
            hiring_id = (page_html.body.find(section,attrs={"class",class_name}).text).split("=")[-1]
            if str.isalnum(str(hiring_id)):
                hiring_id = re.findall(r'\d+', hiring_id)

            else:
                hiring_id = hiring_id

            return hiring_id[-1]
        except Exception ,e :
            return  "hiring id error in page"
    else:
        hiring_id =16492994
