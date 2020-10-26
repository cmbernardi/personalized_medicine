# Personalized Medicine: Redefining Cancer Treatment

Kaggle Competition from 2017: https://www.kaggle.com/c/msk-redefining-cancer-treatment/discussion/35336#198462

### Problem Statement
Develop a Machine Learning algorithm that automatically classifies genetic variations that contribute to tumor growth.

##### There are nine different classes a genetic mutation can be classified on:
1. Likely Loss-of-function
2. Likely Gain-of-function
3. Neutral
4. Loss-of-function
5. Likely Neutral
6. Inconclusive
7. Gain-of-function
8. Likely Switch-of-function
9. Switch-of-function

Therefore, the machine learning problem is a Multi Class Classification.

### Performance Metrics
Multi class log-loss
Confusion matrix

### Data
Provides information about the genetic mutations and clinical evidence (text):

- Gene (the gene where this genetic mutation is located)
- Variation (the aminoacid change for this mutations)
- Class (1-9 the class this genetic mutation has been classified on)
- Text (the clinical evidence used to classify the genetic mutation)
