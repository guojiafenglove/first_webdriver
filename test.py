import requests
import json
test_url = 'http://crcs-http.sfytest3/cashProduct/query'
datalist = {"head":{"requester":"cashProduct/query","user_id":"2000001","timestamp":""},"body":{"id_card_number":"320681198911086645"}
response = requests.post(test_url,json=datalist)
print(response.status_code)
print(response.text)