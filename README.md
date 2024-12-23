N = int(input())
a=int
if N > 1:
    
    for i in range(2,N,1): 
        if N%i==0:
            a=1
            print("Число не является простым")
            break
else:
        print("Введите число больше 1")
if a!=1 and N>1:
   print("Число является простым")
