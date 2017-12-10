# Creating a database engine
# ---------------------------------------------------------------------

# Import necessary module
from sqlalchemy import create_engine
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# ---------------------------------------------------------------------
# What are the tables in the database?
# ---------------------------------------------------------------------

# Import necessary module
from sqlalchemy import create_engine
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Save the table names to a list: table_names
table_names = engine.table_names()
# Print the table names to the shell
print(table_names)

# ---------------------------------------------------------------------
# The Hello World of SQL Queries!
# ---------------------------------------------------------------------

# Import packages
from sqlalchemy import create_engine
import pandas as pd
# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Open engine connection: con
con = engine.connect()
# Perform query: rs
rs = con.execute('SELECT * FROM Album')
# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
# Close connection
con.close()
# Print head of DataFrame df
print(df.head())

# ---------------------------------------------------------------------
# Customizing the Hello World of SQL Queries
# ---------------------------------------------------------------------

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Lastname, Title from Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()
# Print the length of the DataFrame df
print(len(df))
# Print the head of the DataFrame df
print(df.head())

# ---------------------------------------------------------------------
# Filtering your database records using SQL's WHERE
# ---------------------------------------------------------------------

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee where EmployeeID >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
# Print the head of the DataFrame df
print(df.head())

# ---------------------------------------------------------------------
# Ordering your SQL records with ORDER BY
# ---------------------------------------------------------------------

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')
# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate')
    df = pd.DataFrame(rs.fetchall())
    # Set the DataFrame's column names
    df.columns = rs.keys()
# Print head of DataFrame
print(df.head())
