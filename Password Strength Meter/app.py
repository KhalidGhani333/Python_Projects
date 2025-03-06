import streamlit as st
import re


#Title
st.title('🔐 Password Strength Meter')
st.markdown("Enter a password to check its strength:")

# Function to calculate password strength
def check_password_strenght(password:str) -> str:
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score += 1
    if re.search(r"\d",password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

     # Rating the password strength
    if score == 4:
        return '🟢 Strong Password'
    elif score == 3:
        return '🟡 Moderate Password'
    elif score == 2:
        return '🟠 Weak Password'
    else:
        return '🔴 Very Weak Password'

# Initialize session state for last 5 passwords
if 'last_passwords' not in st.session_state:
    st.session_state['last_passwords'] = []

# Input from the user
password = st.text_input("Password",type="password",placeholder="Enter Your Password Here...")


# Password strength check with duplicate password 
if password:
    if password in st.session_state['last_passwords']:
        st.error("❌ You have already used this password recently. Try a different one!")
    else:
        # Update the list of last 5 passwords
        st.session_state['last_passwords'].append(password)

# Keep only the last 5 passwords
        if len(st.session_state['last_passwords']) > 5:
            st.session_state['last_passwords'].pop(0)  
        
        # Display password strength
        strength = check_password_strenght(password)
        st.markdown(strength)

        if 'Very Weak' in strength:
            st.error('Your password is very weak! Use a mix of characters to improve it.')
        elif 'Weak' in strength:
            st.warning('Your password needs improvement! Consider adding uppercase, lowercase, numbers, and special characters.')
        elif 'Moderate' in strength:
            st.info('Your password is okay but could be stronger.')
        elif 'Strong' in strength:
            st.success('Great! Your password is strong.')

