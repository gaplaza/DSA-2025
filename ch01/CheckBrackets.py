from StackFunc import ArrayStack

def checkBrackets(statement):
  stack = ArrayStack(100)
  for ch in statement:
    if ch in ('{', '[', '('):
      stack.push(ch)
    elif ch in ('}', ']', ')'):
      if stack.isEmpty():
        return False
      else:
        left = stack.pop()
        if (ch == '}' and left != '{') or \
           (ch == ']' and left != '[') or \
           (ch == ')' and left != '('):
          return False
  return stack.isEmpty()