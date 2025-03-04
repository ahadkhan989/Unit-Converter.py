import streamlit as st

# Main Heading...
st.title("🌐 Unit Converter")

# Sub Heading...
st.markdown("### Seamless Conversions: Length, Weight, Time")

# 
st.write("Say Goodbye to Manual Conversions: Length, Weight, Time, Instantly")

# A Dropdown for choose category
category = st.selectbox("Which category would you like ?", ["Length", "Weight", "Time"])

def unit_converter(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Mile":
            return value * 0.621371        # 1 kilometer = 0.6213171 Mile
        elif unit == "Mile to Kilometers":
            return value / 0.621371        # 1 Mile = 1.60934 Kilometers
        
    elif category == "Weight":
        if unit == "Kilogram to pounds":
            return value * 2.20462         # 1 Kilogram = 2.20462 Pounds
        elif unit == "Pounds to Kilogram":
            return value / 2.20462         # 1 Pound = 0.453592 Kilogram
    
    elif category == "Time":
        if unit == "Seconds to Minute":
            return value / 60
        elif unit == "Minute to Seconds":
            return value * 60
        elif unit == "Minutes to Hour":
            return value / 60
        elif unit == "Hour to Minutes":
            return value * 60
        elif unit == "Hours to Day":
            return value / 24
        elif unit == "Day to Hours":
            return value * 24


# These conditions are write for a Dropdown
if category == "Length":
    unit = st.selectbox("📏 Select Conversion Mode", ["Kilometers to Mile", "Mile to Kilometers"])

elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion Mode", ["Kilogram to Pounds", "Pounds to Kilogram"])

elif category == "Time":
    unit = st.selectbox("🕑 Select Conversation Mode", ["Seconds to Minute", "Minute to Seconds", "Minutes to Hour", "Hour to Minutes", "Hours to Day", "Day to Hours"])


value = st.number_input("Provide the value to be converted")
if st.button("Convert"):
    result = unit_converter(category, value, unit)
    if isinstance(result, int):
    st.success(f"The result is {float(result):.2f}")
    else:
    st.success(f"The result is {result:.2f}")
    # st.success(f"The result is {result:.2f}")    # result:.2f means k point(.) k baad 2 digits tk value aae...


        