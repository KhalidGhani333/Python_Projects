## 🔐 Secure Data Encryption System Using Streamlit
**📌 Overview**
This project is a secure data encryption and retrieval app built using Python and Streamlit. It allows users to safely store and retrieve their sensitive data using unique passkeys. The data is encrypted using modern cryptographic techniques and stored in memory without any external database.

**🎯 Features**
🔒 Encrypt & Store Data securely using a passkey
🔐 Decrypt Data only when the correct passkey is entered
🚫 Three Failed Attempts lead to automatic logout
🔁 Reauthorization/Login Page after failed attempts
📦 In-Memory Storage (No database needed)
🧠 Simple & Clean UI using Streamlit

## 🧩 How It Works
User Login: App starts with a login page to authorize access.
**Store Data:**
User enters text and a custom passkey.
The text is encrypted using Fernet encryption.
The passkey is hashed and stored with the encrypted text.
**Retrieve Data:**
User provides encrypted data and the same passkey.
If the hashed passkey matches, the data is decrypted and shown.
If the wrong passkey is entered, the attempt count increases.
**Security Measures:**
After 3 wrong attempts, the user is redirected to login.
Failed attempt count resets after successful login.

## ✅ Learning Outcomes
Deep understanding of encryption and hashing
Practical use of Streamlit for UI development
Working with user authentication flows
Building real-world secure data storage systems
