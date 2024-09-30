import itertools
import string
import time
import streamlit as st

# 1. Brute Force Attack
def brute_force_crack(target_password, max_length=5):
    chars = string.ascii_letters + string.digits + string.punctuation
    start_time = time.time()

    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt)
            if attempt == target_password:
                end_time = time.time()
                return (attempt, end_time - start_time)
    return None

# 2. Dictionary Attack
def dictionary_attack(target_password, dictionary_file):
    try:
        with open(dictionary_file.name, 'r') as file:
            start_time = time.time()
            for word in file:
                word = word.strip()
                if word == target_password:
                    end_time = time.time()
                    return (word, end_time - start_time)
    except FileNotFoundError:
        st.error("Dictionary file not found.")
    return None

# 3. Pattern Matching Attack
def pattern_match_attack(target_password):
    common_patterns = ['123456', 'password', 'admin', 'welcome', 'qwerty']
    start_time = time.time()

    for pattern in common_patterns:
        if pattern == target_password:
            end_time = time.time()
            return (pattern, end_time - start_time)
    return None

# 4. Hybrid Attack (Combining Dictionary and Brute Force)
def hybrid_attack(target_password, dictionary_file):
    chars = string.ascii_letters + string.digits + string.punctuation
    try:
        with open(dictionary_file.name, 'r') as file:
            start_time = time.time()
            for word in file:
                word = word.strip()
                for length in range(1, 3):  # Append up to 2 random chars to each word
                    for attempt in itertools.product(chars, repeat=length):
                        attempt_word = word + ''.join(attempt)
                        if attempt_word == target_password:
                            end_time = time.time()
                            return (attempt_word, end_time - start_time)
    except FileNotFoundError:
        st.error("Dictionary file not found.")
    return None

# Streamlit App Layout
st.title("Simple Password Cracker")

# Password input
password = st.text_input("Target Password")

# Attack method selection
attack_method = st.selectbox("Select Attack Method", ["Brute Force", "Dictionary", "Pattern Matching", "Hybrid"])

# Dictionary file upload (Only show when required)
dictionary_file = None
if attack_method in ["Dictionary", "Hybrid"]:
    dictionary_file = st.file_uploader("Upload Dictionary File")

# Start attack button
if st.button("Start Attack"):
    if password == "":
        st.error("Please enter a password.")
    elif attack_method in ["Dictionary", "Hybrid"] and dictionary_file is None:
        st.error("Please upload a dictionary file.")
    else:
        result = None
        if attack_method == "Brute Force":
            result = brute_force_crack(password)
        elif attack_method == "Dictionary":
            result = dictionary_attack(password, dictionary_file)
        elif attack_method == "Pattern Matching":
            result = pattern_match_attack(password)
        elif attack_method == "Hybrid":
            result = hybrid_attack(password, dictionary_file)
        
        if result:
            st.success(f"Password Cracked: {result[0]}\nTime Taken: {result[1]:.2f} seconds")
        else:
            st.warning("Password could not be cracked.")
