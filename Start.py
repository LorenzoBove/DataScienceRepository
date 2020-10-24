import os
import Methods
import subprocess


os.system("pip install virtualenv ")
result = subprocess.check_output("which python3", shell=True)
result=str(result)[2:-3]
os.system("clear")

print("\n\n\n")
os.system("virtualenv -p "+result+" ./_venv")
os.system("source ./_venv/bin/activate ")
os.system("pip3 install -r requirements.txt")
os.system("clear")


a=int(input("Which Method You want to use?\n\nEnter:\n0)Logistic Regression (with Grid Search)"
            "\n1)SVM (with Grid Search)\n"
            "2)Random Forest (with Grid Search)\n3)Convolutional Neural Networks\n"
            "4)LSTM Neural Networks\n"
            "5)KNN (with Grid Search)\n6)K-Means Clustering\n\n"))
print('\n\n')


Methods.inputfunction(a)
