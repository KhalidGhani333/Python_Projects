import hashlib      # module provides secure hashing functions.

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest() # Creates a SHA-256 hash widely used hashing algorithm ,Converts password into bytes needed for hashing
                                                         # Returns the hashed value in hexadecimal format.
stored_logins = {
    "user@example.com":hash_password("password123"),
    "admin@example.com":hash_password("passwordxyz"),
}

def login(email, password_to_check, stored_logins):
    # Checks if the hashed password matches the stored hash
    if email not in stored_logins:
        return False
    
    hashed_password = hash_password(password_to_check)
    return hashed_password == stored_logins[email]

# User login
email = input("Enter your Email :")
password = input("Enter your Password :")

if login(email,password,stored_logins):
    print("You Successfully Login")
else:
    print("Invalid Email and Password!")