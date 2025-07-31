from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.cluster import DBSCAN

def isolation_forest(X, contamination=0.05):
    model = IsolationForest(contamination=contamination, random_state=42)
    labels = model.fit_predict(X)
    return labels, model

def local_outlier_factor(X, contamination=0.05):
    model = LocalOutlierFactor(n_neighbors=20, contamination=contamination)
    labels = model.fit_predict(X)
    return labels, model

def dbscan_anomaly(X, eps=1.2, min_samples=5):
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(X)
    return labels, model
