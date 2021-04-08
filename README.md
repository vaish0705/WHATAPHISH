# WHATAPHISH

# Project Title
WHATAPHISH(https://whataphis.herokuapp.com/)-Phishing url detection website

## PROJECT DESCRIPTION
Phishing is a form of fraud in which the attacker tries to learn sensitive information such as login credentials or account information by sending as a reputable entity or person in email or other communication channels.

The objective of this project is to train machine learning models on the bank related dataset created to predict phishing websites. Both phishing and benign URLs of websites are gathered to form a dataset and from them required URL and website content-based features are extracted.Dataset is stored in the 'phishingurl - Sheet1.csv'(for phishing urls) and 'Copy of benign urls' - Sheet1.csv(for legitimate urls).

The features are extracted and store in the csv file. The working of this can be seen in the 'phishing-url-exrtaction.ipynb' and 'Benign-url-extraction.ipynb'.

Further we have done data preprocessing that is merged two dataframe into one.Than we have split the data into trainig and testing data in 70:30 ratio , than fitted the model and check the accuracy using random forest algorithm.
Random forests for regression and classification are currently among the most widely used machine learning methods.A random forest is essentially a collection of decision trees, where each tree is slightly different from the others. The idea behind random forests is that each tree might do a relatively good job of predicting,

Several antiphishing techniques emerge continuously but phishers come with new technique by breaking all the antiphishing mechanisms. Hence there is a need for efficient mechanism for the prediction of phishing website.

Our app can be used by the users  to differentiate between legitimate or phishing site and to have a smooth online banking experience, building strong customer relationships of trust, reliability and consistency.

## Getting Started

We have used python web framework - Django for connecting the frontend and machine learning model to the server.
# Installing and setting up project on local PC

First activate the virtual environment by changing path to Scripts directory.
cd venv/Scripts
cd  activate

Change path back to original directory (for example, C: \....\WHATAPHISH ) so that we can call manage.py file easily.

pip install -r requirements.txt     
 This will install all the requirements and additional packages used in our project.

After installing the requirements below command will run the server on your local pc.
python manage.py runserver 


