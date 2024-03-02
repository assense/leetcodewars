import random

def interpret(code): 
    code = list(code.split('\n'))
    stack = []
    coord, movement = [0,0], [1,0]
    string_mode = False
    output = ''
    while True:
        
        if coord[0] >= len(code[coord[1]]):
            coord[0] = coord[0] % len(code[coord[1]]) 
        if coord[0] <= -1:
            while coord[0] < 0:
                coord[0] = len(code[coord[1]]) + coord[0]
        if coord[1] >= len(code):
            coord[1] = coord[1] % len(code)
        if coord[1] <= -1:
            while coord[0] < 0:
                coord[1] = len(code) + coord[1]
        
        char = code[coord[1]][coord[0]]
        
        
        if string_mode:
            if char == '"':
                string_mode = False
            else:
                stack.append(ord(char))
            coord[0] += movement[0]
            coord[1] += movement[1]
            continue
            
            
        if char in ('0123456789'):
            stack.append(int(char))
            
        elif char in ('<>^v'):
            if char == '<':
                movement = [-1, 0]
            elif char == '>':
                movement = [1, 0]
            elif char == 'v':
                movement = [0, 1]
            else:
                movement = [0, -1]
                
        elif char == '?':
            movement = random.choice([[0,1], [1,0], [0,-1], [-1, 0]])
            
        
        elif char == '+':
            stack.append(stack.pop() + stack.pop())
        elif char == '-':
            stack.append(-(stack.pop()) + stack.pop())
        elif char == '*':
            stack.append(int(stack.pop() * stack.pop()))
            
        elif char == '/':
            a = stack.pop()
            if a == 0:
                stack.pop()
                stack.append(0)
            else:
                stack.append(stack.pop() // a)
                
        elif char == '%':
            a = stack.pop()
            if a == 0:
                stack.pop()
                stack.append(0)
            else:
                stack.append(stack.pop() % a)
                
        elif char == '!':
            if stack.pop() == 0:
                stack.append(1)
            else:
                stack.append(0)
        
        elif char == '`':
            a = stack.pop()
            if a >= stack.pop():
                stack.append(0)
            else:
                stack.append(1)
                
        elif char == '_':
            if stack.pop() == 0:
                movement = [1, 0]
            else:
                movement = [-1, 0]
        
        elif char == '|':
            if stack.pop() == 0:
                movement = [0, 1]
            else:
                movement = [0, -1]
                
        elif char == '"':
            string_mode = not string_mode
        
        elif char == ':':
            if stack:
                stack.append(stack[-1])
            else:
                stack.append(0)
        
        elif char == "\\":
            if len(stack) <= 1:
                stack.append(0)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)
                
        elif char == '$':
            stack.pop()
        
        elif char == '.':
            output += str(stack.pop())
        
        elif char == ',':
            output += (chr(stack.pop()))
            
        
        elif char == '#':
            coord[0] += movement[0]
            coord[1] += movement[1]
        
        elif char == 'p':
            y = stack.pop()
            x = stack.pop()
            v = stack.pop()
            code[y] = code[y][:x] + str(chr(int(v))) + code[y][x+1:]
            for n in code:
                print(n)
            
        elif char == 'g':
            y = stack.pop()
            x = stack.pop()
            stack.append(ord(code[y][x]))
            
        
        elif char == ' ':
            pass
        
        elif char ==  '@':
            break
            
            
            
        coord[0] += movement[0]
        coord[1] += movement[1]
    return output
