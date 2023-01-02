
import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time
print("Student Examination Portal\nCreated by Soumyadeep Basak")
while True:
    ch=int(input("\nType:\n0.Exit\n1.Student\n2.Course\n3.Batch\n4.Department\n5.Examination\nEnter u r choice:"))
    def join1(L,a):
        str2=''
        for i in L:
            str2=str2+i+a
        str2=str2[:-1]
        return str2
    def g(m):
        if m>=90:
            return ["A","Pass"]
        elif m>=80:
            return ["B","Pass"]
        elif m>=70:
            return ["C","Pass"]
        elif m>=60:
            return ["D","Pass"]
        elif m>=50:
            return ["E","Pass"]
        else:
            return ["F","Fail"]
    def func(df):
        L1=[]
        L2=[]
        for i in df.loc[:,"Marks"]:
            L=g(i)
            L1.append(L[0])
            L2.append(L[1])
        df['Grade']=L1
        df['Pass/Fail']=L2
        return df

    if ch==0:
        break
    elif ch==1:
        ch1=int(input("TYPE:\n0.Create Database\n1.Input student details\n2.Update data\n3.Delete data\n4.Report card(To be generated as a text file result.txt)\nEnter u r choice:"))
        if ch1==0:
            L1=[['StudentID','Name','Roll','Batch']]
            with open("student.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L1)
    
        elif ch1==1:
            n=int(input("Enter the no. of entries:"))
            L1=[]
            for i in range(n):
                L=[]
                StudentID=input("Enter student id:")
                Name=input("Enter name:")
                Roll=input("Enter roll:")
                Batch=input("Enter batch:")
                L=[StudentID,Name,Roll,Batch]
                L1.append(L)
            with open("student.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L1)
    
            df=pd.read_csv("student.csv")
            print(df)

        elif ch1==3:
            df=pd.read_csv("student.csv")
            arr = df.to_numpy()
            np.delete(arr,0,axis=1)
            p=input("Enter student Id :")
            L=[]
            for i in arr:
                if i[0]!=p:
                    print(i)
                    L.append(i)
            df = pd.DataFrame(L, columns = ['StudentID','Name','Roll','Batch'])
            print(df)
            df.to_csv('student.csv', mode='w',index=False)
 
        elif ch1==2:
            df=pd.read_csv("student.csv")
            arr = df.to_numpy()
            np.delete(arr,0,axis=1)
            print(arr)
            p=input("Enter student Id :")
            L=[]
            for i in arr:
              print(i)
              if i[0]!=p:
                  L.append(i)
              else:
                  p1=input("1.Name\n2.Roll\n3.Batch\n")
                  if p1=='1':
                      print(i)
                      p2=input("Enter new name:")
                      i[1]=p2
                      print(i)
                      L.append(i)
                  elif p1=='2':
                      print(i)
                      p2=input("Enter new roll:")
                      i[2]=p2
                      print(i)
                      L.append(i)
                  elif p1=='3':
                      print(i)
                      p2=input("Enter new batch:")
                      i[3]=p2
                      print(i)
                      L.append(i)
            print(L)    
            df = pd.DataFrame(L, columns = ['StudentID','Name','Roll','Batch'])
            print(df)
            df.to_csv('student.csv', mode='w',index=False)
        elif ch1==4:
            df1=pd.read_csv("student.csv")
            df2=pd.read_csv("course1.csv")
            df=pd.merge(df1,df2,on='StudentID')
            p=func(df)
            q=p.loc[:,["StudentID","Name","Roll","CourseName","Marks","Grade","Pass/Fail"]]
            with open("Result.txt", 'w') as f:
                dfn =q.groupby(['StudentID'])
                for i,j in dfn:
                    f.write("\n"+i+"\n")
                    str1 = j.to_string(header=True, index=False)
                    f.write(str1)

    elif ch==2:
        ch2=int(input("0.Create Course database\n1.Input course details\n2.View Student performance\n3.Show course histogram\nEnter u r choice:"))
        if ch2==0:
            L1=[['CourseID','CourseName','Marks']]
            L3=[['CourseID','CourseName','Marks','StudentID']]
            with open("course.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L1)
            with open("course1.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L3)
        elif ch2==1:
            n=int(input("Enter the no. of entries:"))
            L1=[]
            L3=[]
            Dict={}
            for i in range(n):
                L=[]
                CourseID=input("Enter course id:")
                CourseName=input("Enter course name:")
                StudentID=input("Enter student id:")
                Marks=input("Enter marks:")
                Dict[StudentID]=Marks
                L=[CourseID,CourseName,Dict]
                L2=[CourseID,CourseName,Marks,StudentID]
                L1.append(L)
                L3.append(L2)
            with open("course.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L1)
            with open("course1.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L3)
    
            df=pd.read_csv("course.csv")
            print(df)
        elif ch2==2:
            df1=pd.read_csv("student.csv")
            df2=pd.read_csv("course1.csv")

            df=pd.merge(df1,df2,on='StudentID')
            print(df.loc[:,["Roll","Name","Marks"]])
            dfn=df.groupby(['CourseName'])
            for i,j in dfn:
                print("\n"+i)
                print(j.loc[:,["Roll","Name","Marks"]])
        elif ch2==3:
            df1=pd.read_csv("student.csv")
            df2=pd.read_csv("course1.csv")
            df=pd.merge(df1,df2,on='StudentID')
            p=func(df)
            q=p.loc[:,["StudentID","Name","Roll","CourseName","Marks","Grade","Pass/Fail"]]
            plt.hist(df['Grade'])
            plt.xlabel('Grade')
            plt.ylabel('No. of students')
            plt.title('Course statistics')
            

    elif ch==3:
        ch2=int(input("0.Create Batch database\n1.Input Batch Details\n2.View list of all students in a batch\n3.View list of all courses taught in the batch\n4.View complete performance of all students in a batch\n5.Pie Chart of Percentage of all students\nEnter u r choice:"))
        if ch2==0:
            L1=[['BatchID','BatchName','Department Name','List of course','List of students']]
            with open("batch.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L1)
            L2=[['BatchID','BatchName','Department Name','CourseID']]
            L3=[['BatchID','BatchName','Department Name','StudentID']]
            with open("batch2.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L2)
            with open("batch3.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L3)
        
        elif ch2==1:
            n=int(input("Enter the no. of entries:"))
            L1=[]
            L2=[]
            L3=[]
            for i in range(n):
                L=[]
                BatchID=input("Enter BatchID:")
                BatchName=input("Enter BatchName:")
                DepartmentName=input("Enter department name:")
                t1=list(eval(input("Enter list of courses:")))
                t2=list(eval(input("Enter list of students:")))
                str1=join1(t1,";")
                str2=join1(t2,";")
                L=[BatchID,BatchName,DepartmentName,str1,str2]
                L1.append(L)
                if len(t1)!=1:
                    for i in t1:
                        L2p=[BatchID,BatchName,DepartmentName,i]
                        L2.append(L2p)
                else:
                    L2p=[BatchID,BatchName,DepartmentName,t1[0]]
                    L2.append(L2p)
                if len(t2)!=1:
                    for i in t2:
                        L3p=[BatchID,BatchName,DepartmentName,i]
                        L3.append(L3p)
                else:
                    L3p=[BatchID,BatchName,DepartmentName,t2[0]]
                    L3.append(L3p)

            with open("batch.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L1)
            with open("batch2.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L2)
            with open("batch3.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L3)
    
            df=pd.read_csv("batch.csv")
            print(df)
        elif ch2==2:
            df2=pd.read_csv("batch3.csv")
            df1=pd.read_csv("student.csv")
            df=pd.merge(df1,df2,on='StudentID')
            dfn=df.groupby(['BatchName'])
            for i,j in dfn:
                print("\n"+i)
                print(j.loc[:,["Roll","Name","StudentID"]])
        elif ch2==3:
            df2=pd.read_csv("batch2.csv")
            df1=pd.read_csv("course1.csv")
            df=pd.merge(df1,df2,on='CourseID')
            dfn=df.groupby(['BatchName'])
            for i,j in dfn:
                print("\n"+i)
                print(j.loc[:,["BatchID","BatchName","CourseName","CourseID"]])
        elif ch2==4:
            df2=pd.read_csv("batch2.csv")
            df1=pd.read_csv("course1.csv")
            df4=pd.merge(df1,df2,on='CourseID')
            df3=pd.read_csv("student.csv")
            df=pd.merge(df3,df4,on='StudentID')
            dfn=df.groupby(['BatchName'])
            for i,j in dfn:
                print("\n"+i)
                print(j.loc[:,["Roll","Name","StudentID",'CourseName','Marks']])
        elif ch2==5:
            df1=pd.read_csv("student.csv")
            df2=pd.read_csv("department1.csv")
            df=pd.merge(df1,df2,on='BatchID')
            df3=pd.read_csv("course1.csv")
            df4=pd.merge(df,df3,on='StudentID')
            df5=df4.groupby('StudentID')['Marks'].mean()
            df5.plot(kind='pie')
    elif ch==4:
        ch2=int(input("0.Create Department database\n1.Input Department\n2.View all batches in a department \n3.View average performance of all batches in the department\n4.Show department statistics Line plot–Average percentage of all students for each batch)\nEnter u r choice:"))
        if ch2==0:
            L1=[['DepartmentID','Department Name','List of batches']]
            with open("department.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L1)
            L9=[['DepartmentID','Department Name','Batch']]
            with open("department1.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L9)
        elif ch2==1:
            n=int(input("Enter the no. of entries:"))
            L1=[]
            L2=[]

            for i in range(n):
                L=[]
                L3=[]
                
                DepartmentID=input("Enter departmentid:")
                DepartmentName=input("Enter department name:")
                t1=list(eval(input("Enter list of batches:")))
                str1=join1(t1,":")
                L=[DepartmentID,DepartmentName,str1]
                L1.append(L)
                if len(t1)!=1:
                    for i in t1:
                        L3=[DepartmentID,DepartmentName,i]
                        L2.append(L3)
                else:
                    L3=[DepartmentID,DepartmentName,t1[0]]
                    L2.append(L3)
            with open("department1.csv","a") as r2:
                s_writer=csv.writer(r2)
                s_writer.writerows(L2)
            with open("department.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L1)
    
            df=pd.read_csv("department.csv")
            print(df)
        elif ch2==2:
           df=pd.read_csv("department1.csv")
           dfn=df.groupby(['DepartmentID'])
           for i,j in dfn:
                print("\n"+i)
                print(j.loc[:,["BatchID"]])
        elif ch2==3:
            df1=pd.read_csv("student.csv")
            df2=pd.read_csv("department1.csv")
            df=pd.merge(df1,df2,on='BatchID')
            df3=pd.read_csv("course1.csv")
            df4=pd.merge(df,df3,on='StudentID')
            df5=df4.groupby('BatchID')['Marks'].mean()
            print(df5)
        elif  ch2==4:
            df1=pd.read_csv("student.csv")
            df2=pd.read_csv("department1.csv")
            df=pd.merge(df1,df2,on='BatchID')
            df3=pd.read_csv("course1.csv")
            df4=pd.merge(df,df3,on='StudentID')
            df5=df4.groupby('BatchID')['Marks'].mean()
            df5.plot(kind='line')

    elif ch==5:
        ch2=int(input("0.Create Examination database\n1.Input Examination details\n2.View performance of all students in the examination\n3.Show examination statistics:\nEnter u r choice:"))
        if ch2==0:
            L1=[['Marks','CourseName','StudentID']]
            with open("examination.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L1)
        elif ch2==1:
            n=int(input("Enter the no. of entries:"))
            L1=[]

            for i in range(n):
                L=[]
                Marks=input("Enter marks:")
                CourseName=input("Enter coursename:")
                StudentID=input("Enter studentid:")
                L=[Marks,CourseName,StudentID]
                L1.append(L)
            with open("examination.csv","a") as r1:
                s_writer=csv.writer(r1)
                s_writer.writerows(L1)
    
            df=pd.read_csv("examination.csv")
            print(df)
        elif ch2==2:
            df1=pd.read_csv("student.csv")
            df2=pd.read_csv("course1.csv")
            df=pd.merge(df1,df2,on='StudentID')
            dfn =df.groupby(['StudentID'])
            for i,j in dfn:
                print("\n"+i)
                print(j.loc[:,["CourseName","Marks"]])
        elif ch2==3:
            df1=pd.read_csv("student.csv")
            df2=pd.read_csv("course1.csv")
            df=pd.merge(df1,df2,on='StudentID')
            dfn =df.groupby(['BatchName'])
            for i,j in dfn:
                print("\n"+i)
                print(j.loc[:,["Roll","Name","Marks"]])
