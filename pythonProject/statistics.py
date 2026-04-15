import math
class mmm:
    def __init__(self,noi):
        self.noi=noi
    def mean(self,c,b):
        mean=c/len(b)
        return mean
    def median(self,l):
        if self.noi%2==1:
            position=int((self.noi+1)/2)
            median=l[position-1]
            return median
        else:
            position=float((self.noi+1)/2)
            position=int(position-0.5)
            median=(l[position-1]+l[position])/2
            return median
    def mode(self,b,d):
        occur = []
        max=0
        for i in range(len(b)):
            if b[i] not in d:
                d[b[i]]=1
            else:
                d[b[i]]+=1
        for i,v in d.items():
            if v >= max:
                max = v
        for i,v in d.items():
            if v==max:
                occur.append(i)
        if occur==b:
            return "no mode"
        else:
            return occur
    def range(self,y):
        max=y[0]
        min=y[0]
        for i in range(len(y)):
            if y[i] > max:
                max = y[i]
            if y[i] < min:
                min=y[i]
        return f"range={max - min}"
    def variance(self,c,n,f):
        p=[]
        sum1=0.0
        z = open("power.txt")
        lines = z.readlines()
        for i in range(len(n)):
            f.append(n[i]-c)
            if f[i]<0:
                f[i]*=-1
        for i in lines:
                m=i.split(",")
                for h in range(len(n)):
                    if f[h] == float(m[0]):
                        p.append(float(m[1]))
        for i in p:
           sum1+=i
        var=float("%6.1f"%(sum1/(self.noi-1)))
        return var
    def standard(self,u):
        st=0.0
        f = open("power.txt")
        line = f.readlines()
        for i in line:
            k = i.split(",")
            if u==float(k[0]):
                st=k[2]
        return st
    def zscore(self,lis):
        while True:
            inp = input(f"enter which observtion or number u want to calculate the z-score for{lis}:")
            mean = input("enter the mean to calculate the z-score:")
            sd = input("enter the standard deviation to calculate the z-score:")
            try:
                inp=int(inp)
                mean=int(mean)
                sd=float(sd)
                break
            except:
                print("invalid input")
        zs = float((inp - mean) / sd)
        if zs < 0.0:
            return f"the observation {inp} lies {zs} standard deviations below the mean"
        else:
            return f"the observation {inp} lies {zs} standard deviations above the mean"

    def percentile(self,x):
        print("to find the percentile enter the size and percentage")
        size = int(input("enter how many numbers u want to enter to find the percentile:"))
        for i in range(size):
            c = int(input("enter number:"))
            x.append(c)
        x.sort()
        perc = int(input("enter percentage:"))
        loca =size * (perc * (1 / 100))
        result = 0
        if loca == int(loca):
            loca = float(loca + 0.5)
            loca = int(loca - 0.5)
            result = (x[loca - 1] + x[loca]) / 2
        else:
            s = math.ceil(loca)
            result =x[s - 1]
        return f"percentile {perc}=",result
