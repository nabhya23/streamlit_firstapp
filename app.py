import streamlit as st

st.title(":blue[innomatics data app]")

st.header(":red[Data Science Internship]")
st.subheader("Feb 2023")
CODE='''print("hello world")'''
st.code(CODE,language="python")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()
