# Human mobility during UK lockdowns

## End-to-End Data Science Project

In this first lab, you will go through the key steps in a data science project, starting from a research question, though data processing and analysis, to results that can potentially inform public policy. Specifically, we will go through five steps in the [data science lifecycle](https://www.textbook.ds100.org/ch/01/lifecycle_intro.html):
* formulate a research question of real-world relevance
* obtain real-world data, wrangle, and transform data
* explore and visualise data
* generate descriptive findings that can inform decision-making

Later on in the course, we will cover in detail the techniques, code, and workflow we use in this session.   

# Let's formulate our research question

## _How has human mobility differed across the three lockdowns in the United Kingdom during the COVID-19 pandemic?_

_Why is that research question important?_
* concerns many of us
* is of public health policy relevance, and 
* involves large data analysis requiring modern computational technique and tools

# Data to address the question

<img src="https://www.google.com/covid19/static/reports-icon-grid.png" title='Google Covid-19 Community Mobility Data' width="200" height="100" align="right"/>

We will use a real-world and real-time (updated daily) data on human mobility — The Google [Covid-19 Community Mobility Reports](https://www.google.com/covid19/mobility/)

An aggregated and anonymised large data set showing movement trends over time by geography, across six categories of places including retail and recreation, groceries and pharmacies, parks, transit stations, workplaces, and residential.

# Get started with Jupyter/Colab notebook

We will use the [Jupyter notebook]((https://jupyter.org) ) implemented on the Google Cloud, which is called [Google Colaboratory]((https://colab.research.google.com/notebooks/intro.ipynb#recent=true)) (or Colab for short). 

[The Jupyter Notebook](https://jupyter.org) is a user-friendly, free, open-source web application that allows you to combine live software code, explanatory text, visualisations and model outputs in a single computational notebook.

[Colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true) runs Jupyter notebook on the Google Cloud, allowing you to write and execute Python code in your browser and do scalable data analysis with no setup requirements.

You can learn more about the Colab and how to open a new notebook [here](https://colab.research.google.com/notebooks/intro.ipynb#recent=true).

## The Python programming language
We will code using the Python programming language. 
* Python is open source, free, and easy to learn programming language
* Python is one of world’s most popular programming language with a growing community
* Python programming skills are in high demand on the job market
* The Python data science community have developed an ecosystem of fast, powerful, and flexible open source tools for doing data science at scale.

# Let's get coding

The Colab notebook has two types of cells: code and text. You can add new cells by using the `+ Code` and `+ Text` buttons that are in the toolbar above the notebook and also appear when you are between a pair of cells.

Below is a code cell, in which we type in the arithmetic expression `21 + 21`. 

The code is prefixed by a comment. Commenting your code is a good research practice and part of your reproducible workflow. Comments in Python's code cells start with a hashtag symbol `#` followed by a white space character and some text. The text that follows the hashtag symbol on the same line is marked as a comment and is not therefore evaluated by the Python interpreter. Only the code (in this instance, "21 + 21") is evaluated and the output (in this instance, "42") will be displayed below the code cell.

To execute the cell, press `Shift` + `Enter` or click the Play icon on the left.

# Performing a basic arithmetic operation of addition
21 + 21

Python _reads_ the code entered in the cell, _evaluates_ it, and _prints_ the result (42).

# Python tools for data analysis

The Python data science community have developed an open source ecosystem of libraries for data science. 

We will use two main libraries: 
* `pandas` for data loading, wrangling, and analysis
* `seaborn` for data visualisation 

  <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" title='Pandas Logo' width="200" height="100" align="center" />
  
  <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" title='Pandas Logo' width="200" height="100" align="right" />


Think about those Python libraries as tools that allow you to do data science tasks at easy, with minimal programming requirements, while focusing on scalable and reproducible analysis of social data.

We first import the `pandas` library and, by convention, give it the alias `pd`.

# Import the pandas library
import pandas as pd

We can now access all the functions and capabilities the `pandas` library provides.

# Load your data

The Google Covid-19 [Community Mobility Reports](https://www.google.com/covid19/mobility/) data are provided as a comma-separated values (CSV) file. We load the CSV file into Python using the Pandas function `read_csv()`.

### What is a function? 
A function is a block of code that:
* takes input parameters  
* performs a specific task
* returns an output.

The function `read_csv()` will take as an input parameter a comma-separated values (csv) file, read the file, and return Pandas DataFrame.

We call a function by writing the function name followed by parenthesis. The function `read_csv()` takes many input parameters, for example
* `sep` — delimeter to use when reading the file; default is `,` but other possible delimeters include tab characters or space characters. 
* `parse_dates` — a column to be parsed as date and time. 

### Getting help when needed

To learn more about a function, in Colab, you use a question mark `?`. For example, to access help information about the function Pandas function `read_csv()`, you type in

pd.read_csv?

### Reading the Google Covid-19 Community Mobility Reports data

To read the Google Covid-19 Community Mobility Reports data, there is no need to download the file on your local computer. We just call the `read_csv()` function and specify the URL. The code below loads the most recent online version of the data. We also assign the loaded data set to a variable called mobility_trends.

# Loading the Google Covid-19 Community Mobility Reports data from web address (URL)
mobility_trends = pd.read_csv('https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv', parse_dates = ['date']) 

# View your data

# Display the top five rows
mobility_trends.head(10)

`Pandas` stores data as a [DataFrame](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#min-tut-01-tableoriented): 2-dimensional data structure in which variables are in columns, and observations are in rows.

<img src="https://pandas.pydata.org/docs/_images/01_table_dataframe.svg" title='Pandas DataFrame' width="400" height="200"/>

# Data Design: How are data generated? 

* The data shows _percentage changes_ in visitors to (or time spent in) six categories of places compared to baseline days. 
  * A baseline day represents a normal value for that day of the week. 
  * The baseline day is the _median value_ from the 5‑week period Jan 3 – Feb 6, 2020.

# Data Ethics, Privacy, and Fairnes Risks

* _Low privacy risks_: individual privacy is safeguarded as data is aggregated and anonymised.
* _Low Individual Fairness Risk but moderate Group Fairness Risk_: areas with greater mobility during lockdowns may be misattributed to non-compliance while greater mobility could also be due to some groups being essential workers or another category that does not enjoy working from home's privileges.
* _Sources of algorithmic confounding_: the design of the Google Maps' personalised recommendation system likely introduces mobility patterns into data but those would be very small at the geographic scale of the data (i.e., districts, counties).

# Describe your data

# Number of rows and columns in your DataFrame  
mobility_trends.shape

# Show a concise summary of your DataFrame
mobility_trends.info()

## Access specific columns and rows in your data



# Access a column  
mobility_trends['country_region']

We are interested in the data about the United Kingdom.

mobility_trends['country_region'].unique()

# Get the rows about United Kingdom and save it to its own variable
mobility_trends_UK = mobility_trends[mobility_trends['country_region'] == 'United Kingdom']
mobility_trends_UK

# Exploratory data analysis

Let's use the pandas method `describe()` to summarise the central tendency, dispersion and shape of our dataset’s distribution. 

We summarise data from the start day of the first UK lockdown (2020-03-24) and from the start day of the third UK lockdown (2021-01-06). NaN (Not a Number) values are excluded.

# Compute descriptive statistics about the start day of first UK lockdown
mobility_trends_UK[mobility_trends_UK['date'] == '2020-03-24'].describe()

# Compute descriptive statistics about the start day of third UK lockdown
mobility_trends_UK[mobility_trends_UK['date'] == '2021-01-06'].describe()

## Visualising a single time series variable

A time series is a sequence of data points arranged in time order. We import the `seaborn` library and use the `relplot` function to plot the relationship between time and mobility change.

import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

sns.set_theme(context='notebook', style="darkgrid", palette="pastel", font_scale=1.5)

sns.relplot(x = 'date',
            y = 'workplaces_percent_change_from_baseline',
            height = 5, aspect = 3,
            kind = 'line', lw = 3,
            data = mobility_trends_UK)

# Data wrangling

## Transforming from wide to long data format

In the original data, each mobility category is a separate column, which is known as wide data format. Wide data format is easy to read but restricts us to plotting only one mobility category at a time (unless we employ a `for` loop). We can plot all mobility categories simultaneously in `seaborn` after we reshape our data from wide format to long format. Long data format will have one column for all six mobility categories and one column for the values of those categories.

Below is a ['pandas`](https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html)schematic of wide (left) and long format data (right):

<img src="https://pandas.pydata.org/pandas-docs/stable/_images/reshaping_melt.png" title='Pandas DataFrame' width="600" height="300"/>

We use the pandas [`melt`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) function to  reshape our mobility categories from wide to long format. The function transforms a DataFrame into a format where one or more columns are identifier variables (id_vars), while other columns (value_vars) are turned into a long format, returning columns, ‘variable’ and ‘value’. In our example, id_vars are`country_region` and `date`, and value_vars are the six mobility categories. The `melt` function takes the following parameters:
* `DataFrame` — your pandas DataFrame
* `id_vars` — a list of identifier variables
* `value_vars` — a list of variables to turn into long format

At the end we use the `Pandas` method `dropna()` to remove missing values in the DataFrame.

# From wide to long format using the function melt
mobility_trends_UK_long = pd.melt(mobility_trends_UK, 
                                  id_vars =mobility_trends_UK.columns[[1,2,8]], 
                                  value_vars = mobility_trends_UK.columns[9:15]).dropna()
mobility_trends_UK_long

# Visualising mobility trends

# Visualising UK time series data for all six mobility categories
sns.relplot(x = 'date',
            y = 'value',
            col = 'variable', col_wrap = 2, 
            height = 5, aspect = 3,
            kind = 'line', lw = 3,
            facet_kws={'sharey': False},
            data = mobility_trends_UK_long)

# Mobility changes across lockdowns

For each lockdown, we consider the first three weeks for comparability.
* 2020-03-24 — 2020-04-13
* 2020-11-05 — 2020-11-25
* 2021-01-06 — 2021-01-26

# Subsets data about the three lockdowns

lockdown1 = mobility_trends_UK_long[(mobility_trends_UK_long['date'] >= '2020-03-24') & (mobility_trends_UK_long['date'] <= '2020-04-13')]
lockdown2 = mobility_trends_UK_long[(mobility_trends_UK_long['date'] >= '2020-11-05') & (mobility_trends_UK_long['date'] <= '2020-11-25')]
lockdown3 = mobility_trends_UK_long[(mobility_trends_UK_long['date'] >= '2021-01-06') & (mobility_trends_UK_long['date'] <= '2021-01-26')]
  
# Link the three DataFrames into one DataFrame using the Pandas `concat()` function
lockdowns = pd.concat([lockdown1,lockdown2,lockdown3], 
                      keys=["lockdown1", "lockdown2", "lockdown3"]).reset_index()

lockdowns.head()                      

## Split-Apply-Combine
Using the Pandas method `groupby()`, we split the data into groups (lockdown by mobility category), apply the function `mean()`, and combine the results.

# Explore descriptive statistics for one of the lockdown DataFrames
lockdowns.groupby(['level_0', 'variable'], sort=False)['value'].mean()

## Visual comparison of the three UK lockdowns

# Display the three lockdowns as a catplot multi-plot
grid = sns.catplot(x = "country_region",
            y = "value",
            hue = 'variable',
            col ='level_0',
            ci=99,
            kind="bar",
            data=lockdowns);
grid.set_ylabels("Mean mobility change from baseline (%)")

# Zooming in: Regional mobility trends

For decision-making and to inform public health interventions, we need to provide results at a higher resolution, for example at the regional level. Below we visualise the six mobility categories across UK regions (counties, districts) during the first lockdown. 

# Plotting mobility changes across UK regions during the first lockdown
sns.catplot(x="value",
                y="sub_region_1",
                col="variable", kind = 'box',
                sharex = False,
                height=35, aspect=0.13,
                color = 'y',
                data=lockdown1);

# Plotting mobility changes across UK regions during the second lockdown
sns.catplot(x="value",
                y="sub_region_1",
                col="variable", kind = 'box',
                sharex = False,
                height=35, aspect=0.13,
                color = 'y',
                data=lockdown2);

# Plotting mobility changes across UK regions during the third lockdown
sns.catplot(x="value",
                y="sub_region_1",
                col="variable", kind = 'box',
                sharex = False,
                height=35, aspect=0.13,
                color = 'y',
                data=lockdown3);

# Re-cap

Using a Colab computational notebook and Python open source tools, we analysed large real-world COVID-19 mobility data through exploratory data analysis and visualisation to address a research question of public health policy relevance.    

## Accessible hands-on data analysis

We integrated interactive tools and practical hands-on coding that lower barriers to entry for students with little to no programming skills.

## Open reproducible research workflow

We combine research question, Python code, explanatory text (comments), exploratory outputs and visualisations in a single document — anyone can check, reproduce, re-use (when we license open source), and improve our analysis.  
