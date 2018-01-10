import redis
import json
import pickle

formatters = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'END': '\033[0m',
    'BLUE': '\033[34m',
}

try:
    conn = redis.StrictRedis(
        host='192.168.14.11',
        port=6379)
    print(conn)
    conn.ping()
    j_info = conn.info() 
    print("Redis '%s' on '%s'" % (j_info.get('redis_version'), j_info.get('os')))
    print('Connected!')
    print("Current length of 'gpwrss' hash is %d" % (conn.hlen('gpwrss')))
    keytofind = "netto"
    for news in conn.hscan_iter('gpwrss', match='*' + keytofind + '*'):
        print("{RED}key:{END} '%s'".format(**formatters) % news[0].decode('utf-8').replace(keytofind, '{BLUE}' + keytofind + '{END}').format(**formatters))
        r = json.loads(news[1].decode('utf-8'))
        print(r.get('payload'))
        print(r.get('topic'))
        print(r['article']['title'])
        print('-----------------------')
#        print(json.dumps( r, sort_keys=True, indent=4))
except Exception as ex:
    print('Error:', ex)
    exit('Failed to connect, terminating.')

