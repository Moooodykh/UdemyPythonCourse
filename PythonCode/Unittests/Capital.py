'''
Input : string
Output : capitalized string
'''
import string

def capitalized(text):
    return text.capitalize()

def titled(text):
    return string.capwords(text)
# USING CAPWORDS WHICH CAPITAZLIZE EACH WORD EXCEPT SPECIAL SYMBOLS