import os
import sys  # Added import for sys
data_folder = os.path.join('.')
import socket

ip_address = socket.gethostbyname(socket.gethostname())


def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

def count_word_frequency(file_path):
    word_frequency = {}
    with open(file_path, 'r') as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

def get_top_words(word_frequency, n=3):
    return sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)[:n]

if_file_path = os.path.join(data_folder, 'IF.txt')
if os.path.exists(if_file_path):
    word_frequency = count_word_frequency(if_file_path)
    top_words = get_top_words(word_frequency)
    
    print("\nTop 3 most frequent words in IF.txt:")
    for word, count in top_words:
        print(f"'{word}': {count} occurrences")
else:
    print("IF.txt not found in the data folder.")


def handle_contractions(word):
    contractions = {
        "i'm": "i am", "can't": "cannot", "don't": "do not",
        "isn't": "is not", "won't": "will not", "aren't": "are not",
        "hasn't": "has not", "haven't": "have not", "wasn't": "was not",
        "weren't": "were not", "wouldn't": "would not", "couldn't": "could not",
        "shouldn't": "should not", "it's": "it is", "that's": "that is",
        "you're": "you are", "they're": "they are", "we're": "we are",
        "he's": "he is", "she's": "she is", "what's": "what is",
        "where's": "where is", "there's": "there is", "who's": "who is"
    }
    return contractions.get(word.lower(), word)

def count_word_frequency_with_contractions(file_path):
    word_frequency = {}
    with open(file_path, 'r') as file:
        content = file.read().lower()
        words = content.split()
        for word in words:
            expanded_word = handle_contractions(word)
            expanded_words = expanded_word.split()
            for w in expanded_words:
                word_frequency[w] = word_frequency.get(w, 0) + 1
    return word_frequency

always_remember_file_path = os.path.join(data_folder, 'AlwaysRememberUsThisWay.txt')
if os.path.exists(always_remember_file_path):
    word_frequency = count_word_frequency_with_contractions(always_remember_file_path)
    top_words = get_top_words(word_frequency)
    
    print("\nTop 3 most frequent words in AlwaysRememberUsThisWay.txt:")
    for word, count in top_words:
        print(f"'{word}': {count} occurrences")
else:
    print("AlwaysRememberUsThisWay.txt not found in the data folder.")

# Open a file named 'result.txt' in write mode
# Ensure the output directory exists
output_dir = '/home/data/output'
os.makedirs(output_dir, exist_ok=True)

# Open a file named 'result.txt' in the output directory
with open(os.path.join(output_dir, 'result.txt'), 'w') as result_file:
    # Redirect stdout to the file
    original_stdout = sys.stdout
    sys.stdout = result_file

    # Print results 
    print(f"IP Address: {ip_address}")

    if os.path.exists(if_file_path):
        total_words = 0
        for filename in os.listdir(data_folder):
            if filename.endswith('.txt'):
                file_path = os.path.join(data_folder, filename)
                word_count = count_words_in_file(file_path)
                print(f"Number of words in {filename}: {word_count}")
                total_words += word_count
        print(f"Total number of words in all files: {total_words}")
    else:
        print("IF.txt not found in the data folder.")

    # Print results for IF.txt
    if os.path.exists(if_file_path):
        word_frequency = count_word_frequency(if_file_path)
        top_words = get_top_words(word_frequency)
        
        print("\nTop 3 most frequent words in IF.txt:")
        for word, count in top_words:
            print(f"'{word}': {count} occurrences")
    else:
        print("IF.txt not found in the data folder.")

    # Print results for AlwaysRememberUsThisWay.txt
    if os.path.exists(always_remember_file_path):
        word_frequency = count_word_frequency_with_contractions(always_remember_file_path)
        top_words = get_top_words(word_frequency)
        
        print("\nTop 3 most frequent words in AlwaysRememberUsThisWay.txt:")
        for word, count in top_words:
            print(f"'{word}': {count} occurrences")
    else:
        print("AlwaysRememberUsThisWay.txt not found in the data folder.")

    # Restore stdout
    sys.stdout = original_stdout
print("Results have been written to /home/data/output/result.txt")
