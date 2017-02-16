def fib (x):
    if x==0:
        return 1
    if x==1:
        return 1
    return fib (x-1) + fib(x-2)
fibseq=[1,1]
def fib2 (x): 
    #while len(fibseq) < x:
        #fibseq.append ( fibseq[-1]+fibseq[-2] )
    return fibseq [x-1]

while True:
    print "hello"    
    

    
    
