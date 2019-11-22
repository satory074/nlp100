# Input
INPUT = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

# Process
import random as ra

def typoglycemia(word):
    if len(word) <= 4:
        return word
    else:
        return f"{word[0]}{''.join(ra.sample(list(word)[1:-1], len(word[1:-1])))}{word[-1]}"

# Output
print(f"Input : {INPUT}")
print("---")
print(f"Typoglycemia: {' '.join(typoglycemia(w) for w in INPUT.split(' '))}")
