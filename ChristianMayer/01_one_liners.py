# z = [(1, 2), (3, 3), (2, 2)]
#
# k = map(lambda x: x[0] ** x[1], z)
# print(list(k))


z = """Mam tak samo jak Ty
Miasto moje a W nim
Najpiękniejszy mój świat""".split('\n')

k = map(lambda s: (True, s) if 'miasto' in s.lower() else (False, s), z)
print(list(k))

print([(True, s) if 'miasto' in s.lower() else (False, s) for s in z])

# %%

print((lambda x, q: x[x.find(q)-5:x.find(q)+5] if q in x else - 1)(str(z), 'moje'))

print((lambda input_str, srch_seq, preq, seq:
       input_str[input_str.find(srch_seq)-preq:input_str.find(srch_seq)+seq]
       if srch_seq in input_str else - 1)(str(z), 'moje', 7, 4))
