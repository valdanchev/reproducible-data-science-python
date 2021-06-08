# Data Ethics, Bias, and Fairness

Topics of data ethics, privacy, and fairness should be at the beginning of a course, not at the end. Indeed, next iterations of this course should discuss earlier challenges of ethical data science. Data ethics is the last topic in this iteration for two reasons. First, an informed discussion of data ethics issues requires to first build some intuition about the data science life cycle and what can go wrong in that life cycle, including different sources of bias. Learning how to evaluate models in general is a precondition for evaluating models for bias and fairness. Second, moving beyond the issues of data ethics to possible solutions that can address those issues and mitigate biases also requires some exposure to approaches we covered earlier in the course, for example causal inference. Although our focused discussion on data ethics comes last, we discuss issues of data design and biases (e.g., algorithmic confounding), transparency and reproducibility, and other topics of ethical data science throughout the course.

## Key themes
* Ethical challenges, principles, and frameworks. 
* Privacy and consent.
* Detecting and dealing with bias and fairness in data science models. 
* Implications of data science biases: discrimination, profiling, social inequalities.

## Learning resources

<i class="fas fa-book"></i> Jeremy Howard, Sylvain Gugger, and Rachel Thomas. [Chapter 3: Data Ethics.](https://github.com/fastai/fastbook/blob/master/03_ethics.ipynb) In Deep Learning for Coders with fastai and PyTorch: AI Applications Without a PhD. [Online version freely available.](https://github.com/fastai/fastbook/blob/master/03_ethics.ipynb) <br>
&nbsp;&nbsp;&nbsp; <i class="fas fa-play-circle"></i> Associated video lecture [Getting Specific About Algorithmic Bias](https://www.youtube.com/watch?v=S-6YGPrmtYc) by Rachel Thomas. PyBay 2019. Slides are available [here](https://drive.google.com/file/d/15IeWD_8kT4NsO_VwbeWa0qXVBmOa7aPE/view).

<i class="fas fa-book"></i> Mathew Salganik. Chapter 6: Ethics. In Bit by Bit: Social Research in the Digital Age. [Online version freely available.](https://www.bitbybitbook.com/en/1st-ed/ethics/) <br>
&nbsp;&nbsp;&nbsp; <i class="fas fa-play-circle"></i> Associated video lectures Ethics and Computational Social Science by Mathew Salganik, [Part 1](https://www.youtube.com/watch?v=A-5QaX5ZiK8) and [Part 2](https://www.youtube.com/watch?v=TT6dOQMKHhA).

<i class="fas fa-book"></i> <i class="fas fa-code"></i> Ian Foster, Rayid Ghani, Ron S. Jarmin, Frauke Kreuter, Julia Lane. Big Data and Social Science (2nd edition). Chapter 11: Bias and Fairness. [Online version freely available](https://textbook.coleridgeinitiative.org/chap-bias.html).

<i class="fas fa-scroll"></i> Sendhil Mullainathan. 2019. [Biased Algorithms Are Easier to Fix Than Biased People.](https://www.nytimes.com/2019/12/06/business/algorithm-bias-fix.html) New York Times.

<i class="fas fa-book"></i> Kelleher and Tierney. Chapter 6: Privacy and Ethics. In Data Science. MIT Press.

<i class="fas fa-play-circle"></i> Mason A. Porter. Data Ethics. Video lecture and slides available [here](https://zerodivzero.com/short_course/aaac8c66007a4d23a7aa14857a3b778c/title/181b207c7d2941278be4641ea5fe0e21).

<i class="fas fa-code"></i> Pedro Saleiro, Kit T. Rodolfa, Rayid Ghani. [Dealing with Bias and Fairness in Data Science Systems: A Practical Hands-on Tutorial](https://dssg.github.io/fairness_tutorial/). <br>
&nbsp;&nbsp;&nbsp; <i class="fas fa-play-circle"></i> [Corresponding video tutorial](https://www.youtube.com/watch?v=N67pE1AF5cM), KDD 2020 tutorial.

# Discussion: A-level results in 2020 England 

This week we will discuss a data ethics topic instead of doing hands-on coding.  

Our discussion topic: _What could have gone wrong with the A-level results in England in 2020?_
* Algorithm or algorithms? 
* Equations?
* Data science pipeline? 
* Historical data? 
* Design (e.g., inclusion and exclusion criteria)? 
* Conflicting notions of fairness (e.g., individual fairness, group fairness)? 
* Individual decision-making? 
* Politics?

# Learning resources about the A-level controversy

<i class="fas fa-scroll"></i> Why did the A-level algorithm say no? BBC.

<i class="fas fa-play-circle"></i> Chris Giles’s review What went wrong with the A-level algorithm? Financial Times.

<i class="fas fa-scroll"></i> Blame the politicians, not the technology, for A-level fiasco. Financial Times.


# Bias and Fairness in Data Science Systems

Once we come up with discussion points and hypotheses about what could have gone wrong with the A-level controversy, we will review this toolbox for 'Dealing with Bias and Fairness in Data Science Systems' and will determine which discussion points and hypotheses could (or could not) be addressed by such a tool for debiasing data science systems. 

<i class="fas fa-code"></i> <i class="fas fa-play-circle"></i> Pedro Saleiro, Kit T. Rodolfa, Rayid Ghani. [Dealing with Bias and Fairness in Data Science Systems: A Practical Hands-on Tutorial](https://dssg.github.io/fairness_tutorial/). See also the [Corresponding video tutorial](https://www.youtube.com/watch?v=N67pE1AF5cM), KDD 2020 tutorial.

While exploring the toolbox, focus in particular on: 
* Individuals' attributes you would use to evaluate for fairness the A-level data science system, and the reference group to which you would compare. 
* Fairness metrics that you would use to evaluate the A-level model results.