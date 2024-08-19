import streamlit as st
import pandas as pd
import numpy as np

## title of the application
st.title("Hello Streamlit")

##Display simple text
st.write("This is an simple text.")

df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,20,30]
})

st.write("Here is the dataframe")
st.write(df)

##Line chart
chart_data=pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
st.line_chart(chart_data)