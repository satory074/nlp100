def ngram(s, n):
    return [s[i:i+n] for i in range(len(s)-1)]

s = 'I am an NLPer'
w = s.split(' ')

print(ngram(s, 2))
print(ngram(w, 2))