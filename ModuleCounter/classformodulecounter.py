from collections import Counter

l = [1,1,1,1,1,23,4,5,6,7,8,9]
print(Counter(l))

s = 'asdfnefowfosfsowrwfkogsaa'
print(Counter(s))

s = 'How many times doew each word show up in this sentence word word shoe up up show'
words = s.split()
print(Counter(words))
c = Counter(words)
print(c.most_common(2))
print(sum(c.values()))
print(list(c))
print(set(c))
print(dict(c))
print(c.items())
print(Counter(dict(c)))