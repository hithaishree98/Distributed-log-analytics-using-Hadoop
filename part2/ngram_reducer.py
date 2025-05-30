import sys

current_ngram = None
current_count = 0
ngram = None

for line in sys.stdin:
    line = line.strip()
    ngram, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_ngram == ngram:
        current_count += count
    else:
        if current_ngram:
            print(f"{current_ngram}\t{current_count}")
        current_ngram = ngram
        current_count = count

if current_ngram == ngram:
    print(f"{current_ngram}\t{current_count}")


