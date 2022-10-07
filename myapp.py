import streamlit as st
import numpy as np
import pandas as pd
#import scipy
#import statsmodels.api as sm
import matplotlib.pyplot as plt
#import sklearn
#import seaborn as sns

st.title('Streamlit test')
data = pd.read_csv ('1.01.+Simple+linear+regression.csv')

st.subheader('Raw data')
st.write(data.describe())

fig = plt.figure() 
plt.plot([1, 2, 3, 4, 5]) 

st.pyplot(fig)


#st.scatter(x1,y)
#st.xlabel('SAT',fontsize=20)
#st.ylabel('GPA',fontsize=20)
#st.show()



