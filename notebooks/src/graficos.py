import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import joblib
from sklearn.cluster import KMeans

def graficos_elbow_silhouette(X, random_state=42, intervalo_k=(2, 11)):
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    
    elbow = {}
    silhouette = []
    
    k_range = range(*intervalo_k)
    
    for i in k_range:
        kmeans = KMeans(n_clusters=i, random_state=random_state, n_init=10)
        kmeans.fit(X)
        elbow[i] = kmeans.inertia_
        labels = kmeans.labels_
        silhouette.append(silhouette_score(X, labels))
    
    sns.lineplot(x=list(elbow.keys()), y=list(elbow.values()), ax=ax[0])
    ax[0].set_xlabel("K")
    ax[0].set_ylabel("Inertia")
    ax[0].set_title("Elbow Method")
    
    sns.lineplot(x=list(k_range), y=silhouette, ax=ax[1])
    ax[1].set_xlabel("K")
    ax[1].set_ylabel("Silhouette")
    ax[1].set_title("Silhouette Method")
    
    plt.show()

def visualizar_clusters(
    dataframe,
    coluna,
    quantidade_cores,
    centroids,
    mostrar_centroids=True,
    mostrar_pontos=False,
    coluna_clusters=None
):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    
    cores = plt.cm.tab10.colors[:4]
    cores = ListedColormap(cores)
    
    x = dataframe[coluna[0]]
    y = dataframe[coluna[1]]
    z = dataframe[coluna[2]]
    
    ligar_centroids = mostrar_centroids
    ligar_pontos = mostrar_pontos
    
    for i, centroid in enumerate(centroids):
        if ligar_centroids:
            ax.scatter(*centroid, s=300, alpha=0.5)
            ax.text(*centroid, f"{i}", fontsize=16, horizontalalignment="center", verticalalignment="center")
    
        if ligar_pontos:
            s = ax.scatter(x, y, z, c=coluna_clusters, cmap=cores)
            ax.legend(*s.legend_elements(), bbox_to_anchor=(1.3, 1))
    
    ax.set_title("Clusters")
    ax.set_xlabel(coluna[0])
    ax.set_xlabel(coluna[1])
    ax.set_ylabel(coluna[2])
    
    plt.show()