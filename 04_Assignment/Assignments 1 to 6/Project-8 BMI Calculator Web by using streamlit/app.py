import streamlit as st



# App title and introduction
st.title("📏 BMI (Body Mass Index) Calculator")
st.write("Calculate your BMI to find out if you're underweight, normal weight, overweight, or obese.")

# Input sliders for height and weight
height = st.slider("Select your height (in cm):", min_value=100, max_value=250, value=175, step=1)
weight = st.slider("Select your weight (in kg):", min_value=40, max_value=150, value=60, step=1)

# Calculate BMI
bmi = weight / ((height / 100) ** 2)

# Display the BMI result
st.subheader(f"Your BMI is: {bmi:.2f}")

# Determine BMI category
if bmi < 18.5:
    st.error("You are underweight. 🥗 Consider a balanced diet to reach a healthy weight.")
elif 18.5 <= bmi < 24.9:
    st.success("You have a normal weight. 🥳 Keep up the good work!")
elif 25 <= bmi < 29.9:
    st.warning("You are overweight. 🏃‍♂️ Consider regular exercise and a healthy diet.")
else:
    st.error("You are in the obese category.It's important to consult with a healthcare provider.")

# Display BMI categoriespip install streamlit
with st.expander("ℹ️ About BMI Categories"):
    st.write("""
    - **Underweight:** BMI less than 18.5  
    - **Normal weight:** BMI between 18.5 and 24.9  
    - **Overweight:** BMI between 25 and 29.9  
    - **Obesity:** BMI 30 or greater  
    """)
