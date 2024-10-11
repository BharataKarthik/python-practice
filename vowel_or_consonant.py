def vowel():
    char = input("Enter the character: ").lower()

    if char in ("a", "e", "i", "o", "u"):
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonant")

vowel()
