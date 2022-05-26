ch = input("Enter a alphabet : ")[0]
# if given character is Lower case Vowel or Upper case Vowel
# then print vowel otherwise consonant
if ch.lower() in "aeiou":
    print("\n" + ch, "is a vowel.")
else :
    print("\n" + ch, "is a consonant.")
