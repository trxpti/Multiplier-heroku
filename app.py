
import streamlit as st
st.write("""
# Two Number Multiplication App
""")

st.header('User Input Parameters')

def user_input_features():
    n1 = st.number_input("Input Number_1")
    n2 = st.number_input("Input Number_2")

    return n1, n2

n1, n2 = user_input_features()
if st.button('Calculate')
    st.write(n1*n2)
