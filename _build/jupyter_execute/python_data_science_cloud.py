## **Python for Data Analysis on the Cloud**

# Get Started with Jupyter & Colab notebooks

In this course, we will use the Jupyter notebook on the Cloud in the form of Google Colaboratory. 

[The Jupyter Notebook](https://jupyter.org) is an open-source web application that allows you to create and share documents that contain live code, equations, visualisations and narrative text. 

The [Google Colaboratory](https://colab.research.google.com/notebooks/intro.ipynb#recent=true) or Colab for short is a free Jupyter notebook environment that runs on the Google Cloud and requires no setup.

<img src="https://jupyter.org/assets/labpreview.png" align="left" width="400" height="200"/><img src="https://lh3.googleusercontent.com/-U942LFFpDZI/X7w30iDAXkI/AAAAAAAALA4/oVaylpfkynAGhOe7k40ZNP1cwSRYixeRQCNcBGAsYHQ/w1280-h800/screenshot.png" align="middle" width="400" height="200"/>

<br>

You can view notebooks shared publicly without a Google sign-in. In order to execute and change code, a Google account sign-in is required. You can find more information on how to create a Google account [here](https://support.google.com/accounts/answer/27441?hl=en). You can learn more about the Colab and how to open a new notebook [here](https://colab.research.google.com/notebooks/intro.ipynb#recent=true).

Students with no Google account will have an opportunity to access the Jupyter notebook on the cloud via [JupyterHub](https://jupyter.org/hub) and [The Littlest JupyterHub (also known as TLJH)](https://tljh.jupyter.org/) in particular.

<br>

## Learning resources

<i class="fas fa-code"></i> [The Jupyter Notebook.](https://jupyter-notebook.readthedocs.io/en/stable/index.html) Jupyter Team.

<i class="fas fa-code"></i> [Jupyter Notebook Tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook). DataCamp. 

<i class="fas fa-play-circle"></i> <i class="fas fa-code"></i> [Get started with Google Colaboratory](https://www.youtube.com/watch?v=inN8seMm7UI). Jake VanderPlas, Coding TensorFlow.

<i class="fas fa-play-circle"></i> <i class="fas fa-code"></i> [A hands-on introduction to Python for beginning programmers.](https://www.youtube.com/watch?v=MirG-vJOg04&t=1029s) Jessica McKellar, PyCon 2014.

<i class="fas fa-book"></i> <i class="fas fa-code"></i> Charles Severance. [Python for Everybody: Exploring Data In Python 3.](https://www.py4e.com/book)

<i class="fas fa-book"></i> David Amos et al. [Python Basics: A Practical Introduction to Python.](https://realpython.com/products/python-basics-book/) The authors make available [sample chapters](https://static.realpython.com/python-basics-sample-chapters.pdf).  

<i class="fas fa-play-circle"></i> [Getting Started With the Open Science Framework (OSF)](https://youtu.be/2TV21gOzfhw). Center for Open Science.

<br>


### Structure of Colab notebook
The `Colab notebook` has a simple structure that consists of three parts:
* Menubar
* Toolbar
* Cells

For an example of those features, see an example Colab notebook [*Overview of Colaboratory Features*](https://colab.research.google.com/notebooks/basic_features_overview.ipynb) below.

![title](Colab_example.png)

### Manage Jupyter Notebook Files
To open a new notebook:

```
File -> New notebook
```
To rename a notebook: 
```
File -> Rename notebook
```
To access revision history:
```
File -> Revision history
```
To check whether the cells in your notebook are executable in linear order:
```
Runtime -> Restart and run all
``` 
To share your Colab notebook and collaborate, you can create a shareable link by clicking the `Share` button at the top right of your Colab notebook and specify the type of access (e.g., Anyone with the link can view the notebook). You can then copy and share the link with your collaborators.

### Cells 
The notebook has two types of cells: code and text. You can add new cells by using the `+ Code` and `+ Text` buttons that are in the toolbar above the notebook and also appear when you hover between a pair of cells.

# Python Coding for Data Analysis

Below is a code cell, in which we type in the arithmetic expression `21 + 21`. 

The code is prefixed by a comment. Commenting your code is a good research practice and part of your reproducible workflow. Comments in Python's code cells start with a hashtag symbol `#` followed by a white space character and some text. The text that follows the hashtag symbol on the same line is marked as a comment and is not therefore evaluated by the Python interpreter. Only the code (in this instance, "21 + 21") is evaluated and the output (in this instance, "42") will be displayed below the code cell.

To execute the cell, press `Shift` + `Enter` or click the Play icon on the left.

# Performing a basic arithmetic operation of addition
21 + 21

Python _reads_ the code entered in the cell, _evaluates_ it, and _prints_ the result (42).

### Create a toy data set and perform basic data analysis
Let's create a list of the whole numbers (or integers) `4, 2, 8, 6`. 

Lists are one of the [built-in data types](https://docs.python.org/3/tutorial/introduction.html#lists) in Python. Elements in a list are separated by comma `,` and are enclosed in square brackets `[]`:

[4,2,8,6]

Let's assign the list of numbers to a variable called `even_numbers` using the =, which is called the assignment operator.   

even_numbers = [4,2,8,6]

You can now apply built-in functions from the [Python Standard Library](https://docs.python.org/3/library/) to the variable `even_numbers`. A function is a block of code that:
* takes input parameters  
* performs a specific task
* returns an output.

Python has various built-in functions, including `min()`, `max()`, `sorted()`. Take the function `min()`. Using our example of even numbers above, the function `min()` will take as an input parameter the four numbers to compare, perform the comparison, and return the number with the lowest value.

We call a function by writing the function name followed by parenthesis. The function `min()` takes only one input parameter, the input data in the form of a list or another Python data type we will discuss later in the course. When we call the function, we pass our list `even_numbers` as an argument inside the parentheses.

An argument is different from a parameter, although the two terms are often used interchangeably. A parameter is the generic variable listed inside the parentheses of a function, whereas an argument is the actual value or data you pass to the function when you call it.

# Find the number with the lowest value
min(even_numbers)

We can apply any other built-in Python function. For example, the `max()` function returns, intuitively, the number with the highest value. 

# Find the number with the highest value
max(even_numbers)

The function `sorted()` returns a sorted list of numbers in increasing order. We assign the resulting sorted list to a variable named `sorted_even_numbers`:

# Sort numbers in increasing order
sorted_even_numbers = sorted(even_numbers)
sorted_even_numbers

Functions often have multiple parameters. For example, in addition to your input data, the `sorted()` function takes two optional parameters. One of these parameters is `reverse`. If you type in `reverse = True`, the list will be sorted in descending order:

sorted(even_numbers, reverse = True)

Our list of even numbers is now sorted in descending order. 

<img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" width="150" height="100" align = "right">

# Descriptive statistics with `NumPy` 

Functions for scientific computing, data analysis, machine learning, and statistical modeling are not in the Python Standard Library but are part of Python libraries or packages. For example, the Python library [`NumPy`](https://numpy.org) for scientific computing includes functions for computing the mean (average of the numbers) and standard deviation (variation or dispersion of the numbers from the mean).              

To use `NumPy`, we first import the library and, by convention, give it the alias `np`.

# Import the NumPy library
import numpy as np

Now that we imported the module NumPy as `np`, you can view help on the module by typing the module alias followed by a question mark ?

np?

We now use `np.` to append each function we will use from NumPy, for example the functions `mean()` and `std`.

# Compute the mean of our list of numbers
np.mean(even_numbers)

# Compute the standard deviation of our list of numbers
np.std(even_numbers)

# Getting help

In Colab, you use a question mark `?` to access help information. For example, to access help information about a function in the Python Standard Library, such as `min()`, you type in

min?

:::{note}
In Jupyter, you access help by pressing `Shift` + `Tab` when you are typing in a cell in `edit` mode. See this [tutorial](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/) for the difference between `edit` mode and `command` mode.
:::

# Get help about the NumPy function mean()
np.mean?

<img src="https://pandas.pydata.org/docs/_static/pandas.svg" width="150" height="100" align="right">

# Loading real-world data with `pandas`

So far, we have used a toy data example. We will use the [`pandas`](https://pandas.pydata.org/docs/index.html) library to load a real-world data set. We will learn about pandas next session, here will just use key data loading functionality. Let's first import the `pandas` library and, by convention, give it the alias `pd`.

# Import the pandas library
import pandas as pd

<img src="https://ourworldindata.org/uploads/2019/02/OurWorldinData-logo.png" width="120" height="80" align="right">

## Data on Covid-19 by Our World in Data

We will load and explore the Data on COVID-19 by [Our World in Data (OWID)](https://ourworldindata.org/coronavirus). Details about the data are available on this GitHub [repository](https://github.com/owid/covid-19-data/tree/master/public/data): 
> _It is updated daily and includes data on confirmed cases, deaths, hospitalizations, testing, and vaccinations as well as other variables of potential interest._

The data on COVID-19 by Our World in Data is provided as a comma-separated values (CSV) file. We load the CSV file into Python using the `read_csv()` function from `pandas`. There is no need to download the file on your local computer or the cloud. We just specify the URL and use the code below to load the most recent online version of the data. We also assign the loaded data set to a variable called owid_covid.

owid_covid = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

We can now perform various operations on the data object by using the so called `methods`. Examples of `pandas` methods are `head()` and `tail()`; `head()` displays by default the top five rows of the data and `tail()` displays by default the last five rows. You can display a custom number of row by passing that number in in the brackets.

Let's display the top five rows using the method `head()`:

# View the top five rows of the data set
owid_covid.head()

# View the last five rows of the data set
owid_covid.tail()

## Describe the Covid-19 data

In addition to `pandas` methods, we can use `attributes` to access information about the metadata. For example, the attribute `shape` gives the dimensions of a DataFrame.

# Number of rows and columns in the data set
owid_covid_shape = owid_covid.shape
owid_covid_shape

The returned object is called tuples. Like lists, tuples contain a collection of data elements. But unlike lists, which are mutable, tuples are immutable, meaning that the element values cannot change. Also, compared to lists in which elements are inside square brackets `[]`, elements in tuples are inside parentheses `()`. 

To access a particular value in tuple, we use the square brackets. For example, to access the first element (i.e., number of rows) of the tuple `owid_covid_shape`, we type in

owid_covid_shape[0]

To access the second element (i.e., number of columns) of the tuple, we type in 


owid_covid.shape[1]

Note that indexing in Python starts from 0, so first element is index 0, second is index 1, and so on.

As of 11 May 2021, the data set contains 87,310 rows and 59 columns. But this is a live data set in which the number of rows are updated daily. To display these updates, we could use the `print()` function. The line of code below contains background text in quotes `''` and the up-to-date number of rows `owid_covid.shape[0]`  and number of columns `owid_covid.shape[1]` that will be inserted in the sentence each time the cell is executed.

print('In the most current data on COVID-19 by Our World in Data, the number of rows is', owid_covid.shape[0], 'and the number of columns is', owid_covid.shape[1])

In addition to the dimensions of the data set, we can access other metadata using attributes. For example, we can access the column labels of the data set using the attribute `columns`:

owid_covid.columns

Display a concise summary of the DataFrame using the method `info()` 

owid_covid.info()

Let's see what is the highest number of fully vaccinated adults in a country to date. We will use the variable `people_fully_vaccinated_per_hundred` and pandas' `max()` method.

owid_covid['people_fully_vaccinated_per_hundred'].max()

Once we know the highest number of fully vaccinated adults per hundred, we determine the index of the observation (country) associated with that number using the pandas' method `idmax()`. 

index_highest_vaccination = owid_covid['people_fully_vaccinated_per_hundred'].idxmax()
index_highest_vaccination

Finally, we select the particular row (country in this case) by its location in the index using `iloc`. 

owid_covid.iloc[[index_highest_vaccination]]

The above example is only for illustration of pandas functionality. We will unpack different approaches for data slicing and selecting with pandas in section _Data Design and Data Wrangling_.

# Hands-on exercise: Let's practice your Python skills

1. Open a new `Colab` notebook.
2. Add a new `Code` cell and include the following:
    * Import the pandas library and add a comment describing your code
    * Load the Data on COVID-19 by Our World in Data and assign the data to a variable name. Use an informative variable name that clearly describes what the data is about; you can use underscores to separate words in your variable name, e.g. COVID19_Data_Our_World_in_Data. Add a comment. 

3. For the loaded data set: 
    * Show the first 20 observations/rows
    * Show the last 5 observations/rows

4. When ready, share your Colab notebook with the class:
    * Create a shareable link by clicking the Share button at the top right of your Colab notebook   
    * Specify that Anyone with the link can view the notebook
    * Share the link with the class.

Before sharing your notebook, rerun your notebook from top to bottom using `Restart and run all` (under `Runtime` in the Colab menu bar) to ensure that your data analysis is computationally reproducible.

<img src="https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg" width="80" height="40" align="right">

# Markdown Text Cells

Double click a text cell to see the Markdown syntax used to format the text.

## **Headings**
Headings begin with the hash symbol '#,' followed by the space. There are six Headings. To create the largest heading, add one hash symbol, and to create the smallest heading, add six hash symbols.

```
# Header 1, Title example (Not shown below)
## Header 2, Subtitle example
### Header 3,
#### Header 4
##### etc.
```

## Header 2, Subtitle example
### Header 3,
#### Header 4
##### etc.

## **Lists**

```
* Item one (Note the space after *)
* Item two
* Item three
  * Sub-bullet
    * Sub-sub-bullet

```
* Item one
* Item two
* Item three
  * Sub-bullet
    * Sub-sub-bullet
  
  

## **Bold and Italic Text**
```
**This text is bold**
*This text is italic*
~This was mistaken text~
***This is both bold and italic text***
```
**This text is bold**

*This text is italic*

<del>A second line of stricken code</del>

***This is both bold and italic text***

## **Hyperlinks**
Markdown allows you to create links to content on the web using the following syntax: 
```
[Link title](https://)
```
For example, a hyperlink to the [Project Jupyter](https://jupyter.org) would look like that: 

```
[Project Jupyter](https://jupyter.org)
```

:::{note}
You can learn more about `Markdown` in `Jupyter` / `Colab` notebooks [here](https://www.datacamp.com/community/tutorials/markdown-in-jupyter-notebook), [here](https://www.earthdatascience.org/courses/intro-to-earth-data-science/file-formats/use-text-files/format-text-with-markdown-jupyter-notebook/) and [here](https://colab.research.google.com/notebooks/markdown_guide.ipynb#scrollTo=70pYkR9LiOV0). You can learn about the `Markdown` syntax in general [here](https://daringfireball.net/projects/markdown/syntax) and [here](https://www.markdownguide.org).
:::

# Hands-on exercise: Let's practice your Markdown skills
1. Create a new `Colab` notebook file.
2. Add a new `Text` cell and include:
* A notebook title (e.g. My Reproducible Research Workflow)
* A bullet list with:
  * A bold word for `Author`: and then add italised text for your name.
  * A bold word for `Affiliation`: and then add italised text for your University and Department.
  * A bold word for `Date`: and then add text for today’s date.
* Add another Text cell and include:
  * A list of at least two online datasets about Covid-19 you find interesting.
  * Add a hyperlink to each database in your list and include the name of the database in the title of the hyperlink.
* Add another Text cell and write a short research question you would be interesting in addressing using the Covid-19 datasets.

When you complete your exercise, download your notebook and make it available on an Open Science Framework (OSF) repository. You can download your Colab notebook from `File` and then `Download .ipynb`. You can learn how to create an OSF repository and deposit your notebook from the tutorial [Getting Started With the Open Science Framework](https://www.youtube.com/watch?v=2TV21gOzfhw) by the Center for Open Science.   

This exercise draws on Earth Lab's lesson [*Format Text In Jupyter Notebook With Markdown*](https://www.earthdatascience.org/courses/intro-to-earth-data-science/file-formats/use-text-files/format-text-with-markdown-jupyter-notebook/). 