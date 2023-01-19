import csv
import pandas as pd

def main(csvfile):
    #1. This code snippet asks the user for a username and deletes the user's record from file.
    updatedlist=[]
    with open(csvfile,newline="") as f:
      reader=csv.reader(f)
      updatedlist.append(next(reader))
      for row in reader: #for every row in the file
            
                if row[2] =="2019": #as long as the username is not in the row .......
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
    formatted_data1 = list(data1["Entity"])
    formatted_data2 = list(data2["Entity"])
    for country1 in formatted_data1:
        if country1 not in formatted_data2:
            data1.set_index("Entity")
            data1.drop(country1, axis=0)
    for country2 in formatted_data2:
        if country2 not in formatted_data1:
            data2.set_index("Entity")
            data2.drop(country2, axis=0)
            


main("Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv")
main("Assignments\Assignment1\Data\life-expectancy.csv")
equalize("Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv", "Assignments\Assignment1\Data\life-expectancy.csv")
