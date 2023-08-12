class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:
        k=0
        b=[]
        x=0
        for i in range(2,32):
            x=0
            for j in range(2,i):
                if(i%j==0):
                    x=1
                    break
            if(x==0):
                b.append(i)
                k+=1

        f=0
        p=0
        for i in range(l,r+1):
            p=0
            while(i>0):
                i=i&(i-1)
                p+=1
            if(p in b):
                f=f+1
        return f
