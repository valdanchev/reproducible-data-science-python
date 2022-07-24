# Learning from Data to Predict

### Key themes
* The prediction task 
* Supervised learning 
* Machine learning tasks — e.g., regression (continuous) and classification (binary) 
* Building and evaluation of simple prediction models 
* The problem of model overfitting and strategies to avoid it:
  * Splitting the data into training set and testing set
  * Cross-validation
* Introduction to supervised machine learning algorithms, including _k_-Nearest Neighbors and Logistic Regression

### Learning resources
<i class="fas fa-play-circle"></i> [Predictability of life trajectories](https://www.youtube.com/watch?v=sOaPTrhB_uU) by Matthew Salganik

<i class="fas fa-play-circle"></i> [Introduction to Machine Learning Methods](https://youtu.be/pH-WuMW2rRE?t=1) by Susan Athey

<i class="fas fa-play-circle"></i> [Machine Learning with Scikit Learn](https://www.youtube.com/watch?v=HC0J_SPm9co) by Jake VanderPlas

<i class="fas fa-scroll"></i> M Molina & F Garip. 2019. [Machine learning for sociology.](https://osf.io/preprints/socarxiv/a6r9g/) _Annual Review of Sociology._ [Link](https://osf.io/preprints/socarxiv/a6r9g/) to an open-access version of the article available at the Open Science Framework.

<i class="fas fa-book"></i> Ian Foster, Rayid Ghani, Ron S. Jarmin, Frauke Kreuter, Julia Lane. 2021. [Chapter 7: Machine Learning](https://textbook.coleridgeinitiative.org/chap-ml.html). In _Big Data and Social Science_ (2nd edition).

<i class="fas fa-book"></i> Aurélien Géron. 2019. [Chapter 2: End-to-end Machine Learning project](https://github.com/ageron/handson-ml2/blob/master/02_end_to_end_machine_learning_project.ipynb). In _Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow_ (2nd Edition). O’Reilly.<br>




# The Prediction task

[Prediction](https://www.tandfonline.com/doi/full/10.1080/09332480.2019.1579578) is a data science task among other data science tasks, including description and causal inference. [Prediction](https://osf.io/preprints/socarxiv/a6r9g/) is the use of data to map some input _(X)_ to  an  output  _(Y)_. The prediction task is called _classification_ when the output variable is categorical (or discrete), and _regression_ when it is continuous. Our focus in this session will be on classification.

# Prediction tasks in social sciences

There are many [prediction problems in social sciences (summarised in Kleinberg et al. 2015)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4869349/) that can benefit from (supervised) machine learning, for example: 
* In child protection, predicting [when kids are in danger](https://www.nytimes.com/2018/01/02/magazine/can-an-algorithm-tell-when-kids-are-in-danger.html); 
* In the criminal justice system, predicting whether to detain or release arrestees as they await adjudication of their case (e.g., Kleinberg et al. 2015); 
* In population health, [predicting suicides](https://balkin.blogspot.com/2018/10/artificial-intelligence-for-suicide.html); 
* In education, predicting which teacher will have the greatest value add (e.g., Rockoff et al., 2011); 
* In higher education, predicting earlier [university dropouts](https://www.degruyter.com/document/doi/10.1515/jbnst-2019-0006/html);
* In labor market policy, predicting unemployment spell length to help workers decide on savings rates and job search strategies;
* In social policy, predicting highest risk youth for targeting interventions (e.g., Chandler et al., 2011);
* In sociology, predicting [life outcomes (Salganik et al. 2020)](https://www.pnas.org/content/117/15/8398).
<br>

# Predictions gone wrong
Prediction and machine learning models went wrong in a few occasions in different domains, including public health, education, the criminal justice system, and healthcare:
* David Lazer et all. [The Parable of Google Flu: Traps in Big Data Analysis.](https://science.sciencemag.org/content/343/6176/1203) Science.  
* [What went wrong with the A-level algorithm?](https://www.youtube.com/watch?v=jHtMLEhDOVE) Financial Times.
* [Why did the A-level algorithm say no?](https://www.bbc.co.uk/news/education-53787203) BBC.
* [Blame the politicians, not the technology, for A-level fiasco.](https://www.ft.com/content/58dcbfaa-740f-4747-8240-bc5ffb412e67). 
Financial Times.
* [Machine Bias](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing). ProPublica.
* Ziad Obermeyer at all. [Dissecting racial bias in an algorithm used to manage the health of populations](https://science.sciencemag.org/content/366/6464/447). Science.

Regardless of whether you use or not machine learning in your research, knowledge about prediction and machine learning techniques can help you evaluate how those techniques are used across domains and possibly identify ethical challenges and potential biases in those applications. Importantly, such data ethics challenges are found to reside not only in the machine learning algorithms themselves but in the entire [data science 'pipeline' or ecosystem](https://textbook.coleridgeinitiative.org/chap-bias.html).

# Supervised learning 

Learn a model from labeled training data or outcome variable that would enable us to make predictions about unseen or future data. The learning is called supervised because the labels (e.g., email Spam or Ham where 'Ham' is e-mail that is not Spam) of the outcome variable _(Y)_ that guide the learning process are already known. 

# Research problem: vaccine hesitancy 

We will aim to predict people who are unlikely to take a coronavirus vaccine _(Y)_ from socio-demographic and health input features _(X)_. An unbiased prediction of individuals who are unlikely to vaccinate can inform targeted public health interventions, including information campaigns disseminating evidence-based information about Covid-19 vaccines.

# Data: Understanding Society COVID-19

We will use data from [The Understanding Society: Covid-19 Study](https://www.understandingsociety.ac.uk/topic/covid-19). The survey asks participants across the UK about their experiences during the COVID-19 outbreak. We use the Wave 6 (November 2020) web-collected survey data. More information about the survey data and questionnaire is available in the study documentation on the [UK Data Service](https://beta.ukdataservice.ac.uk/datacatalogue/studies/study?id=8644#!/documentation) website. 

The data are safeguarded and is available to users registered with the [UK Data Service](https://beta.ukdataservice.ac.uk/datacatalogue/studies/study?id=8644).

<img src="https://www.cdcs.ed.ac.uk/files/styles/large_16x9/public/2019-08/Spotlighton_AjaMurray_A4_UKHLS_Logo_positive_RGB_300dpi.jpg?itok=YmQnr_oq" width="400" height="200" >

Once access to the data is obtained, the data needs to be stored securely in your Google Drive and loaded in your private Colab notebook. The data is provided in various file formats, we use the `.tab` file format (`tab` files store data values separated by tabs) which can be easily loaded using `pandas`. The web collected data of the survey from Wave 6 (November 2020) is stored in the file `cf_indresp_w.tab`.

:::{note}
The workflow in this session assumes that learners, first, have registered with the UK Data Service and obtained access to the Understanding Society: Covid-19 Study (Wave 6, November 2020, Web-collected data) and, second, have safely and securely stored the data in their Google Drive as a tab-separated values (TAB) file named `cf_indresp_w.tab`. If you have not registered with the UK Data Service and have not obtained access to the data, you can still read the textbook chapter and follow the analytical steps but would not be able to work interactively with the notebook.
:::

## Accessing data from your Google Drive
After you obtain access to the Understanding Society: Covid-19 Study, 2020, you can upload the Wave 6 (November 2020) data set into your Google Drive. Then you will need to connect your Google Drive to your Google Colab using the code below:   

# Import the Drive helper
from google.colab import drive

# This will prompt for authorization.
# Enter your authorisation code and rerun the cell.
drive.mount("/content/drive")

:::{note}
The above code will execute in Colab but will give an error (e.g., `ModuleNotFoundError: No module named 'google'`) when the notebook is run outside Colab.
:::

## Loading the Understanding Society Covid-19 Study (Wave 6, November 2020, Web collected)

import pandas as pd
import numpy as np

# Load the Understadning Society COVID-19 Study web collected data, Wave 6
# Set the delimeter parameter sep to "\t" which indicates tabs
USocietyCovid = pd.read_csv(
    "/content/drive/My Drive/cf_indresp_w.tab",
    sep="\t",
)

# Display all columns in the Understanding Society: COVID-19 Study
pd.options.display.max_columns = None

USocietyCovid.head(0)  # display headings only as the data is safeguarded

USocietyCovid.shape

USocietyCovid.info()

# Defining Output and Input variables

Here are the Output and Input data features we will use in this session.

#### Outcome: Output _(Y)_

|Description| Variable| Values
| ---| ---|---|
|Likelihood of taking up a coronavirus vaccination | cf_vaxxer | 1 = Very likely, 2 = Likely, 3 = Unlikely, 4 = Very unlikely

#### Predictors: Input features _(X)_

We select 4 (demographic and health-related) variables as examples only, no prior literature or expert knowledge is considered. We will discuss the role of prior literature and expert knowledge in the process of variable selection when we learn causal inference approaches. 

|Description| Variable| Values
| ---| ---|---|
|Age | cf_age | Integer values (whole numbers)
| Respondent sex | cf_sex_cv | 1 = Male, 2 = Female, 3 = Prefer not to say
| General health | cf_scsf1 | 1 = Excellent, 2 = Very good, 3 = Good, 4 = Fair, 5 = Poor 
| At risk of serious illness from Covid-19 | cf_clinvuln_dv | 0 = no risk (not clinically vulnerable), 1 = moderate risk (clinically vulnerable), 2 = high risk (clinically extremely vulnerable)

# Data wrangling

# Select output y and input X variables
USocietyCovid = USocietyCovid[
    ["cf_vaxxer", "cf_age", "cf_sex_cv", "cf_scsf1", "cf_clinvuln_dv"]
]
USocietyCovid.head()

import seaborn as sns

sns.set_context("notebook", font_scale=1.5)
%matplotlib inline

fig = sns.catplot(
    x="cf_vaxxer",
    kind="count",
    height=6,
    aspect=1.5,
    palette="ch:.25",
    data=USocietyCovid,
)

# Tweak the plot
(
    fig.set_axis_labels(
        "Likelihood of taking up a coronavirus vaccination", "Frequency"
    )
    .set_xticklabels(
        [
            "missing",
            "inapplicable",
            "refusal",
            "don't know",
            "Very likely",
            "Likely",
            "Unlikely",
            "Very unlikely",
        ]
    )
    .set_xticklabels(rotation=45)
)

Missing observations in Understanding Society are indicated by negative values. Let's convert negative values to NaN using the function `mask` in `pandas`. An alternative approach would be to reload the data using the Pandas `read_csv()` function and provide the negative values as an argument to the parameter `na_values`, as a result of which Pandas will recognise these values as NaN.  

# The function 'mask' in pandas replaces values where a condition is met.
USocietyCovid = USocietyCovid.mask(USocietyCovid < 0)
# Alternatively, you could replace negative values with another value, e.g., 0,
# using the code USocietyCovid.mask(USocietyCovid < 0, 0).
USocietyCovid

# Remove NaN
USocietyCovid = USocietyCovid[
    ["cf_vaxxer", "cf_age", "cf_sex_cv", "cf_scsf1", "cf_clinvuln_dv"]
].dropna()

USocietyCovid

# Plot the new cf_vaxxer (vaccination likelihood) variable

fig = sns.catplot(
    x="cf_vaxxer",
    kind="count",
    height=6,
    aspect=1.5,
    palette="ch:.25",
    data=USocietyCovid,
)

# Tweak the plot
(
    fig.set_axis_labels(
        "Likelihood of taking up a coronavirus vaccination", "Frequency"
    )
    .set_xticklabels(["Very likely", "Likely", "Unlikely", "Very unlikely"])
    .set_xticklabels(rotation=45)
)

To simplify the problem, we will recode `cf_vaxxer` (vaccination likelihood) variable into a binary variable where 1 refers to 'Likely to take up a Covid-19 vaccine' and 2 refers to 'Unlikely to take up a Covid-19 vaccine'. To achieve this, we use the `replace()` method which replaces a set of values we specify (in our case, `[1,2,3,4]`) with another set of values we specify (in our case, `[1,1,0,0]`).     

# Recode cf_vaxxer into a binary variable
USocietyCovid["cf_vaxxer"] = USocietyCovid["cf_vaxxer"].replace(
    [1, 2, 3, 4], [1, 1, 0, 0]
)
USocietyCovid.head()

# Plot the binary cf_vaxxer (vaccination likelihood) variable
fig = sns.catplot(
    x="cf_vaxxer",
    kind="count",
    height=6,
    aspect=1.5,
    palette="ch:.25",
    data=USocietyCovid,
)

# Tweak the plot
(
    fig.set_axis_labels(
        "Likelihood of taking up a coronavirus vaccination", "Frequency"
    )
    .set_xticklabels(["Unlikely", "Likely"])
    .set_xticklabels(rotation=45)
)

USocietyCovid.groupby("cf_vaxxer").count()

USocietyCovid.shape[0]

# 84.6% of respondents very likely or likely to take up a Covid vaccine
# and 15.4% very unlikely or unlikely
USocietyCovid.groupby("cf_vaxxer").count() / USocietyCovid.shape[0]

So far, we have described our outcome variable to make sense of the task but we have neither looked at the predictor variables nor examined any relationships between predictor variables and outcomes. It is a good practice to first split the data into training set and test set and only then explore predictors and relationships in the training set.

# Overfitting and data splitting

#### The problem of model overfitting
Overfitting occurs when model captures 'noise' in a specific sample while failing to recognise general patterns across samples. As a result of overfitting, the model produces accurate predictions for examples from the sample at hand but will predict poorly new examples the model has never seen.

#### Training set, Validation set, and Test set
To avoid overfitting, data is typically split into three groups: 
* Training set — used to train models 
* Validation set — used to tune the model and estimate  model performance/accuracy for best model selection
* Test set - used to evaluate the generalisability of the model to new observations the model has never seen

If your data set is not large enough, a possible strategy, which we will use here, is to split the data into training set and test set, and use cross-validation on the training set to evaluate our models' performance/accuracy. We will use 2/3 of the data to train the predictive model and the remaining 1/3 to create the test set.   

# Split train and test data

from sklearn.model_selection import train_test_split

# Outcome variable
y = USocietyCovid[["cf_vaxxer"]]

# Predictor variables
X = USocietyCovid[["cf_age", "cf_sex_cv", "cf_scsf1", "cf_clinvuln_dv"]]

# Split data into training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, stratify=y, random_state=0
)

print("Train data", X_train.shape, "\n" "Test data", X_test.shape)

# Preprocessing the training data set

## Categorical predictors — dummy variables

Categorical variables are often encoded using numeric values. For example, Respondent sex is recorded as 1 = Men, 2 = Female, 3 = Prefer not to say. The numeric values can be 'misinterpreted' by the algorithms — the value of 1 is obviously less than the value of 3 but that does not correspond to real-world numerical differences. 

A solution is to convert categorical predictors into dummy variables. Basically, each category value is converted into a new column and assigns a 1 or 0 (True/False) values using the function `get_dummies` in `pandas`. The function creates dummy/indicator variables that contain value of 1 or 0. 

The Respondent sex variable is converted below is three columns of 1s or 0s corresponding to the respective value.

# Use get_dummies to convert the Respondent sex categorical variable into
# 3 dummy/indicator variables
X_train_predictors = pd.get_dummies(X_train, columns=["cf_sex_cv"])
X_train_predictors.head()

# Create two DataFrames, one for numerical variables
# and one for categorical variables
X_train_predictors_cat = X_train_predictors[
    ["cf_sex_cv_1", "cf_sex_cv_2", "cf_sex_cv_3"]
]
X_train_predictors_cont = X_train_predictors[["cf_age", "cf_scsf1", "cf_clinvuln_dv"]]

## Continuous predictors — standardisation
We standardise the continuous input variables.

# Standardise the predictors using the StandardScaler function in sklearn
from sklearn.preprocessing import StandardScaler  # For standartising data

scaler = StandardScaler()  # Initialising the scaler using the default arguments
X_train_predictors_cont_scale = scaler.fit_transform(
    X_train_predictors_cont
)  # Fit to continuous input variables and return the standardised dataset
X_train_predictors_cont_scale

#### Combine categorical and continuous predictors into one data array

# Use the concatenate function in Numpy to combine all variables
# (both categorical and continuous predictors) in one array
X_train_preprocessed = np.concatenate(
    [X_train_predictors_cont_scale, X_train_predictors_cat], axis=1
)
X_train_preprocessed

X_train_preprocessed.shape

# Unbalance class problem

In the case of the vaccination likelihood question, one of the classes (likely to vaccinate) has a significantly greater proportion of cases (84.6%) than the other case (unlikely to vaccinate) (15.4%). We therefore face an unbalanced class problem. 

Different methods to mitigate the problem exist. We will use a method called ADASYN: Adaptive Synthetic Sampling Method for Imbalanced Data. The method oversamples the minority class in the training data set until both classes have an equal number of observations. Hence, the data set we use to train our models contains two balanced classes.

from imblearn.over_sampling import ADASYN

# Initialization of the ADASYN resampling method; set random_state for reproducibility
adasyn = ADASYN(random_state=0)

# Fit the ADASYN resampling method to the train data
X_train_balance, y_train_balance = adasyn.fit_resample(X_train_preprocessed, y_train)

The resulting `X_train_balance` and `y_train_balance` now include both the original data and the resampled data. The `y_train_balance` now includes an almost equal number of labels for each class.

# Now that the two classes are balanced, the train data
# is ~14K observations, greater than the original ~8K.
X_train_balance.shape

### Hands-on mini-exercise

Verify that after the oversampling the `y_train_balance` data object contains indeed approximately equal number of observations for both classes, those likely to vaccinate (1) and those unlikely to vaccinate (0). 

Note that `y_train_balance` is a NumPy array. You can check that on your own using the function `type()`, for example: type(y_train).

(y_train_balance == 0).sum()

(y_train_balance == 1).sum()

# Train models on training data

We fit two classifiers — k-Nearest Neighbours (k-NN) and Logistic Regression — on the training data. The k-Nearest Neighbours classifier (k-NN) and Logistic Regression classifier are two widely used classifiers. Our focus is on the end-to-end workflow so we do not discuss the workings of the two classifiers in detail. To learn more about the two classifiers, see [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/05.03-hyperparameters-and-model-validation.html) by Jake VanderPlas (on k-NN) and the DataCamp course [Supervised Learning with scikit-learn](https://learn.datacamp.com/courses/supervised-learning-with-scikit-learn). 

In the models below, we use the default hyperparameters (hyperparameter are parameters that are not learned from data but are set by the researcher to guide the learning process) for both classifiers.

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# Create an instance of k-nearest neighbors (k-NN) classifier.
# We set the hyperparameter n_neighbors=5 meaning that
# the label of an unknown respondent (0 or 1) is a function of
# the labels of its five closest training respondents.
kNN_Classifier = KNeighborsClassifier(n_neighbors=5)

# Create an instance of Logistic Regression Classifier
LogReg_Classifier = LogisticRegression()

# Fit both models to the training data
kNN_Classifier.fit(X_train_balance, y_train_balance.cf_vaxxer)
LogReg_Classifier.fit(X_train_balance, y_train_balance.cf_vaxxer)

# Model evaluation using Cross-validation

Now that your two models are fitted, you can evaluate the accuracy of their prediction. In older approaches, the prediction accuracy is often calculated on the same set of training data used to fit the model. The problem of such an approach is that the model can 'memorise' the training data and show high prediction accuracy on that data set while failing to perform well on new data. For this reason, approaches in data science, and machine learning in particular, prefer to evaluate the prediction accuracy of a model on new data that has not been used in training the model.

## The cross-validation technique

Cross-validation is a technique for assessing accuracy of model prediction without relying on in-sample prediction. We will split our training set into _k_ equal folds or parts. The number of folds can differ but for simplicity we will consider 5-fold cross-validation. How does 5-fold cross-validation work? While keeping aside one fold (or part), we fit the model with the remaining four folds and use the fitted model to predict outcomes of observations in fold one and on this basis compute model prediction accuracy. We repeat the procedure for all 5 folds or parts of the data and compute the average prediction accuracy.

## Metrics to evaluate model performance
Many [metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter) to evaluate model performance exist. We evaluate model performance using the accuracy score. The accuracy score is the simplest metric for evaluating classification models. Simply put, accuracy is the proportion of predictions our model got right. Keep in mind, however, that because of the unbalanced class problem, accuracy may not be the best metric in our case. Because one of our classes accounts for 84.6% of the cases, even a model that uniformly predicts that all respondents are likely to take up the vaccine will obtain very high accuracy of 0.846 while being useless for identifying respondents who are unlikely to take up the vaccine. We will return to this problem shortly.

# Import the function cross_val_score() which performs
# cross-validation and evaluates the model using a score.
# Many scores are available to evaluate a classification mdoel,
# as a starting point, we select the simplest one called accuracy.
from sklearn.model_selection import cross_val_score

# Evaluate the kNN_Classifier model via 5-fold cross-validation
kNN_score = cross_val_score(
    kNN_Classifier, X_train_balance, y_train_balance.cf_vaxxer, cv=5, scoring="accuracy"
)
kNN_score

# Take the mean across the five accuracy scores
kNN_score.mean() * 100

# Repeat for our logistic regression model
LogReg_score = cross_val_score(
    LogReg_Classifier,
    X_train_balance,
    y_train_balance.cf_vaxxer,
    cv=5,
    scoring="accuracy",
)
LogReg_score.mean() * 100

The output from the cross-validation technique shows that the performance of our two models is comparable as measured by the accuracy score. 

At this stage, we could fine-tune model hyperparameters — i.e., parameters that the model does not learn from data, e.g., the number of _k_ neighbours in the _k_-NN algorithm — and re-evaluate model performance. During the process of model validation, we do not use the test data. Once we are happy with how our model(s) perform, we test the model on unseen data.  

# Testing model accuracy on new data

Before we test the accuracy of our model on the test data set, we preprocess the test data set using the same procedure we used to preprocess the training data.

# Preprocessing the test data set

# Use get_dummies to convert the respondent sex categorical variable
# into 3 dummy/indicator variables.
X_test_predictors = pd.get_dummies(X_test, columns=["cf_sex_cv"])

# Create two DataFrames, one for quantitative variables and one for qualitative variables
X_test_predictors_cat = X_test_predictors[["cf_sex_cv_1", "cf_sex_cv_2", "cf_sex_cv_3"]]
X_test_predictors_cont = X_test_predictors[["cf_age", "cf_scsf1", "cf_clinvuln_dv"]]

# Standardise the predictors using the StandardScaler function in sklearn
scaler = StandardScaler()  # Initialising the scaler using the default arguments
X_test_predictors_cont_scale = scaler.fit_transform(
    X_test_predictors_cont
)  # Fit to continuous input variables and return the standardised dataset

# Use the concatenate function in Numpy to combine all variables
# (both categorical and continuous predictors) in one array
X_test_preprocessed = np.concatenate(
    [X_test_predictors_cont_scale, X_test_predictors_cat], axis=1
)
X_test_preprocessed

# Predicting vaccine hesitancy

Use the `predict` function to predict who is likely to take up the COVID-19 vaccine or not using the test data.

y_pred_kNN = kNN_Classifier.predict(X_test_preprocessed)
y_pred_LogReg = LogReg_Classifier.predict(X_test_preprocessed)

y_pred_LogReg

# Model evaluation on test data

Let's evaluate the performance of our models predicting vaccination willingness using accuracy metric.

# Evaluate performance using the accuracy score for the logistic regresson model
from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_pred_LogReg)

# Evaluate performance using the accuracy score for the  k-nearest neighbors model
accuracy_score(y_test, y_pred_kNN)

The accuracy scores are slightly lower on the test set compared to the accuracy score on the training set, indicating that the data split methodology mitigates the risk of overfitting. 

Accuracy is a good metric when the positive class and the negative class are balanced. However, when one of the classes is a majority, as in our case, then a model can achieve a high accuracy by just predicting all observations to be the majority class. However, this is not what we want. In fact, in order to inform an information campaign about vaccination, we are more interested in predicting the minority class, people that are unlikely to take up the vaccine. 

We can use a confusion matrix to further evaluate the performance of our classification models. The confusion matrix shows the number of respondents known to be in group 0 (unlikely to vaccinate) or 1 (likely to vaccinate) and predicted to be in group 0 or 1, respectively.  

The confusion matrix below shows that the logistic model predicts 393 out of the 606 respondents who are unlikely to vaccinate. The model does much better job predicting respondents that are likely to vaccinate, 2066 out of 3331 respondents in the test data set.

# Confusion matrix for the logistic regression model
# plotted via the Pandas crosstab() function

pd.crosstab(
    y_test.cf_vaxxer,
    y_pred_LogReg,
    rownames=["Actual"],
    colnames=["Predicted"],
    margins=True,
)

What do the numbers in the confusion matrix mean?
* True positive - our model correctly predicts the positive class (likely to vaccinate)
* True negative - our model correctly predicts the negative class (unlikely to vaccinate)
* False positive - our model incorrectly predicts the positive class
* False negative - our model incorrectly predicts the negative class

# Here is another representation of the confusion matrix
# using the scikit-learn `confusion_matrix` function
from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, y_pred_LogReg)

# The function ravel() flattens the confusion matrix
tn, fp, fn, tp = confusion_matrix(y_test, y_pred_LogReg).ravel()
print(
    "True negative = ",
    tn,
    "\nFalse positive = ",
    fp,
    "\nFalse negative = ",
    fn,
    "\nTrue positive = ",
    tp,
)

For the k-nearest neighbors model, the confusion matrix  below shows that the k-NN model predicts 316 out of the 606 respondents who are unlikely to vaccinate (the logistic regression model predicts more accurately those unlikely to vaccinate). The model does not predicts well respondents that are likely to vaccinate, 1670 out of 3331 respondents in the test data set. 

Recall that we are less interested in predicting the majority class (likely to vaccinate). Instead, we are interested in predicting the minority class (unlikely to vaccinate) so that the results can inform an information campaign among people that are unlikely to vaccinate.

# Confusion matrix for the k-nearest neighbors model
# plotted via pandas function crosstab
pd.crosstab(
    y_test.cf_vaxxer,
    y_pred_kNN,
    rownames=["Actual"],
    colnames=["Predicted"],
    margins=True,
)

Instead of relying on a single metric, it is often helpful (if not confusing) to compare various metrics. You can use the scikit-learn function [`classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html) to calculate various classification metrics, including [precision and recall](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-report). 

from sklearn.metrics import classification_report

# Various metrics for the logistic regression model
print(classification_report(y_test, y_pred_LogReg))

# Various metrics for the k-nearest neighbors model
print(classification_report(y_test, y_pred_kNN))

Overall, predicting accuracy of approximately 62% and 50% for the two models and the low predictive accuracy of the minority class (unlikely to vaccinate) indicate that the performance of our models is far from optimal. However, the purpose of this lab is not to build a well-performing model but to introduce you to an end-to-end machine learning workflow. 

Keep in mind that it is not a good research practice to now — after you tested the models on the test data — go back and fine-tune the training models as this will introduce overfitting. A good research practice is to fine-tune and improve your model(s) at the stage of training and cross-validation (not after you tested your model on unseen data). Once you select your best performing model(s) at the cross-validation stage, you test the model using the test data and report the performance scores.

As part of your data analysis exercises, you will have another opportunity to build a new machine learning model and evaluate model performance.