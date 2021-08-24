from bs4 import BeautifulSoup as bs
import requests
import re

class spellScraper():

    def __init__(self):
        """initialize a spell scraper with a url and set up soup"""
        self.spell_table_url = 'https://5thsrd.org/spellcasting/spell_indexes/spells_by_level/'
        self.page = requests.get(self.spell_table_url)
        self.soup = bs(self.page.content, "html.parser")

    def getspellurls(self):
        """get the url to each individual spell page"""
        links = self.soup.find_all('a', href=re.compile('\/spellcasting\/spells\/'))

        spell_urls = []
        for link in links:
            spell_name = link.text.replace(" ", '_').lower()
            spell_name = spell_name.replace("'", '')
            spell_name = spell_name.replace("/", '')
            spell_urls.append('https://5thsrd.org/spellcasting/spells/'+spell_name+'/')

        return spell_urls

    def scrapespell(self, spell_url):
        """scrape all the data from a spell page.  return a dictionary"""
        page = requests.get(spell_url)

        # find spell name
        soup = bs(page.content, "html.parser")
        links = soup.find('h1')

        spell_name = links.text
        
        # grab the rest of the data in <p> </p> tags
        data = soup.find_all('p')

        # grab the school and level data works for cantrips only right now
        temp = data[0].find('em')
        str = temp.text
        str = str.split(' ')
        

        if str[1] == 'cantrip':
            spell_level = 0
            spell_school = str[0]
        else:
            a = str[0]
            spell_level = str[0]
            spell_school = str[1]
        
        # grab casting time
        temp = data[1].text
        temp = temp.split('\n')
        
        dataiwant = []
        for element in temp:
            element = element.split(':')
            dataiwant.append(element[1].strip())
        
        spell_casting_time = dataiwant[0]
        spell_range = dataiwant[1]
        spell_components = dataiwant[2]
        spell_duration = dataiwant[3]

        # grab description
        
        spell_description = data[2].text + data[3].text
        

        # return a dictionary of the data
        result = {}
        result['name'] = spell_name
        result['level'] = spell_level
        result['school'] = spell_school
        result['casting_time'] = spell_casting_time
        result['range'] = spell_range
        result['duration'] = spell_duration
        result['components'] = spell_components
        result['description'] = spell_description
        
        return result


# specialcases = [
#     'https://5thsrd.org/spellcasting/spells/magic_circle/',
#     'https://5thsrd.org/spellcasting/spells/blade_barrier/',
#     'https://5thsrd.org/spellcasting/spells/plane_shift/',
#     'https://5thsrd.org/spellcasting/spells/imprisonment/'
# ]
# to get all spell data run spellscrape() in a for loop over all results of getspellurls()