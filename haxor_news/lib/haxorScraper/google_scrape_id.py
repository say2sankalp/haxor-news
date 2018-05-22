
"""
Created by Sankalp Yadav
mail: say2sankalp90@gmail.com
April, 2018

"""


from bs4 import  BeautifulSoup
import  requests
from  .scrape_url import ScrapeUrl



def google_scrape_id(word,month,year):
    scrape_url = ScrapeUrl(word2search= word,month_name= month, year= year)
    if(scrape_url.validation()):
        page = requests.get(scrape_url.hn_url)
        page_html = BeautifulSoup(page.text,"html.parser")

    if(page.status_code is 200) :
        hiring_id = (page_html.body.find("div",attrs={"class","hJND5c"}).text).split("=")
        return hiring_id[-1]
    else:
        hiring_id =16492994


