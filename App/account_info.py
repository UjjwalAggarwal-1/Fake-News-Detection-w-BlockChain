from pyblock.wallet.transaction import PartialTransaction, Transaction
import streamlit as st
from change_screen import *

def show_account_info():
    st.title("ACCOUNT INFORMATION")
    balance = st.session_state.blockchain.get_balance(
        st.session_state.wallet.public_key)
    public_key = st.session_state.wallet.get_public_key()
    st.write("BALANCE = ", balance)
    st.write("PUBLIC KEY = ", public_key)

    if st.button("Back"):
        # Set the previous screen in the session state
        change_screen(st.session_state.previous_screen)