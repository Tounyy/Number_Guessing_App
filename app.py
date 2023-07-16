import streamlit as st
import random

if 'state' not in st.session_state:
    st.session_state['state'] = {'lives': 4}

st.markdown("<h1 style='text-align: center; color: white; font-size: 35px;'> Number Guessing Game </h1>", unsafe_allow_html=True)

select = range(1, 11)
computer = random.choice(select)
player = st.number_input("Vyberte číslo:", min_value=1, max_value=max(select), step=1)

if st.button('Guess'):
    if computer == player:
        st.markdown("<h1 style='text-align: center; color: white; font-size: 25px;'>Vyhrali jste hru!</h1>",
                    unsafe_allow_html=True)
        st.write("Číslo, které jste si vybral: " + str(player))
        st.write("Číslo, které si robot vybral: " + str(computer))
    elif computer > player or player > computer:
        st.session_state['state']['lives'] -= 1
        st.markdown("<h1 style='text-align: center; color: white; font-size: 25px;'>Prohráli jste hru!</h1>", unsafe_allow_html=True)
        st.write("Číslo, které jste si vybral: " + str(player))
        st.write("Číslo, které si robot vybral: " + str(computer))
        st.write("Zbývající životy:", st.session_state['state']['lives'])
        if st.session_state['state']['lives'] == 0:
            st.markdown("<h1 style='text-align: center; color: white; font-size: 25px;'>Vyčerpali jste všechny životy.</h1>", unsafe_allow_html=True)
            st.button('Resetovat')
            st.session_state['state']['lives'] = 4
