# import csv

# with open('IPL.csv', 'r') as read_obj:

# 	# Return a reader object which will
# 	# iterate over lines in the given csvfile
# 	csv_reader = csv.reader(read_obj)

# 	# convert string to list
# 	list_of_csv = list(csv_reader)

# 	print(list_of_csv)

import csv

file = open("IPL.csv", "r")

data = list(csv.DictReader(file, delimiter=","))
file1 = open("Keys.csv", "r")
data1 = (csv.DictReader(file1, delimiter=","))
db={file1:file}
file.close()
print(db)
#print(dict(data1=data))