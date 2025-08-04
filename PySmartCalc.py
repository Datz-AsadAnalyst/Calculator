import streamlit as st
import random
import math
import time
from datetime import datetime

# ---- Setup ----
st.set_page_config(page_title="🧮 Fun Calculator App", page_icon="🧠", layout="centered")

if 'history' not in st.session_state:
    st.session_state.history = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0

# ---- Banner ----
st.title("🧮 Math Magic in Motion! ✨")
st.markdown(f"""  
Datz Calculator 
========================
Welcome to the Fun Datz Calculator!
This is not just any calculator; it's a magical journey through numbers and operations!  
Let's make math fun and interactive!
               
---  
""")

# ---- Name Input ----
name = st.text_input("👤 Enter your name:")
if name:
    st.success(f"Welcome, {name}! Let’s calculate, play and learn math together! 💥")

# ---- Main Mode Selection ----
mode = st.selectbox("Select Mode", ["Basic Calculator", "Scientific Calculator", "Unit Converter", "Mini Game", "AI Math Assistant", "Learning Mode", "Timed Challenge"])

# ---- Basic Calculator ----
if mode == "Basic Calculator":
    op = st.selectbox("Choose operation:", ["Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗"])
    a = st.number_input("Enter first number:")
    b = st.number_input("Enter second number:")

    if st.button("Calculate"):
        result = None
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
                st.error("Negative number not allowed")

    elif sci_op == "Logarithm (log)":
        num = st.number_input("Enter number (positive only):")
        if st.button("Calculate Logarithm"):
            if num > 0:
                result = math.log10(num)
                st.success(f"Result: {result}")
                st.session_state.history.append(f"log({num}) = {result}")
            else:
                st.error("Logarithm undefined for non-positive values")

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
            st.session_state.history.append(f"{value} -> {result:.2f} {unit}")

    elif category == "Weight (kg <-> lbs)":
        direction = st.radio("Direction", ["Kg to Lbs", "Lbs to Kg"])
        if st.button("Convert"):
            result = value * 2.20462 if direction == "Kg to Lbs" else value / 2.20462
            unit = "lbs" if direction == "Kg to Lbs" else "kg"
            st.success(f"Converted: {result:.2f} {unit}")
            st.session_state.history.append(f"{value} -> {result:.2f} {unit}")

    elif category == "Temperature (°C <-> °F)":
        direction = st.radio("Direction", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
        if st.button("Convert"):
            result = (value * 9/5 + 32) if direction == "Celsius to Fahrenheit" else (value - 32) * 5/9
            unit = "°F" if direction == "Celsius to Fahrenheit" else "°C"
            st.success(f"Converted: {result:.2f} {unit}")
            st.session_state.history.append(f"{value} -> {result:.2f} {unit}")

# ---- Mini Games ----
elif mode == "Mini Game":
    st.subheader("🎮 Quick Math Game")
    q1 = random.randint(1, 10)
    q2 = random.randint(1, 10)
    correct = q1 * q2
    user_ans = st.number_input(f"What is {q1} × {q2}?", step=1)

    if st.button("Check Answer 🎯"):
        if user_ans == correct:
            st.success("🎉 Correct!")
            st.balloons()
        else:
            st.error(f"❌ Nope! The answer was {correct}")

# ---- AI Math Assistant ----
# elif mode == "AI Math Assistant":
#     import openai
#     st.subheader("🤖 Ask the AI Math Assistant")
#     api_key = st.text_input("🔑 OpenAI API Key", type="password")
#     query = st.text_area("Ask a math question (e.g., 'What is the integral of x^2?')")
#     if st.button("Get Answer 💬") and api_key:
#         try:
#             openai.api_key = api_key
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[{"role": "user", "content": query}]
#             )
#             result = response.choices[0].message["content"]
#             st.success("✅ Answer:")
#             st.write(result)
#         except Exception as e:
#             st.error(f"Error: {str(e)}")

# ---- Learning Mode ----
elif mode == "Learning Mode":
    if st.toggle("🎈 Enable Learning Mode"):
        num1 = st.slider("Pick a number 🐣", 0, 10)
        num2 = st.slider("Pick another number 🧸", 0, 10)
        st.write(f"✨ {num1} + {num2} = {num1 + num2} 🎉")
        st.info("🧩 Joke: Why did the student do multiplication on the floor? Because he was told not to use tables!")

# ---- Timed Challenge ----
elif mode == "Timed Challenge":
    st.subheader("⏳ Timed Math Challenge")
    q1 = random.randint(10, 99)
    q2 = random.randint(10, 99)
    correct = q1 + q2

    if st.button("🕹️ Start Challenge"):
        st.session_state.start_time = time.time()
        user_ans = st.number_input(f"Solve fast! What is {q1} + {q2}?", step=1)
        if st.button("Submit Answer"):
            time_taken = round(time.time() - st.session_state.start_time, 2)
            if user_ans == correct:
                st.success(f"✅ Correct! Time: {time_taken} sec")
                if time_taken < 10:
                    st.balloons()
            else:
                st.error(f"❌ Incorrect. Answer was {correct}")

# ---- History ----
if st.checkbox("📜 Show History"):
    st.markdown("### 🧾 Calculation History")
    if st.session_state.history:
        for item in st.session_state.history[::-1]:
            st.write("✅", item)
    else:
        st.info("No history yet!")

# ---- Footer ----
st.markdown("---")
st.markdown(
    "<div style='text-align:center; font-weight:bold; font-size:22px;'>"
    "Made with ❤️ by Asad ✨"
    "</div>",
    unsafe_allow_html=True,
)
# ---- Footer Section ----
st.markdown(
    "<div style='text-align:center; font-weight:bold; font-size:18px;'>"
    "Connect with me:"
    "</div>",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div style='text-align:center; font-size:18px; font-weight:bold;'>
        <a href='https://github.com/Datz-AsadAnalyst' 
           style='color:#FAFAFA; background-color:#5257AF; padding:8px 18px; border-radius:8px; text-decoration:none; display:inline-block; border:2px solid #000000;'>
            <b>GitHub</b>
        </a>
    </div>
    <div style='text-align:center; margin-top: 15px; color: rgba(255,255,255,0.7); font-size: 0.9em;'>
        © 2025 PySmartCalc  | All rights reserved.
        <br>
    </div>
    """,
    unsafe_allow_html=True,
)

