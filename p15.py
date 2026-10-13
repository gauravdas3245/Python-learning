sentence = "python is easy and python is powerful"

words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

most_common = words[0]

for word in frequency:
    if frequency[word] > frequency[most_common]:
        most_common = word

print("Most common word:", most_common)
print("Frequency:", frequency[most_common])