ui=input("Type: ")

def isPalindrome(s):
     return s.lower().replace(" ", "")==s.lower().replace(" ","")[::-1]

a = isPalindrome(ui)
if a:
  print("Yes, it's a palindrom")
else:
  print("No, it's NOT a palindrom")
