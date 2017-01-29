	
import urllib2
import urllib
import sys
import base64
import json
import time

# Azure portal URL.
base_url = 'https://westus.api.cognitive.microsoft.com/'
# Your account key goes here.
account_key = 'b2bab03dc5b84640a62a0a2d9ce06f9f'

headers = {'Content-Type':'application/json', 'Ocp-Apim-Subscription-Key':account_key}

# Path to file with JSON inputs.
file_path = 'document.json'
f = open(file_path, 'r')
input_texts = f.read()

# Start topic detection and get the URL we need to poll for results.
print('Starting topic detection.')
uri = base_url + 'text/analytics/v2.0/topics'
req = urllib2.Request(uri, input_texts, headers)
response_headers = urllib2.urlopen(req).info()
uri = response_headers['operation-location']

# Poll the service every few seconds to see if the job has completed.
while True:
	req = urllib2.Request(uri, None, headers)
	response = urllib2.urlopen(req)
	result = response.read()
	obj = json.loads(result)

	if (obj['status'].lower() == "succeeded"):
		break

	print('Request processing.')
	time.sleep(10)

print('Topic detection complete. Result:')
print(obj)

    