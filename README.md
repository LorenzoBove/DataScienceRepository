# DataScienceRepository
Repository with Python Machine Learning and Deep Learning Classification Methods.



The Repository contains a set of different Classifiers:
Logistic Regression, SVM, Random Forest, KNN, LSTM Neural Networks and CNN neural networks.
The input file for the classification is test.csv.
In order to use the programs You will need to start form Start.py which will initialize a virtual environment,
install all the requirements and then ask you which classifier to use.

You can customize the Repository by changing the input data contained in test.csv.
Please make sure the class column in the new csv it's the last one.
In case you want to change the file name, You need to change the path in Methods.py

```
path='test.csv'
```

the feature extraction part is contained in Methods.py and
all methods take input train and test data sets obtained with train_test_split by scikit learn.


# Usage

In order to use the Repository, please make sure to have python3 installed.

Open your local directory and run 

```
python3 Start.py
```

In case this does not work please run

```
which python3
```
and use the output to run Start.py

example

```
/usr/bin/python3 Start.py
```







