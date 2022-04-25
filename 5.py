from flask import Flask
import argparse
import csv

parser = argparse.ArgumentParser(
    description="convert integers to decimal system")
parser.add_argument('--host', required=True)
parser.add_argument('--port', required=True)
parser.add_argument('--file', required=True)
args = parser.parse_args()
app = Flask(__name__)


@app.route('/less')
def index():
    my_dict = {}
    this_dict = {}
    with open(args.file, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=':', quotechar='"')
        for index, row in enumerate(reader):
            if index:
                speed = int(int(row[3]) / int(row[5]))
                if row[4] not in my_dict.keys():
                    my_dict[row[4]] = {'min': speed, 'max': 0}
                else:
                    if speed < my_dict[row[4]]['min']:
                        if my_dict[row[4]]['min'] > my_dict[row[4]]['max']:
                            my_dict[row[4]]['max'] = my_dict[row[4]]['min']
                        my_dict[row[4]]['min'] = speed
                    elif speed > my_dict[row[4]]['max']:
                        my_dict[row[4]]['max'] = speed
    for i in my_dict.keys():
        if my_dict[i]['max'] == 0:
            this_dict[i] = [my_dict[i]['min'], my_dict[i]['min']]
        else:
            this_dict[i] = [my_dict[i]['min'], my_dict[i]['max']]
    return this_dict


app.run(host=args.host, port=args.port)