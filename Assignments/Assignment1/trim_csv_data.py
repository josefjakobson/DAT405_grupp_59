import csv
def main():
    #1. This code snippet asks the user for a username and deletes the user's record from file.
    updatedlist=[]
    with open("Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv",newline="") as f:
      reader=csv.reader(f)
      updatedlist.append(next(reader))
      for row in reader: #for every row in the file
            
                if row[2] =="2019": #as long as the username is not in the row .......
                    updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
      updatefile(updatedlist)
        
def updatefile(updatedlist):
    with open("Assignments\Assignment1\Data\gdp-per-capita-in-us-dollar-world-bank.csv","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")


main()
