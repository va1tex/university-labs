n=int(input())
s=0;
m=0;
h=0;
h=(n//(60*60))%24;
s=(n%(60*60));
m=s//60;
s=s%60;
print('{}:{:02}:{:02}'  .format(h,m,s))