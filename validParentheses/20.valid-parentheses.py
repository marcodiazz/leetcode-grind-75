#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
def isOpen(s):
    if s == '(' or s == '[' or s == '{':
        return True 
    else:
        return False

def closingChar(s):
    if s == '(':
        return ')'
    elif s == '[':
        return ']'
    elif s == '{':
        return '}'

class Solution:
    
    def isValid(self, s: str) -> bool:
        order = []
        if len(s) % 2 == 1:
            return False
        for i in range(len(s)):
            if isOpen(s[i]):
                order.append(closingChar(s[i]))
            if not isOpen(s[i]):
                if len(order) == 0:
                    return False
                if s[i] == order[len(order)-1]:
                    order.pop()
                else: 
                    return False
        if len(order) == 0:             
            return True
        else: return False
    

# @lc code=end

