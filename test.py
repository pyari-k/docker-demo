import read_csv
import ping_google
from datetime import date
import sys
print("Python version")
print (sys.version)
print("\n date: {}".format(date.today()))
print("\n import completed")
read_csv.count_rows_in_csv()
ping_google.ping_google()
