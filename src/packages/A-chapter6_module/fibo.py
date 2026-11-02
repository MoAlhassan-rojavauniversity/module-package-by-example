'''
Fibonacci numbers module
 This module has a global variable name  __name__
 on the command link on the same directory as the fibo.py  type the 
 $ python
 >>> import fibo # you are importing the module fibo  since you are on the same directory it works
 >>> fibo.__name__  # getting the global variable which is the name of the module 
 'fibo' 

 any execution of the module from the command line like the below will make the global variable __name__ to be called "__main__"
 $ python fibo.py 50
 __main__
 
 0 1 1 2 3 5 8 13 21 34


'''
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print(__name__) # if executed from python interpreter ( $ python fibo.py ) it will be given a __main__ as a name  

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

