import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Amazon Music Clustering",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("Amazon Music Clustering")
st.subheader("Music Analytics")

st.sidebar.title("Download Options 📥 ")


original_df=pd.read_csv(r"/Users/suriya/Ukesh_AIML_Projects/Amazon Music Clustering/Data/single_genre_artists.csv")
dataset=original_df.to_csv(index=False)
st.sidebar.download_button(
    label="Original Dataset",
    data=dataset,
    file_name="single_genre_artists.csv",
    mime="text/csv",
    use_container_width=True
)

clustered_df=pd.read_csv(r"/Users/suriya/Ukesh_AIML_Projects/Amazon Music Clustering/Data/Amazon_Music_Clustering.csv")
dataset=clustered_df.to_csv(index=False)
st.sidebar.download_button(
    label="Clustered Dataset",
    data=dataset,
    file_name="Amazon_Music.csv",
    mime="text/csv",
    use_container_width=True
)

tab1,tab2=st.tabs(["Clustering",'Visualization'])


with tab1:
    
    csv_df=pd.read_csv(r"/Users/suriya/Ukesh_AIML_Projects/Amazon Music Clustering/Data/Amazon_Music_Clustering.csv")
    
    st.dataframe(csv_df,use_container_width=True)


with tab2:
    
    st.markdown("""***Cluster 0 :*** *Acoustic and Calm Tracks* , 
                ***Cluster 1 :*** *Energetic Tracks* , 
                ***Cluster 2 :*** *Speech Oriented Tracks*""")
    
    result_df=pd.read_csv(r"/Users/suriya/Ukesh_AIML_Projects/Amazon Music Clustering/Data/PCA_Result.csv")
    
    fig,ax=plt.subplots(figsize=(10,6))

    sns.scatterplot(
        data=result_df,
        x="PC1",
        y="PC2",
        hue="Cluster",
        ax=ax)

    st.pyplot(fig)
    
    cluster_0=pd.read_csv(r"/Users/suriya/Ukesh_AIML_Projects/Amazon Music Clustering/Data/Acoustic and Calm Tracks.csv")
    
    st.sidebar.download_button(
    label="Acoustic and Calm Tracks Dataset",
    data=dataset,
    file_name="Amazon_Music_Acoustic_Calm_Tracks.csv",
    mime="text/csv",
    use_container_width=True
    )
    
    cluster_1=pd.read_csv(r"/Users/suriya/Ukesh_AIML_Projects/Amazon Music Clustering/Data/Energetic Tracks.csv")       
    st.sidebar.download_button(
    label="Energetic Tracks Dataset",
    data=dataset,
    file_name="Amazon_Music_Energetic_Tracks.csv",
    mime="text/csv",
    use_container_width=True
    )
    
    cluster_2=pd.read_csv(r"/Users/suriya/Ukesh_AIML_Projects/Amazon Music Clustering/Data/Speech Oriented Tracks.csv")
    st.sidebar.download_button(
    label="Speech Oriented Tracks Dataset",
    data=dataset,
    file_name="Amazon_Music_Speech_Oriented_Tracks.csv",
    mime="text/csv",
    use_container_width=True
    )
    


