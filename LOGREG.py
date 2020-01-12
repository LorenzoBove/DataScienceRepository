from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import  GridSearchCV
from sklearn.metrics import accuracy_score,log_loss


def LRclassification(X_train,X_test,Y_train,Y_test):
    print("-----------------------------------LOGISTIC REGRESSION-----------------------------------")
    param_grid ={
    "C":[0.001,0.01,0.1,0.2],
    "penalty" : ['l1', 'l2', 'elasticnet'],
    "solver" :['newton-cg', 'lbfgs', 'saga'] ,
        "l1_ratio" : [0.0001,0.001,0.01,0.1]}
       # "multi_class": ['ovr','multinomial'] this only for multiclass
    lr=LogisticRegression()
    gs=GridSearchCV(lr, param_grid,cv=10,error_score=0.0)
    gs.fit(X_train,Y_train)


    print("Best Model Parameters:", gs.best_params_)
    print("Best Model Accuracy= " , gs.best_score_)

    lr = gs.best_estimator_
    lr.fit(X_train,Y_train)
    Y_pred=lr.predict(X_test)
    Y_pred_train=lr.predict(X_train)
    Y_pred_proba=lr.predict_proba(X_test)
    Y_pred_proba_train=lr.predict_proba(X_train)
    PAR=lr.coef_

    print('Log_loss= ',log_loss(Y_test,Y_pred_proba))
    print('Log_loss_train= ',log_loss(Y_train,Y_pred_proba_train))
    print('Coefficients for the Linear Combination= ',PAR)
    return accuracy_score(Y_test,Y_pred),accuracy_score(Y_train,Y_pred_train)