# from your_module import Block, config  # Import necessary modules
import streamlit as st
from change_screen import *
import pyblock.config as config
from pyblock.blockchain.block import *
import time

def block_valid():
    return int(time.time()) - st.session_state.p2pserver.received_block.timestamp <= config.BLOCK_VALIDATOR_CHOOSE_INTERVAL

#CREATE A NEW BLOCK
def propose_block():
    st.title("Create A Block")
    st.write("You are the current block proposer.")

    #TABLE DATA TO SHOW TRANSACTIONS
    table_data = []
    
    #GET CURRENT MEMPOOL TRANSACTIONS
    transactions = st.session_state.p2pserver.transaction_pool.transactions
    
    #DICTIONARY MAPPING ID TO TRANSACTION
    transaction_dict = {
        transaction.id: transaction for transaction in transactions}

    #FOR EACH TRANSACTION
    for transaction in transactions:
        st.subheader(f"Transaction {transaction.id}")
        
        #WHETHER TO INCLUDE IN BLOCK OR NOT
        include_value = st.radio("Include in Block?", [
                                 "False", "True"], key=f"include_{transaction.id}")
        
        #WHETHER NEWS IS FAKE OR TRUE
        vote_value = st.radio("Vote on this Transaction?", [
                              "False", "True"], key=f"vote_{transaction.id}")
        
        #CREATE THE TABLE
        table_data.append({
            "ID": transaction.id,
            "IPFS Address": transaction.ipfs_address,
            "Model Score": transaction.model_score,
            "Sender Reputation": transaction.sender_reputation,
            "Include": include_value,
            "Vote": vote_value
        })

    # DISPLAY TABLE OF TRANSACTIONS WITH SELECT AND VOTE BUTTONS
    st.write("Choose transactions and vote on them:")
    
    #THE SELECTED TRANSACTIONS
    selected_transactions = st.multiselect(
        "Select transactions to Include in Block",
        table_data,
        default=[],
        key="transactions",
        format_func=lambda transaction: transaction["ID"]
    )

    # WARN USER IF MORE THAN ALLOWED TRANSACTIONS SELECTED
    max_selections = config.BLOCK_TRANSACTION_LIMIT
    if len(selected_transactions) > max_selections:
        st.warning(
            f"Maximum selections allowed: {max_selections}. Please deselect items.")

    # CONFIRM THE SELECTION AND VOTES
    if st.button("Create Block") and len(selected_transactions) <= max_selections:
        selected_transaction_objects = []
    
        for transaction in selected_transactions:
            if transaction["Include"] == True:
                transaction_object = transaction_dict[transaction["ID"]]
                if transaction["Vote"] == "True":
                    transaction.positive_votes.add(st.session_state.p2pserver.wallet.get_public_key())
                    
                else:
                    transaction.negative_votes.add(
                        st.session_state.p2pserver.wallet.get_public_key())

                    
                selected_transaction_objects.append(transaction_object)
        
        # CREATE A BLOCK WITH TRANSACTIONS (PASSED AS LIST)
        block = Block.create_block(
            lastBlock=st.session_state.blockchain.chain[-1],
            data=selected_transaction_objects,
            wallet=st.session_state.p2pserver.wallet,
            blockchain=st.session_state.p2pserver.blockchain
        )

        # BROADCAST THE BLOCK
        st.session_state.p2pserver.broadcast_block(block)

        # CONFIRMATION MESSAGE
        st.success("The created block was transmitted.")

    if st.button("Back"):
        change_screen(st.session_state.previous_screen)

    
def view_block_status():

    # IF USER IS THE CURRENT BLOCK PROPOSER
    if st.session_state.p2pserver.block_proposer == st.session_state.wallet.get_public_key():
       change_screen("propose_block")
       
    st.title("View Current Block Status")

    if st.session_state.p2pserver.received_block and block_valid():
        st.write("A valid block has been received.")
        if st.button("Vote on Received Block"):
            change_screen("vote_on_block")
        
    st.write("Current Block Proposer Public Key: ", st.session_state.p2pserver.block_proposer)
    if st.session_state.p2pserver.received_block:
        st.write("Current Confirmations on Receieved Block: ", len(st.session_state.p2pserver.received_block.votes))
    else:
        st.write("No Valid Block Received yet.")
        
    if st.button("Back"):
        change_screen(st.session_state.previous_screen)
            
    