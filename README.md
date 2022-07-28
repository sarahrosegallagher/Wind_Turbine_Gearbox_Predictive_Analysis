# Wind Turbine Reliability Analysis

## Background

This analysis explores wind turbine sensor data via machine learning with the goal to decrease cost and increase reliability. The intent is to build a machine learning algorithm to predict wind turbine failure. With high repair costs for catastrophic failures, predicting these failures would lead to a much lower cost in maintenance. Preventative maintenance is an ongoing question in the field and this analysis takes several approaches to investigate the problem. 

#### Data source description

Real time monitoring data for 4 wind turbines on 59 features over two years. Measurements averaged and recorded every 10 minutes, totaling 200k records. 

#### Questions we hope to answer with data 

Can we predict wind turbine major failures with sensor data? How do different machine learning models solve or fail to solve this problem?

Which features from the sensor data are most correlated with major failures?


## Models 

### Progressive Machine Learning Model Tests
* Logistic Regression 

* Support Vector Machine

* Random Forest

* Oversampling with SMOTE

  * Logistic Regression
  * Random Forest
  
* Neural Network

#### Results 
The most successful model was the Random Forest, with 6 out of 7 major faults correctly predicted (true positives) and 8,000 "false alarms" (false positives).  


### Time Binning Approach (Balanced Random Forest)
This approach addressed the imbalanced dataset by binning the sensor data by time, classifying each measurement based on whether or not there would be a failure in the next bin. The supervised model then attempted to predict if a turbine will experience a major failure in the next time period. 

#### Results 
This model had overall high recall and low precision, indicating that the model included many "false alarms" but that it correctly predicted a high percentage of the actual faults. 



### Minor Faults to Predict Major Faults (Balanced Random Forest) 
This approach sought to determine if we could use minor faults to predict major faults, rather than using the sensor data to predict major faults. 

#### Results 
The precision and recall for this model were similar, at 69% for precision and 70% for recall. 
       
