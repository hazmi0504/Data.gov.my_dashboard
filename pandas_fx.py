# Import pandas package
import pandas as pd
	
# making data frame
data = pd.read_csv("labour_force_by_age_group_state_malaysia_1982_2021_dataset.csv")

state =[]
value =[]

# iterating the columns
for row in data.Age:
    if row in state:
        continue
    state.append(row)

print(state)

# for row in data.Value:
#     value.append(row*1000)

# dict = {'Value': value} 
# df = pd.DataFrame(dict)
# df.to_csv('file2.csv', index=False)
# print(value)