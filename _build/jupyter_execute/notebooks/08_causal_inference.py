# Introduction to Causal Inference

# What causes what? 

Observational data (i.e., data recorded from human activity) and big data sources in particular are rife with spurious correlations between variables that appear to be associated in a model but are not causally linked. As a result, many models would pick some interesting associations in the data, which may appear statistically significant but likely lack practical significance. If the goal is to implement a new policy or interventions that may introduce change in the social world, we need knowledge about the underlying causal structure of the problem — what causes what. Specifically, we would like to know the effect of a particular _treatment_ (any policy or intervention, for example, Work from Home) on an _Outcome_ (for example, Number of coronavirus cases) and compare the observed effect to a counterfactual question, for example, 'What would have been the Number of coronavirus cases if a Work from home policy was not introduced?'.

Causal graphs or DAGs (Directed Acyclical Graphs) are a useful tool for drawing intuitive pictures that:
* Reflect our assumptions about our treatment, outcome, and associated factors. 
* Highlight possible sources of bias (e.g., confounding) which may otherwise be unnoticed.
* Improve our data analysis for causal inference.

In a causal graph (see Figure 1 below), each variable has a corresponding node, and the arrows reflect the direction of causation we assume of the basis of domain knowledge.

## Learning resources

<i class="fas fa-book"></i> <i class="fas fa-code"></i> Scott Cunningham. [Chapter 3: Directed Acyclical Graphs](https://mixtape.scunning.com/dag.html) in [Causal Inference: The Mixtape.](https://mixtape.scunning.com/index.html) Yale University Press.  

<i class="fas fa-book"></i> <i class="fas fa-code"></i> <i class="fas fa-play-circle"></i> [Chapter 6. The Haunted DAG & The Causal Terror](https://xcelab.net/rm/statistical-rethinking/) in Richard McElreath's Statistical Rethinking book and associated [video lecture](https://www.youtube.com/watch?v=l_7yIUqWBmE).

<i class="fas fa-play-circle"></i> Miguel Hernán. [Causal Diagrams: Draw Your Assumptions Before Your Conclusions](https://www.edx.org/course/causal-diagrams-draw-your-assumptions-before-your). edX.

<i class="fas fa-book"></i> Kosuke Imai. [Chapter 2: Causality](http://assets.press.princeton.edu/chapters/s2-11025.pdf) in Quantitative Social Science. Princeton University Press.
 
<i class="fas fa-book"></i> Stephen L. Morgan and Christopher Winship. Counterfactuals and Causal Inference. Cambridge University Press.

<i class="fas fa-book"></i> Hernán MA, Robins JM (2020). [Causal Inference: What If.](https://cdn1.sph.harvard.edu/wp-content/uploads/sites/1268/2021/03/ciwhatif_hernanrobins_30mar21.pdf) Boca Raton: Chapman & Hall/CRC.

<i class="fas fa-scroll"></i> Miguel Hernán, John Hsu, and Brian Healy. [A Second Chance to Get Causal Inference Right: A Classification of Data Science Tasks.](https://amstat.tandfonline.com/doi/pdf/10.1080/09332480.2019.1579578?needAccess=true) CHANCE.


# Confounding—basic definitions

To keep things concrete, in this lab, we will use DAGs to shed some light on the problem of confounding with a focus on two common confounds: (2) the fork and (3) the collider. In particular, we will discuss the collider confound as the 'fork' confound is typically well understood in the social sciences. 


## Definitions
* **Confounding**: any interference such that the effect of predictors X on an outcome of interest Y is not the same as it would have been had we experimentally determined the predictors X. In experimental settings, we have treatment and control groups that are comparable with respect to every characteristic related to the outcome with the only difference being that the treatment group received the treatment and the control group did not.

    * **Fork**: A variable Y is a common cause of X and Z, inducing a spurious correlation between them. This is the most common example of confounding (see [Kosuke Imai's Quantitative Social Science, page 57](https://assets.press.princeton.edu/chapters/s2-11025.pdf)).

    * **Collider**: Relationship between X and Z does not exist unless we condition on Y, which is a collider variable (because the paths from X and Z collide in Y).

<img src="https://miro.medium.com/max/4800/1*bmORaFV5mKqUTaML7ib_Rw.png" width="600" height="300"/>

Figure 1. [DAG representation](https://medium.com/@akelleh/a-technical-primer-on-causality-181db2575e41) of fork (left) and collider (right). Source: [A Technical Primer On Causality](https://medium.com/@akelleh/a-technical-primer-on-causality-181db2575e41) by Adam Kelleher.

# Our example of collider bias

Many canonical examples of collider bias exist in the literature, but we will develop our own example using a data set we know well — the Understanding Society Covid-19 survey data.  

Consider a situation in which both variables Working from home and Age have an effect on the Risk of getting Covid-19 but are not correlated between each other in the entire data set. Then we condition on the respondents who considered the risk for getting Covid-19 'Very likely' as an example of problematic conditioning on a collider variable. After this problematic conditioning, we observe a strong negative relationship between Age and Work from home. In short, Work from home and Age are not correlated in the population but get correlated once conditioning on perceived very high risk of getting Covid-19, introducing collider bias. Of course, in this example we use survey data, and not many would condition on 'Very likely' risk of getting Covid-19, but in many observational data sets, we may have data only about a pre-selected subset of the population so our data may contain such problematic selection, introducing collider bias, by design.

# Drawing causal graphs

To visualise our example as a causal graph, we will use the R package [`ggdag`](https://cran.r-project.org/web/packages/ggdag/ggdag.pdf). This [tutorial](https://cran.r-project.org/web/packages/ggdag/vignettes/bias-structures.html) by Malcolm Barrett gives a good overview of `ggdag` and its capabilities.

In order to run R in a Python Jupyter, we need to install the `rpy2` package which provides Python interface to the R language.

!pip install rpy2

# To enable the %%R cell magic command, which turns a cell to be
# interpreted as an R code, we execute %load_ext rpy2.ipython.
%load_ext rpy2.ipython

Now we can run R code in a cell by adding the R cell magic command `%%R`.

%%R
# You will need to select a CRAN mirror from which
# to install the package; for example, typing in '70' will select UK London
install.packages("ggdag")
# We also install ggplot2, a popular data visualization package in R 
install.packages("ggplot2") 

Import the `ggdag` package (and the `ggplot2` package)

%%R
library(ggdag)
library(ggplot2)
theme_set(theme_dag())

In our model, we assume that both variables _Work from home_ and _Age_ affect the outcome variable, _Risk of getting Covid-19_. We also assume that _Working at home_ and _Age_ are not causally connected. Below we represent our simple model using a causal graph. The node where _Work from home_ and _Age_ arrowheads meet is called a collider, meaning that both variables collide there. Let's now plot a causal graph with our three variables.

%%R
RiskCovid_dag <-collider_triangle(
    x="Not Work from Home", y="Age", m="Perceived risk from getting COVID-19"
)

ggdag(RiskCovid_dag, text=FALSE, use_labels="label", node_size=20, text_size=5)

%%R
ggdag_dseparated(RiskCovid_dag, text=FALSE, use_labels="label", text_size=5)

Although Work from home and Age are not correlated in the population, they may get correlated once we condition on Very high risk of getting Covid-19. The square shape of the variable _Risk of getting Covid-19_ indicates that we condition on that variable being a certain value, in our case on people with Very high perceived risk of getting Covid-19.

%%R
ggdag_dseparated(
    RiskCovid_dag, controlling_for="m", text=FALSE, use_labels="label", text_size=5
)

# Statistical Models in Python

We will now perform our analysis to see how conditioning in a model can introduce a collider bias. 

In this lab, we will use the Python library [`statsmodels`](https://www.statsmodels.org/devel/examples/index.html). `statsmodels` is a Python module that provides functions for the estimation of many different statistical models.

<img src="https://www.statsmodels.org/devel/_images/statsmodels-logo-v2-horizontal.svg" width="400" height="200"/>

You can install `statsmodels` by running the following command:

!pip install statsmodels

# Collider confounder

We will use data from [Understanding Society COVID-19](https://www.understandingsociety.ac.uk/topic/covid-19) (Wave 6, November 2020, web collected) to demonstrate the causal structure of collider confounder. The data are safeguarded and can be accessed via the [UK Data Service](https://beta.ukdataservice.ac.uk/datacatalogue/studies/study?id=8644). Once access to the data is obtained, the data needs to be stored securely in your Google Drive and loaded in your private Colab notebook. The data is provided in various file formats, we use the `.tab` file format (`tab` files store data values separated by tabs) which can be easily loaded using `pandas`. Specifically, the web collected data of the survey from Wave 6 (November 2020) is stored in the file `cf_indresp_w.tab`. Let's load the survey data.

# Import the Drive helper
from google.colab import drive

# This will prompt for authorization.
# Enter your authorisation code and rerun the cell.
drive.mount("/content/drive")

import pandas as pd

# Load the Understadning Society COVID-19 Study web collected data, Wave 6
# Set the delimeter parameter sep to "\t" which indicates tabs
USocietyCovid = pd.read_csv(
    "/content/drive/My Drive/cf_indresp_w.tab",
    sep="\t",
)

# Display headings only as the data is safeguarded
USocietyCovid.head(0)

### Variables

To make things concrete, let's select three variables. 

|Variable in Our Model | Description| Variable Name | Values 
|---| ---| ---|---|
| X | Working at home| cf_wah | 1 = Always, 2 = Often, 3 = Sometimes, 4 = Never
| Z | Age | cf_age | Integer values (whole numbers)
| Y | Risk of getting covid19 | cf_riskcv19 | 1 = Very likely, 2 = Likely, 3 = Unlikely, 4 = Very unlikely

# Select and preprocesses our variables from the Understanding Society Study.
# We also select the weighting variable cf_betaindin_xw we will use later (see
# section 'Weighting to correct for complex sample design' below)

USocietyCovidCollider = USocietyCovid[
    ["cf_wah", "cf_age", "cf_riskcv19", "cf_betaindin_xw"]
]
USocietyCovidCollider = USocietyCovidCollider.mask(USocietyCovidCollider < 0)
USocietyCovidCollider = USocietyCovidCollider.dropna().astype(float)
USocietyCovidCollider

# Work at home versus risk of getting covid
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

sns.set_context("notebook", font_scale=1.5)

fig = sns.catplot(
    x="cf_wah",
    kind="count",
    hue="cf_riskcv19",
    height=6,
    aspect=1.5,
    palette="ch:.25",
    data=USocietyCovidCollider,
    legend=False,
)

# Change the labels of the horizontal x axis
fig.set(xlabel="Working at home")

# Add informative labels to the horizontal x axis
fig.set_xticklabels(["Always", "Often", "Sometimes", "Never"])

# Change title and labels of the legend
plt.legend(
    title="Risk of getting COVID-19",
    loc="upper center",
    labels=["Very likely", "Likely", "Unlikely", "Very unlikely"],
)

# Risk of getting COVID-19 versus age

fig = sns.catplot(
    x="cf_riskcv19",
    y="cf_age",
    kind="box",
    height=5,
    aspect=1.5,  # control plot size
    sharey=False,  # set different y axes for each plot
    data=USocietyCovidCollider,
)

# Add informative labels to the horizontal x axis
fig.set(xlabel="Risk of getting COVID-19")
fig.set_xticklabels(["Very likely", "Likely", "Unlikely", "Very unlikely"])

# Compute the mean of the three variables of interest
USocietyCovidCollider.iloc[:, 0:3].mean()

# Compute the correlation of the three variables of interest
USocietyCovidCollider.iloc[:, 0:3].corr()

# Using weights to adjust for complex sample design

Before we perform data analysis, we need to consider the sample of the Understanding Society COVID-19 Study and the importance of using weights in our analysis. The sample of the Understanding Society COVID-19 Study has a clustered and stratified design with certain types of people being over-represented in the sample by design. For example, the study over-samples ethnic minorities. This complex design allows various research analyses across different population sub-groups and topics but posses also a challenge as the sample does not reflect the population structure. To correctly reflect the population structure, we need to use weights in our analysis. The weights correct for unequal selection probability and other conditions (e.g., non-response). 

The Understanding Society team provides a number of weights reflecting the structure of the data. For the Understanding Society data we use (cross-sectional web-collected survey data from Wave 6, November 2020), the relevant weights variables is `cf_betaindin_xw`. The name of the weight variable reflects the wave for which the weight is calculated (`cf` refers to Wave 6), level of analysis (`indin` refers to individual interview), and data source (`xw` refers to cross-sectional analysis weight).

Weighting in _Understanding Society_ is discussed in the following sources: 
* [Understanding Society COVID-19. User Guide. Version 10.0. December 2021.](https://www.understandingsociety.ac.uk/sites/default/files/downloads/documentation/covid-19/user-guides/covid-19-user-guide.pdf)
* [Weighting and Sample Representation: Frequently Asked Questions. 
Version 1.0. October 2019.](https://www.understandingsociety.ac.uk/sites/default/files/downloads/documentation/user-guides/mainstage/weighting_faqs.pdf)

We use [`DescrStatsW`](https://www.statsmodels.org/dev/generated/statsmodels.stats.weightstats.DescrStatsW.html) from the library `statsmodels` to compute descriptive statistics and tests with weights for case weights:

# Import DescrStatsW
from statsmodels.stats.weightstats import DescrStatsW

# Create a weighted instance using the cf_betaindin_xw weights
USocietyCovidCollider_Weighted = DescrStatsW(
    USocietyCovidCollider.iloc[:, 0:3],
    weights=USocietyCovidCollider.cf_betaindin_xw,
)

# Compute weighted mean of the three variables of interest
# using the mean attribute in statsmodels
USocietyCovidCollider_Weighted.mean

# Compute weighted correlation of the three variables of interest
# using the corrcoef attribute in statsmodels
USocietyCovidCollider_Weighted.corrcoef

Note that the weighted mean and correlation coefficients differ quantitatively from the unweighted versions we computed earlier. The overall pattern of correlation is preserved.

Let's interpret the weighted correlation results:
* Work at home is negatively correlated with Risk of getting COVID-19, indicating that people who rarely or never work at home perceive a greater risk of getting COVID-19. 
* Age is weakly positively correlated with Risk of getting COVID-19, indicating that perceived risk of getting COVID-19 decreases with age.
* Age and work at home are largely not associated in the data set. 

_Note:_ Due to the way the variable Risk of getting COVID-19 is coded (1 = Very likely, 2 = Likely, 3 = Unlikely, 4 = Very unlikely), larger values indicate lower risk. The variable Risk of getting COVID-19 measures perceived risk, which is different from actual risk or health outcome after different age groups get COVID-19. 

# We model the outcome variable Risk of getting COVID-19 and the predictors
# Age and Work at home using a Generalized Linear Model (GLM) in statsmodels.
# We treat our outcome variable as quantitative and thus use the default
# Gaussian distribution family. Weights (cf_betaindin_xw) are applied using the
# parameter freq_weights.

import statsmodels.formula.api as smf

model = smf.glm(
    "cf_riskcv19 ~ cf_age + cf_wah",
    freq_weights=USocietyCovidCollider.cf_betaindin_xw,
    data=USocietyCovidCollider,
).fit()

print(model.summary())

# Although both Age and Work at home have some effect on
# Risk of getting COVID-19, the two predictors are not
# associated in the data set as measured via
# weighted correlation

USocietyCovidCollider_Weighted = DescrStatsW(
    USocietyCovidCollider.iloc[:, 0:2],
    weights=USocietyCovidCollider.cf_betaindin_xw,
)

USocietyCovidCollider_Weighted.corrcoef

Let's condition on the respondents who considered the risk for getting COVID-19 'Very likely'. This is an example of problematic conditioning on a collider variable.

# Create a collider variable — Very likely risk of getting COVID-19.
# Select the respondents who considered the risk for getting COVID-19 'Very likely'.

USocietyCovidColliderRisk = USocietyCovidCollider[
    USocietyCovidCollider["cf_riskcv19"] == 1
]

USocietyCovidColliderRisk

After we condition on those who considered the risk for getting COVID-19 'Very likely', we observe a negative correlation between Age and Work at home. 

# Compute weighted correlation of Age and Work at home

# Create a weighted instance
USocietyCovidColliderRisk_Weighted = DescrStatsW(
    USocietyCovidColliderRisk.iloc[:, 0:2],
    weights=USocietyCovidColliderRisk.cf_betaindin_xw,
)

# Weighted correlation
USocietyCovidColliderRisk_Weighted.corrcoef

### Questions
* Why Age and Work at home were uncorrelated in the population but are negatively correlated once we condition on those who perceive 'Very likely' risk of getting COVID-19?

# Additional material

The examples and code below are from [Chapter 3: Directed Acyclical Graphs](https://mixtape.scunning.com/dag.html) in Scott Cunningham's book [Causal Inference: The Mixtape](https://mixtape.scunning.com/index.html).

The original code is written by [Thomas Caputo](https://github.com/tomcaputo) and is available on [GitHub](https://github.com/tomcaputo/mixtape_learnr/blob/main/Python/Directed_Acyclical_Graphs.ipynb).   

# Gender discrimination and collider bias

Suppose we are interested in studying the effect of gender discrimination on earnings/wages. One approach would be to regress earnings on gender (Model 1 in the regression table below) which indeed shows that women are discriminated against. But then your model is criticised for not taking into account occupation. To address this criticism, you run another model that adjusts for occupation (Model 2 in the regression table below). The outputs of this second model indicates that women are not discriminated against; instead, they receive comparable (or even higher) pay. However, there is a problem in this second model too. Suppose that discrimination is mediated by occupation such that women tend to occupy worse jobs, which are payed less. In this scenario, by controlling for occupation we introduce bias. This is at odds with a widespread practice of adding more and more controls in a model. Such controls may not reduce but introduce bias. To get rid of the introduced bias in the discrimination example, we can condition on both occupation and ability, which is what Model 3 does in the regression table below. This unbiased conditional model confirms that women are discriminated against. In real-world settings, however, ability is unobserved, which would typically preclude us from estimating an unbiased effect of gender discrimination on earnings.

For a detailed account on of the discrimination example, see [Chapter 3: Directed Acyclical Graphs](https://mixtape.scunning.com/dag.html) in Scott Cunningham's book [Causal Inference: The Mixtape](https://mixtape.scunning.com/index.html).

!pip install Stargazer
import numpy as np
import pandas as pd
import statsmodels.api as sm
from stargazer.stargazer import Stargazer

# Data generation and assumptions

data = pd.DataFrame(
    {
        # Half of the population is female.
        "female": np.random.binomial(1, 0.5, size=10000),
        # Innate ability is independent of gender
        "ability": np.random.normal(size=10000),
    }
)

# All women experience discrimination
data["discrimination"] = data.female.copy()
# Data generating processes
data["occupation"] = (
    1
    + 2 * data["ability"]
    + 0 * data["female"]
    - 2 * data["discrimination"]
    + np.random.normal(size=10000)
)

data["wage"] = (
    1
    - 1 * data["discrimination"]
    + 1 * data["occupation"]
    + 2 * data["ability"]
    + np.random.normal(size=10000)
)

data

# Regression models
model1 = sm.OLS.from_formula("wage ~ female", data=data).fit()
model2 = sm.OLS.from_formula("wage ~ female + occupation", data=data).fit()
model3 = sm.OLS.from_formula("wage ~ female + occupation + ability", data=data).fit()

# Output the three regression model's results as Table
stargazer = Stargazer((model1, model2, model3))
stargazer.custom_columns(
    ["Biased Unconditional", "Biased", "Unbiased Conditional"], [1, 1, 1]
)

stargazer

#### Questions
* What is the true direct effect of discrimination on wages?
* Through what channels discrimination impacts wages?
* What makes occupation a collider?
* What control variables can get rid of the collider bias?

# References

Scott Cunningham. [Causal Inference: The Mixtape](https://mixtape.scunning.com/index.html). Yale University Press.

Thomas Caputo. [Teaching Resources for Causal Inference: The Mixtape](https://github.com/tomcaputo/mixtape_learnr). GitHub.  


Hernán MA, Robins JM (2020). [Causal Inference: What If](https://cdn1.sph.harvard.edu/wp-content/uploads/sites/1268/2021/01/ciwhatif_hernanrobins_31jan21.pdf). Boca Raton: Chapman & Hall/CRC.

Richard McElreath. Chapter 6: The Haunted DAG & The Causal Terror. [Statistical Rethinking: A Bayesian Course with Examples in R and Stan](https://xcelab.net/rm/statistical-rethinking/) (2nd ed). Chapman and Hall/CRC.  

Richard McElreath’s lecture on [basic causal inference](https://www.youtube.com/watch?v=l_7yIUqWBmE), collider bias, and back-door criterion.

Stephen L. Morgan and Christopher Winship. [Counterfactuals and Causal Inference](https://www.cambridge.org/core/books/counterfactuals-and-causal-inference/5CC81E6DF63C5E5A8B88F79D45E1D1B7). Cambridge University Press.
