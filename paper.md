---
title: An open learning resource on Reproducible Data Science with Open-Source Python Tools and Real-World Data
tags:
- Python
- Jupyter notebook
- reproducible workflow
- open science
- real-world social data
- exploratory data analysis
- machine learning
- social networks
- data science ethics
date: "19 November 2021"
authors:
- name: Valentin Danchev
  orcid: 0000-0002-7563-0168
  affiliation: 1
affiliations:
- name: Department of Sociology, University of Essex, United Kingdom
  index: 1
bibliography: paper.bib
---

# Summary

This paper describes a computational learning resource on Reproducible Data Science with Open-Source Python Tools and Real-World Data. The resource provides an accessible, hands-on introduction to data science 
techniques, skills, and workflows necessary to perform open, reproducible, and ethical data analysis. By using research problems of real-world relevance (such as vaccine hesitancy and the impact of COVID-19 
lockdown measures on human mobility) and real-world social data (including anonymised mobility data from digital sources and recent COVID-19 survey data), the resource encourages students to use 
open-source tools and coding to learn from diverse and large social data sources.

The learning resource aims to minimise barriers to entry for students from social sciences, public health, and related fields. With no software installation and setup requirements, students can start coding 
from their web browser using free and open-source software (FOSS), including the Python programming language, Jupyter notebook, and Markdown. Through real-world data applications, students are introduced 
to the open source Python ecosystem of libraries for data science—including `pandas` [@Mckinney2010], `seaborn` [@Waskom2021], `scikit-learn` [@Pedregosa2011scikit], `statsmodels` [@Seabold2010statsmodels], 
and `networkX` [@Hagberg2008networkx]—and learn about open and reproducible workflow, data wrangling, data exploration and visualization, pattern discovery (e.g., clustering), prediction and machine learning, 
causal inference, network analysis, and data ethics.

# Statement of Need

The importance of data science education for drawing conclusions from diverse data sources in a transparent, reproducible, and ethical manner and for building data literacy skills 
is now widely recognised [@NAP2018; @Danyluk2021; @Adhikari2021; @Arnold2019turing; @Stoudt2021]. A key challenge ahead for the community of data science educators, and particularly those at the 
intersection of data science and social sciences, is how to democratise the knowledge and skills needed for conducting reproducible data science and to engage students—with little to no programming 
experience and from diverse social and academic backgrounds—in accessible, inclusive, and cross-disciplinary data science learning. To address this and related challenges, successful examples of data 
science curriculum [e.g., @Adhikari2021] have been developed. The learning resource presented in this paper addresses the data-science democratisation challenge through the use of down-to-earth research 
questions and real-world social data sets about the COVID-19 pandemic. Both real-world questions and data can encourage students to engage with hands-on computation, data science techniques, reproducible 
data analysis workflow, and data ethics. The democratisation of reproducible and ethical data science is important for empowering students (and citizens) to use, analyse, and learn from large data sets as 
well as to critically evaluate data, models, and their social impact.

# Learning objectives

The learning resource aims to enable students to:

* Freely use open-source computational tools—e.g., Python, Jupyter Notebook, Markdown—for data analysis.
* Build a transparent and reproducible research workflow.
* Perform data analysis and critically interpret and openly communicate research process, objects, and results.
* Study research questions of societal importance by wrangling, exploring, visualising, and modeling a variety of real-world tabular and network data using Python libraries.
* Apply basic models for machine learning, causal inference, and network analysis to real-world data.
* Identify and deal with methodological issues of overfitting, selection bias, and confounding.
* Articulate and address issues of data ethics and social impact of data science models.
* Write clean, reusable, and reproducible code in Python.

# Content

The learning resource is designed around an understanding of data science as the use of coding to draw conclusions from diverse data sets by solving five classes of 
tasks [@Adhikari2021; @Hernan2019]:

* Data preprocessing—preparing data for analysis using techniques for data cleaning, data wrangling, and data transformation.
* Description—discovering patterns in data using exploratory data analysis, visualisation, and automated discovery techniques.
* Prediction—using information about outcomes we know to make informed guesses about unknown outcomes by applying techniques from simple regression to supervised machine learning.
* Inference—quantifying our degree of certainty to determine whether what we find in our data will hold among different scenarios using resampling methods and related techniques.
* Causal data analysis—studying cause-and-effect questions via the application of causal graphs, counterfactuals, and causal inference techniques.

The resource does not aim to cover a single data science task in detail but introduces students to these tasks with a focus on real-world data and applications, hands-on computation, 
and reproducible data analysis.

The content follows a typical data science lifecycle [@Lau2001], in which students would begin with a research question, and then select their data set(s), preprocess the data, perform descriptive analysis to 
explore basic features of their data, and then model their data to predict an outcome or establish causal effect. Transparency of research process and computational reproducibility are embedded throughout 
the data science lifecycle.

# Prerequisites

Prior knowledge of programming is not required as coding for data analysis is taught from first principles. Background in 
mathematics or statistics are not required beyond basic algebra and descriptive statistics.

# Instructional design

The learning resource is provided in the form of Jupyter textbook that consists of ten chapters, each of which is an independent Jupyter notebook. Each notebook provides 
an introduction of the chapter's topic. To accommodate students’ different styles of learning, each notebook also points to four categories of learning 
materials—i.e., articles, books, videos, and tutorials—that provide learners with background knowledge on the topic before immersing in hands-on coding. 
Coding and data analysis are motivated by data-centered research questions such as "How has human mobility differed across the three lockdowns in the United Kingdom during the COVID-19 pandemic?" 
and "Can we predict people who are unlikely to take a coronavirus vaccine from socio-demographic and health features". A variety of real-world (and daily updated) data sets 
are brought to bear on these research questions, including the COVID-19 Google Community Mobility Reports [@aktay2020] and the Understanding Society: COVID-19 Study [@Burton2020]. Methodologies 
(e.g., supervised 
machine learning, causal inference, network analysis) and techniques (e.g., cross-validation) are briefly described such that students are empowered to apply them without being overwhelmed by 
technical detail. Students can engage with the notebooks, interactively execute the code, examine the outputs, and work on the hands-on coding exercises in an active-learning process.  

The resource is designed to scaffold reproducible and transparent research workflow by integrating research questions, data inputs, computer code, documentation, data analysis, visualizations, and 
narrative text in a single document. This integration of various research objects is made possible by the open-source Jupyter Notebook [@Kluyver2016jupyter]—a user-friendly, free, open-source, 
interactive web tool that implements the notion of "literate programming" [@knuth1984literate] and is widely used across research and education [@perkel2018jupyter]. While the Jupyter computational 
notebook does not guarantee reproducibility [@guzharina2020], it fosters reproducible workflow and good research practices [@Rule2019] by enabling students to describe the process of data analysis 
(not just the "final" results but also the "dead ends"), make transparent choices of parameter selection, and document research outputs, however "useful" or "(un)expected" they may seem.

# Experience of use

The learning resource can be used for different modes of learning, including a semester-long module, training workshop, and independent study. So far, elements of the learning resource have been 
used in a 10-week module delivered in the Spring term of the academic year 2020–2021 to third year undergraduate students at the Department of Sociology, University of Essex. More recently, 
core elements of the resource have formed the backbone of a 1.5-hour hands-on training on reproducible workflow with dynamic documents as part of the Research Transparency and Reproducibility 
Training (RT2), August 23–September 3, 2021, organised by the Berkeley Initiative for Transparency in the Social Sciences. The Jupyter notebook used in the training is publicly 
available and can be accessed via the RT2's repository on the Open Science Framework (https://osf.io/5neky/) and via 
GitHub (https://github.com/valdanchev/dynamic-documents-with-jupyter-notebook).

# Getting started

Learners can access the resource on the dedicated website https://valdanchev.github.io/reproducible-data-science-python and start learning right away.
For hands-on coding, learners can access the interactive versions of the Python Jupyter notebooks via MyBinder and Colab. Binder is a free open online service that 
lets you open and execute Jupyter notebooks and work with the code interactively. Colab is a freely available service that allows one to run Python Jupyter notebooks on the Google Cloud, making it 
possible to interactively write and execute Python code in your browser. While Colab differs from Jupyter notebook in some respects (e.g., keyboard shortcuts), the underlying code is executable across 
computational notebooks.

Below are links to interactive versions of the ten Jupyter notebooks executable via Colab:

* [End-to-End Data Science Project: Human mobility during UK lockdowns](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/end_to_end_data_science_project.ipynb)
* [Python Data Science on the Cloud](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/python_data_science_cloud.ipynb)
* [Open Reproducible Data Science Workflow](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/open_reproducible_workflows.ipynb)
* [Data Design and Data Wrangling](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/data_design_wrangling.ipynb)
* [Data Exploration and Data Visualisation](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/data_exploration_visualisation.ipynb)
* [Pattern Discovery using Unsupervised Learning](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/pattern_discovery_unsupervised_learning.ipynb)
* [Prediction using Supervised Learning](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/prediction_supervised_learning.ipynb)
* [What Causes What? Introduction to Causal inference](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/causal_inference.ipynb)
* [Network Analysis](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/network_analysis.ipynb)
* [Data Ethics, Bias, and Fairness](https://colab.research.google.com/github/valdanchev/reproducible-data-science-python/blob/master/data_ethics.ipynb)

# Acknowledgements

I thank the participants at the 2021 National Workshop on Data Science Education and students at the Research Transparency and Reproducibility Training (RT2) and at the Department of Sociology, 
University of Essex, for helpful feedback. I also thank Kirils Makarovs and Hamid Nejadghorban for help with teaching earlier iterations of the learning resource.

# References
