import pandas as pd
import numpy as np
data = {'Letter': ['A', 'B', 'C', 'D', 'E'], 'Number': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data) #this creates a dataframe using 'data' above containing 5 rows x 2 columns 
np.random.seed(2022) #set random.seed(#) guarantees result will be static and replicable
print(df.loc[np.random.choice(df.index, size=2)]) #randomly selects and prints 2 rows in the dataframe
