import streamlit as st
import string

# Password strength checking function
def check_password_strength(password):
    uppercase = any([1 if c in string.ascii_uppercase else 0 for c in password])
    lowercase = any([1 if c in string.ascii_lowercase else 0 for c in password])
    special = any([1 if c in string.punctuation else 0 for c in password])
    digit = any([1 if c in string.digits else 0 for c in password]) 

    characters = [uppercase, lowercase, special, digit]

    length = len(password)

    score = 0

    common = ["helloworld", "password", "password123", "HelloWorld", "Password123", "Password", "abc123", "xyz123"]

    if password in common:
        return "Password was found in common list, Score: 0 / 7"

    if length > 8:
        score += 1
    if length > 12:
        score += 1
    if length > 17:
        score += 1
    if length > 20:
        score += 1
    length_score = f"Password length is {str(length)}, adding {str(score)} points!"

    if (sum(characters)) > 1:
        score += 1
    if (sum(characters)) > 2:
        score += 1
    if (sum(characters)) > 3:
        score += 1
    char_score = f"Password has {str(sum(characters))} different type of characters, adding {str(sum(characters) - 1)} points!"

    if score < 4:
        strength = f"Password is quite weak! Score: {str(score)} / 7"
    elif score == 4:
        strength = f"Password is ok! Score: {str(score)} / 7"
    elif 4 < score < 6:
        strength = f"Password is pretty good! Score: {str(score)} / 7"
    else:
        strength = f"Password is strong! Score: {str(score)} / 7"
    
    return f"{length_score}\n{char_score}\n{strength}"

# Streamlit App
st.title("Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if not password:
        st.warning("Please enter a password")
    else:
        result = check_password_strength(password)
        st.text_area("Result", result, height=200)
