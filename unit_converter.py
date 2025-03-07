import streamlit as st

st.title("🌎Unit Converter App")
st.markdown("### Converts Lenght, Weight And Time Instantly")
st.write("Welcome! Select a Category, Enter a Value and Get The Converted Result in Real-Time;")

category = st.selectbox("Choose a Catagory", ["Lenght","Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Lenght":
        if unit == "kilometers to miles":
            return value *0.621317
        elif unit == "Miles to kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return  value / 2.20462
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to hours":
            return value / 60 
        elif unit == "Hourse to minutes":
            return value * 60
        elif unit == "Hourse to days":
            return value / 24
        elif unit == "Days to Hourse":
            return value * 24
        
if category == "Lenght":
    unit = st.selectbox("Select Conversation", ["kilometers to miles", "Miles to kilometers"])

elif category == "Weight":
    unit = st.selectbox ("Select Conversation", ["kilograms to pounds", "Pounds to kilograms"])

elif category == "Time":
    unit = st.selectbox ("Select Conversation", ["Seconds to minutes", "Minutes to seconds", "Minutes to hours","Hourse to minutes", "Hourse to days", "Days to Hourse"])

value = st.number_input("Enter the value convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.3f}")
