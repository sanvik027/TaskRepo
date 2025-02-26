def fibonacci(n):
    a,b = 0,1
    count =0
    while count <n:
        yield a
        a,b =b,a+b
        coun+=1
 fib_gen = fibonacci(10)
 for nun in fib_gen:
     print(num,end='')
 
 