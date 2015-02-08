import csv
import json
import requests

csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

# hostname;interval;timestamp;runq-sz;plist-sz;ldavg-1;ldavg-5;ldavg-15
fieldnames = ("hostname","interval","timestamp","runq_sz","plist_sz","ldavg_1","ldavg_5","ldavg_15")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    # json.dump(row, jsonfile)
    # jsonfile.write('\n')

    print json.dumps(row)

    url = "http://192.168.1.7:9200/_bulk"
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(row), headers=headers)
    print(r.text)


