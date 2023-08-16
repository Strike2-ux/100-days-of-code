def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])

print(palindrome("racecar"))
'''
def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])

word = input("Enter a word: ")
if palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
'''
'''
def palindrome(word):
  """Returns True if the given word is a palindrome, False otherwise."""

  if len(word) <= 1:
    return True

  first_letter = word[0]
  reversed_word = reversed(word[1:])

  if first_letter != next(reversed_word):
    return False

  return True


print(palindrome("racecar"))
# True

print(palindrome("madam"))
# True

print(palindrome("hello"))
# False

'''