# 📚 Assignment: Personal Library Manager  

## 🎯 Objective  
Create a **command-line Personal Library Manager** that helps users organize and track their book collection. This program allows users to **add, remove, and search for books**, along with providing basic statistics. Optionally, it can also **save and load** the library data using file handling.  

---

## 🛠️ Features & Requirements  

### 📖 Book Details  
Each book should be stored as a **dictionary** with the following attributes:  

- **📌 Title**: (string) – The book's name  
- **✍️ Author**: (string) – Who wrote the book  
- **📅 Publication Year**: (integer) – The year it was published  
- **📚 Genre**: (string) – Fiction, Non-fiction, Mystery, etc.  
- **✅ Read Status**: (boolean) – `True` if read, `False` if unread  

---

## 📜 Menu System  
The program should present users with the following menu options:  

1️⃣ **Add a Book** – Enter book details and add it to the library 📖  
2️⃣ **Remove a Book** – Delete a book by its title ❌  
3️⃣ **Search for a Book** – Find books by title or author 🔍  
4️⃣ **Display All Books** – Show all books in a formatted list 📋  
5️⃣ **Display Statistics** – Get insights like total books & percentage read 📊  
6️⃣ **Exit** – Close the program 🚪  

---

## 🔍 Functionalities  

### ➕ Add a Book  
- Prompt the user to input book details  
- Store the book as a dictionary in a list  

### ❌ Remove a Book  
- Ask for the **title** of the book to remove  
- Search and remove it from the collection  

### 🔎 Search for a Book  
- Allow searching by **title or author**  
- Display all matching results  

### 📋 Display All Books  
- Show all books in a **neatly formatted table**  

### 📊 Display Statistics  
- **Total Books**: Count all books in the collection  
- **Read Percentage**: Calculate & display the % of books marked as "read"  

### 🚪 Exit  
- Close the program gracefully  

---

## 🔥 **Optional Challenge: File Handling**  
For an advanced touch, implement **file handling** to save and load the library:  

📥 **Save Library to a File** – Save the book collection to `library.txt` when exiting  
📤 **Load Library from a File** – Load existing book data when the program starts  
