#!/usr/bin/env python
# coding: utf-8

# In[35]:


import csv
from goodreads import client
gc = client.GoodreadsClient('pvr3ns4Le0DCqEpAG2jlQ', '4BM2D4d8ZvFcJNqRQ3OjQq1Qh3OrvMAvHiI0lTOUFE')

def takeSecond(elem):
    return elem[1]

with open('datav3.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    fieldnames = next(reader)
    # print(fieldnames)
    csv_reader = csv.DictReader(f,fieldnames=fieldnames)
    cntAuthor={}
    authoridx={}
    anthortotalrating={}
    for row in csv_reader:
        d={}
        for k,v in row.items():
            d[k]=v
        if d['author'] in cntAuthor:
            cntAuthor[d['author']]+=1
            #print(anthortotalrating[d['author']])
            anthortotalrating[d['author']]+=float(d['rating'])
            
        else:
            cntAuthor[d['author']]=1
            authoridx[d['author']]=d['ID']
            #print(float(d['rating']))
            anthortotalrating[d['author']]=float(d['rating'])
#print(anthortotalrating)
authorratingtuple=[]
for i in cntAuthor:
    if cntAuthor[i]>1:
        authorratingtuple.append((i,round(anthortotalrating[i]/cntAuthor[i],3)))
authorratingtuple.sort(key=takeSecond)
#print(authorratingtuple)
authorwork={}
cnt=0
f=open('authorRatingWork.txt','w')
for i in authorratingtuple:
    cnt+=1
    author = gc.author(gc.book(authoridx[i[0]]).authors[0].gid)
    wk=author.works_count
    print("author:%s     works_count:%s      %s/%s"%(i[0],wk,cnt,len(authorratingtuple)))
    authorwork[i]=wk
    line="%s   %s   %s"%(i[0],i[1],wk)
    f.write(line+"\n")
f.close()


# In[36]:


fl=open('authorRatingWork.txt','r')
for lines in fl.readlines():
    print(lines)
fl.close()


# In[71]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
xaxis=[]
yaxis=[]
fl=open('authorRatingWork.txt','r')
for lines in fl.readlines():
    templist=lines.split()
    if int(templist[len(templist)-1])<20000:
        xaxis.append(float(templist[len(templist)-2]))
        yaxis.append(float(templist[len(templist)-1]))
'''
plt.bar(xaxis,yaxis,width=0.05)
#xticks(np.arange(0,5, step = 1)) 
plt.title("author rating versus works count",fontsize=16)
plt.xlabel("author rating",fontsize=10)
plt.ylabel("number of books written",fontsize=10)
plt.show()
'''
plt.figure(figsize=(40,30))
sns.set(style="whitegrid")
ls=sns.jointplot(x=xaxis,y=yaxis,kind="reg")
ls.set_axis_labels("Author ratings","Books Written")


# In[38]:


data={}
fl=open('authorRatingWork.txt','r')
for lines in fl.readlines():
    templist=lines.split()
    if (float(templist[len(templist)-2])<4.0 and float(templist[len(templist)-1])>5000 and float(templist[len(templist)-1])<20000):
        print(templist)


# In[39]:


import csv
with open('datav3.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    fieldnames = next(reader)
    # print(fieldnames)
    csv_reader = csv.DictReader(f,fieldnames=fieldnames)
    cntAuthor={}
    authoridx={}
    anthortotalrating={}
    cnt=0
    for row in csv_reader:
        d={}
        for k,v in row.items():
            d[k]=v
        if 'Disney' in d['author']:
            print(d['title'])
            cnt+=1
print(cnt)


# In[92]:


fl=open('authorRatingWork.txt','r')
lines=fl.readlines()
xx=[]
yy=[]
zz=[]
print(lines[0].split())
a=lines[0].split()
for i in range(1,11):
    ll=lines[len(lines)-i].split()
    aut=''
    for j in ll[0:len(ll)-2]:
        aut+=j
        aut+=' '
    xx.append(aut.rstrip())
    yy.append(int(ll[len(ll)-1]))
    zz.append(float(ll[len(ll)-2]))
print(xx)
print(yy)
print(zz)
plt.figure(figsize=(20,15))
sns.set(font_scale=1.5)
ls=sns.barplot(yy,xx,palette='rocket')
ls.set_xlabel("Books Written",fontsize=30)
ls.set_ylabel("Author Name",fontsize=30)
ls.set_title("Top ten rated author books count",fontsize=50)
fl.close()


# In[97]:


sns.set(font_scale=1.5)
plt.figure(figsize=(20,15))
xs=sns.barplot(zz,xx,palette='rocket')
xs.set_xlabel("average rating",fontsize=30)
xs.set_ylabel("Author Name",fontsize=30)
xs.set_title("Top ten rated author average ratings",fontsize=50)


# In[ ]:




