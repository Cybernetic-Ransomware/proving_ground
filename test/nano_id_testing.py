from nanoid import generate, non_secure_generate


print(generate())
print(generate(size=5))
print(generate('012345', size=10))

print('-' * 20)

print(non_secure_generate())
print([1, 2, 3 | 0])
