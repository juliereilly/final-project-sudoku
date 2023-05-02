import streamlit as st

st.set_page_config(page_title= "Super Sudoku", page_icon=":puzzle_piece:")


with st.container():
    st.title("Super Sudoku!")
    st.write("How to play Super Sudoku-The goal is to fill the the entire board, so each column, row, and 3x3 block contains the numbers 1-9 and only uses each number one time.")


with st.container():
    st.header("Play the Game Now!")
    st.write("To play the Super Sudoku game follow the GitHub link to copy the code and paste into the editer of your choice and then simply start playing")
    st.write("Happy solving! :wave:")
    st.write("[Play Now! > ](https://github.com/dominiquebissey/CIS1051FinalProject/blob/main/Super%20Sudoku%20Game)")

