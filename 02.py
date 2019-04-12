s1 = "パトカー"
s2 = "タクシー"

otpt = [f"{s1_}{s2_}" for s1_, s2_ in zip(s1, s2)]
otpt = ''.join(otpt)

print(otpt)