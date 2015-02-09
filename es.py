import sys
import csv
import json
import optparse
import os
import glob
from datetime import datetime
from elasticsearch import Elasticsearch

id = 1

def get_fieldnames(csvfile):
    header = csvfile.readline()
    fields = header.split(',')
    return fields

def process_file(csvfile, fieldnames):
    global id

    es = Elasticsearch("http://{0}:{1}".format(options.dest_ip, options.dest_port))

    #fieldnames = ("timestamp","kw_energy_consumption","prediction")
    #fieldnames = ("hostname","interval","timestamp","runq_sz","plist_sz","ldavg_1","ldavg_5","ldavg_15")
    reader = csv.DictReader(csvfile, fieldnames)

    for row in reader:
        #datarow = row
        #print json.dumps(datarow)

        if 'timestamp' not in row.keys():
            print "ERROR: no timestamp at row {0}".format(id)
            exit (1)

        for field in fieldnames:
            if field == 'timestamp':
                continue
            datadict = {}
            datadict['id'] = id
            datadict['timestamp'] = row['timestamp']
            datadict['key'] = field
            datadict['value'] = row[field]
            databody = json.dumps(datadict)
            print databody
            res = es.index(index=options.dest_index, doc_type=options.dest_doc_type, id=id, body=databody)
            print res
            id = id + 1

#        datadict = {}
#        datadict['id'] = id
#        datadict['timestamp'] = row['timestamp']
#        datadict['key'] = 'prediction'
#        datadict['value'] = row["prediction"]
#        databody = json.dumps(datadict)
#        print databody
#        res = es.index(index=options.dest_index, doc_type=options.dest_doc_type, id=id, body=databody)
#        print res
#        id = id + 1

def main():
    if options.in_path:
        file_path = os.path.join(options.in_path, "*.csv")
        for filename in glob.glob(file_path):
            print "Processing {0}".format(filename)
            csvfile = open(filename, 'r')
            fields = get_fieldnames(csvfile)
            process_file(csvfile, fields)
    else:
        csvfile = sys.stdin
        process_file(csvfile)


parser = optparse.OptionParser()
parser.add_option('-i', '--in-path', help='Path to  CSV files', dest='in_path', action='store')
parser.add_option('-a', '--dest-ip', help='IPv4 of elasticsearch', dest='dest_ip', action='store')
parser.add_option('-p', '--dest-port', help='Port of elasticsearch', dest='dest_port', default=9200, action='store')
parser.add_option('-x', '--index', help='Elasticsearch index', dest='dest_index', action='store')
parser.add_option('-d', '--doc-type', help='Elasticsearch document type', dest='dest_doc_type', action='store')
parser.add_option('-n', '--run-once', help='Run once mode (non-daemon)', dest='runOnceMode', default=False, action='store_true')
(options, args) = parser.parse_args()

if __name__ == '__main__':
    main()


