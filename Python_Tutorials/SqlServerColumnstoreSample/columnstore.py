#https://stackoverflow.com/questions/32463521/datetime-module-object-has-no-attribute-now

import pyodbc
#import datetime
from datetime import datetime as dt
server = 'AFT-LARRY-PC'
database = 'SampleDB'
username = 'lai3d'
password = 'a1234567'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
tsql = "SELECT SUM(Price) as sum FROM Table_with_5M_rows"
a = dt.now()
with cursor.execute(tsql):
  b = dt.now()
  c = b - a
  for row in cursor:
    print ('Sum:', str(row[0]))
  print ('QueryTime:', c.microseconds, 'ms')