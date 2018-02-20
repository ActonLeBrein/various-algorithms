def Evaluate(str):
    stack = []
    pushChars, popChars = "<({[", ">)}]"
    for c in str :
        if c in pushChars:
            stack.append(c)
        elif c in popChars:
            if not len(stack):
                return False
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(c)]
                if stackTop != balancingBracket:
                    return False
        else:
            pass
    return not len(stack)
    
print Evaluate(')()')
print Evaluate('((as{sd}d))')
print Evaluate('(<ass{}dd))')

dict={'{':'}','[':']','(':')','<':'>'}

def parenthesis_matching(string):
    open_paranthesis=[]
    for item in string:
        if item in dict.keys():
            open_paranthesis.append(item)

        elif (item in dict.values()) and (item==dict[open_paranthesis[-1]]):
            open_paranthesis.pop()

    return len(open_paranthesis) == 0

print parenthesis_matching('([]{})')
print parenthesis_matching('([]{}')
