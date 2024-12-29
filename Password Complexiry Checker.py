import re

def check_password_strength(password):
    # Criteria flags
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    # Check how many criteria are met
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    # Provide feedback based on score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    # Generate detailed feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Include at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Include at least one number.")
    if not special_char_criteria:
        feedback.append("Include at least one special character (!@#$%^&*(),.?\":{}|<>).")
    
    return strength, feedback

def main():
    print("Password Complexity Checker")
    print("---------------------------")
    
    # Input password
    password = input("Enter your password: ").strip()
    
    # Check password strength
    strength, feedback = check_password_strength(password)
    
    # Display results
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f" - {item}")
    else:
        print("Your password meets all security criteria! Great job!")

if __name__ == "__main__":
    main()
