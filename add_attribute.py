import json 

file_path = "jobs/OffersReceived.json"

# Read json data from file
with open(file_path, "r") as file:
    data = json.load(file)

# Add attribute to objects
for company in data["FullTime"]:
    company["Explanation"] = ""

for company in data["Internships"]:
    company["Explanation"] = ""

for company in data["Close"]:
    company["Explanation"] = ""

# #Check blank attributes 
# for a_class in data["Offers"]:
#     if a_class['Format'] == "":
#         print(a_class["Name"])




# Write updated data to file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)