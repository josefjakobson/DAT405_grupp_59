import csv
import pandas as pd

def main(csvfile):
    updatedlist=[]
    with open(csvfile,newline="") as f: #reads the csvfile and creates an array for all the data that we want to keep
      reader=csv.reader(f)
      updatedlist.append(next(reader))
      for row in reader: #for every row in the file
            if row[2] =="2019" and row[1] != '': #Record data from the year 2019 specifically
                updatedlist.append(row) 
      updatefile(csvfile, updatedlist)
        
def updatefile(csvfile, updatedlist):
    with open(csvfile,"w",newline="") as f: #Creates a new csv-file with only the data we wanted
        Writer=csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")


def equalize(csvfile1, csvfile2):
    #This function collects any unique elements that only exist in one of the datasets and removes them

    data1 = pd.read_csv(csvfile1)
    data2 = pd.read_csv(csvfile2)
    formatted_data1 = set(data1["Entity"])
    formatted_data2 = set(data2["Entity"])
    unique_elements = formatted_data1 ^ formatted_data2
    for country in unique_elements:
        if country in formatted_data1:
            data1 = data1.query('Entity != @country')
        elif country in formatted_data2:
            data2 = data2.query('Entity != @country')
    data1.to_csv(csvfile1, index=False)
    data2.to_csv(csvfile2, index=False)
            


main("Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv")
main("Assignments\Assignment1\Data\life-expectancy.csv")
equalize("Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv", "Assignments\Assignment1\Data\life-expectancy.csv")
