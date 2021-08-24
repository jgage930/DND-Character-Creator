import sqlite3 as sql
from spellscraper import spellScraper

connection = sql.connect("database.db")

# define schema
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# insert data
obj = spellScraper()
spell_urls = obj.getspellurls()
specialcases = [
    'https://5thsrd.org/spellcasting/spells/magic_circle/',
    'https://5thsrd.org/spellcasting/spells/blade_barrier/',
    'https://5thsrd.org/spellcasting/spells/plane_shift/',
    'https://5thsrd.org/spellcasting/spells/imprisonment/'
]

# remove special cases
for spell_url in spell_urls:
    if spell_url in specialcases:
        spell_urls.remove(spell_url)

# scrape spell data
for spell_url in spell_urls:
    spell_data = obj.scrapespell(spell_url)
    name = spell_data['name']
    level = spell_data['level']
    school = spell_data['school']
    casting_time = spell_data['casting_time']
    range = spell_data['range']
    duration = spell_data['duration']
    components = spell_data['components']
    description = spell_data['description']

    cur.execute("""
        INSERT INTO spells (name, level, school, casting_time, range, duration, components, description)
        VALUES (?,?,?,?,?,?,?,?)
    """, (name, level, school, casting_time, range, duration, components, description))