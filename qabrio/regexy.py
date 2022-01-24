import re


data = ['21sa2', '0xE5E5E5', 'sfa13', '0xzzs', '0x121010', '0xAF', '0x1210100 x121010']
pattern = '^0x[A-Fa-f0-9]+$'

regex = re.compile(pattern)
print([item for item in data if regex.match(item)])


data = 'alabama Afryka aspartam angina alloha anagram alaska'
pattern = 'A[a-z]*a'

regex = re.compile(pattern)
print(regex.findall(data))


data = 'alabama Afryka aspartam angina alloha anagram alaska'
pattern = '[aA][a-z]*a'

regex = re.compile(pattern)
print(regex.findall(data))

print(type(regex.finditer(data)))

print([item.start() for item in regex.finditer(data)])
print([item.end() for item in regex.finditer(data)])
print([item.span() for item in regex.finditer(data)])

print([item.group() for item in regex.finditer(data)])
print([data[item.start():item.end()] for item in regex.finditer(data)])


data = '6161384834660513160413161513156481362616121386'
pattern = '6[0-9]*6'

regex = re.compile(pattern)
print(regex.findall(data))


data = '6161384834660513160413161513156481362616121386'
pattern = '6[0-9]*?6'

regex = re.compile(pattern)
print(regex.findall(data))
