import streamlit as st

# Set the page config
st.set_page_config(page_title="Fun Streamlit Calculator", page_icon="🧮", layout="centered")

# Title
st.title("🧮 Welcome to the Fun Calculator!")
st.markdown("### Let's do some cool math 🧠")

# User input
name = st.text_input("👤 Enter your name:")

# Show greeting once name is entered
if name:
    st.success(f"Hello, {name}! Let's calculate something awesome today! 💥")

# Select operation
operation = st.selectbox(
    "Choose a math operation 🔢",
    ["Select", "Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗"]
)

# Number input
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number:", format="%.2f")
with col2:
    num2 = st.number_input("Enter second number:", format="%.2f")

# Function to perform calculations
def calculate(op, x, y):
    try:
        if op == "Addition ➕":
            return x + y, "That's a sweet sum! 🍬"
        elif op == "Subtraction ➖":
            return x - y, "Subtracting like a pro! 🧮"
        elif op == "Multiplication ✖️":
            return x * y, "You're multiplying powerfully! 💪"
        elif op == "Division ➗":
            if y == 0:
                return None, "Oops! Division by zero is not allowed. 🚫"
            return x / y, "Clean divide! ✨"
    except Exception as e:
        return None, f"Error: {str(e)}"

# Calculate on button press
if st.button("Calculate 🔍") and operation != "Select":
    result, msg = calculate(operation, num1, num2)
    if result is not None:
        st.success(f"Result: **{result:.2f}**")
        st.info(msg)
    else:
        st.error(msg)
elif operation == "Select" and st.button("Calculate 🔍"):
    st.warning("Please select a valid operation first! ⚠️")

# Add a fun math tip or random fact
import random
math_facts = [
    "Did you know? Zero is the only number that can't be represented in Roman numerals. 🏛️",
    "A 'googol' is the number 1 followed by 100 zeros. 🤯",
    "The number 9 is considered magical in many cultures! 🧙",
    "Multiplying any number by 9 and summing the digits always gives 9. Try it! 🔄",
    "Math is the only subject where you can make hundreds of mistakes and still be 100% correct. 💯"
]

if name:
    st.markdown("---")
    st.subheader("🎉 Fun Math Fact:")
    st.write(random.choice(math_facts))

# Footer
st.markdown("""
---
🧠 Built with Streamlit by [Your Name]
""")
