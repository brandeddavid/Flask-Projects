import csv, json

calleeNumbers = []
freq = []

def callee():

	with open('210.csv', "r") as file:

		reader = csv.reader(file, delimiter=',')

		for item in reader:

			calleeNumbers.append(item[1])

	return calleeNumbers

def totalFrequency(numbers):

	count = {}

	for item in numbers:

		if item in count.keys():

			count[item] += 1

		else:

			count[item] = 1

	freq.append(count)

	return json.dumps(freq)

