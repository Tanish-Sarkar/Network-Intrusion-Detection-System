# Anomaly Detection & Clustering in High-Dimensional Data

## Overview

In real-world data, patterns often hide in complex, high-dimensional spaces. Detecting those patterns — or deviations from them — is crucial for everything from **fraud detection** and **network security** to **market segmentation** and **fault monitoring**.

This project explores the power of **unsupervised learning** to:

* Discover natural groupings in unlabeled data using clustering techniques
* Identify unusual data points through anomaly detection
* Reduce dimensional complexity with advanced reduction techniques like PCA, t-SNE, and UMAP

---

## Why This Project Matters

Unlike supervised learning, where labeled data is readily available, most real-world datasets are **unlabeled**. Unsupervised techniques allow us to extract insights without explicit labels. This is invaluable in domains like:

* **Cybersecurity:** Detecting outliers that could indicate intrusions
* **Finance:** Spotting irregular transactions
* **Healthcare:** Identifying rare diseases or patient clusters
* **Marketing:** Segmenting customers for targeted campaigns

With the growing scale and complexity of data, it's becoming essential to combine **clustering**, **dimensionality reduction**, and **anomaly detection** to make data interpretable and actionable.

---

## Why I Took On This Project

This project challenged me to:

* Think beyond labels and ground-truth answers
* Work with high-dimensional and noisy data
* Explore real-world strategies to simplify and make sense of complex datasets

It helped sharpen my understanding of:

* Clustering algorithms like K-Means, DBSCAN, and Hierarchical Clustering
* Dimensionality reduction tools like PCA, UMAP, and t-SNE
* Anomaly detection models such as Isolation Forest and LOF

---

## Project Highlights

* **Dimensionality Reduction** for visualization and computational efficiency
* **Clustering Analysis** to reveal patterns and groupings
* **Anomaly Detection** to catch rare and suspicious data points
* Clean, modular codebase built with scalability and reproducibility in mind

---

## Dataset

This project uses a high-dimensional, unlabeled dataset to simulate a real-world use case where we must uncover structure and detect outliers — all without labels.

---

## Outcome

This project deepened my understanding of the **core unsupervised learning toolkit** and showed how it can be applied in **security, business intelligence, and operations**. It was also a stepping stone toward more advanced topics like **representation learning and generative models**.
* Visual clustering of normal vs abnormal traffic
* Detection of unknown intrusions using unsupervised methods
* Insights into high-risk traffic patterns via dimensionality plots
* Evaluation using labeled attack data (optional final step)

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


## 🚀 Future Scope

* Deploy real-time intrusion detection via streaming data
* Combine with supervised models for semi-supervised learning
* Integrate with dashboards for network monitoring

---

## 🙌 Acknowledgments

* **UNSW-NB15 Dataset** – [Australian Centre for Cyber Security](https://www.unsw.adfa.edu.au/australian-centre-for-cyber-security/cybersecurity/ADFA-NB15-Datasets/)
* Libraries: Scikit-learn, Seaborn, Plotly, Pandas, NumPy

---

