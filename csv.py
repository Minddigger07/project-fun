

import pandas as pd
file=pd.read_csv('Data Set.csv')
print(file)
print(f"\n\nSorted Data(Name):\n{file.sort_values(['Name'])}")
print(f"\n\nSorted Data(Age):\n{file.sort_values(['Age'])}")

