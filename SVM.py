from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score



def SVMclassification(X_train,X_test,Y_train,Y_test):
    print("-----------------------------------SVM-----------------------------------")
    svc=SVC()
    param_grid={"kernel":["linear","rbf","sigmoid","poly"],
    "gamma":["auto",1,0.1],"C":[1,10,100,1000]}
    gs=GridSearchCV(svc,param_grid,cv=10,error_score=0.0)
    gs.fit(X_train,Y_train)
    print('Best hparameters= ',gs.best_params_)
    print('Best acc= ',gs.best_score_)
    RFC=gs.best_estimator_
    RFC.fit(X_train,Y_train)
    Y_pred=RFC.predict(X_test)
    Y_pred_train=RFC.predict(X_train)
    return accuracy_score(Y_test,Y_pred),accuracy_score(Y_train,Y_pred_train)