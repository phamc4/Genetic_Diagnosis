<p align="center">
  <img src="https://github.com/phamc4/Colorectal-Cancer-Classification/blob/master/images/CCC_Header.png"></img>


## Table of Contents

- [Basic Overview](#basic-overview)
- [Background](#background)
- [Exploring Data](#exploring-data)
  - [Initial Data](#initial-data)
- [Predictive Modeling](#predictive-modeling)
  - [Baseline](#baseline)
  - [Evaluation](#evaluation)
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


### Initial Data
<img src="https://github.com/phamc4/Colorectal_Cancer_Prediction/blob/master/images/original_data.png"></img>


## Predictive Modeling

### Baseline

<p>
  <img align="right" src="https://github.com/phamc4/Colorectal_Cancer_Prediction/blob/master/images/target_label_counts.png"></img>
</p>
By looking at the target column, the number of normal and cancer patients are equally distributed. We can establish a naive baseline that doesn't require a model. Simply predicting adenocarcinoma everytime will give us an accuracy of 50%. Let's see if any of the machine learning approaches can be better than the baseline. You'll see that all the models performed well on this particular dataset

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


<details>
  <summary>
    Random Forest
  </summary>
  
<img src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/rf_model.png"></img>

Out of the box, random forest performed well! By using a grid search to tune the hyperparameters we can see if we can improve it even further. 

<p>
  <img align="left" src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/grid_serch.png"></img>
<p>
  <img alight="right" src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/RF_confusionmatrix.png"></img>
</p>

</details>
<details>
  <summary>
    Naive Bayes 
  </summary>  
  
  Here we apply a straighforward naive bayes approach. It only had one incorrect classification.
  
  ```python
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_pred = nb_model.predict(X_test)

print('Naive Bayes Accuracy:', round(accuracy_score(y_test, nb_pred), 3))
```

Naive Bayes Accuracy: 0.985

  <p>
  <img src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/NB_confusionmatrix.png"></img>
  </p>
  
  </details>
  
  
<details>
  <summary>
    K Means Clustering 
  </summary>
  
  I also tried an unsupervised clustering approach with k-means. I scaled the data and used PCA to reduce the dimensions to try and diminish the effects of the curse of dimensionality. It's performs similarly to the supervised learning models.
  
```python
kmeans = KMeans(n_clusters=2, init='k-means++')
kmeans.fit(X_train_pca)
km_pred = kmeans.predict(X_test_pca)

print('K Means Clustering Accuracy:\n', round(accuracy_score(y_test, km_pred), 3))
```

  <p>
  <img src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/KMeans_confusionmatrix.png"></img>
  
</details>


### Logistic Regression

To interpret the data easier, I implemented a logistic regression with an L1 or Lasso penalty. Lasso is helpful in sending most of the coefficients here down to zero. Here, it gives us more to work with compared to PCA.

```python
logmodel = LogisticRegression(solver='liblinear', penalty='l1')
logmodel.fit(X_train_scaled, y_train)

log_pred = logmodel.predict(X_test_scaled)
log_loss(y_test, log_pred)
```

Total features: 49,386 
<br>
Selected features: 143
<br>

The features in the original dataset contained the probeset ID. I had to go back where I got the original dataset and write a custom function to match the probeset IDs to geneID. If you are doing this in R, they have a simple package that will do this for you called BiomaRt.
<br>

```python
import GEOparse

def get_geneID(geo_id, gsms_id, gpls_id):
    gse = GEOparse.get_GEO(geo=geo_id, destdir="./")
    
    #Get all GSMS(samples) info:
    gse.phenotype_data
    
    #Use sample name to retrieve corresponding data:
    gse.gsms[gsms_id].table
    
    #PLatform info
    probeset = gse.gpls[gpls_id].table
    columns = probeset.columns
    
    return probeset[['ID', 'GB_LIST', 'Gene Title', 'Gene Symbol']], columns
```
<p>
  <img src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/important_genes.png"></img>
  <p>
  <img src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/logisticregression.png"></img>
 </p>


Gene ID            | GenBank ID| 
:-------------------------:|:-------------------------:|
FOXQ1 | [NM_033260](https://www.ncbi.nlm.nih.gov/nuccore/NM_033260)
ETV4  | [NM_001079675](https://www.ncbi.nlm.nih.gov/nuccore/NM_001079675)
GTF2IRD1 | [NM_005685](https://www.ncbi.nlm.nih.gov/nuccore/NM_005685)
MMP11 | [NM_0059640](https://www.uniprot.org/uniprot/P24347)
CLDN1 | [NM_021101](https://www.ncbi.nlm.nih.gov/nuccore/NM_021101)
ENC1  | [NM_003633](https://www.ncbi.nlm.nih.gov/nuccore/NM_003633)
LPAR1 | [NM_001401](https://www.uniprot.org/uniprot/Q92633)
SLC25A34 | [NM_207348](https://www.ncbi.nlm.nih.gov/nuccore/NM_207348)
SFRP1 | [NM_003012](https://www.ncbi.nlm.nih.gov/nuccore/NM_003012)
BEST4 | [NM_153274](https://www.ncbi.nlm.nih.gov/nuccore/NM_153274)
IL6R  | [NM_000565](https://www.ncbi.nlm.nih.gov/nuccore/NM_000565)

<details>
  <summary>
    Top  40 Important Genes according to model
  </summary>
  
  <p>
  <img src="https://github.com/phamc4/Genetic_Diagnosis/blob/master/images/genelist.png"></img>

</details>

## Future Considerations

All the models performed relatively the same. The logistic regression model provided the most insight and also had the best performance on this dataset. Something to consider is how small the dataset is compared to the many features/genes we were measuring. If we had a larger number of rows we could be more confident in our findings here. 
<br>
Outside of data science realm, diving deeper into the genes that the model proposed to be important could further validate the prediction model. There are endless amounts of studies that can be done to a single gene and they're effects on the body due to upregulation or downregulation of their genes. Having a predictive model to narrow down gene importance can get researchers in the right direction.
