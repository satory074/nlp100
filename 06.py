# input
query_x = "paraparaparadise"
query_y = "paragraph"

# process
def ngram(s, n):
    return [s[i:i+n] for i in range(len(s)-1)]

X = ngram(query_x, 2)
Y = ngram(query_y, 2)
is_in_se_X = "se" in X
is_in_se_Y = "se" in Y

# output
print(f"X:{set(X)}")
print(f"Y:{set(Y)}")
print(f"Union: {set(X) | set(Y)}")
print(f"Difference: {set(X) - set(Y)}")
print(f"Product: {set(X) & set(Y)}")
print(f"Is_contain_\"se\"_in_X:{is_in_se_X}")
print(f"Is_contain_\"se\"_in_Y:{is_in_se_Y}")
