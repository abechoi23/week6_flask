""" 
Reformat the String
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string.
Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:
Input: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:
Input: s = "ab123"
Output: "1a2b3
"""

# def reformat_one_liner(str_1):
#     letters = []
#     digits = []
#     for x in str_1:
#         if x.isalpha():
#             letters.append(x)
#         elif x.isdigit():
#             digits.append(x)
#     if abs(len(letters) - len(digits)) > 1:
#         return ''

#     result=[]
#     if len(letters) >= len(digits):
#         for i in range(len(digits)):
#             result.append(letters[i])
#             result.append(digits[i])
#         if len(letters) > len(digits):
#             result.append(letters[-1])
#     else:
#         for i in range(len(letters)):
#             result.append(digits[i])
#             result.append(letters[i])
#         result.append(digits[-1])
#     return ''.join(result)

# print(reformat_one_liner("a0b1c2"))
# print(reformat_one_liner("leetcode"))
# print(reformat_one_liner("1229857369"))
# print(reformat_one_liner("covid2019"))
# print(reformat_one_liner("ab123"))


def reformat(s: str) -> str:
    letters = list(filter(lambda c: c.isalpha(), s))
    digits = list(filter(lambda c: c.isdigit(), s))
    
    # if the difference in length between the two lists is greater than 1, it's impossible to reformat
    if abs(len(letters) - len(digits)) > 1:
        return ''
    
    # determine which list is longer and which is shorter
    longer, shorter = (letters, digits) if len(letters) > len(digits) else (digits, letters)
    
    # create the result string by alternating between the longer and shorter lists
    result = []
    for i in range(len(longer)):
        result.append(longer[i])
        if i < len(shorter):
            result.append(shorter[i])
    
    # if there are any characters left in the longer list, add them to the end
    if len(result) < len(s):
        result.append(longer[-1])
    
    return ''.join(result)

print(reformat("a0b1c2"))
print(reformat("leetcode"))
print(reformat("1229857369"))
print(reformat("covid2019"))
print(reformat("ab123"))