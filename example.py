import pandas as pd
import numpy as np
data = {'Letter': ['A', 'B', 'C', 'D', 'E'], 'Number': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data) #this creates a dataframe using 'data' above containing 5 rows x 2 columns 
print(df.loc[np.random.choice(df.index, size=2)]) #randomly selects and prints 2 rows in the dataframe