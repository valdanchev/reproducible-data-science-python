Textbook outline
==================

The textbook provides an accessible hands-on introduction to data science techniques, skills, and workflows necessary to perform open, reproducible, and ethical data analysis. In the textbook, you will study research problems of real-world relevance, such as vaccine hesitancy and the impact of COVID-19 lockdown measures on human mobility. You will use real-world social data, including large-scale anonymised mobility data from digital sources and recent COVID-19 survey data. 

You will engage with open reproducible data science workflows using open-source and free computational tools, including the Python programming language, Jupyter notebook in the Cloud, Markdown, version control, and the Open Science Framework. No software installation or setup is required as you will use cloud computing. Specifically, you will use Jupyter notebooks on your laptop or tablet (or even smartphone) via free cloud environments such as the Colaboratory (Colab for short) or MyBinder. Fortunately, the Python data science community have developed an open source ecosystem of libraries for data analysis, statistical modelling, machine learning, and network analysis, including the libraries `pandas`, `seaborn`, `scikit-learn`, `statsmodels`, and `networkX`. This suite of libraries will allow us to analyse, visualise, and model data at easy, with minimal programming requirements, while focusing on reproducible analysis of social data.

Most of all, this textbook aims to contribute to inclusive, diverse, and supportive learning.

## Key themes
Throughout the textbook, you will learn, in an accessible way, practical data science skills, including data wrangling, clustering, resampling, and visualisation of various data sources as well as applications of techniques from machine learning (e.g., cross-validation to mitigate the risk of overfitting), causal inference (e.g., causal graphs to detect confounding), and network analysis (e.g., community detection to discover tightly knit communities). The content is organised around four foundational data science tasks — (i) data preprocessing, (ii) description (and exploratory data analysis and visualisation), (iii) prediction, and (iv) causal inference (which includes counterfactuals). Attention is given to model evaluation and problems of overfitting, selection bias, confounding, and computational reproducibility. Throughout the textbook are discussed issues of data ethics, privacy, and fairness of data science models.

The textbook teaches you how to critically evaluate data and biases intrinsic to real-world data and real-time data (many of the COVID-19 data set we use are updated daily). Instead of looking for 'positive' results and 'statistically significant' relationships as a way of finding order in often disorderly data, you will learn open and reproducible workflow. In this workflow, you will describe your steps throughout the research process (not just your final results), make transparent choices of parameter selection, and document in your notebooks the results you have obtained, however 'useful' or '(un)expected' they may seem.

## Prerequisites
Prior knowledge of programming is not required as coding for data analysis will be taught from first principles. Background in mathematics or statistics are not required beyond basic algebra and descriptive statistics. 

## Who this textbook is for
The textbook would be ideal for students in the social sciences, public health, and related fields who want to study real-world problems using diverse data sets but lack data science knowledge and coding skill.

<br>


# What is Reproducible Data Science? 

The textbook is designed around an understanding of data science as the use of coding to draw conclusions from diverse data sets by solving five classes of tasks (see [Ani Adhikari and John DeNero, 2020](https://inferentialthinking.com/chapters/01/what-is-data-science.html); [Hernán et al. 2019](https://doi.org/10.1080/09332480.2019.1579578)): 
1. _Data preprocessing_ — preparing data for analysis using techniques for data cleaning, data wrangling, and data transformation.
2. _Description_ — discovering patterns in data using exploratory data analysis, visualisation, and automated discovery techniques.
3. _Prediction_ — using information about outcomes we know to make informed guesses about unknown outcomes by applying techniques from simple regression to (supervised) machine learning.
4. _Causal data analysis_ — studying cause-and-effect questions via the application of causal graphs, counterfactuals, and causal inference techniques.
5. _Inference_ — quantifying our degree of certainty to determine whether what we find in our data will hold among different scenarios using resampling methods and related techniques.

This textbook does not cover a single data science task in detail but introduces you to these tasks with a focus on real-world data and applications, hands-on computation, and reproducible data analysis.

In a typical [Data Science Lifecycle](https://www.textbook.ds100.org/ch/01/lifecycle_intro.html), we will begin with a research question, and then select our data set(s), preprocess the data, perform descriptive analysis to explore basic features of our data, and then model our data to predict an outcome or establish causal effect. Throughout the data science lifecycle, transparency of research process and computational reproducibility are essential. 

This understanding of data science is inspired by many, including the UC Berkeley's data science program, particularly the courses [Data 8: Foundations of Data Science](http://data8.org/sp21) and [Data 100: Principles and Techniques of Data Science](https://ds100.org), and the associated textbooks, open educational resources, and communities; Matthew Salganik's book [Bit by Bit: Social Research in the Digital Age](https://www.bitbybitbook.com/en/1st-ed/preface/); The Summer Institutes in Computational Social Science by Chris Bail and Matt Salganik and associated [learning resources](https://sicss.io/overview); Ramesh Johari's course at Stanford University [Fundamentals of Data Science](https://web.stanford.edu/class/msande226/); The Turing Way Community and their [Turing Way: A Handbook for Reproducible Data Science](https://the-turing-way.netlify.app/welcome). Finally, the UC Berkeley's 2020 [Workshop on Data Science Education](https://data.berkeley.edu/academics/resources/data-science-education-resources/2020-national-workshop-data-science-education) was instrumental in building both my vision and toolkit for democratising data science.

<br>

# Learning objectives

By the end of the module, you will be able to:

* Freely use computational tools — Python, Jupyter, Markdown — in the cloud to perform and report basic data analysis.
* Wrangle, explore, visualize, and model tabular and network data using Python libraries.
* Build a transparent and reproducible research workflow ranging from data loading to research report.
* Perform, critically interpret, and openly communicate research process and results from analysis using basic models for machine learning and causal inference.
* Identify and deal with issues of overfitting, selection bias, and confounding.
* Articulate and address issues of data ethics and fairness of data science models in the social domain.
* Write a clean, reusable, and reproducible code in Python. 
* Share your work and collaborate on research projects with others.

<br>


# Learning resources

To accommodate students' different styles of learning, I have assembled a range of resources, from books and articles to short video lectures and tutorials on coding and data analysis. You are welcome to focus on learning materials you personally find the most helpful. Below are listed some of the key readings and learning resource that can help you get started, and throughout the textbook I point to particular learning resources that are directly relevant to the lab’s topic.

:::{note}
We distinguish four categories of learning resources by marking articles with a <i class="fas fa-scroll"></i>, books with a <i class="fas fa-book"></i>, videos with a <i class="fas fa-play-circle"></i>, and tutorials with a <i class="fas fa-code"></i>. The categories are not mutually exclusive.
:::

<br>

<i class="fas fa-book"></i> Foster, I., Ghani, R., Jarmin, R.S., Kreuter, F., Lane, J. 2020. **Big Data and Social Science: Data Science Methods and Tools for Research and Practice** (2nd edition). Chapman and Hall/CRC. [[Online version freely available]](https://textbook.coleridgeinitiative.org) <br>
&nbsp;&nbsp;&nbsp;<i class="fas fa-code"></i> Book's Jupyter [notebooks](https://workbooks.coleridgeinitiative.org) with data, code, and practical programming exercises are freely available through Binder and GitHub.

<i class="fas fa-book"></i> Jake VanderPlas. 2016. **Python Data Science Handbook.** O'Reilly. [[Online version freely available]](https://jakevdp.github.io/PythonDataScienceHandbook/) <br>
&nbsp;&nbsp;&nbsp;<i class="fas fa-code"></i> Book's content is freely available in the form of Jupyter [notebooks](https://github.com/jakevdp/PythonDataScienceHandbook).

<i class="fas fa-book"></i> McKinney, W. 2017. **Python for Data Analysis: Data Wrangling with Pandas, Numpy, and IPython** (2nd edition). O′Reilly. <br>
&nbsp;&nbsp;&nbsp;<i class="fas fa-code"></i> Book's materials and Jupyter [notebooks](https://github.com/wesm/pydata-book) are freely available. 

<i class="fas fa-book"></i> Daniel Chen. 2018. **Pandas for Everyone: Python Data Analysis.** Addison-Wesley Professional.<br>
&nbsp;&nbsp;&nbsp;<i class="fas fa-code"></i> Freely available Jupyter [notebooks](https://github.com/chendaniely/pandas_for_everyone) on Pandas. <br>
&nbsp;&nbsp;&nbsp;<i class="fas fa-play-circle"></i> [Introduction to Data Processing in Python with Pandas](https://www.youtube.com/watch?v=5rNu16O3YNE), SciPy 2019 tutorial by Daniel Chen.

<i class="fas fa-book"></i> Aurélien Géron. 2019. **Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 2nd Edition.** O’Reilly.<br>
&nbsp;&nbsp;&nbsp;<i class="fas fa-code"></i> Freely available Jupyter [notebooks](https://github.com/ageron/handson-ml2). <br>

<i class="fas fa-play-circle"></i> [Reproducible Data Analysis in Jupyter](https://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/) by Jake Vanderplas.

<i class="fas fa-play-circle"></i> [Machine Learning with Scikit Learn](https://www.youtube.com/watch?v=HC0J_SPm9co) by Jake VanderPlas.

<i class="fas fa-book"></i> <i class="fas fa-code"></i> The Turing Way Community, Becky Arnold, Louise Bowler, Sarah Gibson, Patricia Herterich, Rosie Higman, ... Kirstie Whitaker. (2019, March 25). **The Turing Way: A Handbook for Reproducible Data Science** (Version v0.0.4). Zenodo. http://doi.org/10.5281/zenodo.3233986 [[Freely available online guide]](https://the-turing-way.netlify.app/welcome)

<i class="fas fa-book"></i> <i class="fas fa-code"></i> Wasser, L. and Palomino, J. (Updated: September 03, 2020) **Introduction to Earth Data Science.** [[Freely available online textbook]](https://www.earthdatascience.org/courses/intro-to-earth-data-science/)

<i class="fas fa-book"></i> Matthew Salganik. 2017. **Bit by Bit: Social Research in the Digital Age.** Princeton University Press. [[Online version freely available]](https://www.bitbybitbook.com/en/1st-ed/preface/)

<i class="fas fa-book"></i> Morgan, S. L. and Winship, C. 2014. **Counterfactuals and Causal Inference** (2nd edition). Cambridge University Press.

<i class="fas fa-book"></i> <i class="fas fa-code"></i> Cunningham, S. 2021. **Causal Inference: The Mixtape.** Yale University Press. [[Online version, including Python code, freely available]](https://mixtape.scunning.com)

<i class="fas fa-book"></i> Kelleher, J. and Tierney, B. 2018. **Data Science.** MIT Press.

<i class="fas fa-code"></i> Pedro Saleiro, Kit T. Rodolfa, Rayid Ghani. [Dealing with Bias and Fairness in Data Science Systems: A Practical Hands-on Tutorial](https://dssg.github.io/fairness_tutorial/). <br>
&nbsp;&nbsp;&nbsp; <i class="fas fa-play-circle"></i> [Corresponding video tutorial](https://www.youtube.com/watch?v=N67pE1AF5cM), KDD 2020 tutorial. 

<br>

# Software stack

The textbook uses [Python](https://www.python.org). Python is open source, freely available, and accessible general-purpose programming language. A great feature of Python (and other open-source programing languages) are the collaborative communities which have developed a diverse ecosystem of powerful libraries or tools for doing data science. Those open-source tools allow us to perform computational data analysis at easy while focusing on the understanding of our results and on their evaluation and implications. The open-source tools for data analysis we will use the most include [`pandas`](https://pandas.pydata.org/docs/index.html) for data loading, wrangling, and exploratory data analysis; [`seaborn`](https://seaborn.pydata.org/#) and [`Matplotlib`](https://matplotlib.org) for data visualisation; [`scikit-learn`](https://scikit-learn.org/stable/index.html) for prediction, pattern discovery and other machine learning tasks; and [`statsmodels`](https://www.statsmodels.org/stable/index.html) for statistical modelling. Many of these tools are built on top of [`NumPy`](https://numpy.org) and [`SciPy`](https://www.scipy.org/scipylib/index.html), two foundational libraries for scientific computing in Python.

We write Python code in [Jupyter Notebooks](https://jupyter.org). The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. 

We use cloud services to run Jupyter Notebook. The cloud infrastructure provides access to pre-configured data science computational environments. Learners can open a notebook and interact with the code without the need of software installation and configuration. Specifically, learners can access the notebooks that form part of this learning resource via MyBinder or Colab. [MyBinder](https://mybinder.org) is a free, public online service that runs Jupyter notebooks in an executable and reproducible environment, enabling interactive data analysis. The [Colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true) is a free environment that runs Jupyter notebooks on the Google Cloud, enabling interactive data analysis.

---
<img src="https://github.com/valdanchev/reproducible-data-science-python/blob/master/images/open_source_python_data_science.png?raw=true">

---

# Data sets

Below is a list of the main data sets we use in the textbook.

:::{note}
We believe in open science and open data, and, therefore, the majority of the textbook uses open data sets. We also believe in responsible use of fine-resolution social data for data science education with the understanding that such fine-resolution data may be safeguarded due to privacy restrictions and risk of disclosure. The textbook, therefore, uses a mixture of (mostly) open data and safeguarded data.
:::

#### **1. Mobility Data from Digital Sources [Open]**

[COVID-19 Google Community Mobility Reports]((https://www.google.com/covid19/mobility/))
* Aggregated and anonymised mobility trends data that protect individual privacy.
* Displays human mobility trends by country and region across categories of places, including retail and recreation, groceries and pharmacies, parks, transit stations, workplaces, and residential. 
* Enables an exploration of changes in mobility trends as a response to non-pharmaceutical public health interventions (e.g., lockdowns, school closure) designed to reduce the spread of COVID-19.

<img src="https://www.google.com/covid19/static/reports-icon-grid.png" title='Google Covid-19 Community Mobility Data' width="300" height="150"/>

#### 2. Survey Data [Safeguarded]

[The Understanding Society: COVID-19 Study](https://www.understandingsociety.ac.uk/topic/covid-19) 
* UK survey asking participants about their experiences during the COVID-19 pandemic. We use [Wave 6](https://www.understandingsociety.ac.uk/2021/01/29/covid-19-survey-wave-6-released) of the survey.
* The data are safeguarded and can be accessed via the [UK Data Service](https://beta.ukdataservice.ac.uk/datacatalogue/studies/study?id=8644).

<img src="https://www.cdcs.ed.ac.uk/files/styles/large_16x9/public/2019-08/Spotlighton_AjaMurray_A4_UKHLS_Logo_positive_RGB_300dpi.jpg?itok=YmQnr_oq" width="300" height="150" >

#### 3. Administrative Data on COVID-19 [Open]

[Our World in Data (OWID)](https://ourworldindata.org/coronavirus) data on COVID-19 confirmed cases, deaths, hospitalizations, testing, and vaccinations reported by governments and international organizations.

<img src="https://ourworldindata.org/uploads/2019/02/OurWorldinData-logo.png" width="120" height="80"> 
<br>
<br>

In addition to the above three data sets, we explore in exercises various other data sets related to COVID-19, including the [World Health Organisation (WHO) COVID-19 Global Data](https://covid19.who.int) and [Apple's COVID-19 Mobility Trends Reports](https://covid19.apple.com/mobility).

<br>


# How to get the most of the open learning resource?

You can read the learning resource in its entirety on this website. You can also view each individual notebook on GitHub by clicking on the respective ![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label) button below. 

To interactively work with the code, you can access the interactive versions of the Jupyter notebooks via the free cloud services [MyBinder](https://mybinder.org) and [Colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true).

* By clicking on a ![Binder](https://mybinder.org/badge_logo.svg) button below, you will launch the Jupyter notebooks in a cloud instance. MyBinder will open the notebooks in a reproducible computational environment (i.e., an environment that contains pre-installed the Python packages used in the original notebooks) from where you can interactively run and modify the code in your browser. MyBinder is a free, public cloud service. No setup or a login is required to execute the notebooks.

* By clicking on a ![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg) you will open a Jupyter notebook on Google Cloud. Once open in your browser, you can interactively run and modify the notebook. Colab is a free cloud service that requires no setup. You can view the notebooks without a login but to execute and modify a notebook, a Google account and a login are required.

| Textbook chapter | View on GitHub | Launch on myBinder.org | Open in Colab |
|--------------|-----------|--------------|-----------|
| [About the textbook](https://valdanchev.github.io/reproducible-data-science-python/notebooks/00_textbook_outline.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/00_textbook_outline.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/00_textbook_outline.ipynb) |
| [End-to-End Data Science Project](https://valdanchev.github.io/reproducible-data-science-python/notebooks/01_end_to_end_data_science_project.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/01_end_to_end_data_science_project.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/01_end_to_end_data_science_project.ipynb) |
| [Python Data Science on the Cloud](https://valdanchev.github.io/reproducible-data-science-python/notebooks/02_python_data_science_on_the_cloud.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/02_python_data_science_on_the_cloud.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/02_python_data_science_on_the_cloud.ipynb) |
| [Open Reproducible Data Science Workflow](https://valdanchev.github.io/reproducible-data-science-python/notebooks/03_open_reproducible_workflows.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/03_open_reproducible_workflows.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/03_open_reproducible_workflows.ipynb) |
| [Data Design and Data Wrangling](https://valdanchev.github.io/reproducible-data-science-python/notebooks/04_data_design_and_data_wrangling.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/04_data_design_and_data_wrangling.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/04_data_design_and_data_wrangling.ipynb) |
| [Data Exploration and Data Visualisation](https://valdanchev.github.io/reproducible-data-science-python/notebooks/05_data_exploration_and_visualisation.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/05_data_exploration_and_visualisation.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/05_data_exploration_and_visualisation.ipynb) |
| [Pattern Discovery using Unsupervised Learning](https://valdanchev.github.io/reproducible-data-science-python/notebooks/06_pattern_discovery_using_unsupervised_learning.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/06_pattern_discovery_using_unsupervised_learning.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/06_pattern_discovery_using_unsupervised_learning.ipynb) |
| [Prediction using Supervised Learning](https://valdanchev.github.io/reproducible-data-science-python/notebooks/07_prediction_using_supervised_learning.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/07_prediction_using_supervised_learning.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/07_prediction_using_supervised_learning.ipynb) |
| [What Causes What? Introduction to Causal inference](https://valdanchev.github.io/reproducible-data-science-python/notebooks/08_causal_inference.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/08_causal_inference.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/08_causal_inference.ipynb) |
| [Network Analysis](https://valdanchev.github.io/reproducible-data-science-python/notebooks/09_network_analysis.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/09_network_analysis.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/09_network_analysis.ipynb) |
| [Data Ethics](https://valdanchev.github.io/reproducible-data-science-python/notebooks/10_data_ethics.html) | [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/valdanchev/reproducible-data-science-python/blob/master/notebooks/10_data_ethics.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/valdanchev/reproducible-data-science-python/604f6843faf5052420d4254073e0ea1db809864c?urlpath=lab%2Ftree%2Fnotebooks%2F04_data_design_and_data_wrangling.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/_build/html/_sources/notebooks/10_data_ethics.ipynb) |

<br>


# Acknowledgment

I am grateful to many people and communities who helped with discussions, advice, and open-source teaching materials (All errors, of course, are mine.):

[Matthew Brett](https://www.birmingham.ac.uk/staff/profiles/psychology/brett-matthew.aspx) \
[Matthew Salganik](http://www.princeton.edu/~mjs3/)\
[Chris Bail](https://dssoc.github.io)\
[Rayid Ghani](http://www.rayidghani.com) \
[Scott Cunningham](http://www.scunning.com) \
[Mason A Porter](https://www.math.ucla.edu/~mason/)\
[Bernie Hogan](https://github.com/oxfordinternetinstitute/sds-python) \
[Adam Dennett](https://www.ucl.ac.uk/bartlett/casa/dr-adam-dennett) \
[Jake Vanderplas](https://github.com/jakevdp)\
[Daniel Chen](https://github.com/chendaniely) \
[James Allen-Robertson](https://www.essex.ac.uk/people/allen57501/james-allen-robertson) \
[Fernando Pérez](http://fperez.org) \
[Chris Holdgraf](https://predictablynoisy.com) \
[Sharad Goel](https://5harad.com) \
[Dani Arribas-Bel](http://darribas.org/index.html)\
[Data Science Education at Berkeley](https://data.berkeley.edu) \
[The Turing Way Community](https://www.turing.ac.uk/research/research-projects/turing-way-handbook-reproducible-data-science) \
[Earth Lab CU-Boulder](https://www.earthdatascience.org/tags/reproducible-science-and-programming/) \
[DataCamp for Classrooms](https://www.datacamp.com/groups/classrooms) \
[Berkeley Initiative for Transparency in the Social Sciences (BITSS)](https://www.bitss.org/resource-library/?_sft_resource_type=websites-audio-video) \
[Meta-Research Innovation Center at Stanford (METRICS)](https://metrics.stanford.edu)\
[The Carpentries](https://carpentries.org)\
[Tiffany Timbers](https://www.tiffanytimbers.com/)\
[Ben Marwick](http://faculty.washington.edu/bmarwick/)

I also thank the participants at the 2021 National Workshop on Data Science Education (organised by UC Berkeley’s Division of Computing, Data Science, and Society), third year students at the Department of Sociology, University of Essex, who studied elements of the learning resource in the Spring term of the academic years 2020–21 and 2021–22, and students at the Research Transparency and Reproducibility Training (RT2) Virtual 2021 (organised by Berkeley Initiative for Transparency in the Social Sciences (BITSS)) for their helpful feedback and kindness. This feedback from a student captures it well: "i was genuinely terrified when the term started and i saw coding and python but this has been great thank you!". I also thank Kirils Makarovs and Hamid Nejadghorban for assistance with teaching earlier iterations of the learning resource.

Finally, thanks to the open science Twitter community for helpful feedback, discussions, and pointers to resources. 

<br>

# Code availability

<i class="fab fa-github"></i>

All materials, code, and data included in this textbook as well as this textbook website are available as a public GitHub repository at https://github.com/valdanchev/reproducible-data-science-python

## License

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](http://creativecommons.org/licenses/by-sa/4.0/)

_Reproducible Data Science with Python_ by [Valentin Danchev](https://valdanchev.github.io) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).