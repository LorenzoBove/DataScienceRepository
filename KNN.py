from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import  GridSearchCV
from sklearn.metrics import accuracy_score,log_loss





def KNNclassification(X_train,X_test,Y_train,Y_test):
    print("-----------------------------------K NEAREST NEIGHBOR-----------------------------------")
    param_grid ={
        "n_neighbors": [1, 2, 3, 4, 5, 7, 10, 12, 15, 20]
    }

    knn=KNeighborsClassifier()
    gs=GridSearchCV(knn, param_grid,cv=10,error_score=0.0)
    gs.fit(X_train,Y_train)

    print('Best hparameters= ',gs.best_params_)
    print('Best acc= ',gs.best_score_)

    knn=gs.best_estimator_
    knn.fit(X_train,Y_train)
    Y_pred=knn.predict(X_test)
    Y_pred_train=knn.predict(X_train)
    y_prob_train = knn.predict_proba(X_train)
    y_prob_test = knn.predict_proba(X_test)
    return accuracy_score(Y_train,Y_pred_train),accuracy_score(Y_test,Y_pred)

'''
for K in Ks:
    print("K=" + str(K))
    knn = KNeighborsClassifier(n_neighbors=K)
    knn.fit(X_train, Y_train)

    y_pred_train = knn.predict(X_train)
    

    y_pred = knn.predict(X_test)
    y_prob = knn.predict_proba(X_test)

    accuracy_train = accuracy_score(Y_train, y_pred_train)
    accuracy_test = accuracy_score(Y_test, y_pred)

    loss_train = log_loss(Y_train, y_prob_train)
    loss_test = log_loss(Y_test, y_prob)

    print("ACCURACY: TRAIN=%.4f TEST=%.4f" % (accuracy_train, accuracy_test))
    print("LOG LOSS: TRAIN=%.4f TEST=%.4f" % (loss_train, loss_test))
    
'''
