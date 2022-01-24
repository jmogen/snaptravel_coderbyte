import pandas as pd
import string
import io

#creating a pandas dataframe from stringified table
data = pd.read_csv(io.StringIO('Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'), sep=';')
newData = pd.DataFrame(data)

from_c = [];
newData = newData.rename(columns={"To_From":"To"})

#iterating through table
for name, values in newData.iteritems():
    if name == "Airline Code":
        #clear punctuation
        for i in range(len(values)):
            values[i] = values[i].translate(str.maketrans('', '', string.punctuation))
    
    if name == "FlightCodes":
        for i in range(len(values)):
            #correct flight codes, this is a unique solution for this table, some edge cases will not work
            if i+1 < len(values):
                if values[i+1] - values[i] == -10:
                    values = values[i+1] - 10
                if values[i+1] - values[i] != 10:
                    values[i+1] = values[i] + 10
    
    if name == "To" or name == "To_From":
        for i in range(len(values)):
            #seperate travel names and capitalize
            values[i] = values[i].upper()
            temp = values[i].split('_')
            values[i] = temp[0]
            from_c.append(temp[1])

newData['From'] = from_c #add column
newData['FlightCodes'] = newData['FlightCodes'].astype(int) #change flight codes from float to int

#print(newData)
