import streamlit as st
import random
import math
import time
from datetime import datetime

# ---- Setup ----
st.set_page_config(page_title="🧮 Fun Calculator App", page_icon="🧠", layout="centered")

# ---- Custom CSS Styling ----
st.markdown("""
<style># ---- Enhanced Name Input Section ----
st.markdown('<div class="mode-selector">', unsafe_allow_html=True)
name = st.text_input("👤 Enter your name:", placeholder="Type your name here...")
if name:
    st.success(f"🎉 Welcome, {name}! Let's calculate, play and learn math together! 💥")
st.markdown('</div>', unsafe_allow_html=True)

# ---- Enhanced Mode Selection ----
st.markdown('<div class="mode-selector">', unsafe_allow_html=True)
st.markdown("### 🎮 Choose Your Adventure:")
mode = st.selectbox("Select Mode", ["Basic Calculator", "Scientific Calculator", "Unit Converter", "Mini Game", "AI Math Assistant", "Learning Mode", "Timed Challenge"], help="Pick a mode to get started with your mathematical journey!")
st.markdown('</div>', unsafe_allow_html=True) Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
    }
    
    /* Title styling */
    .main-title {
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
        background-size: 400% 400%;
        animation: gradient 3s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Banner styling */
    .banner {
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        margin-bottom: 30px;
        border: 2px solid rgba(255,255,255,0.2);
    }
    
    .banner-text {
        color: white;
        font-size: 1.2rem;
        text-align: center;
        font-weight: 500;
        line-height: 1.6;
    }
    
    /* Mode selector styling */
    .mode-selector {
        background: rgba(255,255,255,0.1);
        padding: 20px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        margin-bottom: 25px;
    }
    
    /* Calculator section styling */
    .calc-section {
        background: rgba(255,255,255,0.95);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        border: 2px solid rgba(102,126,234,0.3);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #764ba2, #667eea);
    }
    
    /* Input field styling */
    .stNumberInput input {
        border-radius: 10px;
        border: 2px solid #667eea;
        padding: 10px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stNumberInput input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 10px rgba(102,126,234,0.3);
    }
    
    .stTextInput input {
        border-radius: 10px;
        border: 2px solid #667eea;
        padding: 10px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 10px rgba(102,126,234,0.3);
    }
    
    /* Selectbox styling */
    .stSelectbox select {
        border-radius: 10px;
        border: 2px solid #667eea;
        padding: 10px;
        font-size: 16px;
        background: white;
    }
    
    /* Success message styling */
    .stSuccess {
        background: linear-gradient(90deg, #56ab2f, #a8e6cf);
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #56ab2f;
    }
    
    /* Error message styling */
    .stError {
        background: linear-gradient(90deg, #ff416c, #ff4b2b);
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #ff416c;
    }
    
    /* Info message styling */
    .stInfo {
        background: linear-gradient(90deg, #4facfe, #00f2fe);
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #4facfe;
    }
    
    /* History section styling */
    .history-section {
        background: rgba(255,255,255,0.9);
        padding: 20px;
        border-radius: 12px;
        border: 2px solid rgba(102,126,234,0.3);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    /* Footer styling */
    .footer {
        background: linear-gradient(90deg, #667eea, #764ba2);
        padding: 25px;
        border-radius: 15px;
        margin-top: 30px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .footer-text {
        color: white;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 15px;
    }
    
    .github-btn {
        background: linear-gradient(45deg, #333, #666);
        color: white;
        padding: 12px 25px;
        border-radius: 25px;
        text-decoration: none;
        display: inline-block;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        border: 2px solid white;
    }
    
    .github-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        background: linear-gradient(45deg, #555, #888);
    }
    
    /* Game section styling */
    .game-section {
        background: linear-gradient(135deg, #ff9a9e, #fecfef);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        margin-bottom: 20px;
        border: 2px solid rgba(255,255,255,0.3);
    }
    
    /* Scientific calculator styling */
    .sci-calc {
        background: linear-gradient(135deg, #a8edea, #fed6e3);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }
    
    /* Converter styling */
    .converter {
        background: linear-gradient(135deg, #d299c2, #fef9d7);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        margin-bottom: 20px;
    }
    
    /* Animated background */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
</style>
""", unsafe_allow_html=True)

# ---- Session State Initialization ----
if 'history' not in st.session_state:
    st.session_state.history = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0

# ---- Enhanced Header Section ----
st.markdown('<h1 class="main-title">🧮 Math Magic in Motion! ✨</h1>', unsafe_allow_html=True)

# Enhanced Banner
st.markdown("""
<div class="banner">
    <div class="banner-text">
        🚀 <strong>Datz Calculator - Your Ultimate Mathematical Companion!</strong> 🚀<br>
        ✨ Welcome to the Fun Datz Calculator! ✨<br>
        🎯 This is not just any calculator; it's a magical journey through numbers and operations!<br>
        🔥 Let's make math fun and interactive!
    </div>
</div>
""", unsafe_allow_html=True)

# ---- Name Input ----
name = st.text_input("👤 Enter your name:")
if name:
    st.success(f"Welcome, {name}! Let’s calculate, play and learn math together! 💥")

# ---- Main Mode Selection ----
mode = st.selectbox("Select Mode", ["Basic Calculator", "Scientific Calculator", "Unit Converter", "Mini Game", "AI Math Assistant", "Learning Mode", "Timed Challenge"])

# ---- Enhanced Basic Calculator ----
if mode == "Basic Calculator":
    st.markdown('<div class="calc-section">', unsafe_allow_html=True)
    st.markdown("### 🧮 Basic Calculator")
    st.markdown("Perform simple arithmetic operations with style!")
    
    op = st.selectbox("Choose operation:", ["Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗"], help="Select the operation you want to perform")
    
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Enter first number:", format="%.6f", help="Type your first number here")
    with col2:
        b = st.number_input("Enter second number:", format="%.6f", help="Type your second number here")

    if st.button("🚀 Calculate", key="basic_calc"):
        result = None
        operation_symbol = ""
        
        if op == "Addition ➕":
            result = a + b
            operation_symbol = "+"
        elif op == "Subtraction ➖":
            result = a - b
            operation_symbol = "-"
        elif op == "Multiplication ✖️":
            result = a * b
            operation_symbol = "×"
        elif op == "Division ➗":
            if b != 0:
                result = a / b
                operation_symbol = "÷"
            else:
                st.error("🚫 Cannot divide by zero!")
                result = "Error"

        if result != "Error":
            st.markdown(f"""
            <div style="background: linear-gradient(45deg, #56ab2f, #a8e6cf); 
                        padding: 20px; border-radius: 15px; text-align: center; 
                        box-shadow: 0 5px 15px rgba(0,0,0,0.2); margin: 15px 0;">
                <h2 style="color: white; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                    🎉 {a} {operation_symbol} {b} = <span style="font-size: 1.5em;">{result}</span>
                </h2>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.history.append(f"{op} of {a} and {b} = {result}")
            
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Enhanced Scientific Calculator ----
elif mode == "Scientific Calculator":
    st.markdown('<div class="sci-calc">', unsafe_allow_html=True)
    st.markdown("### 🔬 Scientific Calculator")
    st.markdown("Explore advanced mathematical functions with beautiful visualizations!")
    
    sci_op = st.selectbox("Choose function:", ["Logarithm (log)", "Square Root (√)", "Power (x^y)", "Trigonometry"], help="Select an advanced mathematical operation")
    
    if sci_op == "Power (x^y)":
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Enter base:", format="%.6f")
        with col2:
            exp = st.number_input("Enter exponent:", format="%.6f")
            
        if st.button("🚀 Calculate Power", key="power_calc"):
            result = math.pow(base, exp)
            st.markdown(f"""
            <div style="background: linear-gradient(45deg, #a8edea, #fed6e3); 
                        padding: 20px; border-radius: 15px; text-align: center; 
                        box-shadow: 0 5px 15px rgba(0,0,0,0.2); margin: 15px 0;">
                <h2 style="color: #333; margin: 0;">
                    ⚡ {base}<sup>{exp}</sup> = <span style="font-size: 1.5em; color: #667eea;">{result}</span>
                </h2>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.history.append(f"{base}^{exp} = {result}")

    elif sci_op == "Square Root (√)":
        num = st.number_input("Enter number:", format="%.6f", min_value=0.0, help="Enter a non-negative number")
        if st.button("🚀 Calculate Square Root", key="sqrt_calc"):
            if num >= 0:
                result = math.sqrt(num)
                st.markdown(f"""
                <div style="background: linear-gradient(45deg, #a8edea, #fed6e3); 
                            padding: 20px; border-radius: 15px; text-align: center; 
                            box-shadow: 0 5px 15px rgba(0,0,0,0.2); margin: 15px 0;">
                    <h2 style="color: #333; margin: 0;">
                        📐 √{num} = <span style="font-size: 1.5em; color: #667eea;">{result}</span>
                    </h2>
                </div>
                """, unsafe_allow_html=True)
                st.session_state.history.append(f"√{num} = {result}")
            else:
                st.error("🚫 Negative number not allowed for square root!")

    elif sci_op == "Logarithm (log)":
        num = st.number_input("Enter number (positive only):", format="%.6f", min_value=0.000001, help="Enter a positive number")
        if st.button("🚀 Calculate Logarithm", key="log_calc"):
            if num > 0:
                result = math.log10(num)
                st.markdown(f"""
                <div style="background: linear-gradient(45deg, #a8edea, #fed6e3); 
                            padding: 20px; border-radius: 15px; text-align: center; 
                            box-shadow: 0 5px 15px rgba(0,0,0,0.2); margin: 15px 0;">
                    <h2 style="color: #333; margin: 0;">
                        📊 log₁₀({num}) = <span style="font-size: 1.5em; color: #667eea;">{result}</span>
                    </h2>
                </div>
                """, unsafe_allow_html=True)
                st.session_state.history.append(f"log({num}) = {result}")
            else:
                st.error("🚫 Logarithm undefined for non-positive values!")
                
    elif sci_op == "Trigonometry":
        angle = st.number_input("Enter angle in degrees:", format="%.6f")
        trig_func = st.selectbox("Choose function:", ["Sin", "Cos", "Tan"])
        
        if st.button(f"🚀 Calculate {trig_func}", key="trig_calc"):
            radians = math.radians(angle)
            if trig_func == "Sin":
                result = math.sin(radians)
                symbol = "sin"
            elif trig_func == "Cos":
                result = math.cos(radians)
                symbol = "cos"
            else:  # Tan
                result = math.tan(radians)
                symbol = "tan"
                
            st.markdown(f"""
            <div style="background: linear-gradient(45deg, #a8edea, #fed6e3); 
                        padding: 20px; border-radius: 15px; text-align: center; 
                        box-shadow: 0 5px 15px rgba(0,0,0,0.2); margin: 15px 0;">
                <h2 style="color: #333; margin: 0;">
                    📐 {symbol}({angle}°) = <span style="font-size: 1.5em; color: #667eea;">{result:.6f}</span>
                </h2>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.history.append(f"{symbol}({angle}°) = {result}")
            
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Enhanced Unit Converter ----
elif mode == "Unit Converter":
    st.markdown('<div class="converter">', unsafe_allow_html=True)
    st.markdown("### 🔄 Unit Converter")
    st.markdown("Convert between different units with precision and style!")
    
    category = st.selectbox("Conversion Category", ["Length (meters <-> feet)", "Weight (kg <-> lbs)", "Temperature (°C <-> °F)"], help="Choose the type of conversion you need")
    value = st.number_input("Enter value to convert:", format="%.6f", help="Input the value you want to convert")

    if category == "Length (meters <-> feet)":
        direction = st.radio("Direction", ["Meters to Feet", "Feet to Meters"], horizontal=True)
        if st.button("🚀 Convert Length", key="length_convert"):
            result = value * 3.28084 if direction == "Meters to Feet" else value / 3.28084
            unit_from = "meters" if direction == "Meters to Feet" else "feet"
            unit_to = "feet" if direction == "Meters to Feet" else "meters"
            
            st.markdown(f"""
            <div style="background: linear-gradient(45deg, #d299c2, #fef9d7); 
                        padding: 20px; border-radius: 15px; text-align: center; 
                        box-shadow: 0 5px 15px rgba(0,0,0,0.2); margin: 15px 0;">
                <h2 style="color: #333; margin: 0;">
                    📏 {value} {unit_from} = <span style="font-size: 1.5em; color: #667eea;">{result:.4f} {unit_to}</span>
                </h2>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.history.append(f"{value} {unit_from} -> {result:.4f} {unit_to}")

    elif category == "Weight (kg <-> lbs)":
        direction = st.radio("Direction", ["Kg to Lbs", "Lbs to Kg"], horizontal=True)
        if st.button("🚀 Convert Weight", key="weight_convert"):
            result = value * 2.20462 if direction == "Kg to Lbs" else value / 2.20462
            unit_from = "kg" if direction == "Kg to Lbs" else "lbs"
            unit_to = "lbs" if direction == "Kg to Lbs" else "kg"
            
            st.markdown(f"""
            <div style="background: linear-gradient(45deg, #d299c2, #fef9d7); 
                        padding: 20px; border-radius: 15px; text-align: center; 
                        box-shadow: 0 5px 15px rgba(0,0,0,0.2); margin: 15px 0;">
                <h2 style="color: #333; margin: 0;">
                    ⚖️ {value} {unit_from} = <span style="font-size: 1.5em; color: #667eea;">{result:.4f} {unit_to}</span>
                </h2>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.history.append(f"{value} {unit_from} -> {result:.4f} {unit_to}")

    elif category == "Temperature (°C <-> °F)":
        direction = st.radio("Direction", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"], horizontal=True)
        if st.button("🚀 Convert Temperature", key="temp_convert"):
            result = (value * 9/5 + 32) if direction == "Celsius to Fahrenheit" else (value - 32) * 5/9
            unit_from = "°C" if direction == "Celsius to Fahrenheit" else "°F"
            unit_to = "°F" if direction == "Celsius to Fahrenheit" else "°C"
            
            st.markdown(f"""
            <div style="background: linear-gradient(45deg, #d299c2, #fef9d7); 
                        padding: 20px; border-radius: 15px; text-align: center; 
                        box-shadow: 0 5px 15px rgba(0,0,0,0.2); margin: 15px 0;">
                <h2 style="color: #333; margin: 0;">
                    🌡️ {value}{unit_from} = <span style="font-size: 1.5em; color: #667eea;">{result:.2f}{unit_to}</span>
                </h2>
            </div>
            """, unsafe_allow_html=True)
            st.session_state.history.append(f"{value}{unit_from} -> {result:.2f}{unit_to}")
            
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Enhanced Mini Games ----
elif mode == "Mini Game":
    st.markdown('<div class="game-section">', unsafe_allow_html=True)
    st.markdown("### 🎮 Quick Math Game")
    st.markdown("Test your mental math skills with this fun challenge!")
    
    # Initialize game state
    if 'game_question' not in st.session_state:
        st.session_state.game_question = (random.randint(1, 10), random.randint(1, 10))
        st.session_state.game_score = 0
        st.session_state.game_attempts = 0
    
    q1, q2 = st.session_state.game_question
    correct = q1 * q2
    
    st.markdown(f"""
    <div style="background: rgba(255,255,255,0.3); padding: 20px; border-radius: 15px; 
                backdrop-filter: blur(10px); margin: 15px 0; text-align: center;">
        <h2 style="color: #333; margin-bottom: 15px;">
            🎯 Score: {st.session_state.game_score} | Attempts: {st.session_state.game_attempts}
        </h2>
        <h1 style="color: #667eea; font-size: 2.5em; margin: 0;">
            What is {q1} × {q2}?
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    user_ans = st.number_input("Your answer:", step=1, key="game_answer")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎯 Check Answer", key="check_game"):
            st.session_state.game_attempts += 1
            if user_ans == correct:
                st.session_state.game_score += 1
                st.markdown("""
                <div style="background: linear-gradient(45deg, #56ab2f, #a8e6cf); 
                            padding: 15px; border-radius: 10px; text-align: center; margin: 10px 0;">
                    <h2 style="color: white; margin: 0;">🎉 Correct! Well done!</h2>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()
            else:
                st.markdown(f"""
                <div style="background: linear-gradient(45deg, #ff416c, #ff4b2b); 
                            padding: 15px; border-radius: 10px; text-align: center; margin: 10px 0;">
                    <h2 style="color: white; margin: 0;">❌ Not quite! The answer was {correct}</h2>
                </div>
                """, unsafe_allow_html=True)
            
            # Generate new question
            st.session_state.game_question = (random.randint(1, 10), random.randint(1, 10))
            
    with col2:
        if st.button("🔄 New Question", key="new_question"):
            st.session_state.game_question = (random.randint(1, 10), random.randint(1, 10))
            
    # Accuracy calculation
    if st.session_state.game_attempts > 0:
        accuracy = (st.session_state.game_score / st.session_state.game_attempts) * 100
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px; 
                    text-align: center; margin: 15px 0;">
            <h3 style="color: #333; margin: 0;">
                🎯 Accuracy: {accuracy:.1f}%
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Enhanced AI Math Assistant (Currently Disabled) ----
elif mode == "AI Math Assistant":
    st.markdown('<div class="calc-section">', unsafe_allow_html=True)
    st.markdown("### 🤖 AI Math Assistant")
    st.markdown("Get help with complex mathematical problems using AI!")
    
    st.warning("🔧 **Feature Under Development**: This feature requires an OpenAI API key to function.")
    
    st.markdown("""
    **What you could ask:**
    - "What is the derivative of x²?"
    - "Solve the equation 2x + 5 = 13"
    - "Explain the Pythagorean theorem"
    - "How do I calculate compound interest?"
    """)
    
    api_key = st.text_input("🔑 OpenAI API Key", type="password", help="Enter your OpenAI API key to enable AI assistance")
    query = st.text_area("Ask a math question:", placeholder="e.g., 'What is the integral of x^2?'", help="Type your mathematical question here")
    
    if st.button("💬 Get AI Answer", key="ai_answer"):
        if not api_key:
            st.error("Please enter your OpenAI API key to use this feature.")
        elif not query:
            st.error("Please enter a math question.")
        else:
            st.info("🚀 This feature will be available soon! For now, try the other calculator modes.")
            
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Enhanced Learning Mode ----
elif mode == "Learning Mode":
    st.markdown('<div class="calc-section">', unsafe_allow_html=True)
    st.markdown("### 🎓 Learning Mode")
    st.markdown("Interactive learning with visual feedback and educational content!")
    
    if st.toggle("🎈 Enable Learning Mode", help="Turn on interactive learning features"):
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.slider("Pick a number 🐣", 0, 20, help="Choose your first number")
        with col2:
            num2 = st.slider("Pick another number 🧸", 0, 20, help="Choose your second number")
            
        operation = st.selectbox("Choose operation:", ["Addition ➕", "Subtraction ➖", "Multiplication ✖️"])
        
        if operation == "Addition ➕":
            result = num1 + num2
            symbol = "+"
        elif operation == "Subtraction ➖":
            result = num1 - num2
            symbol = "-"
        else:  # Multiplication
            result = num1 * num2
            symbol = "×"
            
        st.markdown(f"""
        <div style="background: linear-gradient(45deg, #667eea, #764ba2); 
                    padding: 25px; border-radius: 15px; text-align: center; 
                    box-shadow: 0 8px 20px rgba(0,0,0,0.3); margin: 20px 0;">
            <h1 style="color: white; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                ✨ {num1} {symbol} {num2} = <span style="font-size: 1.5em; color: #ffd700;">{result}</span> 🎉
            </h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("🧩 **Math Joke:** Why did the student do multiplication on the floor? Because he was told not to use tables! 😄")
        
        # Visual representation for small numbers
        if num1 <= 10 and num2 <= 10 and operation == "Addition ➕":
            dots1 = "🔵 " * num1
            dots2 = "🔴 " * num2
            result_dots = "🟢 " * result
            st.markdown(f"""
            **Visual Representation:**
            - First number: {dots1}
            - Second number: {dots2}
            - **Result:** {result_dots}
            """)
            
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Enhanced Timed Challenge ----
elif mode == "Timed Challenge":
    st.markdown('<div class="game-section">', unsafe_allow_html=True)
    st.markdown("### ⏳ Timed Math Challenge")
    st.markdown("Test your speed and accuracy under pressure!")
    
    # Initialize challenge state
    if 'challenge_active' not in st.session_state:
        st.session_state.challenge_active = False
        st.session_state.challenge_question = (random.randint(10, 99), random.randint(10, 99))
        st.session_state.challenge_score = 0
        st.session_state.challenge_attempts = 0
    
    q1, q2 = st.session_state.challenge_question
    correct = q1 + q2
    
    if not st.session_state.challenge_active:
        st.markdown("""
        <div style="background: rgba(255,255,255,0.3); padding: 20px; border-radius: 15px; 
                    backdrop-filter: blur(10px); margin: 15px 0; text-align: center;">
            <h2 style="color: #333;">Ready for the challenge? 🚀</h2>
            <p style="color: #666; font-size: 1.1em;">Solve as many problems as you can!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🕹️ Start Challenge", key="start_challenge"):
            st.session_state.start_time = time.time()
            st.session_state.challenge_active = True
            st.rerun()
    else:
        time_elapsed = time.time() - st.session_state.start_time
        
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.3); padding: 20px; border-radius: 15px; 
                    backdrop-filter: blur(10px); margin: 15px 0; text-align: center;">
            <h2 style="color: #333;">⏱️ Time: {time_elapsed:.1f}s | Score: {st.session_state.challenge_score}</h2>
            <h1 style="color: #667eea; font-size: 2.5em; margin: 0;">
                What is {q1} + {q2}?
            </h1>
        </div>
        """, unsafe_allow_html=True)
        
        user_ans = st.number_input("Your answer:", step=1, key="challenge_answer")
        
        if st.button("Submit Answer", key="submit_challenge"):
            st.session_state.challenge_attempts += 1
            if user_ans == correct:
                st.session_state.challenge_score += 1
                st.success(f"✅ Correct! Time: {time_elapsed:.1f} sec")
                if time_elapsed < 10:
                    st.balloons()
            else:
                st.error(f"❌ Incorrect. Answer was {correct}")
            
            # Generate new question
            st.session_state.challenge_question = (random.randint(10, 99), random.randint(10, 99))
            st.session_state.start_time = time.time()
            
        if st.button("🛑 End Challenge", key="end_challenge"):
            st.session_state.challenge_active = False
            final_time = time_elapsed
            accuracy = (st.session_state.challenge_score / max(st.session_state.challenge_attempts, 1)) * 100
            
            st.markdown(f"""
            <div style="background: linear-gradient(45deg, #56ab2f, #a8e6cf); 
                        padding: 20px; border-radius: 15px; text-align: center; margin: 15px 0;">
                <h2 style="color: white; margin: 0;">🏆 Challenge Complete!</h2>
                <p style="color: white; margin: 5px 0;">Score: {st.session_state.challenge_score}/{st.session_state.challenge_attempts}</p>
                <p style="color: white; margin: 5px 0;">Accuracy: {accuracy:.1f}%</p>
                <p style="color: white; margin: 5px 0;">Total Time: {final_time:.1f} seconds</p>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Enhanced History Section ----
if st.checkbox("📜 Show Calculation History", help="View your calculation history"):
    st.markdown('<div class="history-section">', unsafe_allow_html=True)
    st.markdown("### 🧾 Calculation History")
    
    if st.session_state.history:
        st.markdown("**Recent calculations:**")
        for i, item in enumerate(st.session_state.history[::-1][:10], 1):  # Show last 10 items
            st.markdown(f"""
            <div style="background: rgba(102,126,234,0.1); padding: 10px; border-radius: 8px; 
                        margin: 5px 0; border-left: 4px solid #667eea;">
                <span style="font-weight: bold; color: #667eea;">#{i}</span> {item}
            </div>
            """, unsafe_allow_html=True)
            
        if len(st.session_state.history) > 10:
            st.info(f"Showing 10 most recent calculations. Total: {len(st.session_state.history)}")
            
        # Clear history button
        if st.button("🗑️ Clear History", key="clear_history"):
            st.session_state.history = []
            st.success("History cleared!")
            st.rerun()
    else:
        st.markdown("""
        <div style="background: rgba(102,126,234,0.1); padding: 20px; border-radius: 10px; 
                    text-align: center; margin: 15px 0;">
            <h3 style="color: #667eea; margin: 0;">📋 No calculations yet!</h3>
            <p style="color: #666; margin: 5px 0;">Start calculating to see your history here.</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Enhanced Footer Section ----
st.markdown("---")

st.markdown("""
<div class="footer">
    <div class="footer-text">
        Made with ❤️ by Asad ✨
    </div>
    <div style="margin: 15px 0;">
        <p style="color: white; font-size: 1.1em; margin: 10px 0;">
            🚀 Thank you for using Datz Calculator! 🚀
        </p>
        <p style="color: rgba(255,255,255,0.8); margin: 10px 0;">
            Keep calculating, keep learning! 📚✨
        </p>
    </div>
    <div style="margin-top: 20px;">
        <a href='https://github.com/Datz-AsadAnalyst' class="github-btn">
            🐙 Connect on GitHub
        </a>
    </div>
    <div style="margin-top: 15px; color: rgba(255,255,255,0.7); font-size: 0.9em;">
        © 2025 Datz Calculator | Enhanced with Beautiful UI
    </div>
</div>
""", unsafe_allow_html=True)

