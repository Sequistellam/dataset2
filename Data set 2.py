#!/usr/bin/env python
# coding: utf-8

# In[4]:


Q1.


# In[9]:


a = 0

def b():
    global a
    a = c(a)

def c(a):
    return a + 2


# In[10]:


b()


# In[11]:


b()


# In[12]:


b()


# In[13]:


a


# In[17]:


#When the last expression a is evaluated, the value displayed will be 6.
1. After importing the module, the variable a is assigned the initial value of 0.
2. The function b() is executed for the first time. Inside b(), the global keyword is used to specify that the a variable being referenced is the global variable a defined in the module, not a local variable.
3. Inside b(), the function c(a) is called, passing the current value of a (which is 0) as an argument. The c(a) function adds 2 to the value of a and returns the result (2).
4. The returned value from c(a) (which is 2) is then assigned back to the global variable a inside b(), updating its value.
5. At this point, the value of a is 2.
6. The function b() is executed for the second time. The same steps as before are followed: c(a) is called, adding 2 to the current value of a (2), and the returned value (4) is assigned back to the global variable a.
7. Now, the value of a is 4.
8. The function b() is executed for the third time. Again, c(a) is called, adding 2 to the current value of a (4), and the returned value (6) is assigned back to the global variable a.
9. Finally, when the expression a is evaluated, it will display the current value of a, which is 6.
So, the value 6 will be displayed when the last expression (a) is evaluated.


# In[ ]:


Q2. #Dear prof., I do not understand which file midterm.py, I used Filelength.txt from BB


# In[2]:


def fileLength(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the contents and calculate the length
            contents = file.read()
            length = len(contents)
            return length
    except FileNotFoundError:
        print(f"File {filename} not found.")


# In[21]:


fileLength(r'C:\Georgian\Geogrian exept Architecture VM\Programming\DS 2\Filelength.txt')


# In[3]:


fileLength(r'C:\Georgian\Geogrian exept Architecture VM\Programming\DS 2\ilelength.txt') 


# In[ ]:


Q3


# In[5]:


class Marsupial:
    def __init__(self):
        self.pouch = []  # Initialize an empty list to represent the pouch contents

    def put_in_pouch(self, item):
        self.pouch.append(item)  # Add the item to the pouch list

    def pouch_contents(self):
        return self.pouch  # Return the contents of the pouch as a list


# In[6]:


m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
print(m.pouch_contents())


# In[7]:


class Kangaroo(Marsupial):
    def __init__(self, x, y):
        super().__init__()  # Call the superclass (Marsupial) constructor
        self.x = x  # Set the x-coordinate of the Kangaroo
        self.y = y  # Set the y-coordinate of the Kangaroo

    def jump(self, dx, dy):
        self.x += dx  # Move along the x-axis by dx units
        self.y += dy  # Move along the y-axis by dy units

    def __str__(self):
        return f"I am a Kangaroo located at coordinates ({self.x},{self.y})"


# In[8]:


k = Kangaroo(0, 0)


# In[9]:


k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
k.pouch_contents() 


# In[10]:


k.jump(1, 0)
k.jump(1, 0)
k.jump(1, 0)
print(k)


# In[ ]:


Q4


# In[14]:


def collatz(x):
    print(x)
    if x == 1:  # Base case: Stop when the sequence reaches 1
        return
    elif x % 2 == 0:  # If x is even, divide it by 2
        collatz(x // 2)
    else:  # If x is odd, multiply it by 3 and add 1
        collatz(3 * x + 1)


# In[15]:


collatz(1)


# In[16]:


collatz(10)


# In[ ]:


Q5


# In[17]:


def binary(n):
    if n > 1:
        binary(n // 2)  # Recursively call binary() with n divided by 2
    print(n % 2, end='')  # Print the remainder when n is divided by 2


# In[21]:


binary(0)


# In[22]:


binary(1)


# In[23]:


binary(3)


# In[24]:


binary(9)


# In[ ]:


Q6


# In[26]:


from html.parser import HTMLParser

class HeadingParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.in_heading = False
        self.current_tag = ""

    def handle_starttag(self, tag, attrs):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.in_heading = True
            self.current_tag = tag

    def handle_endtag(self, tag):
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.in_heading = False

    def handle_data(self, data):
        if self.in_heading:
            indent_level = int(self.current_tag[1]) - 1
            print(' ' * indent_level + data)


# In[27]:


import requests

url = 'https://raw.githubusercontent.com/Sequistellam/dataset2/main/w3c.html'
response = requests.get(url)

hp = HeadingParser()
hp.feed(response.text)


# In[ ]:


Q7


# In[2]:


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def webdir(url, depth, indent):
    if depth < 0:
        return

    print(' ' * indent + url)  # print url with indentation
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                next_url = urljoin(url, href)  # Create absolute URL
                webdir(next_url, depth - 1, indent + 2)
    except Exception as e:
        print(f"An error occurred: {e}")


# In[ ]:


webdir('https://cat.georgiancollege.ca/programs/bdat/', 2, 0)


# In[ ]:


Q8


# In[ ]:


#I am assuming that the name of table is "weather"


# In[ ]:


a) All the temperature data.
SELECT TemperatureC FROM weather;

b) All the cities, but without repetition.
SELECT DISTINCT City FROM weather;

c) All the records for India.
SELECT * FROM weather WHERE Country = 'India';

d) All the Fall records.
SELECT * FROM weather WHERE Season = 'Fall';

e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters.
SELECT City, Country, Season FROM weather WHERE RainfallMM BETWEEN 200 AND 400;

f) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order.
SELECT City, Country FROM weather WHERE Season = 'Fall' AND TemperatureC > 20 ORDER BY TemperatureC ASC;

g) The total annual rainfall for Cairo.
SELECT SUM(RainfallMM) FROM weather WHERE City = 'Cairo';

h) The total rainfall for each season.
SELECT Season, SUM(RainfallMM) FROM weather GROUP BY Season;


# In[ ]:


Q9


# In[2]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']


# In[6]:


# a) Convert all words in the list to uppercase
upper_case_words = [word.upper() for word in words]
print(upper_case_words)


# In[7]:


# b) Convert all words in the list to lowercase
lower_case_words = [word.lower() for word in words]
print(lower_case_words)


# In[8]:


# c) Calculate the length of each word in the list
word_lengths = [len(word) for word in words]
print(word_lengths)


# In[9]:


# d) For each word, create a list containing the word in uppercase, lowercase and its length
word_properties = [[word.upper(), word.lower(), len(word)] for word in words]
print(word_properties)


# In[10]:


# e) Include only words that have 4 or more characters
long_words = [word for word in words if len(word) >= 4]
print(long_words)

