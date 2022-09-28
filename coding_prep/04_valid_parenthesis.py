"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
   def isValid (self, sequence: str):
       '''
       Function to pair if sequence contains valid parenthesis
       :param sequence: Sequence of brackets
       :return: True is sequence is valid else False
       '''
       stack = []
       opening = set('([{')
       closing = set(')]}')
       pair = {')' : '(' , ']' : '[' , '}' : '{'}
       for i in sequence :
           if i in opening :
               stack.append(i)
           if i in closing :
               if not stack :
                   return False
               elif stack.pop() != pair[i] :
                   return False
               else :
                   continue
       if not stack :
           return True
       else :
           return False

if __name__ == '__main__':
   sequence = '{[()]}'
   print(f'Is {sequence} valid ? : {Solution().isValid(sequence)}')
   sequence1 = '{[()]}{]{}}'
   print(f'Is {sequence1} valid ? : {Solution().isValid (sequence1)}')