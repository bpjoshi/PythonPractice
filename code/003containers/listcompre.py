words1=["welcome", "to", "the", "hotel", "california"]

words2=[w for w in words1]
print(words2)
words2=[w for w in words1 if len(w)>3]
print(words2)

words2=[w.upper() if len(w)>3 else w for w in words1]
print(words2)
