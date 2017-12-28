'''
Created on 18-Jul-2017

@author: Ashok
'''
print('************welcome to college fee enquery management************')
rollno=input('enter the roll number:')
no1="17csr";
no2="16csr";
no3="15csr";
no4="14csr";
i=0;
j=5;
roll="0";
ans=0;
m=5;
n=8;
a=0;
b=2;
year="";
for m in range (m,n):
    roll=roll+rollno[m]
roll1=int(roll)
for a in range (a,b):
    year=year+rollno[a]
if year=="17": 
    for i in range(i,j):
        if rollno[i]==no1[i]:
            ans=ans+1;
    fh1=open("first.txt","r")
    print('ROLLNO           NAME                ADMISSION           FIRST GRDUATE       FEES')
    print (fh1.readlines()[roll1-1])
    fh1.close()
elif year=="16":
    for i in range(i,j):
        if rollno[i]==no2[i]:
            ans=ans+1;
    fh2=open("second.txt","r")
    print('ROLLNO           NAME                ADMISSION           FIRST GRDUATE       FEES')
    print (fh2.readlines()[roll1-1])
    fh2.close()
elif year=="15":
    for i in range(i,j):
        if rollno[i]==no3[i]:
            ans=ans+1;
    fh3=open("third.txt","r")
    print('ROLLNO           NAME                ADMISSION           FIRST GRDUATE       FEES')
    print (fh3.readlines()[roll1-1])
    fh3.close()
elif year=="14":
    for i in range(i,j):
        if rollno[i]==no4[i]:
            ans=ans+1;
    fh4=open("fourth.txt","r")
    print('ROLLNO           NAME                ADMISSION           FIRST GRDUATE       FEES')
    print (fh4.readlines()[roll1-1])
    fh4.close()