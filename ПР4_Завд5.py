vowels = {"a", "e", "i", "o", "u", "y"}


text = input("Введіть список: ")
text = text.lower()

vowel_letters = []
consonant_letters = []

for c in text:
    if c.isalpha():
        if c in vowels:
            vowel_letters.append(c)
        else:
            consonant_letters.append(c)

print("Кількість голосних:", len(vowel_letters))
print("Кількість приголосних:", len(consonant_letters))

if len(vowel_letters) > len(consonant_letters):
    print("Голосних більше")
elif len(consonant_letters) > len(vowel_letters):
    print("Приголосних більше")
else:
    result = set(vowel_letters + consonant_letters)
    print("Голосних і приголосних порівну")
