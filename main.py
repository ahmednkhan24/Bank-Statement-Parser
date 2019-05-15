import FMS as f

if __name__ == "__main__":
    filenames = [
        '0131.csv',
        '0228.csv'
    ]
    
    outputFileName = '2018.csv'
    
    donors = {}
    
    for filename in filenames:
        donors = f.parseFile(donors, filename)
        print(filename + ' completed...')
    
    donors = f.sortDict(donors)
    
    f.createFile(donors, outputFileName, filenames[0], filenames[len(filenames) - 1])
    print('Done! :)')