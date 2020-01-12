import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

#Per determinare il valore di k possiamo utilizzare l'elbow method,
# che ci dice che il valore da scegliere è quello in cui si osserva il ' \
#cambiamento di velocità nel grafico

def KMEANSclusteringfunction(X):
    sse = {}
    Y = np.array(X['species'])
    LE=LabelEncoder()
    Y=LE.fit_transform(Y)
    X['labeled']=Y
    X=X.drop(['species'],axis=1)

    for k in range(1, 10):
        kmeans = KMeans(init="k-means++", n_clusters=k).fit(X)
        #print(data["clusters"])
        sse[k] = kmeans.inertia_ # Inertia: Sum of distances of samples to their closest cluster center
    plt.figure()
    plt.plot(list(sse.keys()), list(sse.values()),marker='o')
    plt.xlabel("Number of clusters", fontsize=16)
    #somma delle distance al quadrato
    plt.ylabel("Squared sum of distances ", fontsize=16)
    plt.savefig("number_of_k.png")
    plt.show()
    plt.close()
    k=int(input("Insert number of Clusters please =)\n\n"))
    kmeans = KMeans(init="k-means++", n_clusters=k).fit(X)
    y_kmeans = kmeans.predict(X)
    print(X)
    X1=X['sepal_length'].values
    X2=X['petal_length'].values
    plt.scatter(X1, X2, c=y_kmeans, s=50, cmap='viridis')
    plt.show()
    return
