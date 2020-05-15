<p align="center">
  <img src="https://github.com/phamc4/Colorectal-Cancer-Classification/blob/master/images/CCC_Header.png"></img>


## Table of Contents

- [Basic Overview](#basic-overview)
- [Background](#background)
- [Exploring Data](#exploring-data)
  - [Initial Intake](#initial-intake)
- [Predictive Modeling](#predictive-modeling)
  - [Baseline](#baseline)
  - [Evaluation](#evaluation)
  - [Tuning](#tuning)
- [Performance](#performance)
- [Future Considerations](#future-considerations)

## Basic Overview

Colorectal cancer is the third leading cause of cancer-related death worldwide. 
Microarray technology provides a promising approach of exploiting gene profiles for cancer diagnosis and may help in early diagnosis to treat the disease effectively. 
This study will seek to predict colorectal cancer from microarray data by using machine learning models.

## Background

Genes control how our cells work by coding for proteins. The thousands of proteins in each cell have specific functions and act as messengers for the cell. 
In all types of cancer, some of the body's cells begin to divide uncontrollably due to mutations in our genes and spread into surrounding tissues.
Many genes contributing to cancer development fall into broad categories:

-<b>Tumor suppressor genes.</b> These are protective genes that monitor how quickly a cell divides into new cells and controls when a cell dies. When a tumor suppressor gene mutates, cells grow uncontrollably and may eventually for a tumor.

-<b>Proto-oncogenes</b> Under normal circumstances, these genes are involved in cell growth and proliferation or inhibition of apoptosis(cell death). If these genes are mutated the will up regulate the promotion of cellular growth, predisposing the cell to cancer.

A microarray analysis is used to detect and measure the expression of thousands of genes at the same time. By applying machine learning I am looking to see if we can predict or classify new cases of colorectal cancer by gene expression monitoring.


## Exploring Data

<img src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/ncbi_logo.png"></img>

The data was taken from CuMiDa which contains cancer microarray datasets that have been extensively curated from 30,000 studies from the Gene Expression Omnibus. The dataset didn't require much cleaning, mainly just encoding the target variable and dropping a column. However there are columns which only specify the Affymetrix probe Id and not the gene associated with it. This should be addressed when doing logistic regression to determine feature(gene) importance.


**Initial Data**
<img src="https://github.com/phamc4/Colorectal_Cancer_Prediction/blob/master/images/original_data.png"></img>


## Predicitve Modeling

### Baseline

<p>
  <img align="right" src="https://github.com/phamc4/Colorectal_Cancer_Prediction/blob/master/images/target_label_counts.png"></img>
</p>
By looking at the target column, the number of normal and cancer patients are equally distributed. We can establish a naive baseline that doesn't require a model. Simply predicting adenocarcinoma everytime will give us an accuracy of 50%. Let's see if any of the machine learning approaches can be better than the baseline. 

## Evaluation

### PCA

With almost 50,000 features, it was worth considering reducing the dimensionality of the dataset. Let's, first approach this problem with principal component analysis (PCA).

I set a threshold to capture 80% of the explained variance to see how many features were required to meet that threshold.
32 features explained around 80% of the variance! From 50,000 to 32 features.

<img src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/explained_variance.png"></img>

Let's see what the PCA looks like with three principal components and 2 principal components.

<p>
  <img align="left" src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/3d%20PCA.png"></img>
<p>
  <img alight="right" src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/2d%20PCA.png"></img>
</p>


## Random Forest

<img src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/rf_model.png"></img>

Out of the box, random forest performed well! By using a grid search to tune the hyperparameters we can see if we can improve it even further. 

<p>
  <img align="left" src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/rf_model.png"></img>
<p>
  <img alight="right" src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/RF_confusionmatrix.png"></img>
</p>
