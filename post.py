import requests
import json
test_url = 'http://rcs-decision.sfytest3/api/element'
datalist = {"element_id":"blacklist_consume_main","input_element":{"id_card_number":"320681198911086645","name":"郭佳凤","mobile":"18721550656","device_id":"20171206247c6584a","source_type":"ios","ip":"101.81.78.146","product_type":"P","adult_tourist_number":2,"baby_tourist_number":2,"child_tourist_number":2,"departure_date":"2018-2-15","merchant_code":"10301000011","order_amount":"1300","order_date":"2018-01-11","user_id":"20000199","trade_number":"301801111116057673"}}
headers = {"content-Type":"application/json"}
response = requests.post(test_url,headers=headers,json=datalist)
print(response.status_code)
print(response.text)

