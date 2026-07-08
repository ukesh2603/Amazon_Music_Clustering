# Amazon Music Clustering

## Project Overview

Music streaming platforms contain millions of songs with diverse audio characteristics. Grouping similar songs based on these characteristics helps improve music recommendation systems, playlist generation and user listening experience.

This project applies **Unsupervised Machine Learning** techniques to cluster songs from the **Amazon Music Dataset** using their audio features. The workflow includes data preprocessing, feature scaling, dimensionality reduction using PCA, K-Means clustering, cluster evaluation, visualization and Streamlit dashboard.

---

## Objectives

- Analyze and preprocess music data.
- Select meaningful audio features for clustering.
- Apply dimensionality reduction using PCA.
- Cluster similar songs using K-Means.
- Evaluate cluster quality using Silhouette Score.
- Interpret clusters based on audio characteristics.
- Build a Streamlit application for visualization and exploration.

---

## Dataset

**Dataset:** `single_genre_artists.csv`

The dataset contains song metadata along with audio features.

### Selected Features

- duration_ms
- danceability
- energy
- loudness
- speechiness
- acousticness
- instrumentalness
- liveness
- valence
- tempo

### Removed Columns

- id_songs
- name_song
- name_artists
- id_artists

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit

---

# Project Workflow

## 1. Data Exploration

- Loaded the dataset
- Checked shape and data types
- Verified missing values
- Checked duplicate records
- Removed unnecessary columns

---

## 2. Feature Selection

The following numerical audio features were selected for clustering:

- Danceability
- Energy
- Loudness
- Speechiness
- Acousticness
- Instrumentalness
- Liveness
- Valence
- Tempo
- Duration

These features represent the rhythm, mood, energy level, instrumentation and overall characteristics of each song.

---

## 3. Data Preprocessing

Since clustering algorithms are distance based, all features were standardized using:

```python
StandardScaler()
```

This ensures every feature contributes equally during clustering.

---

## 4. Dimensionality Reduction

Principal Component Analysis (PCA) was applied to reduce dimensionality before clustering.

```python
PCA(n_components=6)
```

The first six principal components preserve most of the dataset's variance while reducing computational complexity.

---

## 5. Clustering

K-Means clustering was applied on the PCA transformed dataset.

```python
KMeans(n_clusters=3)
```

### Evaluation

**Silhouette Score**

```
0.282
```

The songs were grouped into **three meaningful clusters** based on their audio characteristics.

---

## Cluster Interpretation

### Cluster 0 — Acoustic and Calm Tracks

**Characteristics**

- Low danceability
- Low energy
- High acousticness
- Moderate instrumentalness
- Slower tempo
- Softer songs

**Suitable For**

- Relaxation
- Study music
- Acoustic playlists
- Evening listening

---

### Cluster 1 — Energetic Tracks

**Characteristics**

- High danceability
- High energy
- Loud songs
- Low acousticness
- Positive mood
- Faster tempo

**Suitable For**

- Workout playlists
- Party playlists
- Driving music
- Pop recommendations

---

### Cluster 2 — Speech Oriented Tracks

**Characteristics**

- High speechiness
- High liveness
- Moderate danceability
- Shorter duration
- Slower tempo

**Suitable For**

- Podcasts
- Spoken word
- Live performances
- Interviews

---

# Visualizations

The project includes visualization to understand the clustering results.

- PCA Scatter Plot

---

# Results

- Successfully clustered over **95,000 songs**.
- Reduced feature dimensionality using PCA.
- Identified three distinct music categories.
- Created meaningful cluster profiles.
- Exported clustered dataset for further analysis.
- Built Streamlit dashboard for exploring the results.

---

# Streamlit Dashboard Features

The dashboard provides:

- View Original Dataset
- View Clustered Dataset
- Download Original Dataset
- Download Clustered Dataset
- Download Cluster-wise CSV Files
- PCA Scatter Plot Visualization

---

# Project Structure

```
Amazon_Music_Clustering/
│
├── Data/
│   ├── single_genre_artists.csv
│   ├── Amazon_Music_Clustering.csv
│   ├── PCA_Result.csv
│   ├── Acoustic and Calm Tracks.csv
│   ├── Energetic Tracks.csv
│   └── Speech Oriented Tracks.csv
│
├── Screenshots/
│   ├── Cluster_Result.png

├── app.py
├── Clustering.ipynb
├── Data_Loading_and_Preprocessing.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/Amazon_Music_Clustering.git
```

Navigate to the project

```bash
cd Amazon_Music_Clustering
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# Future Improvements

- Build a content based music recommendation system.
- Deploy the Streamlit application online.
- Integrate Spotify API for real time recommendations.

---

## ⭐ If you found this project useful, please consider giving it a Star on GitHub!
