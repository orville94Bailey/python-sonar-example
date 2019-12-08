import os
import json
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
# Request headers
        'api_key': os.environ['wmatatoken'],
}

params = urllib.parse.urlencode({
})

try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/StationPrediction.svc/json/GetPrediction/F03?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        result = json.loads(data)
        conn.close()
except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
for item in result["Trains"]:
        if item["Line"] == 'YL' and item["Destination"] == 'Hntingtn':
                print(item)
input()
