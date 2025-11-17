import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import matplotlib.pyplot as plt

nltk.download("gutenberg")
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

text = gutenberg.raw("shakespeare-caesar.txt")

print("Перші 200 символів тексту:")
print(text[:200])

words = word_tokenize(text)
print("\nКількість слів у тексті:")
print(len(words))

freq = nltk.FreqDist(words)

print("\n10 найбільш вживаних слів (до видалення):")
print(freq.most_common(10))

top_words = [w for w, c in freq.most_common(10)]
top_counts = [c for w, c in freq.most_common(10)]

plt.figure(figsize=(10, 5))
plt.bar(top_words, top_counts)
plt.title("10 найбільш вживаних слів (до видалення)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.grid(True)
plt.show()

stop_words = set(stopwords.words("english"))
punct = set(string.punctuation)

cleaned_words = []

for w in words:
    w = w.lower()
    if w not in stop_words and w not in punct:
        cleaned_words.append(w)

print("\nКількість слів після видалення:")
print(len(cleaned_words))

freq_clean = nltk.FreqDist(cleaned_words)

print("\n10 найбільш вживаних слів (після видалення):")
print(freq_clean.most_common(10))

top_words_clean = [w for w, c in freq_clean.most_common(10)]
top_counts_clean = [c for w, c in freq_clean.most_common(10)]

plt.figure(figsize=(10, 5))
plt.bar(top_words_clean, top_counts_clean)
plt.title("10 найбільш вживаних слів (після видалення)")
plt.xlabel("Слова")
plt.ylabel("Частота")
plt.grid(True)
plt.show()
