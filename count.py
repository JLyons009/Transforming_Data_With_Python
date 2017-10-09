import read
from collections import Counter


data = read.load_data()

all_headlines = ""
for headline in data['headline']:
    all_headlines += str(headline).lower() + " "

all_words = all_headlines.split(" ")
word_counts = Counter(all_words)

if __name__ == "__main__":
    print(word_counts.most_common(100))