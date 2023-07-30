import streamlit as st
import random

# Initialization Session State
if 'lives' not in st.session_state:
    st.session_state['lives'] = 3

# Nadpis
st.markdown("<h1 style='text-align: center; color: white; font-size: 35px;'> Number Guessing Game </h1>", unsafe_allow_html=True)

# Počítač
select = range(1, 11)
if 'computer' not in st.session_state:
    st.session_state['computer'] = random.choice(select)

# Hráč
player = st.number_input("Vyberte číslo:", min_value=1,max_value=max(select), step=1)

# Funkce restartování hry
def reset_game():
    st.session_state['lives'] = 3
    st.session_state['computer'] = st.session_state['computer'] = random.choice(select)

if st.button('Click'):
    if st.session_state['computer'] == player:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 25px;'>Vyhrali jste hru!</h1>", unsafe_allow_html=True)
        st.write("Číslo, které jste si vybral: " + str(player))
        st.write("Číslo, které si robot vybral: " + str(st.session_state['computer']))
        reset_game()
    elif st.session_state['computer'] > player or player > st.session_state['computer']:
        st.write("Zbývající životy:", st.session_state.lives)
        st.session_state['lives'] -= 1
        st.write("Číslo, které jste si vybral: " + str(player))
    if st.session_state['lives'] == -1:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 25px'>Prohráli jste hru!</h1>", unsafe_allow_html=True)
        st.write("Číslo, které si robot vybral: " + str(st.session_state['computer']))
        reset_game()
    if st.button("Restartovat Hru"):
        reset_game()
