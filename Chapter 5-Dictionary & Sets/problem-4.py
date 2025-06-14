s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(s)

b = len(s)

print(b)

# python evaluates only numerical value , therefore 20 == 20.0
