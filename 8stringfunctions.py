#check if string is palindrome or not
name=input('enter the string')
if name == name[::-1]:
    print('palindrome')
else:
    print('not palindrome')

#count vowels in string
count=0
s=input('enter string').lower()
for ch in s:
    if ch in 'aeiou': 
        count+=1
print(count) #remember indentation 
      
#Reverse each word in sentance
s = "hello world"
words = s.split()
rev = [w[::-1] for w in words]
print(" ".join(rev))  # ➝  'olleh dlrow'