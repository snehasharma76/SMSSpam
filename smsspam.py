# -*- coding: utf-8 -*-
"""SMSSpam.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17omDXfqgBgT4nUsKXgRan64WRLZSQXE-

##Import Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""##Import Dataset"""

dataset = pd.read_csv('SMSSpamCollection.tsv', delimiter = '\t', quoting = 3 , header = None)

"""##Cleaning Text"""

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 5574):
  review = re.sub('[^a-zA-Z]', ' ' , dataset[1][i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  review = [ps.stem(w) for w in review if not w in set( all_stopwords)]
  review = ' '.join(review)
  corpus.append(review)

print(corpus)

"""## Creating the Bag of Words model"""

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 6000)
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[: , 0].values

print(x)

len(x[0])

"""##Encoding Data"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

"""##Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)

print(x_test)

"""##Training the Naive Bayes model on the Training set"""

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)

"""##Predicting the Test set results"""

y_pred = classifier.predict(x_test)

"""##Making the Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)