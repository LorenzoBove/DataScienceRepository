import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from SVM import SVMclassification
from CNN import CNNclassification
from LSTM import LSTMclassification
from RF  import RFclassification
from LOGREG import LRclassification
from KNN import KNNclassification
from K_MEANS_CLUSTERING import KMEANSclusteringfunction
import numpy as np

def inputfunction(a):


    print('----------------------PREPROCESSING---------------------------------')


    path='test.txt'
    Data=pd.read_csv(path,sep=',')

    print(Data)

    X=Data.drop(['species'],axis=1)
    Y=Data['species'].values
    X=np.array(X)
    LE = LabelEncoder()
    Y=LE.fit_transform(Y)
    MM = MinMaxScaler()
    X = MM.fit_transform(X)





    print('----------------------END OF PREPROCESSING---------------------------')
    #######################################################################
    #####END OF PREPROCESSING (WE HAVE X and Y, so to test the code you only need
    # to change the features X and the target Y)


    ts = float(input("Enter test_size for Train/Test splitting, 0.2 suggested =)\n\n"))


    X_train ,X_test ,Y_train ,Y_test= train_test_split(X ,Y ,test_size=ts ,random_state=0)


    #Y_train=np.array(Y_train)
    #Y_test = np.array(Y_test)
    print('TRAIN/TEST DIMENSIONS')
    print('X_train=' ,X_train.shape)
    print('X_test=' ,X_test.shape)
    print('Y_train=' ,Y_train.shape)
    print('Y_test=' ,Y_test.shape)




    if a== 0:
        accuracy_test, accuracy_train = LRclassification(X_train, X_test, Y_train, Y_test)
        print('Logistic Regression accuracy on the test set is ', accuracy_test)
        print('Logistic Regression accuracy on the train set is ', accuracy_train)
        return

    if a == 1:
        accuracy_test, accuracy_train = SVMclassification(X_train, X_test, Y_train, Y_test)
        print('SVM accuracy on the test set is ', accuracy_test)
        print('SVM accuracy on the train set is ', accuracy_train)
        return

    if a == 2:
        accuracy_test, accuracy_train = RFclassification(X_train, X_test, Y_train, Y_test)
        print('Random Forest accuracy on the test set is ', accuracy_test)
        print('Random Forest accuracy on the train set is ', accuracy_train)
        return

    if a == 3:
        score_test, score_train = CNNclassification(X_train, X_test, Y_train, Y_test)
        print('Convolutional Score on test Set= ', score_test)
        print('Convolutional Score on train Set= ', score_train)
        return
    if a == 4:
        score_test, score_train = LSTMclassification(X_train, X_test, Y_train, Y_test)
        print('LSTM Score on test Set= ', score_test)
        print('LSTM Score on train Set= ', score_train)
        return
    if a == 5:
        score_test, score_train = KNNclassification(X_train, X_test, Y_train, Y_test)
        print('KNN Score on test Set= ', score_test)
        print('KNN Score on train Set= ', score_train)
        return
    if a == 6:
        KMEANSclusteringfunction(Data)
        return
