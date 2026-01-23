# Name: Ongom Ronald
# Program: passwords.py
# Purpose: Check the strength of a password based on
#          dictionary words, common passwords, length,
#          and complexity.
# Course: CSE 111 - Programming with Functions

# Enhancements (Creativity):
# 1. Displays a descriptive strength label (Very Weak → Very Strong)
# 2. Provides improvement suggestions for weak passwords
# 3. Counts how many passwords the user tested before quitting


# Character type constants (provided by Sven)
LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
         "n","o","p","q","r","s","t","u","v","w","x","y","z"]

UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
         "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

DIGITS = ["0","1","2","3","4","5","6","7","8","9"]

SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
           "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",",
           ".", "<", ">", "?", "/", "\\", "`", "~"]


def word_in_file(word, filename, case_sensitive=False):
    """
    Checks if a word exists in a file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            file_word = line.strip()
            if case_sensitive:
                if word == file_word:
                    return True
            else:
                if word.lower() == file_word.lower():
                    return True
    return False


def word_has_character(word, character_list):
    """
    Checks if the word contains at least one character
    from the given character list.
    """
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):
    """
    Calculates the complexity of a word based on
    character types used.
    """
    complexity = 0

    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1

    return complexity


def password_strength(password, min_length=10, strong_length=16):
    """
    Determines password strength from 0 to 5.
    """

    # Dictionary word check (case insensitive)
    if word_in_file(password, "wordlist.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # Common password check (case sensitive)
    if word_in_file(password, "toppasswords.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # Length check (too short)
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # Strong length check
    if len(password) > 15:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # Complexity-based strength
    complexity = word_complexity(password)
    strength = 1 + complexity

    return strength


def strength_label(strength):
    """
    Returns a descriptive label for the strength score.
    """
    labels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong",
        5: "Very Strong"
    }
    return labels.get(strength, "Unknown")


def improvement_suggestions(password):
    """
    Suggests improvements for weak passwords.
    """
    suggestions = []

    if len(password) < 10:
        suggestions.append("Increase password length")

    if not word_has_character(password, LOWER):
        suggestions.append("Add lowercase letters")

    if not word_has_character(password, UPPER):
        suggestions.append("Add uppercase letters")

    if not word_has_character(password, DIGITS):
        suggestions.append("Add numeric digits")

    if not word_has_character(password, SPECIAL):
        suggestions.append("Add special symbols")

    if suggestions:
        print("Suggestions to improve your password:")
        for suggestion in suggestions:
            print("-", suggestion)


def main():
    """
    User input loop for password testing.
    """
    print("Password Strength Checker")
    print("Enter 'Q' to quit.\n")

    attempts = 0

    while True:
        password = input("Enter a password to test: ")

        if password.lower() == "q":
            print(f"\nYou tested {attempts} password(s).")
            print("Exiting Password Strength Checker.")
            break

        attempts += 1
        strength = password_strength(password)
        label = strength_label(strength)

        print(f"Password Strength Score: {strength} ({label})")

        if strength < 4:
            improvement_suggestions(password)

        print()


if __name__ == "__main__":
    main()