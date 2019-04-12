s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

idx1head = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict_ = {}

li = s.split()

for i, s in enumerate(li):
    j = 1 if i+1 in idx1head else 2
    dict_[s[:j]] = i

print(dict_)