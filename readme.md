\# Heart Disease Prediction System



\## 📌 Project Overview

Heart disease remains a leading cause of global mortality. This project is a \*\*Machine Learning-based Web Application\*\* designed to predict the likelihood of heart disease in patients based on 14 key medical attributes (e.g., age, cholesterol, blood pressure).



The system uses a \*\*Logistic Regression\*\* model trained on clinical data, achieving an accuracy of \*\*~88.2%\*\*. It is deployed using \*\*Flask\*\*, providing a user-friendly interface for early detection and proactive health management.



\## 🚀 Key Features

\* \*\*Web Interface:\*\* Easy-to-use form for inputting patient data (built with Flask).

\* \*\*Machine Learning Model:\*\* Logistic Regression optimized with SMOTE (Synthetic Minority Over-sampling Technique) to handle data imbalance.

\* \*\*High Accuracy:\*\* Validated with an 88.2% accuracy rate.

\* \*\*Real-time Prediction:\*\* Instant risk assessment (Heart Disease / Healthy).



\## 🛠️ Technology Stack

\* \*\*Language:\*\* Python

\* \*\*Web Framework:\*\* Flask

\* \*\*Data Processing:\*\* Pandas, NumPy

\* \*\*Machine Learning:\*\* Scikit-learn (Logistic Regression, Random Forest, SVM)

\* \*\*Visualization:\*\* Matplotlib, Seaborn



\## 📊 Methodology \& Results

We evaluated three models (Logistic Regression, Random Forest, SVM) and found \*\*Logistic Regression\*\* to be the most effective for this dataset due to its interpretability and performance on linear data.



\### Model Performance (Post-SMOTE)

| Metric | Score |

| :--- | :--- |

| \*\*Accuracy\*\* | \*\*88.2%\*\* |

| Precision | 0.86 |

| Recall | 0.88 |

| F1-Score | 0.87 |



\### Confusion Matrix Insights

On our test set, the model correctly identified:

\* \*\*27\*\* True Positives (Correctly predicted Heart Disease)

\* \*\*23\*\* True Negatives (Correctly predicted Healthy)



\## 📂 Dataset

The model was trained on a dataset containing 303 records with the following key features:

1\.  \*\*Age\*\*

2\.  \*\*Sex\*\*

3\.  \*\*CP\*\* (Chest Pain Type)

4\.  \*\*Trestbps\*\* (Resting Blood Pressure)

5\.  \*\*Chol\*\* (Cholesterol)

6\.  \*\*Fbs\*\* (Fasting Blood Sugar)

7\.  \*\*Restecg\*\* (Resting ECG)

8\.  \*\*Thalach\*\* (Max Heart Rate)

9\.  \*\*Exang\*\* (Exercise Induced Angina)

10\. \*\*Oldpeak\*\* (ST depression)

11\. \*\*Slope\*\* (Slope of peak exercise ST segment)

12\. \*\*Ca\*\* (Number of major vessels)

13\. \*\*Thal\*\* (Thalassemia)



\## ⚙️ How to Run Locally



1\. \*\*Clone the Repository\*\*

&nbsp;  ```bash

&nbsp;  git clone \[https://github.com/YourUsername/Heart-Disease-Prediction.git](https://github.com/YourUsername/Heart-Disease-Prediction.git)

&nbsp;  cd Heart-Disease-Prediction

