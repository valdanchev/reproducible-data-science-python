# Open Reproducible Data Science Workflow
<br>

> "An article about computational science in a scientific publication is _not_ the scholarship itself, it is merely _advertising_ of 
> the scholarship. The actual scholarship is the complete software development environment and the complete set of instructions which 
> generated the figures."
>[— J. B. Buckheit and D. L. Donoho, 1995](https://statweb.stanford.edu/~wavelab/Wavelab_850/wavelab.pdf)

<br>

> <img src="https://github.com/valdanchev/reproducible-data-science-python/blob/master/images/reproducibility_spectrum.png?raw=true" width="600" height="200">
>
>[— Marwick et al, 2017, Open science in archaeology](https://eprints.gla.ac.uk/148887/7/148887.pdf)

## Key themes

* The role of transparency and reproducible workflow in scientific research. 
* The reproducibility problem.
* Plausible sources of the reproducibility problem:
  * Biases in data analysis, including p-hacking, HARKing (Hypothesizing After Results are Known), and publication bias
  * Lacking transparency of computer code, data, and materials.  
* Rules for open and reproducible workflows
* Open-source tools for reproducible research, including `Jupyter` and `Colab` notebooks, `Markdown`, dependency management via `pip`, version control.

<br>

## Learning resources

### Concepts

<i class="fas fa-scroll"></i> Regina Nuzzo. [How scientists fool themselves – and how they can stop](https://www.nature.com/news/how-scientists-fool-themselves-and-how-they-can-stop-1.18517). Nature.

<i class="fas fa-scroll"></i> Christie Aschwanden. [Science Isn’t Broken—It’s just a hell of a lot harder than we give it credit for](https://fivethirtyeight.com/features/science-isnt-broken/#part1). FiveThirtyEight.

<i class="fas fa-scroll"></i> Marcus Munafò et al. (2017) [A manifesto for reproducible science](https://www.nature.com/articles/s41562-016-0021). Nature Human Behaviour.

<i class="fas fa-scroll"></i> Jeffrey Perkel (2018) [Why Jupyter is data scientists’ computational notebook of choice](https://www.nature.com/articles/d41586-018-07196-1). Nature.

<i class="fas fa-scroll"></i> Tom Hardwicke et al. (2019) [Calibrating the scientific ecosystem through meta-research](https://www.annualreviews.org/doi/abs/10.1146/annurev-statistics-031219-041104). Annual Review of Statistics and Its Application.

<i class="fas fa-book"></i> Garret Christensen, Jeremy Freese, Edward Miguel (2019) [Chapter 11: Reproducible Workflow. In Transparent and Reproducible Social Science Research: How to Do Open Science](https://www.ucpress.edu/book/9780520296954/transparent-and-reproducible-social-science-research). University of California Press.

<i class="fas fa-play-circle"></i> [Reproducibility: The Basics](https://youtu.be/yHXNawfYGYM). (With Brian Nosek)

<i class="fas fa-play-circle"></i> [Researcher degrees of freedom](https://www.youtube.com/watch?v=uN3Q-s-CtTc&list=PLAKyhL4GNnqNv4qv0yr0MopAtfBOiT25I&index=4), [P-hacking](https://www.youtube.com/watch?v=V7pvYLZkcK4&list=PLAKyhL4GNnqNv4qv0yr0MopAtfBOiT25I&index=7), and [P-curve](https://www.youtube.com/watch?v=V7pvYLZkcK4&list=PLAKyhL4GNnqNv4qv0yr0MopAtfBOiT25I&index=7). (By Berkeley Initiative for Transparency in the Social Sciences, BITSS)

### Tutorials
<i class="fas fa-play-circle"></i> [Reproducible Data Analysis in Jupyter](https://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/). Jake Vanderplas.

<i class="fas fa-play-circle"></i> [Getting Started With the Open Science Framework (OSF)](https://youtu.be/2TV21gOzfhw). Center for Open Science.

<i class="fas fa-play-circle"></i> Data Science Productivity Tools: [Creating a GitHub Repository](https://youtu.be/7slCKVGNoLE?list=UUEHNLIrfyOC_y8qiR7KXJVA), [Using git at the Command Line](https://youtu.be/gSOKxdo5jkw?list=UUEHNLIrfyOC_y8qiR7KXJVA), [Git and GitHub](https://youtu.be/_wFpjY56iKs?list=UUEHNLIrfyOC_y8qiR7KXJVA). Rafael Irizarry.

<i class="fas fa-code"></i> [Introduction to Open Reproducible Science Workflows](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/). Earth Lab CU Boulder.

<i class="fas fa-code"></i> [Welcome To Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb#scrollTo=lSrWNr3MuFUS). Google Colaboratory.

<i class="fas fa-code"></i> [Markdown in Jupyter Notebook](https://www.datacamp.com/community/tutorials/markdown-in-jupyter-notebook). DataCamp.

<i class="fas fa-code"></i> [Markdown Guide](https://colab.research.google.com/notebooks/markdown_guide.ipynb#scrollTo=70pYkR9LiOV0). Google Colaboratory.

<i class="fas fa-code"></i> [The Markdown Guide](https://www.markdownguide.org). Matt Cone and collaborators.

<br>

# What is computational reproducibility and why it matters?

The terms of reproducibility (and computational reproducibility) and replicability are sometimes used interchangeably but they differ. 

> **Reproducibility** means "obtaining consistent results using the same input data, computational steps, methods, and conditions of analysis"; it is synonymous with computational reproducibility.

> **Replicability** "means obtaining consistent results across studies aimed at answering the same scientific question, each of which has obtained its own data."

> **Why does reproducibility and replicability matter?** "Reproducibility and replicability are often cited as hallmarks of good science. Being able to reproduce the computational results of another researcher starting with the same data and replicating a previous study to test its results facilitate the self-correcting nature of science."

> **Why do we study computational reproducibility right now?** "Computational reproducibility is more prominent now than ever because of the growth in reliance on computing across all of science. When a researcher reports a study and makes the underlying data and code available, those results should be computationally reproducible by another researcher."

Source: [Reproducibility and Replicability in Science (2019), National Academies of Sciences, Engineering, and Medicine](https://www.nationalacademies.org/our-work/reproducibility-and-replicability-in-science)

Our focus is on the _reproducibility_ of our data analysis workflow, and on _computational reproducibility_ in particular.

# Open Reproducible Workflow in Jupyter/Colab Notebooks

An important aspect of reproducible research is the integration of various components, including data gathering, data manipulation, data analysis and outputs in an open research workflow.

The [Jupyter](https://jupyter.org) and [Colab](https://colab.research.google.com/notebooks/intro.ipynb?utm_source=scs-index#) notebooks are an open-source web applications that allow you to create and share documents that contain code, equations, visualisations and narrative text. While a popular tool for [data exploration](https://www.nature.com/articles/d41586-018-07196-1), the notebook can also support your reproducible research workflow by integrating **executable code**, **data inputs**, **results**, and **documentation** within a single notebook, along with **images**, **HTML**, **LaTeX**, **videos** and more.

In the previous session, you have learned how to use the Jupyter / Colab notebook to:
* run code interactively using the [`Python`](https://www.python.org) programming language and
* document your code and outputs using [`Markdown`](https://daringfireball.net/projects/markdown/syntax), an open and easy-to-use markup language for creating formatted text.

Writing your `Python` code and `Markdown` documentation within Jupyter/Colab notebooks facilitates open and reproducible science workflow through integration of various components — data inputs, code for data manipulation, analysis, visualisation, and results — within a single file that can be openly shared and communicated with others.

The Jupyter/Colab notebooks support reproducibility but do not guarantee it. In fact, a recent [study](https://blog.jetbrains.com/datalore/2020/12/17/we-downloaded-10-000-000-jupyter-notebooks-from-github-this-is-what-we-learned/) of 10 million Jupyter notebooks hosted on GitHub have found that 36 per cent of the notebooks could not be reproduced because the code cells were not originally executed in a linear order. The tool is not sufficient for reproducible data analysis. We also need a reproducible research workflow that helps us transition from ["nonlinear, interactive, trial-and-error style of exploration to a more linear and reproducible analysis based on organized, packaged, and tested code" (Jake VanderPlas, 2017)](https://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/).  


<img src="https://zenodo.org/api/iiif/v2/0555299a-9eeb-4122-80cd-41ce3ea8b616:47ef35bc-fab9-47f1-9e13-bcd4d63d595a:reproducible_logbook.png/full/750,/0/default.png" width="1200" height="700">

**Figure 1.** _Open and reproducible scientific workflow using Jupyter notebook and related open-source tools_. Source: [Juliette Taka and Nicolas M. Thiery. Publishing reproducible logbooks explainer comic strip. Zenodo. DOI: 10.5281/zenodo.4421040 (2018)](https://zenodo.org/record/4421040#.YInMpC1Q0mk).

# Rules for Reproducible Workflow

Let's consider a few [simple rules for reproducible research workflow with Jupyter/Colab notebook (Rule at al, 2019)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007007):

> ***Document the process, not just the results*** — "... make sure to document all your explorations, even (or perhaps especially) those that led to dead ends. These comments will help you remember what you did and ... why you chose a particular parameter value, where you copied a block of code from, or what you found interesting about an intermediate result." 

> ***Use cell divisions to make steps clear*** — "... try to make each cell in your notebook perform one meaningful step of the analysis that is easy to understand from the code in the cell or the surrounding markdown description. Modularize your code by cells and label the cells with markdown above the cell. Think of each cell as being one paragraph, having one function, or accomplishing one task (for example, create a plot)."

> ***Modularize code*** — "It is always good practice to avoid duplicate code, but in notebooks, it is especially easy to copy a cell, tweak a few lines, paste the resulting code into a new cell or another notebook, and run it again. This form of experimentation is expedient but makes notebooks difficult to read and nearly impossible to maintain if you want to change the functionality of or fix a bug in the copied code. Instead, wrap code you are about to copy and reuse in a function, which you can then call from as many cells as desired."

> ***Record dependencies*** — "Rerunning your analysis in the future will require accessing not only your code but also any module or library that your code relied on."

> ***Use version control*** — "Version control is a critical adjunct to notebook use because the interactive nature of notebooks makes it easy to accidentally change or delete important content. Furthermore, since notebooks contain code and code inevitably contains bugs, being able to determine the history of when a given bug you have discovered was introduced to the code versus when it was fixed—and thus what analyses it may have affected—is a key capability in scientific computation."

   * Git and GitHub are widely used tools for version control [[see Ten Simple Rules for Taking Advantage of Git and GitHub (Perez-Riverol et al, 2016)](https://doi.org/10.1371/journal.pcbi.1004947) but are known to have a steep learning curve. For version control, we will use the built-in Colab functionality Revision history, which can be accessed from `File` —> `Revision history`.

> ***Design your notebooks to be read, run, and reused*** — "... store your notebooks in a public code repository with a clear README file and a liberal open source license granting permission to reuse your code."

   * Public code repositories that enable code sharing, team collaboration, and open source licensing include [GitHub](https://github.com), [GitLab](https://about.gitlab.com), [Open Science Framework (OSF)](https://osf.io).

> ***Share and explain your data*** — "Having access to a clearly annotated notebook is of little use to those wanting to reproduce or extend your results if the underlying data are locked away. Strive to make your data or a sample of your data publicly available along with the notebook."

   * Data repositories for medium to large sized anonymized data include [figshare](https://figshare.com/), [zenodo](https://zenodo.org/), and [Dryad](https://datadryad.org/stash/our_mission).

# Reproducible research report

To create a reproducible research report, use throughout the notebook:
* Python code in Code cells
* Hashtag symbol `#` in Code cells to introduce a comment line describing your Python code. Code commenting is a very important part of computational data analysis. 
* Markdown language in Text cells to write up your methods, results, and interpretation.

At the end of a session, rerun your notebook from top to bottom using `Restart and run all` (under `Runtime` in the Colab menu bar) to ensure computational reproducibility.

# Recording dependencies

Throughout the textbook, we will refer to the rules for reproducible research workflow. We illustrate below a few simple rules (e.g., comment your code; use cell division to make your steps clear) with a focus on recording software dependencies, which is a key prerequisite for computational reproducibility. 

Reproducing your data analysis in the future will require reusing not only your data and code but also any module and library as well as their respective versions that you employed in your code. It is a good practice to record those dependencies so that others or your future self (i.e., you in a month's time) can recreate the environment underlying your analysis.

Let's first determine your Python version. You can check your Python version in a Code cell by typing `!python --version`.

# Check Python version
!python --version

To install and manage Python software modules or libraries, you can use a package-management system, such as [`pip`](https://pypi.org/project/pip/). Using `pip`, you can download and install a specific version of a module/library you plan to use in your data analysis. For example, you can install the library for causal inference [`DoWhy`](https://microsoft.github.io/dowhy/example_notebooks/dowhy_simple_example.html#) version [0.6](https://pypi.org/project/dowhy/#id4) released on 03 March 2021 by typing `!pip install doWhy==0.6`. Note that we use two consecutive equal marks `==` called the equality operator instead of a single equal marks `=` which is an assignment operator in Python.

# Install and import a Python library.
# The flag -q is short for --quiet and is used to hide output/warnings
!pip install -q dowhy==0.6
import dowhy

If many modules and libraries are already preinstalled, as in Colab, you can use `pip` to record the specific version of those modules and libraries. For example, the command `!pip freeze` returns installed modules and libraries listed in alphabetical order.

# List installed packages - listed are both packages available with Colab
# and packages we have installed in this session (e.g. the library DoWhy)
!pip freeze

You can type in `>` following the `!pip freeze` command to save the list of Python packages to a requirements file named `requirements.txt` (details about the `requirements.txt` file are provided at the end of the notebook). The character `>` saves any command output to a file.

!pip freeze > requirements.txt

You can access the version information about a particular package (e.g., numpy or pandas) using the `grep` command. `grep` is a command-line tool which searches for a pattern (in our case, the word `numpy` and the word `pandas`) and prints each line that matches the pattern.

# Return installed libraries that contain
# the text 'numpy' or 'pandas' in their name
!pip freeze | grep numpy
!pip freeze | grep pandas

As of April 2021, Colab uses `numpy` 1.19.5 and `pandas` 1.2.0. It is possible to install and import a different version, for example the latest version of pandas (1.2.4) (released on 12 April 2021) by executing the following command:

```
!pip install pandas==1.2.4
import pandas as pd
```

For the `pip` approach for recording package dependencies to work, we need to keep track of each and all packages we use in a notebook. This may not always be the case, leaving open the possibility for undocumented dependencies in our notebook (when we fail to document one or more packages on which our data analysis depends on). To address this, you can use a notebook extension such as [`watermark`](https://github.com/rasbt/watermark) which will print out a list of your dependencies that are explicitly imported/used in your notebook. 

# Install the watermark extension
!pip install -q watermark

# Load the watermark extension
%load_ext watermark

# Show packages that were imported
%watermark --iversions

Once you identify the versions of all dependencies in your notebook, it is a good practice to list them at the bottom of your notebook. In addition, the information is often stored in a `requirements.txt` file on a GitHub repository. The file simply lists all of your package dependencies and their versions in the following format: 

```
IPython==5.5.0
pandas==1.2.0
dowhy==0.6
```

You can use the package [`pipreqsnb`](https://pypi.org/project/pipreqsnb/) to automatically save a list of all Python packages (and their versions) used in your current notebook to a file named `requirements.txt`. The file `requirements.txt` will be created in your working directory after you execute the command below.

# Install the pipreqsnb package
!pip install -q pipreqsnb

# Run pipreqsnb after specifying the path to the notebook
!pipreqsnb ../notebooks/03_open_reproducible_workflows.ipynb

The requirements file (`requirements.txt`) can be then used by tools like [Binder](https://mybinder.org) to build a [Docker container](https://www.docker.com/resources/what-container) that recreates the computational environment (including packages and package versions) you have used in your data analysis, making your code immediately reproducible by others irrespective of their computational environment (e.g., operating system or software  versions). Reproducing your computational environment is a key precondition for others to be able to reproduce your data analysis.