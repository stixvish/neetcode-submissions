class Solution:
  def isValid(self, s: str) -> bool:
    canon = {"]": "[", "}": "{", ")": "("}
    stack = []
    for c in s:
        if c in canon.values():
            stack.append(c)
        else:
            if stack:
                top = stack.pop()
                if top != canon[c]:
                    return False
            else:
                return False
    if stack:
        return False
    return True
