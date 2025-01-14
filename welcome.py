import streamlit as st

my_pages = st.navigation({
    "------------------------------------------------------------": [
        st.Page("my_pages/project.py", title="Özet", icon="💻"),
    ],
    "-------------------------------------------------------------": [
        st.Page("my_pages/predict.py", title="Kanser Riski Tahmin", icon="🔬")
    ],
})
my_pages.run()