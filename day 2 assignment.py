# Assignment -1
# Create a data frame with 10 rows on random numbers and 4 coloumns, ( coloumns labelled as a,b,c,d)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline
import seaborn as sns
from numpy.random import randn, randint, uniform, sample
df = pd.DataFrame(randn(10,4), columns = ['a','b','c','d'])
print(df) #For Data set 
df.plot(kind='bar',title='Bar plot')
