import csv
import sys

'''
Usage: Place the python script and .csv reader in the same directory for 
simplicity. Next, navigate to the directory of the .csv in question using 
your favourite cli.

python bank3.py example.csv > output.txt 

The above usage assumes windows use. Linux users, you know what to do.
'''
    

def getNames():
    """ Gets the amount of flatmates and their names, 
    builds dictionary for reach"""
    
    numberOfPeople = int(input("Please enter the number of people " +
    "living together: "))
    print("Please enter the names of your flatmates individually")
    peoplesNames = dict()
    
    for i in range(numberOfPeople):
        temp = input("Name: ")                                  #.upper()    
        peoplesNames.update({temp: [[],0]})
    
    # Adds an entry for unexplained transactions
    peoplesNames.update({'Unknown':[[], 0]})
    return (peoplesNames, numberOfPeople)
    
def openCSV():
    f = open(sys.argv[1], newline = '', )
    reader = csv.reader(f)
    f.readline() # Skips first line, which is usaully the account number
    rowNumber = 0
    return reader
    
def setColumns(peoplesNames, reader):

        addition = []
        rowNumber = 0
        found = False
           
        # Read the first two lines to get input/output columns       
        for row in reader:
            if rowNumber >= 2:
                break
            else:
                rowNumber += 1
                # For each item in row, test if it's a number, i is index
                for i in range(len(row)):
                    if found == False:
                        for name in peoplesNames.keys(): 
                            # Fix as some banks use lower case names for AP's
                            if name in row[i] or name.upper() in row[i] or name.lower() in row[i]:
                                nameColumn = i
                                found = True
                    try:    
                        float(row[i])
                    except:
                        pass
                    else:
                        addition.append([i, float(row[i])])
       
        if addition[0][1] + addition[2][1] == addition[3][1]:
            print("YAY, input/output must be index 3")
            return (3, nameColumn)
        else:
            print("Must be other way around i.e. index 4 ")
            return (4, nameColumn)
    
def getTransactions(reader, inputColumn, nameColumn, peoplesNames):
    """ Iterates through the .csv reader, returns transactions """
    for row in reader:
        # Money in/Money out as adding a negative is == subtracting
        for person in peoplesNames:
            if person in row[nameColumn] or person.lower() in row[nameColumn] or person.upper() in row[nameColumn]:
                # index 1 is their current total, 0 is trans list
                peoplesNames[person][1] += float(row[inputColumn])
                peoplesNames[person][0].append(row[nameColumn]) ###
                break
        else:
            peoplesNames['Unknown'][1] += float(row[inputColumn])
            peoplesNames['Unknown'][0].append(row[nameColumn]) ###
    return peoplesNames

                    
            
    
def main():
    reader = openCSV()   
    #try:
    peoplesNames, numberOfPeople = getNames()
    inputColumn, nameColumn = setColumns(peoplesNames, reader) 
    transDict = getTransactions(reader, inputColumn, nameColumn, peoplesNames)
    output =  open('output.txt', 'w')

    #for key, val in transDict.items():
        #print(key)
        #print("Transaction List: \t", val[0])
        #print("Ending contribution: \t", val[1], " " \
        #+ "\n--------------------------------------------- \n")

    
    for key, val in transDict.items():
        output.write(key)
        output.write("Transaction List: \t \n%s\n" % val[0])
        output.write("Ending contribution: \t \n%d " % val[1])
        output.write("\n--------------------------------------------- \n") 
        
    output.close()
    sys.exit(0) # Exits Python
 
if __name__ == "__main__":
    main()
   

    


    