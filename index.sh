# hostname;interval;timestamp;runq-sz;plist-sz;ldavg-1;ldavg-5;ldavg-15
#curl -XPUT http://192.168.1.9:9200/loadavg -d '
#{
# "mappings" : {
#  "_default_" : {
#   "properties" : {
#    "hostname" : {"type": "string", "index" : "not_analyzed" },
#    "interval" : {"type": "integer", "index" : "not_analyzed" },
#    "timestamp" : { "type" : "date", "format": "yyyy-MM-dd HH:mm:ss"},
#    "runq_sz" : { "type" : "integer" },
#    "plist_sz" : { "type" : "integer" },
#    "ldavg_1" : { "type" : "float" },
#    "ldavg_5" : { "type" : "float" },
#    "ldavg_15" : { "type" : "float" }
#   }
#  }
# }
#}
#';
curl -XPUT http://192.168.1.9:9200/loadprediction -d '
{
 "mappings" : {
  "_default_" : {
   "properties" : {
    "timestamp" : { "type" : "date", "format": "yyyy-MM-dd HH:mm:ss"},
    "key" : { "type" : "string" },
    "value" : { "type" : "float" }
   }
  }
 }
}
';
