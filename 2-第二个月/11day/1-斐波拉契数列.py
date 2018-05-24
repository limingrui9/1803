def fib():
    i = 0
    a,b = 0,1
    while i<8:
        print("_____haha____")
        yield b
        a,b = b,a+b
        i+=1

print(b = fib())
