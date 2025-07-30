# 🔐 Network Intrusion Detection System (NIDS)

A comprehensive **unsupervised machine learning project** to detect and understand **network intrusions** using advanced techniques like **clustering**, **dimensionality reduction**, and **anomaly detection**.

---

##  Project Overview

In today’s digital era, cyber-attacks and unauthorized network access are growing threats. The goal of this project is to **analyze network traffic data and identify potential intrusions or malicious behavior** — without relying on labeled attack data.

This project applies powerful **unsupervised learning techniques** to uncover hidden structures and anomalous patterns in network traffic, helping in the early detection of security threats.

---

## Objectives

* Understand patterns in high-dimensional network traffic data
* Group similar behaviors using **clustering algorithms**
* Reduce dimensionality for visualization and performance using **PCA** and **t-SNE**
* Detect outliers (possible intrusions) using **anomaly detection models**
* Evaluate the quality of clusters and flagged anomalies

---

## 🔍 Techniques & Tools

| Component                | Tools / Techniques                           |
| ------------------------ | -------------------------------------------- |
| Data Processing          | Pandas, NumPy, Label Encoding, Scaling       |
| Dimensionality Reduction | PCA, t-SNE, UMAP                             |
| Clustering               | K-Means, DBSCAN, Hierarchical Clustering     |
| Anomaly Detection        | Isolation Forest, Local Outlier Factor (LOF) |
| Evaluation               | Silhouette Score, Visualization              |
| Visualization            | Seaborn, Matplotlib, Plotly                  |
| Project Structure        | Modular Python (with `src/`, `notebooks/`)   |

---

## 🗃️ Dataset

We use **[UNSW-NB15](https://www.kaggle.com/datasets/sampadab17/network-intrusion-detection)** — a widely used network intrusion dataset containing both normal and malicious traffic types.

It includes:

* Features: \~49 network features (flow bytes, packet rates, etc.)
* Labels: Normal / Attack type (used for final evaluation only)

---

## 🧱 Folder Structure

```
network-intrusion-detection/
│
├── data/
│   └── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_eda.ipynb
│   └── 02_clustering.ipynb
│   └── 03_dim_reduction.ipynb
│   └── 04_anomaly_detection.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── dimensionality.py
│   ├── anomaly.py
│   └── utils.py
│
├── outputs/
│   └── plots/
│   └── models/
│
├── requirements.txt
└── main.py
```

---

## 📈 Outcomes

* Visual clustering of normal vs abnormal traffic
* Detection of unknown intrusions using unsupervised methods
* Insights into high-risk traffic patterns via dimensionality plots
* Evaluation using labeled attack data (optional final step)

---

## 🚀 Future Scope

* Deploy real-time intrusion detection via streaming data
* Combine with supervised models for semi-supervised learning
* Integrate with dashboards for network monitoring

---

## 🙌 Acknowledgments

* **UNSW-NB15 Dataset** – [Australian Centre for Cyber Security](https://www.unsw.adfa.edu.au/australian-centre-for-cyber-security/cybersecurity/ADFA-NB15-Datasets/)
* Libraries: Scikit-learn, Seaborn, Plotly, Pandas, NumPy

---

