import sqlite3
import pytz
import datetime
import csv
from django.utils import timezone

#def import_database_table():
conn = sqlite3.connect('db.sqlite3')
ptr = conn.cursor()

tz=pytz.timezone('America/New_York')
dt=datetime.datetime.now()

 #ptr.execute("""CREATE TABLE Inventory (
 #               id integer,
  #              name text,
   #             price_per_lb real,
    #            stock_in_lbs integer
     #           )""")
 
 #ptr.execute("""CREATE TABLE JDelInventory (
 #               id integer,
 #               name text,
 #               price real,
 #               ingredients text
 #               )""")     
     

 #ptr.execute("INSERT INTO Inventory VALUES (00110, 'SEABASS', 2.15, 15)")
 #conn.commit()

 #----------------------------------------------------------------------------------------
with open('inventorymain.csv') as csv_file:
  field_names = ["inventory_id","name","units","safety_stock","price_per_unit"]
  csv_reader = csv.DictReader(csv_file, fieldnames=field_names)
  line_count = 0
  for row in csv_reader:
    params = (int(row["inventory_id"]), row["name"], int(row["units"]), int(row["safety_stock"]), float(row["price_per_unit"]),datetime.date.today())
    ptr.execute("INSERT INTO manageInventory_inventory VALUES (?,?,?,?,?,?)", params)
    conn.commit()
    print(f'{row["inventory_id"]}\t{row["name"]}\t{row["units"]}\t{row["safety_stock"]}\t{row["price_per_unit"]}')
 #-----------------------------------------------------------------------------------------


#ptr.execute("SELECT * FROM home_item WHERE id=8")


#print(ptr.fetchone())
#conn.commit()

conn.close()
