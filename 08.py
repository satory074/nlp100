# Input
INPUT = "I am a Perfect Human."

# Process
def cipher(sentence):
    return "".join(chr(219 - ord(s)) if s.islower() else s for s in sentence)

# Output
print(f"Input : {INPUT}")
print("---")
print(f"Encode: {cipher(INPUT)}")
print(f"Decode: {cipher(cipher(INPUT))}")
