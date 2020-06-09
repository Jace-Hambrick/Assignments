import sqlite3


def total_characters():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) FROM charactercreator_character'
    print('There are', curs.execute(query).fetchall() ,'Characters')

def total_subclasses():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) FROM charactercreator_cleric'
    print('There are', curs.execute(query).fetchall() ,'Clerics')
    query = 'SELECT COUNT (*) FROM charactercreator_fighter'
    print('There are', curs.execute(query).fetchall() ,'Fighters')
    query = 'SELECT COUNT (*) FROM charactercreator_mage'
    print('There are', curs.execute(query).fetchall() ,'Mages')
    query = 'SELECT COUNT (*) FROM charactercreator_thief'
    print('There are', curs.execute(query).fetchall() ,'Thieves')
    query = 'SELECT COUNT (*) FROM charactercreator_necromancer'
    print('There are', curs.execute(query).fetchall() ,'Necromancers')

def total_items():
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    query = 'SELECT COUNT (*) FROM armory_item'
    print('There are', curs.execute(query).fetchall(),'items in the game')
  #  query = 'SELECT COUNT (*) FROM armory_weapon'
   # print(curs.execute(query).fetchall() ,' of the items are weapons')