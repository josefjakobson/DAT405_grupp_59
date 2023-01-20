import csv
import pandas as pd

def main(csvfile):
    #1. This code snippet asks the user for a username and deletes the user's record from file.
    updatedlist=[]
    with open(csvfile,newline="") as f:
      reader=csv.reader(f)
      updatedlist.append(next(reader))
      for row in reader: #for every row in the file
            if row[2] =="2019" and row[1] != '': #as long as the username is not in the row .......
                updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
      updatefile(csvfile, updatedlist)
        
def updatefile(csvfile, updatedlist):
    with open(csvfile,"w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")


def equalize(csvfile1, csvfile2):
    data1 = pd.read_csv(csvfile1)
    data2 = pd.read_csv(csvfile2)
    formatted_data1 = set(data1["Entity"])
    formatted_data2 = set(data2["Entity"])
    symmetric_difference = formatted_data1 ^ formatted_data2
    for country in symmetric_difference:
        if country in formatted_data1:
            data1 = data1[data1.Entity != country]
        elif country in formatted_data2:
            data2 = data2[data2.Entity != country]
    
    data1.to_csv(csvfile1, index = False)
    data2.to_csv(csvfile2, index = False)

            


main("Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv")
main("Assignments\Assignment1\Data\life-expectancy.csv")
equalize("Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv", "Assignments\Assignment1\Data\life-expectancy.csv")
