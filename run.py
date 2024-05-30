#!/usr/bin/python3
"""test different code"""
import models
from models.user import User
from models.artisan import Artisan
from models.user import User
from models.review import Review
from models.booking import Booking
from models.service import Service
from models.artisan import Artisan
from models import storage
from hashlib import md5

'''
# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)



user = storage.get(User, "dfea2585-36a2-4228-aff0-1d035ddd2c7d")
if user:
    user.is_artisan = True
    i = Artisan(user_id=user.id, service_category="Tailoring", skills="sewing", experience="5 years", availabilty="weekends", pricing="affordable")
    print()
    #user.artisan_profile = i
    storage.new(i)
    storage.save()

    print(i)


print()
obj = storage.get(User, "ac6a67fd-a4d8-4627-8038-d7a09cde98a9")
if not obj:
    print('no such object')
storage.delete(obj)
storage.save()


s = Service(user_id="3c4a2536-e8dd-40e7-a713-fe656c6a1aec", name="i need a tailor", description="he should be able to sew mens wear", category1="c8ec9761-cd43-4af6-a31b-87d64634bb3d")
print()




#print(a)
storage.new(s)
storage.save()

print(s)


c = Category(name='Tailoring', description='sewing of differnt kinds of clothings')
storage.new(c)
storage.save()
print()
print(c)


b = Booking(user_id="3c4a2536-e8dd-40e7-a713-fe656c6a1aec", artisan_id="56d76dc4-9725-4462-9866-51090c9628be", service_request_id="630aeb39-e220-4b69-be3b-f2c34170d9cc", payment_info="Not paid")
print()




#print(a)
storage.new(b)
storage.save()

print(b)


List = [1, 2.5, ['anotherone', 10, 'i know'], 'a', 'akin', 5.85]
print(len(List))

from utility.utils import get_distance_with_addr
try:
  addr = get_distance_with_addr('e3e5d284-477e-43fe-a67b-137aa4553306', '33b0aa27-5122-49ca-94b2-7a25a37d395e')
  print(addr)
except Exception as e:
  print('error', e)


import requests

secret = "Xlg8T8JbZQpfAfjOUsnE2jfQCNLjQKYN"
key = "dE8yKAWANjyVG2ZE"
league_id = "2"
last_matches = "1"

url = f"https://livescore-api.com/api-client/competitions/table.json?competition_id={league_id}&include_form={last_matches}&key={key}&secret={secret}"

data = requests.get(url).json()

competition_name = data['data']['competition']['name'].replace(' ', '_').join(['_', '.json'])
with open(competition_name, 'w') as f:
  f.write(str(data))


import requests
import time
phone_number = '0706572897413'
url = f'http://127.0.0.1:8000/api/v1/users/number/{phone_number}'
data = {
    'phone_number': '070657274135',
    'password': 'djt567hjnhjhjjdj',
}

headers = {
    'Content-Type': 'application/json',
}

response = requests.get(url, json=data, headers=headers)

if response.status_code == 200:
    #print(response.json())
    token = response.text
    print('presponse:', response.text, response.status_code)
else:
    print("Response:", response.text,
          "responseCode: ",  response.status_code
          )
'''

import requests

print('test artisans')
url = f'http://127.0.0.1:8000/api/v1/artisans'

r = requests.get(url)
if r.status_code == 200:
  artisan_list = r.json()
  
else:
  artisan_list = None

#print(artisan_list)


# Add artisans onboard
user_url = f'http://127.0.0.1:8000/api/v1/users'
artisan_url = f'http://127.0.0.1:8000/api/v1/artisans'
phone_number = input('Enter your Phone Number:  ')
password = input('Enter you password to become a user before becoming an artisan:  ')
availability = input('Enter how available you are:  ')
price = input('Enter how much you can charge per hour on a job:  ')
experience = input('Enter your experience:  ')
data = {
  'phone_number': phone_number,
  'password': password,
  'availability': availability,
  'price': price,
  'experience': experience,

}
headers = {
    'Content-Type': 'application/json',
}

r = requests.post(artisan_url, json=data, headers=headers)
if r.status_code == 200:
  user = r.content
  user_id = data['id']
  print('User created, Your user id is', user_id)



else:
  print('error', r.status_code, r.reason, r.text, r.content, r.ok)