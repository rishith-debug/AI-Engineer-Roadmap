import math
print(math.sqrt(256))

import random
print(random.randint(1,100))

import datetime
print(datetime.datetime.now())

import os
print("current working directory")
print(os.getcwd())

import json
student = { 
           "Name" : " Rishith",
           "Branch" : "CSE",
           "year" : 2
           }
python_data = json.dumps(student)
json_data = json.loads(python_data)
print(python_data)
print(json_data)

import my_module
my_module.greet("Rishith")