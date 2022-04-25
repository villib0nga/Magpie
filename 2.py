import sys
import csv
import json

data = list(map(str.strip, sys.stdin))[0]
this_dict = {}
with open(data, encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index:
            if str(row[1]) in this_dict.keys():
                this_list = this_dict[str(row[1])]
                this_list.append(row[3])
                this_dict[str(row[1])] = this_list
            else:
                this_list = [row[3]]
                this_dict[str(row[1])] = this_list
for i in this_dict.keys():
    enum = this_dict[i]
    enum.sort()
    this_dict[i] = enum
with open('accuracy.json', 'w') as cat_file:
    json.dump(this_dict, cat_file)