from statistics import mmm
b = int(input("choose which type of calculations you want: 1-measure of center(mean,median,mode) \n 2-measure of variability(range,variance,standard deviation) \n 3-measure of relative standards(z-score,percentile)"))
num = int(input("enter how many inputs do u want to enter to the list:"))
li=list()
di=dict()
li2=list()
li3=list()
sum=0
for i in range(num):
    c = int(input("enter number:"))
    li.append(c)
    sum+=li[i]
li.sort()
obj1=mmm(num)
s=obj1.mean(sum,li)
m=obj1.variance(s,li,li3)
if b==1:
    f = open("output.txt","at")
    f.write(f"measure of center :\nmean={str(s)}\nmedian={str(obj1.median(li))}\nmode={str(obj1.mode(li, di))}\n")
    f.close()
elif b==2:
    f = open("output.txt","at")
    f.write(f"measure of variability :\n {str(obj1.range(li))}\nvariance={str(m)}\nstandard deviation={str(obj1.standard(m))}\n")
    f.close()
else:
    f = open("output.txt","at")
    f.write(f"measure of relative standard :\n z score={str(obj1.zscore(li))}\n{str(obj1.percentile(li2))}\n")
    f.close()
