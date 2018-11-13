import re

class Payment:
    # constructor
    def __init__(self, date, description, amount):
        # parse the month and day the quickpay donation was sent
        month = date[:2]
        day = date[3:5]

        name = ''
        number = ''

        if 'Quickpay With Zelle Payment From ' in description:
            # remove the quickpay message
            description = description.replace('Quickpay With Zelle Payment From ', '')
            # finds the index of the space right before the number
            index = re.search('\d', description).start()
            # extract the name
            name = description[:index - 1]
            # extract the payment number
            number = description[index:]
        else:
            name = 'DEPOSIT'
            number = description

        self.__donorName = name
        self.__donationConfNum = number
        self.__donationAmount = amount
        self.__donationDate = date
        self.__donationMonth = month
        self.__donationDay = day

    # getters
    def getName(self):
        return self.__donorName

    def getAmount(self):
        return self.__donationAmount

    def getMonth(self):
        return self.__donationMonth

    def getDay(self):
        return self.__donationDay

    def toString(self):
        string =  ''
        string += 'Name: ' + self.getName() + '\n'
        string += 'Amount: $' + str(self.getAmount()) + '\n'
        string += 'Date: ' + self.getMonth() + '/' + self.getDay() + '\n'
        return string