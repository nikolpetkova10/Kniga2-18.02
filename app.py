import streamlit as st
if "books" not in st.session_state:
  st.session_state.books = []

title = st.text_input("Title")
author = st.text_input("Author")

if st.button("Enter a book"):
  book = {
    "title": title, "author": author }
  st.session_state.books.append(book)
  st.success("The book is added!")

st.write("### List with books: ")
st.write(st.session_state.books)
                      
