from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score





def RFclassification(X_train,X_test,Y_train,Y_test):
    print("-----------------------------------RANDOM FORESTS----------------------------------")
    RFC=RandomForestClassifier()

    param_grid={
    "n_estimators":[10,20,30],
    "max_depth":[5,6,7,8,8,10]


    }
    gs=GridSearchCV(RFC,param_grid,cv=10,error_score=0.0)
    gs.fit(X_train,Y_train)
    print('Best hparameters= ',gs.best_params_)
    print('Best acc= ',gs.best_score_)

    RFC=gs.best_estimator_
    RFC.fit(X_train,Y_train)
    Y_pred=RFC.predict(X_test)
    Y_pred_train=RFC.predict(X_train)
    return accuracy_score(Y_train,Y_pred_train),accuracy_score(Y_test,Y_pred)