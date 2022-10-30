import numpy as np
import statistics as st
myList=[35,15,54,75,8,3,8]
print(f"Mean = {np.mean(myList):}")
print(f"Median = {np.median(myList)}")
print(f"Mode = {st.mode(myList):}")
print(f"Standard Deviation = {np.std(myList):}")
print(f"Percentile = {np.percentile(myList,50)}")
