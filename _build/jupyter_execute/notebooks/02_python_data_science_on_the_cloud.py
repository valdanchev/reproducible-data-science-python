## **Python for Data Analysis on the Cloud**

# Get Started with Jupyter & Colab notebooks

In this course, we will use the Jupyter notebook on the cloud.

[The Jupyter notebook](https://jupyter.org) is an open-source web application that allows you to create and share documents that contain live code, equations, visualisations, and narrative text. 

There are many free services that allow you to run Jupyter notebooks on the cloud. We will use Colab and Binder.  

[Colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true) is a free environment that runs Jupyter notebooks on the Google Cloud and requires no install or setup. You can view notebooks shared publicly without a Google sign-in. In order to execute and change code interactively, a Google account sign-in is required. You can find more information on how to create a Google account [here](https://support.google.com/accounts/answer/27441?hl=en). You can learn more about the Colab and how to open a new notebook [here](https://colab.research.google.com/notebooks/intro.ipynb#recent=true).

[MyBinder](https://mybinder.org) is a free, community-led infrastructure that opens Jupyter notebooks in an interactive and reproducible environment and requires no install or setup. Binder requires no account registration or log-in to execute and change code interactively.

<img src="https://jupyter.org/assets/homepage/jupyterpreview.webp" align="left" width="400" height="200"/>
<img src="https://lh3.googleusercontent.com/edryGqlH18ng3ff18ffCbHuLEqfWpSJuO-1sejiV6t3ZYuUEpLYD4nqD1oha8yI4K4c9y1lqaseOckOrG7wZ-M4vaQ=w640-h400-e365-rj-sc0x00ffffff" align="middle" width="400" height="200"/>

<br>

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

<img src="https://github.com/valdanchev/reproducible-data-science-python/blob/master/images/Colab_example.png?raw=true"/>

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

The code is prefixed by a comment. Commenting your code is a good practice and part of your reproducible workflow. Comments in Python’s code cells start with a hashtag symbol # followed by a single space and some text. The text that follows the hashtag symbol on the same line is marked as a comment and is not therefore evaluated by the Python interpreter. Only the code (in this instance, “21 + 21”) is evaluated and the output (in this instance, “42”) will be displayed below the code cell.

To execute the cell, press `Shift` + `Enter` or click the Play icon on the left.

# Perform a basic arithmetic operation of addition
21 + 21

Python _reads_ the code entered in the cell, _evaluates_ it, and _prints_ the result (42).

### Create a toy data set and perform basic data analysis
Let's create a list of the whole numbers (or integers) `4, 2, 8, 6`. 

Lists are one of the [built-in data types](https://docs.python.org/3/tutorial/introduction.html#lists) in Python. Elements in a list are separated by comma `,` and are enclosed in square brackets `[]`:

[4, 2, 8, 6]  # create a list

The comment `# create a list` is an example of an inline comment. Inline comments refers to a code statement on the same line. Inline comments are separated by at least two spaces from the code statement. Similar to block comments, inline comments start with a hashtag symbol # followed by a single space and some text.

Let's assign the list of numbers to a variable called `even_numbers` using the =, which is called the assignment operator.   

even_numbers = [4, 2, 8, 6]

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

sorted(even_numbers, reverse=True)

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

In Jupyter and Colab, you can access help information by using the `help()` function or a question mark `?`. For example, to access help information about a function in the Python Standard Library, such as `min()`, you type in

help(min)

# Alternatively, you can symply type
min?

:::{note}
In Jupyter, you access help by pressing `Shift` + `Tab` when you are typing in a cell in `edit` mode. See this [tutorial](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/) for the difference between `edit` mode and `command` mode.
:::

# Get help about the NumPy function mean()
help(np.mean)

# Readability of your Python code

To write readable, consistent, and clean code, it is important to consider the [PEP 8 (or Python Enhancement Proposal) style guide for Python code](https://peps.python.org/pep-0008/). The guide describes the rules for writing a readable Python code. Below are outlined key rules to keep in mind when you write your Python code (for details and examples, check out the [PEP 8 style guide](https://peps.python.org/pep-0008/).


* **Naming conventions**
    * Variable names (e.g., `even_numbers`) should be lowercase, with words separated by underscores as necessary to improve readability.
    * Names to avoid (as, in some fonts, they are indistinguishable from the numerals one and zero): the characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single character variable names.


* **Comments**
    * PEP 8 distinguishes block comments, inline comments, and documentation strings (or docstrings for short):
        * Block comments in Python's code cells apply to the lines of code that follows them, and follow the same indentation as the code. Block comments are typically formed of complete sentences, each sentence starting with a capitalized word and ending in a period. Each line of a block comment starts with a hashtag symbol `#` followed by a single space and some text.
        * Line comments appears on the same line as a statement and is separated by at least two spaces from the statement. Each line comment starts with a hashtag symbol `#` followed by a single space and some text.
        * Dockstrings are used to document Python modules, functions, classes, or methods. Docstrings are surrounded by `"""triple double quotes"""`. You likely read docstrings more often (for example, when accessing help information about a function) than write them. See [PEP 8](https://peps.python.org/pep-0008/#documentation-strings) for details on docstrings.


* **Maximum line length**
    * Limit all lines to a maximum of 79 characters. To split a long command over multiple lines, one can break down code into readable statements using parenthesis. Another approach is to use the backslash symbol `\`. 
    * Long blocks of text (comments) should be limited to 72 characters. 
    * When applicable and agreed upon, it would be okay to increase the line length limit up to 99 characters, provided that comments are still limited to 72 characters.
    

* **Indentation**
    * Indentation in Python is the spaces at the beginning of a code line. Indentation is important not only because of code readability but particularly because in Python statements arranged at the same indentation level are considered to form part of a single code block. So, incorrect indentation in Python would likely produce an IndentationError or an errorless output.
    * Use 4 spaces per indentation level.
    

* **Tabs or Spaces?**
    * Spaces are the preferred indentation method.
    * Python disallows mixing tabs and spaces for indentation.
    
    
* **Whitespace in Expressions and Statements**
    * Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not). (e.g., `sorted_even_numbers = sorted(even_numbers)`)
    * Don’t use spaces around the `=` sign when used to indicate a keyword argument (e.g., `reverse=True`)


As mentioned in PEP 8, section *A Foolish Consistency is the Hobgoblin of Little Minds*, style guide recommendations may not be applicable in some circumstances. In such circumstances, you could look for examples from the Python community and use your best judgment.  

# Running Terminal commands in Jupyter/Colab notebook

In addition to running Python code, we will also execute Terminal commands in our Jupyter notebooks. Terminal commands are very useful for obtaining information (for example, you can check the version of your Jupyter notebook, Python, or packages), managing computer files, and installing Python packages. 

To execute Terminal commands, you would typically need to use a command-line interface (CLI) such as the Terminal (macOS) or Command Prompt (Windows), which can be challenging. Fortunately,  [Jupyter notebook allows you to run Terminal commands in the notebook code cells](https://anaconda.zendesk.com/hc/en-us/articles/360023858254-Executing-Terminal-Commands-in-Jupyter-Notebooks) by prepending an exclamation mark (`!`) to the beginning of the command. Any command appearing after the mark in the line will not be executed from the Python environment but from your operating system's command-line interface (CLI). You can think of the exclamation mark (`!`) as introducing command-line interface (You can learn more about the command-line interfaces from [this tutorial](http://swcarpentry.github.io/shell-novice/) by The Carpentries). 

As an example, you can determine the version of the Jupyter notebook you use by typing the line below, in which the question mark (`!`) is followed by the command `jupyter-notebook` and the flag `--version`. Command-line flags are used to specify options and modify command's execution. As an output, the command prints the version of your active Jupyter notebook.

!jupyter-notebook --version

# Installing packages with `pip`

Command-line tools are particularly useful for installing packages that are not part of the [Python standard library](https://docs.python.org/3/library/). To install packages, we will use the Python's packaging manager `pip`. A list of all Python packages available for instalation via `pip` can be found at https://pypi.org. 

Because `pip` is a command-line tool, we will prepend an exclamation mark (`!`) to the package installation command every time we use `pip`. The `pip install` command supports flags, for example we will specify the flag `-q` (short for `--quiet`) that hides output/warnings which may cause confusion initially. For example, to install the Python package for statistical modeling, `statsmodels`, we would type:

!pip install -q statsmodels

The command above installs the most recent version of a package, which you can determine (along other useful information about the package) by typing:

!pip show statsmodels

If you are interested in installing a previous version of `statsmodels` (for example, for the purpose of reproducing a research project which uses a previous version), you can find the available previous versions at https://pypi.org and install a version of choice by typing the version number, for example:

!pip install -q statsmodels==0.12.2

# Jupyter magic commands

Jupyter *magic commands* are special commands that add to the Python syntax and provide capabilities that help researchers solve various research problems related to data analysis and workflow. Magic commands are prefixed in the Jupyter notebook by a single `%` character when they operate on one line of code (known as line magics) or by double `%%` characters when they operate on multiple lines of code (known as cell magics).

You can list all available magic commands by using the line magic `%lsmagic` as shown below.

%lsmagic

Some of the popular magic commands we will use include:

* Printing out the execution time of a Python command

%time np.mean(even_numbers)

* Listing all variables already defined in the current notebook

%who

* Displaying matlpotlib/Seaborn graphs in the notebook (applies to older versions of Jupyter notebook, obsolete in newer versions)

%matplotlib inline

You can read more about the Jupyter magic commands [here](https://ipython.readthedocs.io/en/stable/interactive/magics.html#) and [here](https://jakevdp.github.io/PythonDataScienceHandbook/01.03-magic-commands.html).    

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

owid_covid = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")

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

print(
    "In the most current data on COVID-19 by Our World in Data, the number of rows is",
    owid_covid.shape[0],
    "and the number of columns is",
    owid_covid.shape[1],
)

In addition to the dimensions of the data set, we can access other metadata using attributes. For example, we can access the column labels of the data set using the attribute `columns`:

owid_covid.columns

Display a concise summary of the DataFrame using the method `info()` 

owid_covid.info()

Let's see what is the highest number of fully vaccinated adults in a country to date. We will use the variable `people_fully_vaccinated_per_hundred` and pandas' `max()` method.

owid_covid["people_fully_vaccinated_per_hundred"].max()

Once we know the highest number of fully vaccinated adults per hundred, we determine the index of the observation (country) associated with that number using the pandas' method `idmax()`. 

index_highest_vaccination = owid_covid["people_fully_vaccinated_per_hundred"].idxmax()
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