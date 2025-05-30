import sys

def generate_ngrams(text, n):
    ngrams = []
    words = text.split()  
    for word in words:
        word = word.lower()  
        for i in range(len(word) - n + 1):
            ngrams.append(word[i:i+n])
    return ngrams

n = int(sys.argv[1])

for line in sys.stdin:
    line = line.strip()
    ngrams = generate_ngrams(line, n)
    for ngram in ngrams:
        print(f"{ngram}\t1")

