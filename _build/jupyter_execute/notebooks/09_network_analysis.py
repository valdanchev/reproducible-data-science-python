# Network analysis with NetworkX

This lab provides an introduction to the study of social networks. Network data and network analysis focus on the _relationships_ between entities, including individuals, organisations, countries, and other entities. In the course so far, the data we have studied were from different sources, including digital, administrative, and survey sources, but with one common feature — these were tabular data. Tabular data is structured into rows, each representing a distinct observation (e.g., individuals, counties) and columns representing observations' attributes. By contrast, in network data we are not primarily interested in the attributes of distinct observations but in the relationships between those observations.

A network is a set of nodes (also called vertices) and a set of edges (also called links) between them. In networks, nodes represent individuals (or other entities, including countries, organisations, and Web pages) and links represent various social ties, including friendship, kinship, acquaintanceship, or hyperlinks.

Network analysis studies the patterns of relationships that emerge from the interaction of individuals or other entities. Such patterns are often described as _network structure_. Network structure can be characterised at different scales: 
* local scale (e.g., nodes, dyads, and triads)
* meso-scale (e.g., network communities)
* macro-scale (e.g., network diameter)

Different metrics and methods have been developed to measure properties of network structure at the local, meso, and macro scales. For example, community detection methods have been developed to study meso-scale network structure. 

The rationale of network analysis is that the position of a node in a network affects relevant social outcomes, for example node importance and performance in a social system. An overview of network analysis can be found in [Wasserman and Faust (1994)](https://books.google.co.uk/books?id=CAm2DpIqRUIC&printsec=frontcover&redir_esc=y#v=onepage&q&f=false) and [Newman (2018)](https://global.oup.com/academic/product/networks-9780198805090?cc=us&lang=en&).

In this lab, we will first create and study a small toy network in order to build an intuition about basic network concepts and diagnostics. We will then study a social network of characters in the movie Star Wars Episode IV: A New Hope.

## Learning resources

<i class="fas fa-scroll"></i> Stephen Borgatti, Ajay Mehra, Daniel Brass, Giuseppe Labianca. 2009. [Network Analysis in the Social Sciences.](https://science.sciencemag.org/content/323/5916/892/tab-pdf) Science.

<i class="fas fa-scroll"></i> Petter Holme, Mason A. Porter, Hiroki Sayama. [Who Is the Most Important Character in Frozen? What Networks Can Tell Us About the World](https://kids.frontiersin.org/articles/10.3389/frym.2019.00099). Frontiers for Young Minds.

<i class="fas fa-play-circle"></i> Mark Newman. [1. The Connected World](https://www.youtube.com/watch?v=yAtsm5xkb5c) and [2. What Networks Can Tell Us About the World](https://www.youtube.com/watch?v=lETt7IcDWLI). Santa Fe Institute.

<i class="fas fa-code"></i> Rob Chew’s and Peter Baumgartner [Connected: A Social Network Analysis Tutorial with NetworkX.](https://www.youtube.com/watch?v=7fsreJMy_pI) PyData 2016. Authors’ Jupyter notebooks are available on [GitHub](https://github.com/rtidatascience/connected-nx-tutorial/tree/master/notebooks).

<i class="fas fa-book"></i> <i class="fas fa-code"></i> Menczer, F., Fortunato, S., Davis, C. 2020. A First Course in Network Science. Cambridge University Press. Authors’ Jupyter notebooks are available on [GitHub](https://github.com/CambridgeUniversityPress/FirstCourseNetworkScience). 

<i class="fas fa-book"></i> <i class="fas fa-code"></i> Edward L. Platt. 2020. Network Science with Python and NetworkX Quick Start Guide: Explore and visualize network data effectively. Packt Publishing. Author’s Jupyter notebooks are available on [GitHub](https://github.com/PacktPublishing/Network-Science-with-Python-and-NetworkX-Quick-Start-Guide).

<i class="fas fa-scroll"></i> Santo Fortunato and Darko Hric. 2016. [Community detection in networks: A user guide.](https://arxiv.org/pdf/1608.00163.pdf). Physics Reports. An open access version of the article is available on the [arXiv](https://arxiv.org/pdf/1608.00163.pdf).

<i class="fas fa-scroll"></i> Mason A. Porter, Jukka-Pekka Onnela, Peter J. Mucha. 2009. [Communities in Networks.](https://www.ams.org/notices/200909/rtx090901082p.pdf) Notices of the AMS.

<i class="fas fa-scroll"></i> Valentin Danchev and Mason A. Porter. 2018. [Neither global nor local: Heterogeneous connectivity in spatial network structures of world migration](https://www.math.ucla.edu/~mason/papers/danchev2018-final-with_supp.pdf). Social Networks.

<i class="fas fa-code"></i> [NetworkX tutorial.](https://networkx.org/documentation/networkx-2.0/tutorial.html)
  
## Networks and COVID-19

<i class="fas fa-scroll"></i> [Mapping the Social Network of Coronavirus](https://www.nytimes.com/2020/03/13/science/coronavirus-social-networks-data.html). New York Times.

<i class="fas fa-scroll"></i> David Holtz et al. [Interdependence and the cost of uncoordinated responses to COVID-19.](https://www.pnas.org/content/117/33/19837) PNAS.

<i class="fas fa-scroll"></i> S. Chang, E. Pierson, P. W. Koh, J. Gerardin, B. Redbird, D. Grusky, J. Leskovec. [Mobility network models of COVID-19 explain inequities and inform reopening.](https://cs.stanford.edu/people/jure/pubs/covid-nature20.pdf) Nature.

# Open network data repositories
* [Network Repository. An Interactive Scientific Network Data Repository.](http://networkrepository.com/index.php)
* [Mark Newman's website](http://www-personal.umich.edu/~mejn/netdata/)
* [Pajek datasets](http://vlado.fmf.uni-lj.si/pub/networks/data/default.htm)
* [Stanford Large Network Dataset Collection](http://snap.stanford.edu/data/index.html)
* [Moviegalaxies—Social networks in movies](https://moviegalaxies.com)

## NetworkX

We will perform network analysis using [NetworkX](https://networkx.org). NetworkX is a Python library for creating, analysing, and visualising networks: 
* written in pure Python
* flexible and easy to install
* relatively scalable


![](https://networkx.org/_static/networkx_logo.svg)

## Other Python libraries for network analysis
* [python-igraph](https://igraph.org/python/)  
    * written in C/C++ with interfaces to Python and R 
    * pros: performance and speed; cons: installation can be a hurdle
* [graph-tool](https://graph-tool.skewed.de)
    * written in C++
    * fast algorithms and powerful visualisations
* [Pymnet](http://www.mkivela.com/pymnet/): Multilayer Networks Library for Python
    * written in Python, based on Matplotlib and integrated with NetworkX 
    * handle multilayer networks: analysis and visualisation

# Network representations

Below are four different representations of a network. Those four different network representations refer to the same set of nodes and the same set of edges connecting those nodes. 

In the network, each person is a _node_. For example, Nancy is a node (ID 3) connected to three other nodes: Emma (ID 2), John (ID 4), and Emily (ID 5). Those three people are _neighbors_ of Nancy. In network terms, Nancy has a _degree_ of three. Similarly, Sophie has two neighbors (i.e., nodes to which Sophie is connected) so we say she has a degree of two.

This is an example of a simple network. Simple networks are characterised as:
* Undirected — edges between each pair of nodes have no direction such that if an edge from node A to node B is present, the edge from B to A is also present. By contrast, in directed networks, edges point to only one direction.
* Unweighted — edges between each pair of nodes are either present or absent. By contrast, in weighted networks, edges have weights assigned to them.

<img src="https://github.com/valdanchev/reproducible-data-science-python/blob/master/images/network_representation_undirected.png?raw=true">

# Import Networkx and other packages we will use

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from scipy.stats.stats import pearsonr

%matplotlib inline

# Creating an undirected network

We begin by creating an empty undirected network using `Graph()` in `networkx` (We already imported `networkx` as `nx`). The created empty network has no nodes and no edges.

# Create an empty network
G = nx.Graph()
# G = nx.DiGraph()  # To create a directed network

Let's add a colection of nodes. 

# Add nodes
G.add_node(1)

# Alternatively, you can add a set of nodes from a list
G.add_nodes_from([2, 3, 4, 5, 6])

Let's now add a collection of edges connecting the nodes. 

# Add edges
G.add_edge(1, 2)
G.add_edge(1, 4)

# Alternatively, you can add a set of edges from a list
G.add_edges_from([(1, 5), (2, 4), (2, 6), (3, 4), (5, 6)])

# Check the created edges
G.edges()

Examine basic properties of the graph using the `info()` function.

# Check basic properties of the graph
print(nx.info(G))

# Draw a network
nx.draw(G, with_labels=True, node_color="#F4ABAA", node_size=600)
plt.savefig("GraphUndirected.png", dpi=600)

# Computing network diagnostics

We compute various network diagnostics, ranging from local (node-level) diagnostics (degree centrality) to global (network-level) diagnostics (e.g., network diameter).

## Node-level diagnostics

**Node degree**

Node degree is simply the number of connections a node has.


# Compute node degree
nx.degree(G)

# Print node degree in a more readable format
for node in G.nodes:
    print(node, nx.degree(G, node))

**Number of triangles**

Number of triangles refers to any three connected nodes that include a node.

# Compute the number of triangles per node
for node in G.nodes:
    print(node, nx.triangles(G, node))

**Clustering** 

Clustering of a node is the fraction of possible triangles (i.e., the number of actual triangles divided by the number of possible triangles).

# Compute the clustering coefficient for nodes
for node in G.nodes:
    print(node, nx.clustering(G, node))

Let's consolidate our code and print the above local network diagnostics in one place

# Multiple network diagnostics
print("node degree triangles clustering")
for node in nx.nodes(G):
    print(node, nx.degree(G, node), nx.triangles(G, node), nx.clustering(G, node))

The above node-level diagnostics consider only direct connections to a node without taking into account the global structure of a network. Let's compute diagnostics that take into account the global structure of our network. 

**Betweenness centrality and shortest paths**

One such diagnostic is _betweenness centrality_. Nodes with high betweenness centrality are thought to connect otherwise disconnected nodes and in this sense to harness coordination and communication flow in social networks.   

How do we compute betweenness centrality? Consider that between any pair of nodes there is a shortest path connected that pair, the betweenness centrality of a node is the sum of the fraction of shortest paths between all pairs that pass through a node.

To make things concrete, let's first compute the shortest paths between a pair of nodes that go through a node. For example, the shortest paths that go through node 1: 2 &rightarrow; 5, 3 &rightarrow; 5, 4 &rightarrow; 5.

# Compute the shortest paths that go through a node
for i in range(2, 5):
    print(list(nx.all_shortest_paths(G, source=i, target=5)))

Let's compute now the betweenness centrality for node 1. 

The shortest paths, which pass through node 1, are between the pairs: 

2 &rightarrow; 5

3 &rightarrow; 5

4 &rightarrow; 5

| Pairs of nodes | Number of shortest paths through node 1 | Number of all shortest paths |
|---| --- | --- |
| 2 &rightarrow; 5 | 1 | 2 |
| 3 &rightarrow; 5 | 1 | 1 |
| 4 &rightarrow; 5 | 1 | 1 |

Betweenness centrality for node 1 is then computed as:

$1/2 + 1/1 + 1/1 = 2.5$

# Compute betweenness centrality
nx.betweenness_centrality(G, normalized=False)

If `normalized = True`, then betweenness centrality of a node is normalised by $((n - 1)(n - 2))/2$. In our example graph: 

$((6 - 1)(6 - 2))/2 = (5 * 4)/2 = 20 / 2 = 10$.

Hence the normalized betweenness centrality of, for example, node 1 is $2.5/10 = 0.25$.

# Compute normalized betweenness centrality
nx.betweenness_centrality(G, normalized=True)

**Eigenvector centrality**

Eigenvector centrality is another diagnostic that considers non-direct connections. If node degree measures the number of connections of a node, eigenvector centrality measures the extent to which those connected to a node are themselves highly connected nodes. Eigenvector centrality is an indicator of the influence of a node in a network. People with high eigenvector centrality in social and information networks are influential because they are connected to others who are themselves highly connected and, thus, can easily reach many other people in the networks.   

# Compute eigenvector centrality
nx.eigenvector_centrality(G)

In our small undirected network, node 1 and node 2 have the highest eigenvector centrality due to their connections to each other and to node 4, each of which has degree of 3 and is therefore highly connected in this network of six nodes.   

## Network-level diagnostics

We now consider network-level diagnostics. 

**Average shortest path**

One diagnostic that characterises the global structure of a network is the average shortest path for the network.

# Compute the average shortest path for the network
nx.average_shortest_path_length(G)

**Network diameter**

Network diameter is another network-level diagnostic. Diameter of a network is the longest of all the path lengths or the maximum distance between nodes in a network. 

nx.algorithms.distance_measures.diameter(G)

# Assortative mixing

Assortativity or assortative mixing (also called homophily) is the preference of nodes with similar attributes to interact between each other. In other words, "similarity breeds connection" [McPherson et al. Am. Soc. Rew.](https://doi.org/10.1146/annurev.soc.27.1.415). To illustrate the tendency for assortative mixing, we first add node attributes. 

## Adding node attributes

# Add gender attribute to existing nodes
G.nodes[1]["gender"] = "female"
G.nodes[2]["gender"] = "female"
G.nodes[3]["gender"] = "male"
G.nodes[4]["gender"] = "male"
G.nodes[5]["gender"] = "female"
G.nodes[6]["gender"] = "female"

# Assign different colour to nodes with different attribute classes
nodes_colors = []
for node in G.nodes:
    if G.nodes[node]["gender"] == "female":
        nodes_colors.append("#40E0D0")
    else:
        nodes_colors.append("#E6E6FA")

# The resulting list of colors for female ('#a5b41f') and male ('#1fb4a5')
nodes_colors

Plot the network with node colours representing gender categories 

nx.draw(G, with_labels=True, node_color=nodes_colors, node_size=600)

# Save the graph
plt.savefig("GraphUndirectedGender.png", dpi=600)

## Measuring assortativity

Let's see if indeed similarity with respect to gender attributes breeds connections in our toy network. Networks in which similar nodes are more likely to connect than dissimilar nodes are called assortative.

# Compute assortativity coefficient
nx.attribute_assortativity_coefficient(G, attribute="gender")

Nodes may be linked because they have similar social attributes but also because they have similar number of links or a similar role in a network. Let's see if nodes with similar node degree are more likely (i.e., degree assortativity) or less likely (i.e., degree disassortativity) to be linked in our example network.

# Assortativity for node degree
nx.degree_assortativity_coefficient(G)

# Creating a directed network

# Create an empty directed network
DG = nx.DiGraph()

# Add nodes
DG.add_nodes_from([1, 2, 3, 4, 5, 6])

# Add edges
DG.add_edges_from([(1, 2), (1, 4), (1, 5), (2, 4), (2, 6), (3, 4), (5, 6)])

# Draw the directed network
nx.draw(DG, with_labels=True, node_color="#FFC0CB", node_size=400)

# Save the graph
plt.savefig("GraphDirected.png", dpi=600)

# Compute out-degree and in-degree
print("node out_degree out_degree")
for node in nx.nodes(DG):
    print(node, DG.out_degree(node), DG.in_degree(node))

# Compute betweenness_centrality
nx.betweenness_centrality(DG, normalized=True)

> #### Discussion: How network diagnostics differ across directed and undirected networks?

# A fun example—Star Wars network

In this section we use a [small weighted network reconstructed from the movie Star Wars Episode IV: A New Hope by Evelina Gabasova](http://evelinag.com/blog/2015/12-15-star-wars-social-network/). The network is also used in the [network analysis' tutorial in R by Alex Hanna, Pablo Barbera, and Dan Cervone](https://cdn.rawgit.com/pablobarbera/data-science-workshop/master/sna/01_networks_intro.html). For interactive social networks of characters in films and series, see the website [Moviegalaxies.com](https://moviegalaxies.com).  

Each node in the Star Wars Episode IV: A New Hope network represents a character and each edge represents the number of times a pair of characters appeared together in a scene of the movie. Edges are undirected and weighted.

We use a version of the edge list file named `star-wars-network.csv` (the file can also be found on this [GitHub repository](https://raw.githubusercontent.com/pablobarbera/data-science-workshop/master/sna/data/star-wars-network-edges.csv) by Pablo Barberá), which we read using the Pandas function `read_csv()`.

StarWars_df = pd.read_csv(
    "https://raw.githubusercontent.com/valdanchev/reproducible-data-science-python/master/data/star-wars-network.csv"
)
StarWars_df.head()

We now create a graph object using the NetworkX function `from_pandas_edgelist()`

GraphStarWars = nx.from_pandas_edgelist(
    StarWars_df, source="source", target="target", edge_attr=True
)

# Check the graph
print(nx.info(GraphStarWars))

# Returns the number of edges in a network
GraphStarWars.size()

# Returns total weight sum
GraphStarWars.size(weight="weight")

# Check the weight of the edge between a pair of nodes
GraphStarWars["C-3PO"]["R2-D2"]["weight"]

# Specify figure size
plt.figure(figsize=(12, 12))

# Compute node position using the default spring_layout
node_position = nx.spring_layout(GraphStarWars)

# Draw the Star Wars Episode IV network
nx.draw(GraphStarWars, node_position, node_color="#F4ABAA", with_labels=True)

# Add edge weights
edge_labels = nx.get_edge_attributes(GraphStarWars, "weight")
nx.draw_networkx_edge_labels(GraphStarWars, node_position, edge_labels=edge_labels)

# Save the graph
plt.savefig("GraphStarWars.png", dpi=600)

# Global network diagnostics

Let's compute the average shortest path to characterise the global structure of the network. Recall that the average shortest path determines the extent to which characters in the Star Wars network are distant from one another.

# Compute the average shortest path for the network
nx.average_shortest_path_length(GraphStarWars)

The other global diagnostic we consider is network diameter. Recall that the diameter of a network is the longest of all the path lengths or the maximum distance between nodes in a network. 

nx.algorithms.distance_measures.diameter(GraphStarWars)

# Meso-scale network diagnostics

To study the meso-scale properties of a network, we identify network communities. Network communities are collection of nodes that are more connected to each other than to other communities compared to a null model. Many community detection methods have been developed to identify community structure in networks. To identify network communities in the Star Wars network, we will use a technique called modularity maximisation. We will maximise modularity using the Louvain community detection heuristics.

# Install and import the Louvain community detection algorithm.
!pip install python-louvain
import community as community_louvain

# Detect the community structure of the graph which
# maximises the modularity using the Louvain heuristices.
partition = community_louvain.best_partition(GraphStarWars, resolution=1)

# Set figure size that is larger than the default
plt.figure(figsize=(10, 10))

nx.draw(
    GraphStarWars,
    with_labels=True,
    pos=nx.spring_layout(GraphStarWars),  # spring_layout is the default layout
    node_color=list(partition.values()),
    cmap=plt.cm.coolwarm,
    node_size=1000,
)

# Save the graph
plt.savefig("GraphStarWars.png", dpi=600)

# Local network diagnostics

# Compute node degree (i.e., the number of edges adjacent to that node)
for node in GraphStarWars.nodes:
    print(node, nx.degree(GraphStarWars, node))

# Sort the node degrees in descending order
GraphStarWars_degrees = nx.degree(GraphStarWars)
sorted(GraphStarWars_degrees, key=lambda x: x[1], reverse=True)

# Plot a histogram for node degrees
degree_values = dict(GraphStarWars_degrees).values()

plt.hist(degree_values, 6)
plt.xlabel("Degree")
plt.ylabel("Number of nodes")
plt.title("Star Wars Episode IV network")

# Compute node strenght (i.e., the sum of the edge weights adjacent to a node)
gsw_weights = nx.degree(GraphStarWars, weight="weight")
sorted(gsw_weights, key=lambda x: x[1], reverse=True)

# Compute the number of triangles
triangles = nx.triangles(GraphStarWars)
sorted(triangles.items(), key=lambda x: x[1], reverse=True)[0:10]

# Compute clustering
clustering = nx.clustering(GraphStarWars)
sorted(clustering.items(), key=lambda x: x[1], reverse=True)[0:10]

# Compute the average shortest path for the network
nx.average_shortest_path_length(GraphStarWars)

# Get the distance from one character (e.g., Luke) to any other character
nx.shortest_path_length(GraphStarWars, "LUKE")

# Get the shortes path between any two characters
nx.shortest_path(GraphStarWars, "LUKE", "DARTH VADER")

# Compute betweenness centrality — unweighted
betweenness = nx.betweenness_centrality(GraphStarWars, normalized=False)
sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[0:10]

# Compute betweenness centrality — weighted
betweenness = nx.betweenness_centrality(
    GraphStarWars, weight="weight", normalized=False
)
sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[0:10]

# Compute eigenvector centrality
eigenvector = nx.eigenvector_centrality(GraphStarWars)
sorted(eigenvector.items(), key=lambda x: x[1], reverse=True)[0:10]

# References
* Menczer, F., Fortunato, S., Davis, C. 2020. [A first course in network science.](https://www.cambridge.org/highereducation/books/first-course-in-network-science/EE22722F27519D8BB1443C7225C57BAF#overview) Cambridge University Press.
* Rob Chew’s and Peter Baumgartner’s tutorial [Connected: A Social Network Analysis Tutorial with NetworkX](https://www.youtube.com/watch?v=7fsreJMy_pI). PyData 2016. 
* Edward L. Platt. 2020. [Network Science with Python and NetworkX Quick Start Guide: Explore and visualize network data effectively](https://github.com/PacktPublishing/Network-Science-with-Python-and-NetworkX-Quick-Start-Guide). Packt Publishing.
* Evelina Gabasova. 2015. [The Star Wars social network](http://evelinag.com/blog/2015/12-15-star-wars-social-network/). 