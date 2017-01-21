# Project on Entity Resolution and Cleaning Dirty Data
# Part 1
## Cleaning Dirty Data 

### MAIN STEPS

1) Install PyEnchant
2) Run python3 clean.py class.txt
3) Open cleaned.txt(for output)
1) Run python3 query.py cleaned.txt
__________________________________________

#### First step - Cleaning the data 
* Python Script used - clean.py
##### DESCRIPTION ABOUT TRANSFORMATION
###### GROUPING PROFESSORS AND COURSES
The main scope of the clean.py python script is to clean the given data. The given data is set of professor names and corresponding course names, it has several spell errors and format related the flaws. The aim is to clean the data in a way that the spelling errors are corrected, the duplicates are removed and displayed appropriately.

Initially we give the given class.txt file as input and run the python script by using the command:-

```python3 clean.py class.txt```

Now the python script will first obtain the professor name and the corresponding courses in two different arrays. Then, as hinted in the question, we process the professor name and obtain the last name of all the professors. After this we observe that several professor names have been repeated in the given input. Now we process the professor last
names and the corresponding courses and obtain unique professor name and corresponding course names. At this point we 
also convert the first letter of every word to a capital letter and we also sort all the professors and corresponding courses names are orderes in alphabetical order.

###### SPELL CHECK
The next step would be to check the spelling of the course names. The courses of all the corresponding professors are passed to a function which uses PyEnchant to check the spelling of the words. PyEnchant is dictionary libraries which should be installed seperately(INSTALLATION METHOD IN THE END). Each word is checked and if there are any errors in the
word Enchant is used to get suggestions for correct word. At this point we don't replace words just like that. We check the Edit Distant between the existing word and the suggested word. There other cases too where we don't correct any word that is lesser than the length of three or two so that strings like 3D and 2D do not change to an incorrect course name.

###### DETECTING DUPLICATES
Then, we check for duplicate courses under each professor using Jaccard similarity. The Jaccard Similarity is calculated between all the courses under a professor. For example, if any course is repeated under a professor, the duplicate is  eliminated.

_______________________________

##### Second step - Querying Data from cleaned.txt

* Python script used - query.py

###### DESCRIPTION
Initially we run the query.py file and give cleaned.txt file as input by giving the following command:-

```python3 query.py cleaned.txt```

cleaned.txt file contained the cleaned data that was obtained from clean.txt

The queries are being executed in the following method:-

q1 - The first query askes us to give the distinct courses in that are available. All the courses are put into a
list and we find the unique courses.

q2 - Here we have to find the courses that have been taught by Professor Mitchell Theys. To do this we find the
corresponding courses taught by Professor Theys. At this point, we don't have to order in the alphabetical oreder
since the obtained cleaned data from clean.py is already in alphabetical order.

q3 - In this query, we have find the two professor among the professors who teach at least 5 course whose interests
align the most. Here, as mentioned in the question Jaccard Similarity is used. The Jaccard Similarty is used between
all the possible combinations of professors. Then the maximum Jaccard Similarity is taken all the values obtained. The
maximum value signifies that the courses taught by the pair of professors are most aligned. Now the pair of professors 
are found are output.

___________________________________

##### COMMANDS TO BE USED TO RUNNING ON TERMINAL

1) Cleaning Data

```python3 clean.py class.txt```

2) Querying Data

```python3 query.py cleaned.txt```

___________________________________

##### INSTALLING OF EXTRA PACKAGES

Enchant has to be installed specifically for Python3 to run Enchant
It can be done using the following command:-

```sudo apt-get install python3-enchant ```
Link:- https://www.howtoinstall.co/en/ubuntu/precise/universe/python3-enchant/

___________________________________

##### REFERENCES AND LINKS

* Split() and Strip() in Python - http://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python

* title() - http://www.tutorialspoint.com/python/string_title.htm

* sort() - https://wiki.python.org/moin/HowTo/Sorting

* PyEnchant - http://pythonhosted.org/pyenchant/

* Jaccard Similarity - http://www.planetcalc.com/1664/

* Code Snippet - Edit Distance
    ```
    def edit_distance(s1, s2):
        m=len(s1)+1
        n=len(s2)+1
        tbl = {}
        for i in range(m): tbl[i,0]=i
        for j in range(n): tbl[0,j]=j
        for i in range(1, m):
            for j in range(1, n):
                cost = 0 if s1[i-1] == s2[j-1] else 1
                tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)
        return tbl[i,j]
    ```
Link:- http://stackoverflow.com/questions/2460177/edit-distance-in-python

________________________________________

NOTE1:- The formatting of this README.md file may vary in the different operating systems.
NOTE2:- Extra comments have been added to clean.py and query.py to explain the code further.

### About this project

This project was done as a part of CS 491: Introduction to Data Science at UIC

# Part 2
# Web Scrapping use Beautiful Soup

## Reformatting Data: Super Bowl Champions

### MAIN STEPS

1) Install BeautifulSoul
2) Run python3 transform.py
3) Open result.csv(for output)
_________________________________________

### DESCRIPTION

* Python script used - transform.py

Initially we execute the python script by running the following command:-

```python3 transform.py```

This question generally involves the usages of BeautifulSoup which is a tool that is used to scrap data from web pages. This tool can read formats such as HTML, CSS, XML, etc. The first step is to install BeautifulSoup(MENTIONED BELOW). Using a tool called urllib(which is installed with python3) we open the web page:-

https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions

After this we use function such as findAll() to find the desired table to print. Then format the data by using string functions such as split(), get_text() and rstrip().
Then we create a file .csv file named result.csv and write all our obtained results into the .csv file.

__________________________________________

### INSTALLING EXTRA PACKAGES

Installing BeautifulSoup for Python3 Specifically so that we can use BeautifulSoup on Python3

```sudo apt-get install python3-setuptools```

```sudo easy_install3 beautifulsoup4```
__________________________________________

### REFERENCES AND LINKS

* Split() and Strip() in Python - http://stackoverflow.com/questions/4071396/split-by-comma-and-strip-whitespace-in-python

* rstrip() - http://www.tutorialspoint.com/python/string_rstrip.htm

* get_text() - http://stackoverflow.com/questions/16121001/suggestions-on-get-text-in-beautifulsoup

* BeautifulSoup - http://www.crummy.com/software/BeautifulSoup/bs4/doc/

__________________________________________

NOTE1:- The formatting of this README.txt file may vary in the different operating systems.
NOTE2:- Extra comments have been added to transform.py to explain the code further.
__________________________________________
### About this project

This project was done as a part of CS 491: Introduction to Data Science at UIC


