def checkPalindrome(wordToCheck):
    wordToCheck = wordToCheck.lower().replace(" ", "")
    return wordToCheck == wordToCheck[::-1]
  
wordToCheck = str(input("Please type a word you want check if it's a palindrome word\n>"))
resoult = checkPalindrome(wordToCheck)
  
if resoult:
    print("The word", wordToCheck, "is a Palindrome Word!")
else:
    print("The word", wordToCheck, "isn't a Palindrome Word.")