# SHOW ALL CURRENT TRANSACTIONS IN MEMPOOL
import streamlit as st
from change_screen import *
import pandas as pd
from datetime import datetime
from pyblock.ipfs.ipfs_handler import *


def show_transactions():
    st.title("Current Network Transactions")
    transac_pool = st.session_state.p2pserver.transaction_pool.transactions
    
    if len(transac_pool) < 1:
        st.write("The network doesn't have any mempool transactions currently. Please come back later.")
    
    else:
        table_data = []
        for transaction in transac_pool:
            content = IPFSHandler.get_from_ipfs(transaction.ipfs_address)
            table_data.append({
                "Model Score": transaction.model_score,
                "Sender Reputation": transaction.sender_reputation,
                "Sender Stake": st.session_state.p2pserver.blockchain.get_stake(transaction.sender_address),
                # "Is Auditor": 
                "Transaction Fee": transaction.fee,
                "Timestamp": datetime.fromtimestamp(transaction.timestamp).strftime("%I:%M %p on %d %B, %Y"),
                "Title": content.split("\n")[0],
                "Text": " ".join(content.split("\n")[1: ]),
                "Sender Address": transaction.sender_address,
                "ID": transaction.id
            })

        st.dataframe(pd.DataFrame(table_data), height=500)

    if st.button("Back"):
        change_screen(st.session_state.previous_screen)
