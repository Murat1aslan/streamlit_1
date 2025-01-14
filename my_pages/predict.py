import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt
from joblib import load
from datetime import date, datetime

# Sayfa Ayarları
st.set_page_config(page_title="Kanser Tahmin", page_icon="images/icon1.png", layout="wide")

# Başlık
st.title("Bilgileri Doldurunuz")
st.markdown("**Kanser Riski** tahmin sonucunuzu görmek için lütfen aşağıdaki bilgileri eksiksiz giriniz!")

# Kullanıcıdan Girdiler
name = st.text_input("Ad")
surname = st.text_input("Soyad")
Gender = st.selectbox("Cinsiyet", ['Kadın', 'Erkek'], index=1)
Air_Pollution = st.slider("Hava Kirliliği", 0, 8)
Genetic_Risk = st.slider("Genetik Risk", 0, 7)
chronic_Lung_Disease = st.slider("Kronik Akciğer Hastalığı", 0, 7)
Balanced_Diet = st.slider("Dengeli Beslenme", 0, 7)
Obesity = st.slider("Obezite", 0, 7)
Smoking = st.slider("Sigara Kullanımı", 0, 8)
Chest_Pain = st.slider("Göğüs Ağrısı", 0, 9)
Coughing_of_Blood = st.slider("Kanlı Öksürük", 0, 9)
Weight_Loss = st.slider("Kilo Kaybı", 0, 8)
Shortness_of_Breath = st.slider("Nefes Darlığı", 0, 9)
Swallowing_Difficulty = st.slider("Yutma Güçlüğü", 0, 8)
Dry_Cough = st.slider("Kuru Öksürük", 0, 7)

# Modelin Yüklenmesi
ridge_classifier_model = load("model2.pkl")

# Cinsiyet dönüşümü
Gender = 2 if Gender == "Erkek" else 1

# Veri çerçevesi oluşturma
input_df = pd.DataFrame({
    "Gender": [Gender],
    "Air Pollution": [Air_Pollution],
    "Genetic Risk": [Genetic_Risk],
    "chronic Lung Disease": [chronic_Lung_Disease],
    "Balanced Diet": [Balanced_Diet],
    "Obesity": [Obesity],
    "Smoking": [Smoking],
    "Chest Pain": [Chest_Pain],
    "Coughing of Blood": [Coughing_of_Blood],
    "Weight Loss": [Weight_Loss],
    "Shortness of Breath": [Shortness_of_Breath],
    "Swallowing Difficulty": [Swallowing_Difficulty],
    "Dry Cough": [Dry_Cough]
})

# Tahmin yapma
online_pred = ridge_classifier_model.predict(input_df)

# Sonuçlar Ekranı
if st.button("Sonuçları Gör"):
    st.info("Sonuçlar aşağıda görüntülenmektedir.")
    today = date.today()
    time = datetime.now().strftime("%H:%M:%S")

    # Sonuç DataFrame'ini oluşturma
    result = 'Riskli' if online_pred[0] == 1 else 'Düşük Risk'
    online_results_df = pd.DataFrame({
        'Ad': [name],
        'Soyad': [surname],
        "Tarih": [today],
        "Saat": [time],
        "Sonuç": result
    })

    # **Sonuç metnini özelleştirme (Büyük ve Koyu)**:
    st.markdown(
        f"<h3 style='color: black; font-size: 24px; font-weight: bold;'>Sonuç: {result}</h3>", 
        unsafe_allow_html=True
    )

    st.dataframe(online_results_df)

     # **Özelliklerin Kanser Riski Üzerindeki Etkisini Gösterme**:
    # Katsayılar ve girilen verileri alıyoruz
    coefficients = ridge_classifier_model.coef_[0]  # Katsayılar
    feature_names = input_df.columns  # Özellik isimleri
    input_values = input_df.iloc[0].values  # Kullanıcıdan alınan veriler

    # Özelliklerin kanser riski üzerindeki etkisini hesaplayacağız
    effects = coefficients * input_values  # Etkiler (katsayılar * kullanıcı verisi)

    # Etkilerin mutlak değerini alıyoruz
    abs_effects = abs(effects)

    # Etkilerin toplamını hesaplayalım
    total_effect = sum(abs_effects)

    # Eşik değeri belirleyelim (örneğin %5'lik etkiyi alt sınır olarak kabul edelim)
    threshold_percentage = 0.05 * total_effect  # %5 etkiden küçük olanları "Diğer"de gösterelim

    # Etkisi düşük olanları "Diğer" olarak gruplamak için etki değerlerine bakıyoruz
    grouped_effects = []
    other_effect = 0
    grouped_labels = []

    # Türkçeleştirilmiş özellik isimleri
    turkish_labels = {
        "Gender": "Cinsiyet",
        "Air Pollution": "Hava Kirliliği",
        "Genetic Risk": "Genetik Risk",
        "chronic Lung Disease": "Kronik Akciğer Hastalığı",
        "Balanced Diet": "Dengeli Beslenme",
        "Obesity": "Obezite",
        "Smoking": "Sigara Kullanımı",
        "Chest Pain": "Göğüs Ağrısı",
        "Coughing of Blood": "Kanlı Öksürük",
        "Weight Loss": "Kilo Kaybı",
        "Shortness of Breath": "Nefes Darlığı",
        "Swallowing Difficulty": "Yutma Güçlüğü",
        "Dry Cough": "Kuru Öksürük"
    }

    for i, effect in enumerate(abs_effects):
        if effect < threshold_percentage:
            other_effect += effect  # Küçük etkileri topluyoruz
        else:
            grouped_effects.append(effect)  # Büyük etkileri ayrı tutuyoruz
            grouped_labels.append(turkish_labels[feature_names[i]])

    # Eğer bir "Diğer" kategorisi varsa, bunu listeye ekleyelim
    if other_effect > 0:
        grouped_effects.append(other_effect)
        grouped_labels.append("Diğer")

    # Pasta grafiği için etiket ve değerler
    fig, ax = plt.subplots(figsize=(5, 4), dpi=100)

    # Pasta grafiğini oluşturuyoruz
    ax.pie(grouped_effects, labels=grouped_labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.set_title('Girilen Bilgilerin Kanser Tahmin Sonucuna Etkileri')

    # Grafiği streamlit'te göster
    st.pyplot(fig)

else:
    st.markdown("Sonuçları görüntülemek için lütfen butona *tıklayınız*.")
