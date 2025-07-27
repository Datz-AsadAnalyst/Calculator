import streamlit as st
import math
import random
from datetime import datetime

# ---- Set Page Config ----
st.set_page_config(page_title="Fun Streamlit Calculator", page_icon="🧮", layout="centered")

# ---- Banner Section ----
st.markdown(f"""
# 🧮 Math Magic in Motion! ✨  
**Streamlit Calculator | Powered by Python ⚙️ | {datetime.now().strftime('%Y-%m-%d')}**
---  
""")

# ---- Initialize History ----
if 'history' not in st.session_state:
    st.session_state.history = []

# ---- User Input ----
name = st.text_input("👤 Enter your name:")
if name:
    st.success(f"Welcome, {name}! Let’s calculate something amazing! 💥")

# ---- Calculator Type ----
mode = st.selectbox("What would you like to use?", ["Basic Calculator", "Scientific Calculator", "Unit Converter"])

# ---- Basic Calculator ----
if mode == "Basic Calculator":
    op = st.selectbox("Choose operation:", ["Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗"])
    a = st.number_input("Enter first number:")
    b = st.number_input("Enter second number:")

    if st.button("Calculate"):
        try:
            if op == "Addition ➕":
                result = a + b
            elif op == "Subtraction ➖":
                result = a - b
            elif op == "Multiplication ✖️":
                result = a * b
            elif op == "Division ➗":
                result = a / b if b != 0 else "Cannot divide by 0"
            st.success(f"Result: {result}")
            st.session_state.history.append(f"{op} of {a} and {b} = {result}")
        except Exception as e:
            st.error(str(e))

# ---- Scientific Calculator ----
elif mode == "Scientific Calculator":
    sci_op = st.selectbox("Choose function:", ["Logarithm (log)", "Square Root (√)", "Power (x^y)"])
    
    if sci_op == "Power (x^y)":
        base = st.number_input("Enter base:")
        exp = st.number_input("Enter exponent:")
        if st.button("Calculate Power"):
            result = math.pow(base, exp)
            st.success(f"Result: {result}")
            st.session_state.history.append(f"{base}^{exp} = {result}")
    
    elif sci_op == "Square Root (√)":
        num = st.number_input("Enter number:")
        if st.button("Calculate Square Root"):
            if num >= 0:
                result = math.sqrt(num)
                st.success(f"Result: {result}")
                st.session_state.history.append(f"√{num} = {result}")
            else:
                st.error("Square root of negative number is not real.")

    elif sci_op == "Logarithm (log)":
        num = st.number_input("Enter number (positive only):")
        if st.button("Calculate Logarithm"):
            if num > 0:
                result = math.log10(num)
                st.success(f"Result: {result}")
                st.session_state.history.append(f"log({num}) = {result}")
            else:
                st.error("Logarithm undefined for non-positive values.")

# ---- Unit Converter ----
elif mode == "Unit Converter":
    category = st.selectbox("Conversion Category", ["Length (meters <-> feet)", "Weight (kg <-> lbs)", "Temperature (°C <-> °F)"])
    value = st.number_input("Enter value to convert:")

    if category == "Length (meters <-> feet)":
        direction = st.radio("Direction", ["Meters to Feet", "Feet to Meters"])
        if st.button("Convert"):
            result = value * 3.28084 if direction == "Meters to Feet" else value / 3.28084
            unit = "feet" if direction == "Meters to Feet" else "meters"
            st.success(f"Converted: {result:.2f} {unit}")
            st.session_state.history.append(f"{value} converted to {result:.2f} {unit}")

    elif category == "Weight (kg <-> lbs)":
        direction = st.radio("Direction", ["Kg to Lbs", "Lbs to Kg"])
        if st.button("Convert"):
            result = value * 2.20462 if direction == "Kg to Lbs" else value / 2.20462
            unit = "lbs" if direction == "Kg to Lbs" else "kg"
            st.success(f"Converted: {result:.2f} {unit}")
            st.session_state.history.append(f"{value} converted to {result:.2f} {unit}")

    elif category == "Temperature (°C <-> °F)":
        direction = st.radio("Direction", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
        if st.button("Convert"):
            result = (value * 9/5 + 32) if direction == "Celsius to Fahrenheit" else (value - 32) * 5/9
            unit = "°F" if direction == "Celsius to Fahrenheit" else "°C"
            st.success(f"Converted: {result:.2f} {unit}")
            st.session_state.history.append(f"{value} converted to {result:.2f} {unit}")

# ---- Show Calculator History ----
if st.checkbox("📜 Show Calculation History"):
    st.markdown("### 🕘 Your Calculation History")
    if st.session_state.history:
        for item in st.session_state.history[::-1]:
            st.write("✅", item)
    else:
        st.info("No calculations yet.")

# ---- Fun Fact ----
math_facts = [
    "Zero is the only number that can't be represented in Roman numerals.",
    "A googol is the number 1 followed by 100 zeros.",
    "The number 9 is considered magical in many cultures.",
    "Multiplying any number by 9 and summing the digits gives 9.",
    "Math is the only place where you can make mistakes and still be 100% correct."
]
st.markdown("---")
st.markdown(f"📚 **Did You Know?** {random.choice(math_facts)}")

# ---- Footer ----
st.markdown("""
---
Made with ❤️ using Streamlit  
""")

