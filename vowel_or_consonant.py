def vowel_or_consonant():
    try:
        char = input("Enter the character: ").lower()

        if len(char) != 1 or not char.isalpha():
            print("Please enter a single alphabetic character.")
            return
        
        if char in ["a", "e", "i", "o", "u"]:
            print(f"{char} is a vowel.")
        else:
            print(f"{char} is a consonant.")
    except Exception as e:
        print(f"An error occurred: {e}")

vowel_or_consonant()
