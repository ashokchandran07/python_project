'''
Created on 17-Jul-2017

@author: Ashok
'''
print('************welcome to college fee enquery management************')
year=int(input('enter the year:'))
rollno=input('enter the roll number:')
no="17csr";
i=0;
j=5;
ans=0;
for i in range(i,j):
    if rollno[i]==no[i]:
        ans=ans+1
        print(rollno[i])
        if year==1 and ans==5:
            fh1=open("first.txt","r")
            cmp=fh1.read(8)
            print(cmp)
            print('ROLLNO           NAME                ADMISSION           FIRST GRDUATE       FEES')
            print (fh1.readlines())
            fh1.close()
        
    elif year==2:
        fh2=open("second.txt","r")
        print('ROLLNO           NAME                ADMISSION           FIRST GRDUATE       FEES')
        print (fh2.readlines()[rollno-1])
        fh2.close()
    elif year==3:
        fh=open("third.txt","r")
        print('ROLLNO           NAME                ADMISSION           FIRST GRDUATE       FEES')
        print (fh.readlines()[rollno-1])
        fh.close()
    elif year==4:
        fh4=open("fourth.txt","r")
        print('ROLLNO           NAME                ADMISSION           FIRST GRDUATE       FEES')
        print (fh4.readlines()[rollno-1])
        fh4.close()
    else:
        print('sry enter the correct year')

