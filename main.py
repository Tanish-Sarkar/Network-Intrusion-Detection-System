from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.anomaly import dbscan_anomaly
from src.clustering import apply_dbscan
from src.dimensionality import apply_tsne
from src.utils import plot_clusters
import os

def main():
    current_dir = os.path.dirname(__file__)  
    file_path = os.path.join(current_dir, './data/raw/Train_data.csv')

    df = load_data(file_path)
    print("✅ Data Loaded Successfully...")
    print(f"Shape: {df.shape}")

    X, y = preprocess_data(df)
    print("✅ Data Preprocessed...")

    # Dimensionality Reduction
    X_tsne, _ = apply_tsne(X)
    print("✅ PCA Completed...")

    # Clustering
    labels_dbscans, _ = apply_dbscan(X)
    plot_clusters(X_tsne, labels_dbscans, "DBSCAN Clustering (t-SNE Projection)")

    # Anomaly Detection
    labels_dbscans, _ = dbscan_anomaly(X)
    plot_clusters(X_tsne, labels_dbscans, "DBSCAN Outliers (t-SNE Projection)")

    

if __name__ == "__main__":
    main()
