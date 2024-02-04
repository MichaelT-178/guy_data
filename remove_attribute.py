import json

with open('jobs/WhereToApply.json', 'r') as file:
    data = json.load(file)
    
     
for company in data["Companies"]:
    attribute_to_remove = "Color"

    company.pop(attribute_to_remove, None)


with open('jobs/WhereToApply.json', 'w') as file:
    json.dump(data, file, indent=4)
