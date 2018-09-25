# Random forest
This algo supposedly performs good even without hypter-parameter tuning. This algo can be used for both classification and regression tasks. RF is a supervised learning algorithm, i.e. the trainig data is labeled.

# Table of Contents
1. [How it works](#how-it-works)
2. [Pros and Cons](#pros-and-cons)
3. [Third Example](#third-example)


## How it works
Random forest works by making multiple decision trees and combining them to give a more accurate and stable prediction. Random forests add randomness to the model and try to generate decision trees based on the sampled data.

Random forests are nothing but ensemble of decision trees. When we want to get a prediction out of a Random forest, we take a majority vote of the constituent Decision trees.

### Feature Importance
Random forests contain a number of Decision trees this makes the relative importance of features possible to be calculated. This is calculated by some measure called `impurity`. Will talk on this later if I understand this.

What we look after running the dataset with a random forest and getting the *feature importance* values for each of the feature is to drop those features that have a lower feature importance. This is suggested as the more number of features a model has, more likely it is to suffer from overfitting.

### Important Hypterparameters

  * n_estimators
One of the obvious parameter is the number of decision trees to be generated and `n_estimators` is nothing but the number of trees to be generated. The tradeoff here we look is the increase in computation vs more stable predictions.

  * max_features
This is I think same as the depth of the tree. That is limiting the depth of the tree or in other words, limiting the number of features that a decision tree can decide on.

  * min_sample_leaf
This is tha min no. of leafs that are required to split an internal node, i.e. based on the ans of this feature, the split should have at-least this number of data_points on both side. This is basically used to reduce overfitting by increasing the value of min_sample_leaf.

### Implementational Parameters
  * n_jobs 
  This tells the engine how many processors that it can use.

  * random_state
  Random seed to be used.

## Pros and Cons

  * These types of algorithms are fast to train but slow to predict as the number of trees makes it slow. On the other hand, the more number of trees the more stable is the prediction, but again at the cost of the time it takes to find the predition, given a set of trained trees.

  * This model is really basic and should be the first model one tries to get a idea of the dataset. Also it is difficult to build a bad Random Forest.

  * The importance it assigns to the features is to a great extent accurate.

  * Random Forests are really hard to beat, in terms of accuracy scores. Althogh neural networks are able to beat them, but on the downside, NN require some time to train and also RFs accept different feature types, eg. binary, numerical, categorical.

- Apoorv Agnihotri.

ref - https://towardsdatascience.com/the-random-forest-algorithm-d457d499ffcd