import re

def match(text):
    # Regex: \b means word boundary, [Oo] matches 'O' or 'o'
    # \w* matches the rest of the word (letters, digits, underscore)
    # We also allow punctuation right after the word by extending the match
    words = re.findall(r'\b[Oo]\w*[^\s]*', text)
    
    # Build dictionary: key = word, value = length
    result = {word: len(word) for word in words}
    return result
print(match("Oh, maybe Olly is over it"))
# Output: {'Oh,': 3, 'Olly': 4, 'over': 4}
