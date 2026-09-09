import json
student = {
               "NAME" : "RISHITH",
               "CLASS" : "AIML",
               "AGE" : 20
}
json_data = json.dumps(student)
json_data = json.loads(json_data)
print(json_data)