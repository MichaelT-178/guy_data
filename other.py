import json 

with open("jobs/WhereToApply.json", "r") as file:
    content = file.read()
    data = json.loads(content)



companies = []

for company in data["Companies"]:
    companies.append(company['CompanyName'])



for c in companies:
    if companies.count(c) > 1:
        print(c)