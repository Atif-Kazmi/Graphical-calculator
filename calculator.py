import streamlit as st
import math

# Set up the title of the app
st.title("Scientific Calculator")

# Input fields for the user to enter numbers and choose operation
st.write("Enter the values below:")

# Number input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number (if applicable)", value=0.0)

# Operation selection
operation = st.selectbox(
    "Choose an operation",
    (
        "Addition", 
        "Subtraction", 
        "Multiplication", 
        "Division", 
        "Power", 
        "Square root", 
        "Logarithm (Base 10)", 
        "Exponential", 
        "Sine", 
        "Cosine", 
        "Tangent"
    )
)

# Initialize result variable
result = None

# Perform the chosen operation
if operation == "Addition":
    result = num1 + num2

elif operation == "Subtraction":
    result = num1 - num2

elif operation == "Multiplication":
    result = num1 * num2

elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Cannot divide by zero")

elif operation == "Power":
    result = num1 ** num2

elif operation == "Square root":
    if num1 >= 0:
        result = math.sqrt(num1)
    else:
        st.error("Cannot calculate the square root of a negative number")

elif operation == "Logarithm (Base 10)":
    if num1 > 0:
        result = math.log10(num1)
    else:
        st.error("Logarithm is only defined for positive numbers")

elif operation == "Exponential":
    result = math.exp(num1)

elif operation == "Sine":
    result = math.sin(math.radians(num1))

elif operation == "Cosine":
    result = math.cos(math.radians(num1))

elif operation == "Tangent":
    result = math.tan(math.radians(num1))

# Display the result
if result is not None:
    st.write(f"Result: {result}")
