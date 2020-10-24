import os
import Methods

os.system("which python3")

a=int(input("Which Method You want to use?\n\nEnter:\n0)Logistic Regression (with Grid Search)"
            "\n1)SVM (with Grid Search)\n"
            "2)Random Forest (with Grid Search)\n3)Convolutional Neural Networks\n"
            "4)LSTM Neural Networks\n"
            "5)KNN (with Grid Search)\n6)K-Means Clustering\n\n"))
print('\n\n')


Methods.inputfunction(a)
