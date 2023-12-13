alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
word = input("Enter keyword: ").upper()
word = [v for v in word if v in alpha]

seen = set()
key = [v for v in word if not (v in seen or seen.add(v))]
alpha = [v for v in alpha if v not in key[:-1]]
split = alpha.index(key[-1])
key += alpha[split + 1:]
key += alpha[:split]

print("".join(key))
