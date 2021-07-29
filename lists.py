if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        commands, *num = input().split()
        code = list(map(int, num))
        if commands == 'insert':
            index, value = code[0], code[1]
            result.insert(index,value)
        elif commands == 'print':    
            print(result)
        elif commands == 'remove':
            result.remove(code[0])
        elif commands == 'append' :
            result.append(code[0])
        elif commands == 'sort':
            result.sort()
        elif commands == 'pop':
            result.pop()
        elif commands == 'reverse':
            result.reverse()
        

