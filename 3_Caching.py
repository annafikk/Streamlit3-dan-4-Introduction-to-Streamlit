import streamlit as st

# Define a function to be cached
@st.cache_data
def expensive_computation(input_value):
    # Simulate a time-consuming computation
    result = input_value ** 2
    return result

# Streamlit app
st.title("Streamlit Caching Example")

# Input widget to get a user's input
input_value = st.slider("Enter a value", 1, 100, 1)

# Call the cached function
result = expensive_computation(input_value)

# Display the result
st.write(f"Result of expensive computation: {result}")
