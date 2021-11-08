#!/usr/bin/env python
# coding: utf-8

# ## Problem 1: BeautifulSoup (35 pts)

# Observe the code chunk below. It uses BeautifulSoup to "scrape" information from NYTimes. Make sure you have internet connection (and have installed BeautifulSoup), run the code chunk.

# In[1]:


get_ipython().system('pip install BeautifulSoup4')


# In[2]:


from bs4 import BeautifulSoup as bs
import urllib.request 


# In[3]:


import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
paragraphs = soup.find_all('p')

for p in paragraphs:
    print(p.get_text())


# Can you guess what each line of the code is doing? How many functions were called in the cell above?

# In[ ]:


import requests
# This means we'll retrieve data from a specified URI.

from bs4 import BeautifulSoup
# We'll use BeautifulSoup.

base_url = 'http://www.nytimes.com'
# This is the url where we'll retrieve data. 

r = requests.get(base_url)
# We will get data from the url: http://www.nytimes.com

soup = BeautifulSoup(r.text)
# We'll select only texts from the website.

paragraphs = soup.find_all('p')
# We'll select paragraphs from the text.

for p in paragraphs:
    print(p.get_text())
# Print paragraphs 


# Play around with the "soup" variable (print it out helps), and try to parse out the NYTimes headlines for today. Here some helpful information on how to do that: https://www.dataquest.io/blog/web-scraping-tutorial-python/; https://proxiesapi-com.medium.com/scraping-the-new-york-times-with-python-and-beautiful-soup-6e5f3bc58e39

# In[6]:


get_ipython().system('pip install requests soupsieve lxml')


# In[31]:


import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text)
paragraphs = soup.find_all("h3")

for h3 in paragraphs:
    print(h3.get_text())


# 
# ## Problem 2: Exceptions (10 pts)
# 
# Below is a function called weighted_avg that takes a list of grades and a corresponding list of weights and returns the weighted average of the grades. The function raises what is called an "exception" if:
# 
#     a weight is less than 0 or greater than 100
#     the weights do not add to 100
#     the number of weights and grades are not equal
#     a grade is below 0 (grades above 100 would be considered extra credit and are acceptable)
# 

# In[ ]:


def weighted_avg(grades,weights):
 
    if any(weight < 0 or weight > 100 for weight in weights):
        raise Exception ("Error: A weight is less than 0 or greater than 100")

    elif sum(weights) != 100:
        raise Exception ("Error: The weights do not add to 100")

    elif len(grades) != len(weights):
        raise Exception ("Error: The number of weights and grades are not equal")

    elif any (grade < 0 for grade in grades):
        raise Exception ("Error: A grade is below 0")

    else:
        avg = 0
        for i in range(len(grades)):
            avg += grades[i] * (weights[i] / 100)
        return avg   

grades1 = [88,99,100,70]
weights1 = [30, 30, 30, 5]

grades2 = [78, 75, 80, 99]
weights2 = [110, 10, -20, 0]

grades3 = [84, 80, 67, 97]
weights3 = [50, 25, 25]

grades4 = [100, 80, 90, 75]
weights4 = [20, 25, 25, 30]


# Catching Exceptions (read through and understand)
# 
# Below is a try...except... procedure to catch an exception or an error.
# 
# The program tries to execute the weighted_avg function, but the sum of weights is not 100, so it raised an error/exception. Normally, the execution stops. However, with an "except" statement, it catches the exception if it arises and keeps executing with the backup plan. This is useful when trying to scrape information from a website to ensure you have a backup plan to resume execution if you fail to connect to the web server or you did not get the desired information. 

# In[ ]:


grades5 = [100, 80, 90, 75]
weights5 = [20, 20, 25, 30]

import sys
try:
    weighted_avg(grades5, weights5)
except:
    e = sys.exc_info()[0]
    print( "Error: %s" % e )


# In[ ]:


# Did the above code make sense? Your answer here: 


# ## Problem 3: Pandas (10 pts)

# Create a pandas dataframe with:
# 
# 1. a column called "words", which contains the unique words from the NYTimes headlines from above
# 2. a column called "frequency", which contains the frequency of those words from the headlines
# 
# Save the pandas dataframe into a csv file.

# In[ ]:


# Your code here


# ## Problem 4: Twint (20 pts)

# Run the following cell to install twint:
# 
# (Note that we are not directly "pip install twint" because sometimes packages are not properly updated with Python versions. Since twint only works for Python 3.6, and most of us have newer versions of Python (>3.8), we found a version of twint that'll support newer version of Python)

# In[ ]:


get_ipython().system('pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint')
get_ipython().system('pip install nest_asyncio')


# Import Twint and a asynchronous coordination package (since Twitter server will reply to us when they are available)

# In[ ]:


import twint
import nest_asyncio
nest_asyncio.apply()


# Carefully study the following code, learn about what the parameters do (i.e., Search, Limit, Pandas: https://github.com/twintproject/twint)

# In[ ]:


c = twint.Config()
c.Search = "#woman"
c.Limit = 1
c.Pandas = True
c.Hide_output= True
twint.run.Search(c)
dataframe = twint.storage.panda.Tweets_df
dataframe


# Adapt the above program to scrape the last 10 tweets from Elon Musk (hint: his twitter handle is "elonmusk")

# In[ ]:


# Your code here


# Save the pandas data frame with elon musk tweets into a CSV file

# In[ ]:


# Your code here

