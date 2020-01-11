i = float(input())
if i < 3:
    print("f(%.2f)=1.2" % i)
elif i == 3:
    print("f(%.2f)=10" % i)
else:
    d = 2 * i + 3
    print("f(%.2f)=%.2f" % (i, d))
