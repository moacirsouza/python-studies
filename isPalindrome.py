from unidecode import unidecode
import re


ui=input("Type your text: ")


def cleaningItAll(s):
  return re.sub("[^a-zA-Z0-9_]", "", unidecode(s).lower()).replace(" ", "")


def isPalindrome(s):
  return cleaningItAll(s)==cleaningItAll(s)[::-1]


if isPalindrome(ui):
  nope=""
else:
  nope="NOT "

print(f"It's {nope}a palindrom!")
