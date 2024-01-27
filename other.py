import json 

with open("jobs/WhereToApply.json", "r") as file:
    content = file.read()
    data = json.loads(content)


print(len(data["Companies"]))