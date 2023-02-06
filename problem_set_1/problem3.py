s = 'azcbobobegghakllln'

temp_text = "" # 현재 확인중 text
final_text = "" # 가장긴 text

# 글자수만큼 for 실행
for i in range(len(s)):
  # -1번째 charactrer  현재 character 비교
  # if 알파벳 순이면 temp_text에 문자를 더함
  if (s[i-1:i] <= s[i:i+1]):
    temp_text += s[i:i+1]
  # 알파벳 순이면 temp_text를 새로 만듬
  else :
    temp_text = s[i:i+1]

  if(len(temp_text) > len(final_text)) :
    final_text = temp_text

print('Longest substring in alphabetical order is: ' + final_text)  