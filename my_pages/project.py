import streamlit as st

# Sayfa Ayarları
st.set_page_config(
    page_title="Kanser Tahmin Testi",
    page_icon="images/cancer.png",
    layout="wide",
    menu_items={"About": "For More Information\n" + "https://istdatascience.com/"})

# Başlık Ekleme
st.title("Kanseri Bil, Önemse, Korun ve Tanıyı Ertelemeden Erken Harekete Geç!")

st.markdown(" Kanser farkındalığı detaylı bilgiler için [T.C SAĞLIK BAKANLIĞI](https://hsgm.saglik.gov.tr/tr/haberler/4-subat-duenya-kanser-guenue.html?highlight=WyJrYW5zZXIiLCJrYW5zZXJpIiwia2Fuc2VyaW5kZW4iLCJrYW5zZXJpbmUiLCJrYW5zZXJpbmluIiwia2Fuc2VybGVyZGUiLCJrYW5zZXJkZW4iLCJrYW5zZXJlIiwia2Fuc2VyaW4iLCJrYW5zZXJsZSIsImthbnNlcmxlciIsImthbnNlcmxlcmkiLCJrYW5zZXJsZXJpbiIsImthbnNlcmxlcmluZGUiLCJrYW5zZXJsZXJpbmluIiwia2Fuc2VybGVcdTAxNWZtZW1pXHUwMTVmIiwia2Fuc2VyZGUiLCJrYW5zZXJsZXJpbmRlbiIsImthbnNlcm9qZW4iLCJrYW5zZXJpbmkiLCJrYW5zZXJsZXJpbmUiLCJwcmVrYW5zZXJcdTAwZjZ6Iiwia2Fuc2Vyb2plbmxlcmUiLCJ2ZXJlbmthbnNlciIsIlx1MjAxY2thbnNlcmRlbiIsImthbnNlcmxlcmRlbiIsIlx1MjAxY2thbnNlciIsImthbnNlcmxlcmUiLCJrYW5zZXJsaSIsImthbnNlcmluZGUiLCJrYW5zZXJvamVuaWsiLCJtZW1la2Fuc2VyaW5pbiIsImthbnNlcnNpeiIsImthbnNlcmxlcmluaSIsImthbnNlcm9qZW5sZXJpIiwib2t1bGxhcmthbnNlciIsIlx1MjAxY2thbnNlcmkiLCJrYW5zZXJpXHUwMzA3IiwiZmFya1x1MDEzMW5kYWxcdTAxMzFcdTAxMWZcdTAxMzFuXHUwMTMxbiIsImZhcmtcdTAxMzFuZGFsXHUwMTMxXHUwMTFmXHUwMTMxblx1MDEzMSIsImZhcmtcdTAxMzFuZGFsXHUwMTMxXHUwMTFmXHUwMTMxIiwiZmFya1x1MDEzMW5kYWxcdTAxMzFcdTAxMWZcdTAxMzF2ZWhhcmVrZXRpbGlcdTAxNWZraWxlcmluaWt1bGxhbmFyYWsiLCJmYXJrXHUwMTMxbmRhbFx1MDEzMVx1MDExZlx1MDEzMW5hIiwiZmFya1x1MDEzMW5kYWxcdTAxMzFcdTAxMWZcdTAxMzFuIiwiZmFya1x1MDEzMW5kYWxcdTAxMzFcdTAxMWZcdTAxMzFtXHUwMTMxelx1MDEzMSJd), sayfasını ziyaret edebilirsiniz")

# Resim Ekleme
st.image("images/cancer.png")

st.markdown("Yapay Zeka ile makine öğrenmesi modeli geliştirilmiştir. Sizler de **Kanser Riski Tahmin** sayfasından bilgilerinizi girerek, alışkanlıklarınız ile ne oranda kanser riski taşıdığınızı görebilirsiniz.")
st.markdown("Makine öğrenmesi modeli geliştirilirken birçok kişinin gerçek bilgilerinin bulunduğu veri setleri kullanılmıştır.")
st.markdown("*Farkındalık, bir adım daha ileriye gitmek, sağlığınızı korumak ve sevdiklerinize güzel bir gelecek bırakmak için en güçlü adımdır.!*")
