import sys
from collections import Counter

def count_vowels(file_path):
    vowels = 'aeiou'
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
        frequency = Counter(char for char in text if char in vowels)
        return frequency
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python frequency.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    result = count_vowels(file_path)
    print("Vowel Frequency:")
    for vowel, count in result.items():
        print(f"{vowel}: {count}")
