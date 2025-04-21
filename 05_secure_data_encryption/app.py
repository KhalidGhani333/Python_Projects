import streamlit as st
import hashlib                               # we store securely passkey in hash value
from cryptography.fernet import Fernet       # encryption algorithm . encrypt and decrypt the data
import base64                                # To encode key in Fernet-safe format


# Session Variables
if "users_data" not in st.session_state:
    st.session_state.users_data = {}

if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if "user" not in st.session_state:
    st.session_state.user = ""

#  Helper Functions 

# Hashing passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Generate key from passkey
def make_key(passkey):
    return base64.urlsafe_b64encode(hashlib.sha256(passkey.encode()).digest()[:32])

# Encrypt data
def encrypt(text, passkey):
    key = make_key(passkey)
    return Fernet(key).encrypt(text.encode()).decode()

# Decrypt data
def decrypt(encrypted_text, passkey, correct_hash):
    if hash_passkey(passkey) != correct_hash:
        return None
    try:
        key = make_key(passkey)
        return Fernet(key).decrypt(encrypted_text.encode()).decode()
    except:
        return None

# ----------------- Sidebar -----------------
if st.session_state.is_logged_in:
    menu = ["Home", "Store", "Retrieve", "Logout"]
else:
    menu = ["Login"]

choice = st.sidebar.selectbox("Menu", menu)

# ----------------- Login -----------------
if choice == "Login":
    st.title("🔐 Secure Data Encryption App")
    st.subheader("🔓 Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if user and pwd:
            st.session_state.is_logged_in = True
            st.session_state.user = user
            st.success(f"✅ Welcome, {user}!")
        else:
            st.error("❌ Enter username and password.")

# ----------------- Logout -----------------
elif choice == "Logout":
    st.session_state.is_logged_in = False
    st.session_state.user = ""
    st.session_state.login_attempts = 0
    st.success("✅ You have logged out.")

# ----------------- Home -----------------
elif choice == "Home":
    st.title("🔐 Secure Data Encryption App")
    st.subheader("🏠 Home")
    st.write(f"Hello **{st.session_state.user}** ! Welcome to your secure vault.")
    st.markdown("⬅ Use the sidebar to **Store** or **Retrieve** secret Data.")

# ----------------- Store Data -----------------
elif choice == "Store":
    st.title("🔐 Secure Data Encryption App")
    st.subheader("📦 Store Data")

    secret = st.text_area("Enter secret data")
    key1 = st.text_input("Create passkey", type="password")
    key2 = st.text_input("Confirm passkey", type="password")

    if st.button("Encrypt & Save"):
        if not secret or not key1 or not key2:
            st.error("⚠️ All fields are required.")
        elif key1 != key2:
            st.error("❌ Passkeys do not match.")
        else:
            encrypted = encrypt(secret, key1)
            hashed_key = hash_passkey(key1)
            user = st.session_state.user

            if user not in st.session_state.users_data:
                st.session_state.users_data[user] = []

            st.session_state.users_data[user].append({
                "encrypted": encrypted,
                "passkey_hash": hashed_key
            })

            st.success("✅ Data stored securely!")
            st.code(encrypted)

# ----------------- Retrieve Data -----------------
elif choice == "Retrieve":
    st.title("🔐 Secure Data Encryption App")
    st.subheader("🔍 Retrieve Data")

    user = st.session_state.user
    entries = st.session_state.users_data.get(user, [])

    if not entries:
        st.warning("📭 No data found.")
    else:
        passkey = st.text_input("Enter passkey", type="password")

        if st.button("Decrypt"):
            found = False

            for entry in entries:
                result = decrypt(entry["encrypted"], passkey, entry["passkey_hash"])
                if result:
                    st.success("✅ Decrypted!")
                    st.code(result)
                    st.session_state.login_attempts = 0
                    found = True
                    break

            if not found:
                st.session_state.login_attempts += 1
                left = 3 - st.session_state.login_attempts
                st.error(f"❌ Wrong passkey. Attempts left: {left}")

                if st.session_state.login_attempts >= 3:
                    st.warning("🚫 Too many wrong tries. Logged out.")
                    st.session_state.is_logged_in = False
                    st.session_state.user = ""
                    st.stop()

# ----------------- Footer -----------------
st.markdown("---")
st.caption("🔒 Secure Data Locker | Made by Khalid")
