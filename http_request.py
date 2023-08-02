# -------------- Stage 1 / getting all possible letters ------------------

import requests

def call_webpage(url):
    try:
        response = requests.get(url)
        return response.json()  # Assuming the response is in JSON format
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    url = "https://0ijq1i6sp1.execute-api.us-east-1.amazonaws.com/dev/stream"
    results = []

    for _ in range(100):
        data = call_webpage(url)
        if data:
            results.append(data)

    print(results)

# -------------- Stage 2 / store unique letters ------------------

letter_counts = []

for letter in results:
    if letter not in letter_counts:
        letter_counts.append(letter)
        
print(letter_counts)

# -------------- Stage 3 / using words.txt to search word with corresponding letters ------------------

filtered_words = []

with open('words.txt', 'r') as file:
    for line in file:
        word = line.strip().lower()
        # Check if all letters in letter_counts are present in the word
        if all(letter in word for letter in letter_counts):
            filtered_words.append(word)

print(filtered_words)