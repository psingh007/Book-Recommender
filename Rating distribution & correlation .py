
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np 
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from pylab import plot, show
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors


# In[2]:


fig, ax = plt.subplots()
sns.set() 
def rate_distribution(x):
    '''
    purpose: plots a histogram to show the rating distribution for the books. 
    :param x: input average rating of the books 
    :type x: data
    '''
    sns.distplot(x['rating'],color="g")
    ax.set_xlabel('Rating distribution')
    ax.set_ylabel('Frequency')


data = pd.read_csv("datav3.csv")
rate_distribution(data)


# In[3]:


data = pd.read_csv("datav3.csv")
def segregation(x):
    '''
    purpose: segragate the ratings for the books to 5 intervals. 
    :param x: input data 
    :type x: data
    '''
    values = []
    for val in x.rating:
        if  val>=0 and val<=1:
            values.append("Between 0 and 1")
        elif val>1 and val<=2:
            values.append("Between 1 and 2")
        elif val>2 and val<=3:
            values.append("Between 2 and 3")
        elif val>3 and val<=4:
            values.append("Between 3 and 4")
        elif val>4 and val<=5:
            values.append("Between 4 and 5")
        else:
            values.append("NaN")
    print(len(values))
    return values


# In[4]:


data = pd.read_csv("datav3.csv")
def rating_pie(data):
    '''
    purpose: plot a pie chart of ratings distribution for the books . 
    :param x: input data 
    :type x: data
    '''
    data['rating'] = segregation(data)
    ratings_pie = data['rating'].value_counts().reset_index()
    labels = ratings_pie['index']
    colors = ['lightblue','coral','darkmagenta','bisque', 'black']
    percent = 100.*ratings_pie['rating']/ratings_pie['rating'].sum()
    fig, ax1 = plt.subplots()
    ax1.pie(ratings_pie['rating'],colors = colors, 
            pctdistance=0.85, startangle=90, explode=(0.05, 0.05, 0.05, 0.05, 0.05))
    #Draw a circle now:
    centre_circle = plt.Circle((0,0), 0.70, fc ='white')
    fig1 = plt.gcf()
    fig1.gca().add_artist(centre_circle)
    #Equal Aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')
    plt.tight_layout()
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(labels, percent)]
    plt.legend( labels, loc = 'best',bbox_to_anchor=(0.1, 1.),)
rating_pie(data)


# In[5]:


data = pd.read_csv("datav3.csv")
def reviews_rating(data):
    '''
    Checking for any relation between text_reviews_count and ratings.
    '''
    plt.figure(figsize=(15,10))
    data.dropna(0, inplace=True)
    sns.set_context('paper')
    ax =sns.jointplot(x="rating",y='text_reviews_count', kind='scatter',  data= data[['text_reviews_count', 'rating']],color='g')
    ax.set_axis_labels("Rating", "Text Review Count")
    plt.show()    
reviews_rating(data)


# In[11]:


data = pd.read_csv("datav3.csv")
def reviews_rating2(data):
    '''
    Checking for any relation between text_reviews_count and ratings.
    '''
    plt.figure(figsize=(15,10))
    data.dropna(0, inplace=True)
    sns.set_context('paper')
    trial =data[~(data['text_reviews_count']>500)]
    ax =sns.jointplot(x="rating",y='text_reviews_count', kind='scatter',  data= trial, color='g')
    ax.set_axis_labels("Rating", "Text Review Count") 
    plt.show()
reviews_rating2(data)


# In[7]:


data = pd.read_csv("datav3.csv")
def rat_counts_rating(data):
    '''
    Checking for any relation between ratings_count and ratings.
    '''
    plt.figure(figsize=(15,10))
    data.dropna(0, inplace=True)
    sns.set_context('paper')
    ax =sns.jointplot(x="rating",y='ratings_count', kind='scatter',  data= data[['ratings_count', 'rating']],color='brown')
    ax.set_axis_labels("Rating", "Rating Count")
    plt.show()
rat_counts_rating(data)


# In[14]:


data = pd.read_csv("datav3.csv")
def rat_counts_rating2(data):
    '''
    Checking for any relation between ratings_count and ratings.
    '''
    plt.figure(figsize=(15,10))
    data.dropna(0, inplace=True)
    sns.set_context('paper')
    trial = data[~(data['ratings_count']>1000)]
    ax =sns.jointplot(x="rating",y='ratings_count', kind='scatter',  data= trial,color='brown')
    ax.set_axis_labels("Rating", "Rating Count")
    plt.show()
rat_counts_rating2(data)


# In[8]:


data = pd.read_csv("datav3.csv")
def pages_rating(data):
    '''
    Checking for any relation between num_pages and ratings.
    '''
    plt.figure(figsize=(15,10))
    data.dropna(0, inplace=True)
    sns.set_context('paper')
    ax =sns.jointplot(x="rating",y='num_pages', kind='scatter',  data= data[['num_pages', 'rating']], color='darkcyan')
    ax.set_axis_labels("Rating", "Number of Pages")
    plt.show()
pages_rating(data)


# In[17]:


data = pd.read_csv("datav3.csv")
def pages_rating2(data):
    '''
    Checking for any relation between num_pages and ratings.
    '''
    plt.figure(figsize=(15,10))
    data.dropna(0, inplace=True)
    sns.set_context('paper')
    trial = data[~(data['num_pages']>1500)]
    ax =sns.jointplot(x="rating",y='num_pages', kind='scatter',  data=trial, color='darkcyan')
    ax.set_axis_labels("Rating", "Number of Pages")
    plt.show()
pages_rating2(data)

