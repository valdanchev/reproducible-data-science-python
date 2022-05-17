# Discovering patterns in data

This lab will first introduce you to key concepts in machine learning for social science. Our focus will be on a particular branch of machine learning called unsupervised learning, which includes techniques for clustering and dimensionality reduction. We will then focus on hands-on data analysis with the `scikit-learn` library for machine learning in Python. Our research objective is to group UK counties with similar mobility trends using two popular techniques of unsupervised learning: _k_-means clustering and Principal Components Analysis (PCA).

## Key themes
* Definition of machine learning.
* Supervised and unsupervised learning.
* Introduction to unsupervised learning techniques, including clustering (_k_-means) and dimensionality reduction (Principal Component Analysis (PCA)).
* Hands-on machine learning with `scikit-learn`.
* Data-informed model parameter selection.

## Learning resources

<i class="fas fa-scroll"></i> M Molina & F Garip. 2019. [Machine learning for sociology.](https://osf.io/preprints/socarxiv/a6r9g/) _Annual Review of Sociology._ [Link](https://osf.io/preprints/socarxiv/a6r9g/) to an open-access version of the article available at the Open Science Framework.

<i class="fas fa-book"></i> Ian Foster, Rayid Ghani, Ron S. Jarmin, Frauke Kreuter, Julia Lane. 2021. [Chapter 7: Machine Learning](https://textbook.coleridgeinitiative.org/chap-ml.html). In _Big Data and Social Science_ (2nd edition).

<i class="fas fa-play-circle"></i> [What is Machine Learning?](https://www.youtube.com/watch?v=f_uwKZIAeM0) OxfordSparks.


### Additional resources

<i class="fas fa-book"></i> Kosuke Imai. 2018. Chapter 3.7.3: The _k_-means algorithm. In _Quantitative Social Science_. Princeton University Press. 

<i class="fas fa-book"></i> Jake VanderPlas. 2016. [In Depth: k-Means Clustering](https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html). In 
_Python Data Science Handbook_.

<i class="fas fa-book"></i> Sebastian Raschka. 2018. Python Machine Learning. Packt Publishing. 

<br>


# Machine Learning: What is it? What is it good for?
> Field of study that gives computers the ability to learn [from  data] without being explicitly programmed.
>
> *—Arthur Samuel, 1959*

## Data science tasks we can solve using machine learning
1. Pattern discovery using unsupervised machine learning
2. Prediction using supervised machine learning

## Unsupervised and Supervised learning

Two types of machine learning are often distinguished in the literature: unsupervised learning and supervised learning

1. Unsupervised learning — no outcome variable / labeled data are available, and the structure of data is unknown. The goal of unsupervised learning is to explore the structure of data and discover hidden structures and meaningful information without the guidance of outcome variable / labeled data. To uncover such hidden structures in data, we use unsupervised learning techniques, including clustering (e.g., k-Means) and dimensionality reduction (e.g., Principal Component Analysis (PCA)).

> <i class="fas fa-play-circle"></i> [Unsupervised Learning](https://www.youtube.com/watch?v=jAA2g9ItoAc), Machine Learning's course by Andrew Ng

2. Supervised learning — learn a model from labeled training data or outcome variable that would enable us to make predictions about unseen or future data. The learning is called supervised because the outcome variable as well as labels (e.g., email Spam or Ham where 'Ham' is e-mail that is not Spam) that guide the learning process are already known.

> <i class="fas fa-play-circle"></i> [Supervised learning](https://www.youtube.com/watch?v=bQI5uDxrFfA), Machine learning's course by Andrew Ng

In this lab, we will be focusing on unsupervised learning. 

# Research problem: clustering counties by mobility

Let's formulate our simple research problem: to inform a public health intervention, we need to group a number of counties in the UK with similar mobility trends. We frame this problem as a clustering task and perform _k_-means clustering to sort the UK counties into clusters with similar mobility trends.  

# _k_-means clustering

Clustering is an exploratory data analysis (EDA) task that aims to group a set of observations into subgroups or clusters (without any prior information about cluster membership) such that observations assigned to the same cluster are more similar to each other than those in other clusters. To cluster observations in our mobility data, we will employ the _k_-means algorithm.

### The _k_-means algorithm

> The k-means algorithm is an iterative algorithm in which a set of operations are repeatedly performed until a noticeable difference in results is no longer produced. The goal of the algorithm is to split the data into _k_ similar groups where each group is associated with its centroid, which is equal to the within-group mean. This is done by first assigning each observation to its closest cluster and then computing the centroid of each cluster based on this new cluster assignments. These two step are iterated until the cluster assignment no longer changes.
>
> The _k_-means algorithm produces the prespecified number of clusters _k_ and consists of the following steps: 
>1. Choose the initial centroids of _k_ clusters. 
>2. Given the centroids, assign each observations to a cluster whose centroid is the closest to that observation. 
>3. Choose the new centroid of each cluster whose coordinate equals the within-cluster mean of the corresponding variable.
>4. Repeat Steps 2 and 3 until cluster assignment no longer change.
>
> —Kosuke Imai. 2018. Quantitative Social Science. Princeton University Press.

See also <i class="fas fa-book"></i> [Jake VanderPlas' Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html).

On k-Means Advantages and Disadvantages, read [here](https://developers.google.com/machine-learning/clustering/algorithm/advantages-disadvantages). 

### Recent applications of _k_-means clustering in social sciences

<i class="fas fa-scroll"></i> Garip, F. 2012. [Discovering diverse mechanisms of migration: The Mexico–US Stream 1970–2000](https://www.jstor.org/stable/41857399). Population and Development Review, 38(3), 393-433. [Open access version](https://dash.harvard.edu/bitstream/handle/1/10872801/garip_pdr_2012.pdf;jsessionid=17835B14A077877CBC9516BC9A1D890E?sequence=1).
 
<i class="fas fa-scroll"></i> Bail, C. A. (2008). [The configuration of symbolic boundaries against immigrants in Europe](https://www.jstor.org/stable/25472513). American Sociological Review, 73(1), 37-59.

# Let's get coding with `scikit-learn`

[Scikit-learn](https://scikit-learn.org/stable/) is simple, efficient, and widely used library for machine learning in Python.  

# Import libraries for today's lab

# Data analysis & visualisation
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(font_scale=1.5)
%matplotlib inline

# Suppress warnings to avoid potential confusion
import warnings

# Machine learning
from sklearn.cluster import KMeans  # For performing k-means
from sklearn.decomposition import PCA  # For performing PCA
from sklearn.preprocessing import StandardScaler  # For standartising data

warnings.filterwarnings("ignore")

### Load and process the mobility data, select UK data and compute mean mobility trends 

# Load the mobility data
mobility_trends_complete = pd.read_csv(
    "https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv",
    parse_dates=["date"],
)

mobility_trends_complete

Select a manageable subset of the dataset covering the period from 15 February 2020 to 30 June 2021 using the functions `subperiod_mobility_trends()` and `rename_mobility_trends()` we defined in the previous chapter *Exploratory Data Analysis and Visualisation*. 

mobility_trends_complete

# %load preprocess_mobility_trends.py


def subperiod_mobility_trends(data, start_date, end_date):
    """
    Add your mobility data in `data`.

    This function selects a subperiod of the mobility data based on prespecified start data and end date.
    """
    mobility_trends = data[
        data["date"].isin(pd.date_range(start=start_date, end=end_date))
    ]
    return mobility_trends


def rename_mobility_trends(data):
    """
    This function renames the column headings of the six mobility categories.
    """
    mobility_trends_renamed = data.rename(
        columns={
            "retail_and_recreation_percent_change_from_baseline": "Retail_Recreation",
            "grocery_and_pharmacy_percent_change_from_baseline": "Grocery_Pharmacy",
            "parks_percent_change_from_baseline": "Parks",
            "transit_stations_percent_change_from_baseline": "Transit_stations",
            "workplaces_percent_change_from_baseline": "Workplaces",
            "residential_percent_change_from_baseline": "Residential",
        }
    )
    return mobility_trends_renamed

mobility_trends = subperiod_mobility_trends(
    mobility_trends_complete, "2020-02-15", "2021-06-30"
)

mobility_trends

mobility_trends = rename_mobility_trends(mobility_trends)
mobility_trends

Select data for the United Kingdom and compute mean mobility trends for each county.

# Select data for the UK
mobility_trends_UK = mobility_trends[
    mobility_trends["country_region"] == "United Kingdom"
]

# Compute mean mobility trends for each UK county per mobility category
# and assign the result to the variable mobility_trends_UK_mean
mobility_trends_UK_mean = mobility_trends_UK.groupby("sub_region_1")[
    [
        "Retail_Recreation",
        "Grocery_Pharmacy",
        "Parks",
        "Transit_stations",
        "Workplaces",
        "Residential",
    ]
].mean()

mobility_trends_UK_mean

### The _k_-means clustering algorithm in `scikit-learn` 

The `KMeans` estimator class in scikit-learn allows you to set up the algorithm parameters before fitting the estimator to the data. 

Parameters of the `KMeans` algorithm include:

- `n_clusters` — Number of clusters `k` to form (same as the number of centroids to generate).

- `init` _('random' or 'k-means++', default='k-means++')_ Method of selection of initial centroids. 'random' selects n_clusters observations (rows) at random from data for the initial centroids. ‘k-means++’ selects initial cluster centers in a way that speeds up convergence.

- `n_init` _(default = 10)_ — Number of times the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n_init consecutive runs. The best output is measured in terms of the sum of squared distances of samples to their closest cluster center.

- `max_iterint` _(default=300)_ — Maximum number of iterations of the k-means algorithm for a single run.

- `random_state` _(default=None)_ For computational reproducibility, determines random number generation for centroid initialization.

We instantiate the KMeans class with the following arguments:

kmeans = KMeans(n_clusters=3, init="k-means++", n_init=10, max_iter=300, random_state=0)

kmeans

# Data preprocessing

We preprocess the data in a format expected by the `scikit-learn` library. As part of the data preprocessing, we first remove countries with one or more NaN (Not a Number) using the Pandas method `dropna()`. Although some `scikit-learn` functions, such as `StandardScaler()`, handle NaNs, others, such as `fit()`, may require fine-tuning, so we remove NaNs at this stage to avoid unexpected downstream problems.

:::{tip}
`scikit-learn` works on any numeric data stored as NumPy arrays, SciPy sparse matrices, or (nowadays) pandas DataFrame. If needed, you can convert Pandas DataFrame into a NumPy array using the Pandas method `to_numpy()`.
:::

# Drop NaNs from the DataFrame
mobility_trends_UK_mean_NaNdrop = mobility_trends_UK_mean.dropna()
mobility_trends_UK_mean_NaNdrop

# Data standardisation

It is a good practice to standardise our input features or variables before applying the k-means algorithm. Standardisation of input features in a data set is a common requirement for many statistical and machine learning estimators. By standardising individual features, all features are converted to the same scale so that the output of the clustering procedure is not influenced by how individual features are measured. 

In our example data, the six features are measured on a similar scale so one may argue that standardisation is not strictly necessary but we will perform it so that the procedure is part of your data analysis workflow. 

The `sklearn.preprocessing` module includes [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler) among other methods for data scaling. The `StandardScaler` method calculates a standard score or _z-score_ of a sample observation `x` as `z = (x - M) / SD` where M is the mean of the sample observations and SD is the standard deviation of the sample observations. In simple words, for each observation in a column, we subtract the mean and divide by the standard deviation of that column.

# Data standardisation
scaler = StandardScaler()  # Initialising the scaler using the default arguments
mobility_trends_UK_standardised = scaler.fit_transform(
    mobility_trends_UK_mean_NaNdrop
)  # Fit to input data (continuous variable) and return the standardised variables

mobility_trends_UK_standardised

In the above cell, we printed out the full arrays. This may be necessary for research transparency but in some settings, for example when you deal with large data, may not be practical. In such settings, you could select and print out only a couple of rows. For example, to print out the first 3 rows, you type in:    

mobility_trends_UK_standardised[0:3,]

We now fit the k-means class we already created (`kmeans`) to our data. This will perform 10 runs of the k-means algorithm (each with a different centroid seed) on your data with a maximum of 300 iterations per run:

kmeans.fit(mobility_trends_UK_standardised)

You can access estimator's learned parameters using an underscore suffix '_'. For example, the attribute `labels_` will display the cluster each observation or sample (in our example, county) belongs to. The labels of the clusters can be accessed by typing your k-means object (which we called 'kmeans') followed by a '.' and the `labels_` attribute.

kmeans.labels_

The cluster labels indicate that, for example, the first county, Aberdeen City, is assign to cluster 2, the second county, Aberdeenshire, to cluster 0, and so on.

You can also access the coordinates of cluster centers using the `cluster_centers_` attribute. This will show the means of the points in each cluster for each of the six variables.

kmeans.cluster_centers_

You can include the cluster assignment as a column in your original DataFrame. Let's name the new column 'clusters'.


mobility_trends_UK_mean_NaNdrop["clusters"] = kmeans.labels_
mobility_trends_UK_mean_NaNdrop

# Choosing the optimal number of clusters

In the example above, our choice of the number of clusters, _k_, was arbitrary. Let's find a more informative method of choosing the optimal _k_ for our data. One such method is the [Elbow method](https://en.wikipedia.org/wiki/Elbow_method_(clustering)) for choosing optimal _k_. 

Using the Elbow method, we run the k-means algorithm with various values of _k_ and plot each value of _k_ against the sum of squared distances between each data point (county in the UK) and its cluster centroid. For the case of _k_ = 1 all data points will be assigned to the same cluster, resulting in higher sum of squared distances. As _k_ increases, the sum of squared distances will be close to zero because each data point would be assigned to its own cluster.

We perform multiple runs of the k-means clustering algorithm using a `for` loop.

# Performing `for` loop

A `for` loop is used to repeatedly execute a block of code, and is perfect fit for repeatedly executing the k-means algorithm. The `for` loop will iterate over a sequence of _k_ values, and for each value of _k_ will estimate the k-means algorithm. 

Let's first look at a simple example of a `for` loop:

for number in range(1, 4):
    print(number)

In this example (and in `for` loops in general), there are two parts: 
 * `for` loop statement, which in this example is '`for` number in range (1,4):'
    * `number` is the variable name; we could have specified a different variable name;
    * `range (1,4)` specifies the set of values to loop or iterate over; `range (1,4)` is the range of numbers 1, 2, 3. The first argument (1) is the starting point, and the second argument (4) is the endpoint (not included in the range)  
    * the word 'in' connects the two components in the `for` loop statement
    * the `for` loop statement ends in a colon ':'.
 * the loop body, which contains the code to be executed at each iteration of the `for` loop. Each line in the loop body is indented four spaces, and this indentation is how the interpreter knows that a line is part of the loop or not. In our example, 'print(number)' is the loop body.

At each iteration of the `for` loop, the variable `number` is assigned the next number in the range from 1 to 3, and then the value of `number` is printed. The loop runs once for each number in the sequence from 1 to 3, so the body loop 'print(number)' executes 3 times. 

This loop description draws on the _Real Python's_ book [Python Basics](https://realpython.com/tutorials/basics/) (pages 153–154) and on the [Kaggle's Python tutorial](https://www.kaggle.com/colinmorris/loops-and-list-comprehensions).

## Choosing _k_ via `for` loop
We are now ready to apply the `for` loop to the k-means algorithm.
In the code below, the `for` loop statement is '`for` k in K' where _k_ is the variable name and _K_ is the set of values ranging from 1 to 30. The loop body contains the three lines of code related to the `k-means()` initiation, estimation, and output. Each of the three lines in the loop body are indented four spaces. The loop will run 30 times, so all three lines related to the `k-means()` algorithm will be executed 30 times. 

# Run the k-means algorithm for values of k between 1 and 30

Sum_of_squared_distances = []  # Initialise a list

K = range(
    1, 31
)  # range with a starting point 1 and endpoint 31, which is not included in the range
for k in K:  # a for loop iterating over values of k ranging from 1 to 30
    kmeans = KMeans(n_clusters=k)  # Initialise the KMeans estimator for a value of k
    kmeans.fit(
        mobility_trends_UK_standardised
    )  # Perform the KMeans estimator by the fit() method
    Sum_of_squared_distances.append(
        kmeans.inertia_
    )  # Store the sum of squared distances (stored in kmeans.inertia_)
    # for each run using the Python append() function.

Sum_of_squared_distances

# Elbow plot 

Let's plot k against the sum of squared distances. The plot below shows how the sum of squared distances varies with values of _k_ between 1 and 30.

# Plot size
plt.figure(figsize=(8.2, 5.8))

# Generate the plot
grid = sns.lineplot(x=K, y=Sum_of_squared_distances)

# Add x and y labels
labels = grid.set(xlabel="Number of clusters, k", ylabel="Total squared distances")

For our data set, the elbow of the curve (where the curve "bends") is not apparent but total squared distances seem to decrease slowly after _k_ = 4. So we rerun our k-means algorithm with _k_ = 4.

k = 4
kmeans_k4 = KMeans(
    n_clusters=k, init="k-means++", n_init=10, max_iter=300, random_state=0
)

kmeans_k4.fit_transform(mobility_trends_UK_standardised)

Let's view to which cluster each observation or sample (in our example, UK county) in our data set was assigned to:

kmeans_k4.labels_

Here are also the centers of the four detected clusters:

kmeans_k4.cluster_centers_

_K_-Means is an an iterative algorithm so a set of operations are repeatedly performed until sum of distances from each observation to its cluster centroid is minimised and the cluster assignment no longer updates. How many iterations were needed for the algorithm to converge in our case?

kmeans_k4.n_iter_

As we did earlier, we add the cluster assignment as a column to our DataFrame. We name the column 'clusters_k4'.

# Add the 4-cluster assignment to your DataFrame
mobility_trends_UK_mean_NaNdrop["clusters_k4"] = kmeans_k4.labels_
mobility_trends_UK_mean_NaNdrop

Our next step will be to assess the way in which clusters are similar or different with respect to each mobility category. To accomplish this, we plot the clusters against each mobility category using the Seaborn function `catplot`.

# Create a variable 'mobility_category'
mobility_categories = [
    "Retail_Recreation",
    "Grocery_Pharmacy",
    "Parks",
    "Transit_stations",
    "Workplaces",
    "Residential",
]

# Use a for loop to plot the clusters across the six mobility categories

for mobility_category in mobility_categories:
    sns.catplot(
        x="clusters_k4",
        y=mobility_category,
        kind="swarm",
        data=mobility_trends_UK_mean_NaNdrop,
    )

# Dimensionality Reduction via PCA

The above plots visualise each variable separately. A more informative approach would be to take into account all six dimensions simultaneously. However, there is a difficulty in visualising and perceiving multidimensional data beyond two or three dimensions. One solution is to use the dimensionality reduction technique Principal Component Analysis (PCA).

We can apply the PCA to reduce the six mobility trends to just 2 dimensions, and then use those 2-dimensional approximations to visualise our clusters using a scatter plot.

The `sklearn` library is very consistent so the workflow we used to run `k-means` applies to `PCA` too. We first initialise the [PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) estimator using the default arguments except for `n_components` where we specify to keep only 2 components. Then we perform the estimator using the `fit()` method. Below we use the `fit_transform()` method to simultaneously fit the estimator to data and apply the dimensionality-reduction transformation to data.  

# We reuse our standardised data set
mobility_trends_UK_standardised

# Initialise the Principal component analysis (PCA) algorithm with 2 components
pca = PCA(n_components=2)

# Apply the dimensionality reduction on the six mobility categories
pca_components = pca.fit_transform(mobility_trends_UK_standardised)

# Transformed values arranged as observations/samples in rows
# and number of components in columns
pca_components

Now we can run the k-means algorithm on the two principal components:

k = 4
kmeans_k4_pca = KMeans(
    n_clusters=k, init="k-means++", n_init=10, max_iter=300, random_state=0
)
kmeans_k4_pca.fit(pca_components)

# Labels of clusters to which each observation was assigned to
kmeans_k4_pca.labels_

# Add the 4-cluster assignment on the PCA components to your DataFrame
mobility_trends_UK_mean_NaNdrop["clusters_k4_pca"] = kmeans_k4_pca.labels_
mobility_trends_UK_mean_NaNdrop

# Visualising mobility clusters

Let's plot the resulting clusters along the two principal components using a scatter plot.

# Set figure size
plt.figure(figsize=(11.7, 8.27))

# Scatterplot with the 1st principal component on the horizontal x axes
# and the 2nd principal component on the vertical y axis
grid = sns.scatterplot(
    x=pca_components[:, 0],
    y=pca_components[:, 1],
    hue=kmeans_k4_pca.labels_,
    alpha=0.8,
    s=120,
)

# Add labels to the horisontal x axis and vertical y axis
labels = grid.set(xlabel="1st principal component", ylabel="2nd principal component")

# Plot the cluster centroids
sns.scatterplot(
    x=kmeans_k4_pca.cluster_centers_[:, 0],
    y=kmeans_k4_pca.cluster_centers_[:, 1],
    hue=range(k),
    s=220,
    alpha=0.8,
    ec="black",
    legend=False,
)

# Add title 'Cluster' to the legend and locate it in the upper right of the plot
plt.legend(title="Cluster", loc="upper right")

In the figure above, we plot the 1st principal component against the 2nd principal component derived from the six mobility types. Each data point is a county in the UK. Larger dots represent the cluster centroid (which is typically not a data point). Colour scheme represents cluster assignment.

The figure above lacks county labels which we would need in order to interpret our results from k-means clustering. 

Let's add labels to data points so that we can associate each county with its name. 

# Enlarge figure size
plt.figure(figsize=(32, 24))

# Scatterplot with the 1st principal component on the horizontal x axes
# and the 2nd principal component on the vertical y axis
grid = sns.scatterplot(
    x=pca_components[:, 0],
    y=pca_components[:, 1],
    hue=kmeans_k4_pca.labels_,
    alpha=0.9,
    s=120,
)

# Add labels to the horisontal x axis and vertical y axis
labels = grid.set(xlabel="1st principal component", ylabel="2nd principal component")

# Plot the cluster centroids
sns.scatterplot(
    x=kmeans_k4_pca.cluster_centers_[:, 0],
    y=kmeans_k4_pca.cluster_centers_[:, 1],
    hue=range(k),
    s=240,
    alpha=0.8,
    ec="black",
    legend=False,
)

# This for loop assign country name to each data point iteratively
for line in range(0, mobility_trends_UK_mean_NaNdrop.shape[0]):
    grid.text(
        pca_components[line, 0] + 0.1,
        pca_components[line, 1],  # where the labels should be positioned
        mobility_trends_UK_mean_NaNdrop.index[line],  # add labels to each data point
        horizontalalignment="left",
        size="small",
        color="black",
        weight=None,
    )

# Add title 'Cluster' to the legend and locate it in the upper right of the plot
plt.legend(title="Cluster", loc="upper right");

Because PCA transforms our six variables into a two-dimensional space, we cannot anymore see how a particular cluster or county is positioned with respect to any particular mobility category. 

If you need to cluster counties with regard to any pair of variables, you could run k-means on particular pairs of variables and plot the cluster assignment for those variables. For example, below we run the k-means algorithm on two variables: retail and recreation mobility and workplaces mobility.

# We first fit k-means to two variables retail_recreation and workplaces
# using the standardised data. We specify the number of clusters to be
# formed as k = 4  but keep in mind that we did not performed the Elbow method
# on these two variables in particular.

k = 4
kmeans_k4_2vars = KMeans(
    n_clusters=k, init="k-means++", n_init=10, max_iter=300, random_state=0
)

# 0 indicates the retail_recreation mobility variable
# and 4 indicates workplaces mobility variable
kmeans_k4_2vars.fit(mobility_trends_UK_standardised[:, [0, 4]])

Plot the resulting clusters along the two mobility variables — retail and recreation mobility and workplaces mobility — using a scatter plot.

# Plot the clusters
plt.figure(figsize=(11.7, 8.27))

grid = sns.scatterplot(
    x=mobility_trends_UK_standardised[:, 0],
    y=mobility_trends_UK_standardised[:, 4],
    hue=kmeans_k4_2vars.labels_,
    alpha=0.8,
    s=120,
)

# Plot the centers
sns.scatterplot(
    x=kmeans_k4_2vars.cluster_centers_[:, 0],
    y=kmeans_k4_2vars.cluster_centers_[:, 1],
    hue=range(k),
    s=220,
    alpha=0.8,
    ec="black",
    legend=False,
)
grid.set(
    xlabel="Retail and Recreation Mean Change Mobility",
    ylabel="Workplaces Mean Change Mobility",
)

# Add title 'Cluster' to the legend and locate it in the upper right of the plot
plt.legend(title="Cluster", loc="upper right")

Let's add UK county labels in the figure below as we did before. 

# Enlarge figure size
plt.figure(figsize=(28, 22))

# Scatterplot with the 1st principal component on the horizontal x axes
# and the 2nd principal component on the vertical y axis
grid = sns.scatterplot(
    x=mobility_trends_UK_standardised[:, 0],
    y=mobility_trends_UK_standardised[:, 4],
    hue=kmeans_k4_2vars.labels_,
    alpha=0.9,
    s=120,
)
grid.set(
    xlabel="Retail and Recreation Mean Change Mobility",
    ylabel="Workplaces Mean Change Mobility",
)

# Plot the cluster centroids
sns.scatterplot(
    x=kmeans_k4_2vars.cluster_centers_[:, 0],
    y=kmeans_k4_2vars.cluster_centers_[:, 1],
    hue=range(k),
    s=240,
    alpha=0.8,
    ec="black",
    legend=False,
)

# This for loop assign country name to each data point iteratively
for line in range(0, mobility_trends_UK_mean_NaNdrop.shape[0]):
    grid.text(
        mobility_trends_UK_standardised[line, 0] + 0.1,
        mobility_trends_UK_standardised[
            line, 4
        ],  # where the labels should be positioned
        mobility_trends_UK_mean_NaNdrop.index[
            line
        ],  # add labels to each data point iteratively
        horizontalalignment="left",
        size="small",
        color="black",
        weight=None,
    )

# Add title 'Cluster' to the legend and locate it in the upper right of the plot
plt.legend(title="Cluster", loc="upper right");

# Related approaches: Hierarchical clustering
Other clustering approaches include hierarchical clustering. Below is a heatmap resulting from an application of hierarchical clustering on the mobility trends data at the UK county level. See the `clustermap` function in `seaborn` for details about parameters and possible arguments. We set `z_score = 1`, meaning that data will be standardised (z-scores) on the columns. We also specify a color map `cmap = 'vlag'`, which is a kind of mapping from data values to color space. 

The heatmap displays similarities between mobility categories (columns) and counties in the UK (rows). 

# Hierarchically-clustered heatmap

# Decrease font size to fit all county labels
sns.set(font_scale=1)

sns.clustermap(
    mobility_trends_UK_mean_NaNdrop.iloc[:, 0:6],
    z_score=1,
    cmap="vlag",
    figsize=(12, 40),
)

# Hands-on exercise
You would like to know whether mobility trends in the UK over the last year of the pandemic were similar to the mobility trends in some other countries, and to which countries in particular.

To learn this, you use k-means clustering to group world countries in the COVID-19 Community Mobility Reports data set according to their mobility across mobility categories.

Write your Python code and Markdown below.

Below is a solution to the hands-on exercise.

# Compute mean mobility trends by country and remove NaN (Not a Number) values
mobility_trends_countries = (
    mobility_trends.groupby("country_region")[
        [
            "Retail_Recreation",
            "Grocery_Pharmacy",
            "Parks",
            "Transit_stations",
            "Workplaces",
            "Residential",
        ]
    ]
    .mean()
    .dropna()
)
mobility_trends_countries.head()

# Data standardisation
scaler = StandardScaler()
StandardisedData = scaler.fit_transform(mobility_trends_countries)
StandardisedData

# Run PCA with two components
pca_countries = PCA(n_components=2)
pca_countries = pca_countries.fit_transform(StandardisedData)
pca_countries

# Select optimal number of clusters, k

Sum_of_squared_differences_countries = []

K = range(1, 31)
for k in K:
    kmeans_countries = KMeans(n_clusters=k)
    kmeans_countries.fit(pca_countries)
    Sum_of_squared_differences_countries.append(kmeans_countries.inertia_)

Sum_of_squared_differences_countries

# Plot the number of clusters against the sum of squared differences

# Plot and font size
plt.figure(figsize=(11.7, 8.27))
sns.set(font_scale=1.5)

# Generate the plot
grid = sns.lineplot(x=K, y=Sum_of_squared_differences_countries)

# Add x and y labels
labels = grid.set(xlabel="Number of clusters, k", ylabel="Total squared distances")

# k = 4 appears optimal so we specify n_clusters=4  and run the KMeans algorithm
kmeans_countries_k4 = KMeans(n_clusters=4)
kmeans_countries_k4.fit(pca_countries)

# Labels of clusters each country belongs to
kmeans_countries_k4.labels_

# Plot the clusters along the two principal components

sns.set(font_scale=1.3)
plt.figure(figsize=(20.7, 16.27))

grid = sns.scatterplot(
    x=pca_countries[:, 0], y=pca_countries[:, 1], hue=kmeans_countries_k4.labels_
)

for label in range(0, mobility_trends_countries.shape[0]):
    grid.text(
        pca_countries[label, 0],
        pca_countries[label, 1],
        mobility_trends_countries.index[label],
    )

# Add the cluster membership as a new column
mobility_trends_countries["clusters_countries_k4"] = kmeans_countries_k4.labels_
mobility_trends_countries

# Check in which cluster the United Kingdom was assigned
UK_cluster = mobility_trends_countries[
    mobility_trends_countries.index == "United Kingdom"
]
UK_cluster

# Access the UK cluster label
UK_cluster.clusters_countries_k4[0]

# Identify which other countries were assigned to the same cluster as
# the United Kingdom. These countries were found to be similar to
# the United Kingdom in terms of mobility trends since mid-February 2020.
mobility_trends_countries[
    mobility_trends_countries.clusters_countries_k4
    == UK_cluster.clusters_countries_k4[0]
]