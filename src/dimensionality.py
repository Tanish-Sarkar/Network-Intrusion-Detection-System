from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap.umap_ as umap

def apply_pca(X, n_components=2):
    model = PCA(n_components=n_components)
    X_pca = model.fit_transform(X)
    return X_pca, model

def apply_tsne(X, n_components=2):
    model = TSNE(n_components=n_components, random_state=42)
    X_tsne = model.fit_transform(X)
    return X_tsne, model

def apply_umap(X, n_components=2):
    reducer = umap.UMAP(n_components=n_components, random_state=42)
    X_umap = reducer.fit_transform(X)
    return X_umap, reducer

