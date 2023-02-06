s = 'azcbobobegghakl'

findText = 'bob'
result = 0
for i in range(len(s)):
  if(s[:3] == findText):
    result +=1

  s = s[1:]

print('Number of times bob occurs is:' + str(result))
