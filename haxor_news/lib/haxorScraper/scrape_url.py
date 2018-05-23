
"""
Created by Sankalp Yadav
mail: say2sankalp90@gmail.com
April, 2018

"""
# Logic implemented as mini scraper
# say2sankalp

from datetime import  datetime


class ScrapeUrl():

    def __init__(self, word2search="hackernews who is hiring", month_name= "april", year= 2018):
        self.baseUrl = "https://www.google.co.in/search?num=1&q="
        self.word2search = str(word2search)
        self.month = str(month_name)
        self.year = str(year)

    def validation(self):
        current_month = datetime.today().month
        if str.isdigit(self.year) and (not self.month is  ["",None]):
            self.hn_url = self.baseUrl+self.word2search.replace(" ","+")+self.month+self.year
            return True
        else:
            raise Exception("parameter missing")

    def __str__(self):
        return "Url is [{}]".format(self.hn_url)

    def __repr__(self):
        return self.hn_url








