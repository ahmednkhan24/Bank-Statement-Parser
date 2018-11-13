import csv
import Payment

donors = {}

def printDictionary():
    for key, value in donors.items():
        print(key)
        for payment in value:
            print(payment.toString())
        print("\n\n")

# given an array of payments from a donor, the function
# then calculates the total amount of payments the donor
# donated for each month of the year
def accumulate(donor):
    # dictionary to hold the total for each month
    yearly = {}
    # initialize keys 1-12 to 0.0
    for i in range(12):
        yearly[i+1] = 0.0

    # calculate the total donations for each month and update dictionary
    month = 1
    index = 0
    while index < len(donor) and month < 13:
        if month == int(donor[index].getMonth()):
            yearly[month] = yearly[month] + donor[index].getAmount()
            index = index + 1
        else:
            month = month + 1

    return yearly

# given the name of a csv file, function
# reads from the file and updates the donors dictionary
def parseFile(fileName):
    with open(fileName, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # skip the first line of headers
        next(csv_reader)

        for line in csv_reader:
            # grab raw data
            date = line[0]
            description = line[2]
            amount = float(line[3])

            # convert raw data to defined data object
            donation = Payment.Payment(date, description, amount)

            # insert data object into dictionary
            name = donation.getName()
            if name in donors:
                donors[name].append(donation)
            else:
                arr = [donation]
                donors[name] = arr


parseFile('test.csv')
    
printDictionary()
print()
for key, value in donors.items():
    yearly = accumulate(value)
    for key, value in yearly.items():
        print(value)
    