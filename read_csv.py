import pandas as pd

def count_rows_in_csv():
	exc_file = pd.read_csv("test_csv.csv")
	rows=exc_file.shape[0]
	print("\n number of rows in the csv = {}".format(rows))
