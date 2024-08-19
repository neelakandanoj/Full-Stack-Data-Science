import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("Enter the name:")
st.write(f"Hello {name}")
age=st.slider("Select the age:",0,100,20)
st.write(f"Your Age is {age}.")
options=["Python",'c++','java','C#']
choice=st.selectbox("Choose your favorite language.",options)
st.write(f"Your choice is {choice}")

data={
    "Name":['Arun','Ram','Kishore'],
    "Age":[30,20,30],
    "City":['Chennai','Bangalore','Delhi']
}
df=pd.DataFrame(data)
st.write(df)

uploaded=st.file_uploader("choose a csv file",type="csv")
if uploaded is not None:
    df=pd.read_csv(uploaded)
    st.write(df)