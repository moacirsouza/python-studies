def isPalindrome(s):
     return s.lower().replace(" ", "")==s.lower().replace(" ","")[::-1]
