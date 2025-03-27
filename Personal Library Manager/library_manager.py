import streamlit as st
import json  # Use as a database to store books data

# Load and save library data
FILENAME = "library.json"

def load_library():                       # Reads the library.json file.
    try:
        with open(FILENAME, "r") as file:  # Read as a file
            return json.load(file)         # If the file exists, it reads and returns the stored books.
    except :                               # FileNotFoundError
        return []

def save_library(library):
    with open(FILENAME, "w") as file:
        json.dump(library, file, indent=4)

# Load the existing library data
library = load_library()

# Enhanced UI
st.set_page_config(page_title="Personal Library Manager", page_icon="📚", layout="wide")
st.title("📚 Personal Library Manager")
st.markdown("---")

menu = st.sidebar.radio("📌 Select an option", ["➕ Add Book","📖 View Library", "❌ Remove Book", "🔍 Search Book", "📊 Library Statistics"])

if menu == "📖 View Library":
    st.header("📚 Your Library")
    if library:
        st.table(library)
    else:
        st.warning("No books in library. Add some books!")

elif menu == "➕ Add Book":
    st.header("➕ Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("📖 Title")
        author = st.text_input("✍️ Author")
        year = st.number_input("📅 Year" ,min_value=1990 ,max_value=2025)
        genre = st.text_input("🎭 Genre")
        read_status = st.checkbox("✅ Mark as Read")
        submit = st.form_submit_button("📥 Add Book")
        
        if submit:
            if not title or not author or not year or not genre:
                st.error("❌ All fields must be filled before adding a book!")
            else:
                library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
                save_library(library)
                st.success("📘 Book added successfully!")
           

elif menu == "❌ Remove Book":
    st.header("❌ Remove a Book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("📌 Select a book to remove", book_titles)
        if st.button("🗑 Remove Book", key="remove_btn"):
            library = [book for book in library if book["title"] != selected_book]
            save_library(library)
            st.success("🗑 Book removed successfully!")
           
    else:
        st.warning("No books in your library. Add some first!")

elif menu == "🔍 Search Book":
    st.header("🔍 Search a Book")
    search_term = st.text_input("🔎 Enter title or author name")

    if st.button("🔍 Search", key="search_btn"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("❌ No book found!")

elif menu == "📊 Library Statistics":
    st.header("📊 Library Statistics")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read_status"])
    unread_books = total_books - read_books
    
    st.metric(label="📚 Total Books", value=total_books)
    st.metric(label="✅ Books Read", value=read_books)
    st.metric(label="📖 Books Unread", value=unread_books)
