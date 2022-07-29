# Wind Turbine Reliability Analysis

## Background

This analysis explored wind turbine sensor data via machine learning with the goal to decrease cost and increase reliability. The intent was to build a machine learning algorithm to predict wind turbine failure. With high repair costs for catastrophic failures, predicting these failures could lead to triggering maintenece operations that would result in failure prevention at a fraction of the repair cost. Preventative maintenance is an ongoing question in the field and this analysis took several approaches to investigate the problem. 

This repository has an associated Heroku web application: https://wind-turbine-reliability.herokuapp.com/

#### Data source description

Real time monitoring data for 4 wind turbines on 59 features over two years. Measurements averaged and recorded every 10 minutes, totaling 200k records. 

#### Questions we hope to answer with data 

Can we predict wind turbine major failures with sensor data? How do different machine learning models solve or fail to solve this problem?

Which features from the sensor data are most correlated with major failures?


## Models 
The following machine learning models were used to assess the predictability of the sensor data on the fleet of four wind turbines as a whole. 


### Progressive Machine Learning Model Tests
* Logistic Regression 

* Support Vector Machine

* Random Forest

* Oversampling with SMOTE

  * Logistic Regression
  * Random Forest
  
* Neural Network

#### Results 
In general, we believe almost all of the models overfit on the training data. Most models successfully identified no fault states but failed to identify the fault states accurately. The most successful model was the Random Forest, with 6 out of 7 major faults correctly predicted (true positives) in the test set.  However, 8,000 "false alarms" (false positives) were detected in the test set. Several aspects of the data may have contributed to these results. First, the data was severely imbalanced with only 14 labeled faults and over 200,000 no fault states. Second, it was unclear whether all of the features were predictive of faults at all. Future investigations should evaluate the features for actual importance in fault prediction. 


### Time Binning Approach (Balanced Random Forest)
This approach addressed the imbalanced dataset by binning the sensor data by time, classifying each measurement based on whether or not there would be a failure in the next bin. The supervised model then attempted to predict if a turbine will experience a major failure in the next time period. 

#### Results 
This model had overall high recall and low precision, indicating that the model included many "false alarms" but that it correctly predicted a high percentage of the actual faults. 


### Minor Faults to Predict Major Faults (Balanced Random Forest) 
This approach sought to determine if we could use minor faults to predict major faults, rather than using the sensor data to predict major faults. 

#### Results 
The precision and recall for this model were similar, at 69% for precision and 70% for recall. 
       
