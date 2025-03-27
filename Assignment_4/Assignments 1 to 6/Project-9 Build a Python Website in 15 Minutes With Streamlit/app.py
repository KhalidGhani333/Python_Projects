import streamlit as st
import random

st.title('Number Guessing Game')

# Initialize or reset the game
if 'target' not in st.session_state:
    st.session_state.target = random.randint(1, 50)
    st.session_state.attempts = 0

st.header('Guess a number between 1 and 100')

# Input from the user
guess = st.number_input('Enter your guess:', min_value=1, max_value=50, step=1)

if st.button('Submit Guess'):
    st.session_state.attempts += 1
    if guess < st.session_state.target:
        st.warning('Too low! Try a higher number.')
    elif guess > st.session_state.target:
        st.warning('Too high! Try a lower number.')
    else:
        st.success(f'Congratulations! You guessed it in {st.session_state.attempts} attempts.')
        if st.button('Play Again'):
            st.session_state.target = random.randint(1, 50)
            st.session_state.attempts = 0
