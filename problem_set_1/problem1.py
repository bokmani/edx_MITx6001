s = 'azcbobobegghakl'
vowel = ['a','e','i','o','u']
result = 0

for i in s:
  if (vowel.count(i) > 0):
    result +=1

print('Number of vowels: ' + str(result))