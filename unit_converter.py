import streamlit as st  # 📌 Importing Streamlit for building the UI

# 🏷️ App Title & Description
st.title("🌎 Unit Converter App")  # App title with an emoji
st.markdown("### 🔄 Convert Length, Weight, and Time Instantly")  
st.write("📌 Welcome! Select a category, enter a value, and get the converted result in real-time.")

# 📂 Category Selection (Length, Weight, Time)
category = st.selectbox("📌 Choose a Category", ["Length", "Weight", "Time"])

# 📌 Function to Perform Unit Conversion
def convert_units(category, value, unit):
    """
    This function takes the category (Length, Weight, or Time), 
    the value to be converted, and the selected unit type.
    It returns the converted value based on the selected conversion type.
    """
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621317  # 🔄 1 km = 0.621317 miles
        elif unit == "Miles to Kilometers":
            return value / 0.621371  # 🔄 1 mile = 1.60934 km

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462  # 🔄 1 kg = 2.20462 lbs
        elif unit == "Pounds to Kilograms":
            return value / 2.20462  # 🔄 1 lb = 0.453592 kg

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60  # ⏳ 1 second = 1/60 minutes
        elif unit == "Minutes to Seconds":
            return value * 60  # ⏳ 1 minute = 60 seconds
        elif unit == "Minutes to Hours":
            return value / 60  # ⏳ 1 minute = 1/60 hours
        elif unit == "Hours to Minutes":
            return value * 60  # ⏳ 1 hour = 60 minutes
        elif unit == "Hours to Days":
            return value / 24  # ⏳ 1 hour = 1/24 days
        elif unit == "Days to Hours":
            return value * 24  # ⏳ 1 day = 24 hours

# 📌 Based on Selected Category, Display Relevant Conversion Options
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])

elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])

elif category == "Time":
    unit = st.selectbox("⏳ Select Conversion", 
                        ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours",
                         "Hours to Minutes", "Hours to Days", "Days to Hours"])

# 🔢 User Input for Value to Convert
value = st.number_input("🔢 Enter the Value to Convert", min_value=0.0, step=0.1)

# 🔘 Button to Perform Conversion
if st.button("🚀 Convert"):
    result = convert_units(category, value, unit)  # Call the conversion function
    st.success(f"✅ The result is {result:.3f}")  # Display result with 3 decimal places
