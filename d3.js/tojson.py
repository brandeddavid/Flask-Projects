import csv, json

jsonObject = {"POI": 201, 'calldetails':[]}

with open("210.csv", "r") as file:

	reader = csv.reader(file, delimiter=',')

	details = {}

	for item in reader:

		details['phoneNumber'] = item[1]
		details["callType"] = item[4]

		jsonObject["calldetails"].append(details)

		details = {}

	jsonObject = json.dumps(jsonObject)

jsonObject = json.loads(jsonObject)

print (type(jsonObject))

