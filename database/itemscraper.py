from bs4 import BeautifulSoup as bs
import requests

class itemScraper():

    def __init__(self):
        self.myurl = 'http://private-5e.wikidot.com/general:equipment'
        self.mypage = requests.get(self.myurl)
        self.mysoup = bs(self.mypage.content, 'html.parser')
        self.mytables = self.mysoup.find_all('table', class_='wiki-content-table')

    def getstartingwealth(self):
        result = []

        tables = self.mytables
        for table in tables:
            # get name of table
            headings = table.find_all('th')
            tabletitle = []
            for heading in headings:
                tabletitle.append(heading.text)
            
            # get content of the table
            entries = table.find_all('td')
            tabledata = []
            for entry in entries:
                tabledata.append(entry.text)

            result.append({'table_title':  tabletitle, 'table_data':  tabledata})

        return result
