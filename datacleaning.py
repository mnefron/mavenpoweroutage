import pandas as pd

#enumerate all the US states (and DC)
states = [ 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'District of Columbia', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

#specify where the dirty data is located (file name)
input = 'DOE_Electric_Disturbance_Events_Edited 11.30.23.xlsx';

#read dirty data into a pandas data frame
df = pd.read_excel(input)

#set up new dataframe to hold clean data
dfout = pd.DataFrame(
    {
        'Date Event Began': [],
        "state": []
    }
)

#iterate over each row in the dirty data
i=0
for index, row in df.iterrows():
    #hack to avoid duplicated state names. Set up list of seen states for this row. 
    #iterate over each of the states in the state list. If that state appears in the "Area Affected" column...
    extracted_states = []
    for state in states:
        if state in row['Area Affected']: 
            if state not in extracted_states:
                 print(row['Area Affected'],":: ", state)
                 #...set the "State" field for this row in the output data frame
                 dfout.loc[i] = [row['Date Event Began'], state]
                 i += 1
                 #make sure we don't include the state again for the same row (e.g. if row says "Eastern Ohio and Western Ohio", output is just "Ohio")
                 extracted_states.append(state)

#write cleaned output to csv file
dfout.to_csv('output.csv')



