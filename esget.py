import sys
import csv
import json
import optparse
from datetime import datetime
from elasticsearch import Elasticsearch


def main():
    es = Elasticsearch("http://192.168.1.7:9200")

    res = es.get(index="loadavg", doc_type='doc_type', id=1)
    print(res['_source'])

    es.indices.refresh(index="loadavg")

    res = es.search(index="loadavg", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(ldavg_1)s %(ldavg_5)s %(ldavg_15)s" % hit["_source"])

parser = optparse.OptionParser()
parser.add_option('-i', '--in', help='Input CSV file', dest='in_file', action='store')
parser.add_option('-n', '--run-once', help='Run once mode (non-daemon)', dest='runOnceMode', default=False, action='store_true')
(options, args) = parser.parse_args()

if __name__ == '__main__':
    main()


