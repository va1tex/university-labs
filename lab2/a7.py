x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
f1=0;
f2=0;
if x1%2==y1%2:
    f1=1
else:
    f1=2
if x2%2==y2%2:
    f2=1
else:
    f2=2
if f1==f2:
    print("YES");
    if f1==1:
        print("WHITE")
    else:
        print("BLACK")
else:
    print("NO")