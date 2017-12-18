# PY-Import-Data

## Importing Data in Python - Part 1

### 1-A Introduction and Flat Files 

**Snippet** | **Description** | **Remarks** | **Dataset**
--- | --- | --- | ---
Importing entire textfile | Basic Read & Close | none | none
Importing text files line by line | Basic Read - limited lines | Concept of context manager | d
Using NumPy to import flat files | Numpy loadtxt() function | none | MNIST dataset
Customizing your NumPy import | np loadtxt() arguments | none | digits_header.txt
Importing different datatypes | np loadtxt() different datatypes | skip rows | seaslug.txt
Working with mixed datatypes (2) | np recfromcsv | dtype = none | titanic.csv
Using pandas to import flat files as DataFrames (1) | pd read_csv | dataframe | titanic.csv
Using pandas to import flat files as DataFrames (2) | pd read_csv | dataframe to numpy array | digits.csv
Customizing your pandas import | pd read_csv arguments | missing values masking | titanic_corrupt.txt

### 1-B Importing data from other file types

**Snippet** | **Description** | **Remarks** | **Dataset**
--- | --- | --- | ---
Loading a pickled file | pickle format | pickle package | data.pkl
Listing sheets in Excel files | excel sheetnames | pandas ExcelFile | battledeath.xlsx
Importing sheets from Excel files | pandas ExcelFile | multiple sheets import | battledeath.xlsx
Customizing your spreadsheet import | parsing columns | xl.parse | battledeath.xlsx
Importing SAS files | SAS7BDAT file  | convert SAS to dataframe | sales.sas7bdat
Importing Stata files | Pandas stata | pd read_stata | disarea.dta
Using h5py to import HDF5 files | HDF5 import & structure | h5py.File | LIGO_data.hdf5
Extracting data from your HDF5 file | HDF5 group extract | none | LIGO_data.hdf5
Loading .mat files | Matlab files inmport | scipy.io.loadmat | albeck_gene_expression.mat
The structure of .mat in Python | Matlab dictionnary | none | none

### 1-C Working with Relational Databases 

**Snippet** | **Description** | **Remarks** | **Dataset**
--- | --- | --- | ---
Creating a database engine | sqlalchemy - create_engine | none | none
What are the tables in the database | create_engine & engine.table_names | sqlite DB | none 
Hello world of the SQL Queris | execute SELECT statement | engine.connect - con.execute - pd DF | Chinook.sqlite
Customizing the Hello World of SQL Queries | execute SELECT statement | columns - keys | Chinook.sqlite
Filtering your database records using SQL's WHERE | Select Where statement | pd.DataFrame(rs.fetchall()) | chinook.sqlite
Ordering your SQL records with ORDER BY | Select Where Order statement | none | chinook.sqlite
Pandas and The Hello World of SQL Queries | pandas read_sql_query VS con.execute | sqlalchemy - pandas | chinook.sqlite
Pandas for more complex querying | pandas read_sql_query SELECT where order | none | chinook.sql
power of SQL lies in relationships between tables: INNER JOIN | select INNER JOIN Statement | none | chinook.sqlite

======================================

## Importing Data in Python - Part 2

### 2-A Importing data from the Internet 

**Snippet** | **Description** | **Remarks** | **Dataset**
--- | --- | --- | ---
Importing flat files from the web: your turn! | urllib urlretrieve | none | winequality.csv @ amazon
Opening and reading flat files from the web | pandas url read_csv | none | winequality.csv @ amazon
Importing non-flat files from the web | pandas read_excel | excel xls | latitude.xls
Performing HTTP requests in Python using urllib | urllib - urlopen & Request | HTML paga | URL
Printing HTTP request results in Python using urllib | urllib - urlopen & Request | HTML paga | URL
Performing HTTP requests in Python using requests | requests pkg | HTML page extract | URL
Parsing HTML with BeautifulSoup | requests & BeautifulSoup | extract HTML info | URL
Turning a webpage into data using BeautifulSoup: getting the text | requests & BeautifulSoup | extract HTML info | URL
Turning a webpage into data using BeautifulSoup: getting the hyperlinks | requests & BeautifulSoup | extract HTML info | URL

## 2-B Interacting with APIs to import data from the web

**Snippet** | **Description** | **Remarks** | **Dataset**
--- | --- | --- | ---
Loading and exploring a JSON | json.load | key-value pair | a_movie.JSON
API requests | requests + parsing API info | none | none
JSON–from the web to Python | requests + parsing API info + JSON parsing | none | none
Checking out the Wikipedia API | API & JSON | none | wikipedia-page

## 2-C Diving deep into the Twitter API

**Snippet** | **Description** | **Remarks** | **Dataset**
--- | --- | --- | ---
API Authentication | tweepy AOUTH package | access & consumer key-token | none
Streaming tweets | tweepy Stream | filtering and capturing | none
Load and explore your Twitter data | tweepy & json handling | tweets to list | none 
Twitter data to DataFrame | pandas | list to DataFrame | none
A little bit of Twitter text analysis | dataframe analysis | wordcount | none
