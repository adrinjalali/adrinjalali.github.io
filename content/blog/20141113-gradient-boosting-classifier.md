Title: How to Synthesize Data Perfectly Suited for Gradient Boosting Classifier
Date: 2014-11-13
Status: draft

### Background
In cancer therapy, classifying a patient into the right sub-class of the relevant cancer is crucial and in many cases it can be life saving/threatening. Bioinformaticians have been trying to tackle this problem for many years, and have some advances in some areas. But still to this date, there is no reliable computational method for many hard sub-classes. Some difficulties on the way to solve this problem are:

   - Biological processes inside cells are not deterministic and are rather stochastic.
   - The number of parameters to the problem are way more than the number of sample points at hand. If you consider genes as parameters and patients as sample points from the process, the corresponding number will be 20k+ vs a few hundreds or usually even less.
   - Measurements are noisy and in virtually all cases they suffer from batch effects, which is understandable considering complications of library preparation and instrument calibration.

To see why these characteristics of the data makes the problem hard, it is enough to generate a large number of purely random features for small enough number of samples, and randomly label them with two classes. Then take half of the samples, train classifier models on them, and check how they perform on the unseen test data. You will see that they can easily perform with 100% accuracy on the train set, but purely random on the test samples.

These facts all together make it almost impossible to apply methods trained on some data sets to a data set measured at a different time/place, which makes them unreliable.

#### Data Synthesis
Here I will present a method to synthesize data in a binary classification scenario, and I will show how some different methods perform on the synthesized data. 

The data synthesis is based on the assumption that genes work in a network, but for simplicity we assume they work on disjoint sets of networks. We also assume the network works differently in different conditions, i.e. different cancer sub-types in this case. Then we try to find those subsets and infer corresponding Bayesian process from our data. The data synthesis can be summarized as bellow:

=== Infer Bayesian Networks from Data ===
 - Take an arbitrary data set, in this case breast cancer from TCGA database;
 - Cluster features into arbitrary number of clusters;
 - Take some of these clusters, for each cluster `c`:
   * infer a Bayesian network and its parameters from samples of the two classes (our problem is a binary classification), hence having two sets of Bayesian networks for each cluster, i.e. one set for class A and one set for class B. For each Bayesian network in class A, there is a corresponding network in class B having identical set of nodes, but different edges and parameters.

=== Generate Random Samples ===
 - Samples include "discriminating" and "non-discriminating" features. To take a sample from class A (or B), we take a sample from Bayesian networks inferred from class A (or B), and put them together in a vector. For non-discriminating features we simply take a sample from a Gaussian distribution regardless of the class of the sample.
 - Add noise to samples:
   * Randomly choose some of the Bayesian networks and replace their corresponding features with samples from a Gaussian regardless of the class to which the sample belongs, i.e. shutting off a whole network.
   * Randomly choose some of the discriminating features and replace them with a sample from a Gaussian distribution regardless of the class to which the sample belongs, i.e. shutting off parts of the networks.

#### Results
