# Data Design & Data Wrangling

'Data wrangling' is the mundane labor of collecting, loading, transforming, and preparing data for exploration and analysis. Although it is hard to put a number on it, [estimates](https://www.nytimes.com/2014/08/18/technology/for-big-data-scientists-hurdle-to-insights-is-janitor-work.html) indicate that data scientists spend from 50 per cent to 80 per cent of their time on data wrangling. The importance of data wrangling has been recognised in [social sciencies](https://doi.org/10.1177/2378023118817378) as well. 

Although data wrangling may seem a-theoretical, some of the decisions you would make would in fact depend on how the data were generated or designed.

In this lab, we will first discuss issues related to data design and will then practice hands-on data wrangling with `pandas` and other Python libraries for data analysis. We will wrangle open data sets, including the Google Covid-19 Community Mobility Reports and Apple Mobility Trends Reports.

## Key themes
* What are data? How are data generated (i.e., data design)? 
* Data wrangling with `pandas`: loading, selecting, and transforming data.

## Learning resources

<i class="fas fa-book"></i> Matthew Salganik. [2.3 Ten common characteristics of big data](https://www.bitbybitbook.com/en/1st-ed/observing-behavior/). In _Bit by Bit: Social Research in the Digital Age_. [[Online version freely available]]((https://www.bitbybitbook.com/en/1st-ed/preface/))

<i class="fas fa-book"></i> Lisa Gitelman and Virginia Jackson. [“Raw Data” Is an Oxymoron. Introduction.](https://raley.english.ucsb.edu/wp-content/Engl800/RawData-excerpts.pdf) MIT Press.

<i class="fas fa-scroll"></i> Sabina Leonelli. [Scientific Research and Big Data.](https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=science-big-data) The Stanford Encyclopedia of Philosophy.

<i class="fas fa-book"></i> <i class="fas fa-code"></i> Sam Lau, Joey Gonzalez, and Deb Nolan. [The Data Science Lifecycle](https://www.textbook.ds100.org/ch/01/lifecycle_intro.html). In [_Principles and Techniques of Data Science_](https://www.textbook.ds100.org/intro.html).

<i class="fas fa-scroll"></i> Steve Lohr. [For Big-Data Scientists, ‘Janitor Work’ Is Key Hurdle to Insights](https://www.nytimes.com/2014/08/18/technology/for-big-data-scientists-hurdle-to-insights-is-janitor-work.html). New York Times. 

<i class="fas fa-scroll"></i> Alexander Kindel et al. [Improving Metadata Infrastructure for Complex Surveys: Insights from the Fragile Families Challenge](https://doi.org/10.1177/2378023118817378). 
Socius.  

<i class="fas fa-play-circle"></i> <i class="fas fa-code"></i> [Introduction to Data Processing in Python with Pandas](https://www.youtube.com/watch?v=5rNu16O3YNE), SciPy 2019 Tutorial by Daniel Chen. See also freely available Jupyter notebooks: [01-intro.ipynb](https://github.com/valdanchev/scipy-2019-pandas/blob/master/notebooks/01-intro.ipynb) and [02-tidy.ipynb](https://github.com/valdanchev/scipy-2019-pandas/blob/master/notebooks/02-tidy.ipynb).

<br>


```{admonition} Activity: Discussing data biases
After reading the section [Ten common characteristics of big data](https://www.bitbybitbook.com/en/1st-ed/observing-behavior/) in Matthew Salganik's book _Bit by Bit_, we will discuss how each characteristic of big data applies to the digital data sets we are analysing in this and next sections, including the [Google COVID-19 Community Mobility Reports](https://www.google.com/covid19/mobility/) and [Apple Mobility Trends Reports](https://covid19.apple.com/mobility).
```

<img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" title='Pandas Logo' width="200" height="100" align="right" />

# Get started with [`pandas`](https://pandas.pydata.org/docs/getting_started/index.html#getting-started)
The `pandas` library:
* is a fast, powerful, and flexible open source tool for doing real world data analysis in Python.
* offers a diverse range of high-performance tools for data loading, cleaning, wrangling, merging, reshaping,  and summarising.
* is the go-to data science library in Python.

# Importing `pandas`

To use `pandas`, we first import the library via the Python's `import` command and give it the alias pd:

import pandas as pd

pd.__version__

# Suppress warnings to avoid potential confusion
import warnings
warnings.filterwarnings("ignore")

# Loading your data

Pandas supports many data file formats, including csv, excel, sql, json.
For details, see [How do I read and write tabular data?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write) For example, once you import pandas as pd, you can load a .csv file using the function `pd.read_csv()`, an Excel file using the function `pd.read_excel()`, and a JSON file using the function `pd.read_json()`.

<img src="https://pandas.pydata.org/docs/_images/02_io_readwrite.svg" width="800" height="400" >

# Loading Covid-19 data sets via URL 


<img src="https://www.google.com/covid19/static/reports-icon-grid.png" title='Google Covid-19 Community Mobility Data' width="200" height="100" align="right"/>

What are the Google Covid-19 [Community Mobility Reports](https://www.google.com/covid19/mobility/)?

* Aggregated and anonymized sets of freely available data that protect individual privacy.
* Shows trends of human mobility over time by country and region, across six categories of places, including retail and recreation, groceries and pharmacies, parks, transit stations, workplaces, and residential.
* The data shows how visitors to (or time spent in) categorized places change compared to baseline days. A baseline day represents a normal value for that day of the week. The baseline day is the median value from the 5‑week period Jan 3 – Feb 6, 2020. 

An overview of the data from the mobility data can be found [here](https://www.google.com/covid19/mobility/).

The code below loads the most recent version of the Covid-19 Google Community Mobility Reports as a `pandas` DataFrame object and assign the object to a variable called 'mobility_trends'

mobility_trends = pd.read_csv(
    "https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv",
    parse_dates=["date"],
)

mobility_trends

`Pandas` load the data as a DataFrame object. We can confirm this by using the built-in function `type()`:

type(mobility_trends)

## What is a [DataFrame](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#min-tut-01-tableoriented)?


> A DataFrame is a 2-dimensional data structure that can store data of different types (including characters, integers, floating point values, categorical data and more) in columns.

<img src="https://pandas.pydata.org/docs/_images/01_table_dataframe.svg" title='Pandas DataFrame' width="400" height="200"/>


# Viewing, Describing, and Accessing your Data

Once we have our data as a DataFrame data structure, we can view, describe, and access the data by applying [basic functionalities](https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html) associated with that structure. For example, we can perform various operations by using the so called `methods`. Examples of `pandas` methods are `head()` and `tail()`; `head()` displays by default the top five rows of the data and `tail()` displays by default the last five rows. You can display a custom number of row by passing that number in the brackets.

## View your data

# Show the first five rows using the method DataFrame.head()
mobility_trends.head()

# Show the last five rows using the method DataFrame.tail()
mobility_trends.tail()

# Specify the number of rows to return
mobility_trends.tail(10)

## Describing your DataFrame

# Dimensionality — number of rows and columns — of a DataFrame
mobility_trends.shape

# Use the print function to display the number of rows and columns
# in a DataFrame at the time of cell execution.
# Import the 'datetime' module (used below to display the current date)
import datetime

print(
    "\nAs of",
    datetime.datetime.now(),
    "The Google COVID-19 Community Mobility Reports contain",
    mobility_trends.shape[0],
    "rows and",
    mobility_trends.shape[1],
    "columns.",
)

# Accessing columns using the DataFrame.columns attribute
mobility_trends.columns

Let's display a concise summary of our DataFrame using the method `info()`

# Information about a DataFrame
mobility_trends.info()

Among other information, displayed are labels of the columns and the data type of each column. For example 'float64' refers to a floating point number, i.e., a number with a decimal point. In the Community Mobility Reports, floating point numbers are used to display the percentage mobility change for each category of places.

# Accessing columns and rows in your data

## Accessing columns

You can can access columns via column name and column position.

* *Accessing columns via column name*

Let's access a single column.

# Get the country column and save it to its own variable
# The double square bracket option `[[]]` gives DataFrame

mobility_trends_countries = mobility_trends[["country_region"]]
mobility_trends_countries.head()

# Display the type of data structure

type(mobility_trends_countries)

# The single square braket `[]` option gives Series
# pandas Series is a one-dimensional data structure or simply put, a single column

mobility_trends_countries_series = mobility_trends["country_region"].head()

# Display the type of data structure
type(mobility_trends_countries_series)

Let's now access multiple columns. We can access multiple columns by using a Python list. We use square brakets to create a list, for example `['country_region', 'sub_region_1', 'date']`. Python lists are useful as they store multiple items in the same variable.

mobility_trends[["country_region", "sub_region_1", "date"]].head()

* *Accessing columns via column position*

# Accessing columns 1, 2, adn 7 via column position and show the top five rows

mobility_trends.iloc[:, [1, 2, 7]].head()

# Accessing a subset of rows and columns. We access the top 3 rows and columns 1, 2, and 7

mobility_trends.iloc[0:3, [1, 2, 7]].head()

# Hands-on exercise

1. Create a new code cell.
2. Access the first 100 rows and the following columns from the DataFrame `mobility_trends`:

    * `country_region_code`
    * `date` 
    * `retail_recreation`

3. Assign the output to a variable called `mobility_trends_subset`.

## Accessing rows

Rows can be accessed via row labels `df.loc` and row index `df.iloc`.

# Before accessing particular rows, let's see the names of all countries in the dataset.
# We can achieve that by listing all unique values in the 'country_region' column.
mobility_trends.country_region.unique()

# Accessing specific rows from a DataFrame.
# We are interested in the data about the United Kingdom.

mobility_trends_UK = mobility_trends[
    mobility_trends["country_region"] == "United Kingdom"
]

mobility_trends_UK.head()

# Accessing data about multiple countries using the isin() method.
mobility_trends_countries = mobility_trends[
    mobility_trends["country_region"].isin(
        ["United Kingdom", "Germany", "Italy", "Sweden"]
    )
]

mobility_trends_countries.head()

# Filter by two conditions — country and county — simultenously
# First let's see the list of counties in the dataset

mobility_trends[
    mobility_trends["country_region"] == "United Kingdom"
].sub_region_1.unique()

# Access data about UK and Essex
mobility_trends_UK_Essex = mobility_trends[
    (mobility_trends["country_region"] == "United Kingdom")
    & (mobility_trends["sub_region_1"] == "Essex")
]

mobility_trends_UK_Essex.head()

In the above example, you could simply type in  
```
mobility_trends[mobility_trends['sub_region_1']=='Essex']
```
The command will return the same result as there is no region called 'Essex' outside the UK. However, there are instances in the data where regions in different countries have the same name. When this is the case, not specifying the country would return confusing outputs.

## Accessing multiple rows and columns and conditioning

mobility_trends_UK

# Let's see which UK counties had the lower retail and recreation mobility
# the day after Italy went in lockdown on 9 March 2020
mobility_trends_UK_10MARCH2020 = mobility_trends_UK.loc[
    (mobility_trends_UK["date"] == "2020-03-10")
    & (mobility_trends_UK["retail_and_recreation_percent_change_from_baseline"] < 0),
    ["sub_region_1", "retail_and_recreation_percent_change_from_baseline"],
]

# Sort in decreasing order
mobility_trends_UK_10MARCH2020.sort_values(
    by="retail_and_recreation_percent_change_from_baseline", ascending=True
)

# UK counties with the lower retail and recreation
# the day after UK went in lockdown on 23 March 2020
mobility_trends_UK_24MARCH2020 = mobility_trends_UK.loc[
    (mobility_trends_UK["date"] == "2020-03-24")
    & (mobility_trends_UK["retail_and_recreation_percent_change_from_baseline"] < 0),
    ["sub_region_1", "retail_and_recreation_percent_change_from_baseline"],
]

# Sort in decreasing order
mobility_trends_UK_24MARCH2020.sort_values(
    by="retail_and_recreation_percent_change_from_baseline", ascending=True
)

Let's identify the places in the UK with the highest reduction of workplaces mobility.

# We need to first find the index of the row
# with the highest reduction of workplaces mobility
mobility_trends_UK_workplaces = mobility_trends_UK[
    "workplaces_percent_change_from_baseline"
].idxmin()

mobility_trends_UK_workplaces

# Use the above index to access the row
# with the highest reduction of workplaces mobility
mobility_trends.iloc[[mobility_trends_UK_workplaces]]

In our basic exploratory data analysis, we found that as of 21 April 2021 the largest percentage mobility change in workplaces was in the London Borough of Islington, Greater London, on 13 April 2020 when the workplaces mobility was reduced with 91 per cent compared to a baseline period. This result is only for exploratory purposes. Note that [the same mobility in two different days would result in different percentage changes](https://support.google.com/covid19-mobility/answer/9824897?hl=en&ref_topic=9822927) due to the way in which actual mobility is compared to a baseline in the Google Covid-19 Community Mobility Reports.

# Handling Missing Values
Many data sets have missing values and the mobility data is not an exception. Handling missing values is a very common problem in data analysis. We will cover two simple ways of handling missing values in data: 
* Deletion — missing observations are simply dropped from the data set. 
    * Likewise - removes all data for an observation that has one or more missing values.     
    * Pairwise — removes observations with missing values only for the variables used in the current procedure (e.g., model or technique).
* Imputation — missing observations are replaced with inferred values. We will cover simple imputation methods in which missing values are replaced with column mean or row mean.

For more advanced methods and functionality, including interpolation methods, see the section ['Working with missing data'](https://pandas.pydata.org/pandas-docs/version/0.19.1/missing_data.html) in Pandas documentation.

## Detecting missing values
In `pandas`, missing values are represented as `NaN`, which stands for Not a Number. To detect missing values, we can use the function `isna()` (other functions, for example `isnull()` can be used to the same effect). The function returns boolean values (False, True) indicating whether each corresponding value in a DataFrame is missing.

mobility_trends.isna()

Let's determine the number of missing values for each column in the DataFrame.

mobility_trends.isna().sum()

It would be useful to quantify the percentage of values that are missing per column. To achieve this, we simply divide the number of missing values in a column by the number of rows in the DataFrame (and multiply the result by 100).

mobility_trends.isna().sum() / mobility_trends.shape[0] * 100

Let's now repeat the procedure for the UK mobility data only: 

mobility_trends_UK.isna().sum() / mobility_trends_UK.shape[0] * 100

The output shows that the missing values in most mobility categories are below 5 per cent except the missing values for residential mobility (8%) and parks mobility (21.7%).

## Removing missing values

We can remove missing values using the Pandas function [`dropna()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html). The default functionality removes rows that contain at least one missing value. The `dropna()` function provides other capabilities as well. For example, it is possible to remove columns (instead of rows) that contain missing values by specifying `axis = 1` within the brackets. Also, we can specify under what conditions rows or columns are removed: use `how = any` if you would like to drop rows or columns that contain any missing value, which is the default functionality; use `how = all` if you would like to drop rows or columns in which all values are missing.

mobility_trends_UK.dropna()

We did not specify particular columns on which to perform the `dropna()` function. Because we have a column ('metro_area') for which all values are missing, the `dropna()` function removed all observations from the DataFrame. This is analogous to a likewise deletion of missing values.

A more informative approach would be to specify the columns we are going to use in our analysis and drop missing values only for this subset of variables. We can drop rows that contain any missing values in the six mobility categories by passing the labels of those categories to the parameter `subset` as shown below:

mobility_trends_UK.dropna(subset=mobility_trends_UK.iloc[:, 9:15].columns)

mobility_trends_UK.shape

After removing the rows that contain missing values in the six mobility categories/columns, we are left with 137992 rows out of 191064 rows, a reduction of approximately 28%.

## Replacing missing values

Let’s replace NaN values with the mean of non-missing values. For example, we can replace missing values in the columns 'workplaces_percent_change_from_baseline' and 'residential_percent_change_from_baseline' by the mean of values in the two columns as determined by the Pandas `mean()` method.

# Replace the NaNs in the columns 'workplaces_percent_change_from_baseline'
# and 'residential_percent_change_from_baseline'
# by the mean of the non-missing values.
mobility_trends_UK[
    [
        "workplaces_percent_change_from_baseline",
        "residential_percent_change_from_baseline",
    ]
].fillna(
    value=mobility_trends_UK[
        [
            "workplaces_percent_change_from_baseline",
            "residential_percent_change_from_baseline",
        ]
    ].mean()
)

We now have the same number of rows (191064) as the original mobility_trends_UK DataFrame, with each missing value replaced by the mean value for the respective column. More advanced (and practical) approaches of replacing missing values can take into account groupings in the data and replace missing values with the mean value of a group of counties or the mean value of a time period; those operations would require more advanced Pandas functionality such as `groupby()`, which we will use in the next lab.

<img src="https://covid19-static.cdn-apple.com/applications/covid19-mobility/current/static/og_image_v1.png" width="200" height="100" align="right"/>

# Compare mobility data formats

A related aggregate, privacy-preserving, and freely available mobility data set is the Apple's [Mobility Trends Reports](https://covid19.apple.com/mobility). The data is updated daily and reflect in aggregate requests for directions in Apple Maps for select countries/regions, sub-regions and cities.  

The Mobility Trends Reports data can be downloaded from the website https://covid19.apple.com/mobility. However, because the data file is not at a stable location (URL), we cannot load the data from the website but instead access the data from a [COVID-19 mobility data aggregator on GitHub](https://github.com/ActiveConclusion/COVID19_mobility).

mobility_trends_covid_apple = pd.read_csv(
    "https://raw.githubusercontent.com/ActiveConclusion/COVID19_mobility/master/apple_reports/applemobilitytrends.csv"
)
mobility_trends_covid_apple.head()

```{admonition} Activity: Discussing data formats
Compare the format of the data in the _Apple Mobility Trends Reports_ to the format of the data in the _Google COVID-19 Community Mobility Reports_ and in _Our World in Data COVID-19 data_. Focus in particular on similarities and differences in how time series data is represented across data sets.
```

# Recording dependencies

# Install the watermark extension
!pip install -q watermark

# Load the watermark extension
%load_ext watermark

# Show packages that were imported
%watermark --iversions

Save a list of the packages (and their versions) used in the current notebook to a file named `requirements.txt`.

# Run pipreqsnb after specifying the path to the notebook
!pipreqsnb ../notebooks/04_data_design_and_data_wrangling.ipynb