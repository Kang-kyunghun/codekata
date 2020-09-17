def reverseString(s):
  
  for i in range(len(s)):
    a = s.pop()
    s.insert(i, a)
  return s
  

s = ["h","e","l","l","o"]
print(reverseString(s))