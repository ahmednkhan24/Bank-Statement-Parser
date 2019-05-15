import csv
import Payment

def __printDictionary(donors):
    for key, value in donors.items():
        print(key)
        for payment in value:
            print(payment.toString())
        print("\n\n")

# given an array of payments from a donor, the function
# then calculates the total amount of payments the donor
# donated for each month of the year
def __accumulate(donor):
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

def sortDict(donors):
    d = {}
    for i in sorted(donors.keys()):
        d[i] = donors[i]
    donors = d
    return donors

# given the name of a csv file, function
# reads from the file and updates the donors dictionary
def parseFile(donors, fileName):
    with open(fileName, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            # grab raw data
            date = line['Date']
            description = line['Description']
            amount = float(line['Amount'])

            # convert raw data to defined data object
            donation = Payment.Payment(date, description, amount)

            # insert data object into dictionary
            name = donation.getName()
            if name in donors:
                donors[name].append(donation)
            else:
                arr = [donation]
                donors[name] = arr
    return donors

# given the name of a csv file, function writes to the file
def createFile(donors, fileName, first, last):
    with open(fileName, 'w') as csv_file:
        headers = ['Name', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Total']
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(headers)

        for donorName, totalDonations in donors.items():
            data = []
            data.append(donorName)
            yearly = __accumulate(totalDonations)
            total = 0.0
            for month, monthlyDonation in yearly.items():
                total = total + monthlyDonation
                data.append(str(monthlyDonation))
            data.append(str(total))
            csv_writer.writerow(data)

        csv_writer.writerow(['From', 'To'])
        csv_writer.writerow([first, last])
