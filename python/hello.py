import urllib.request
import json
import time

def pp_json(json_thing, dict=None, sort=True, indents=4):
    json_obj = ""
    if type(json_thing) is str:
        json_obj = json.loads(json_thing)
    else:
        json_obj = json_thing

    for json_struct in json_obj:
        if dict == None:
            print(json.dumps(json_struct, sort_keys=sort, indent=indents))
        else:
            try:
                for name, value in dict.items():
                    result_key = json_struct.get(name)
                    if type(value) is list:
                        result_value = json_struct.get(value[0], {}).get(value[1])
                        value_name = "%s.%s" % (value[0], value[1])
                    else:
                        result_value = json_struct.get(value)
                        value_name = value
                    if result_value == None:
                        result_value = 0
                    print("%s '%s' %s %d" % (name, result_key, value_name, result_value))
            except KeyError:
                print("ID doesn't exist")
    return None

class MyJsonMetricsClass:
    def __init__(self, mainurl, username, password):
        passman = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, mainurl, username, password)
        authhandler = urllib.request.HTTPBasicAuthHandler(passman)
        opener = urllib.request.build_opener(authhandler)
        urllib.request.install_opener(opener)

    def getStats(self, theurl):
        pagehandle = urllib.request.urlopen(theurl)
        print("%s: Get url '%s' with status %s:%s" % (time.ctime(), theurl, pagehandle.status, pagehandle.reason))
        return pagehandle.read().decode('utf-8')


queues_dict = {"name":"messages_ready"}
exchange_dict = {"name": ["message_stats", "publish_in"], "name": ["message_stats", "publish_out"]}
connection_dict = {"name":"channels"}


myJsonMetrics = MyJsonMetricsClass('http://localhost:15672', 'guest', 'guest')
#for i in range(10):
pp_json(myJsonMetrics.getStats('http://localhost:15672/api/queues'), queues_dict)
pp_json(myJsonMetrics.getStats('http://localhost:15672/api/exchanges'), exchange_dict)
pp_json(myJsonMetrics.getStats('http://localhost:15672/api/consumers'))
pp_json(myJsonMetrics.getStats('http://localhost:15672/api/connections'), connection_dict)


#    time.sleep(10)

