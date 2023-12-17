import streamlit as st
import joblib
import numpy as np

# Modeli yükleme
def load_model():
    # Model dosyasının yolunu doğru bir şekilde belirtin
    model = joblib.load("random_forest_model.pkl")
    return model

# Ana sayfa gösterimi
def show_home():
    st.title('Random Forest Modeli ile Bilgisayar Fiyat Tahmini')
    st.write('Bu uygulama, bir bilgisayarın özelliklerine göre fiyatını tahmin etmek için Random Forest modelini kullanır.')

# Tahmin yapma sayfası
def show_prediction_page(model):
    st.title('Bilgisayar Fiyat Tahmini')

    # Kullanıcıdan özellikleri alma
    os_options = {'Windows': 1, 'MacOS': 2, 'Linux': 3, 'FreeDos': 4}
    cpu_options = {'Intel': 1, 'AMD': 2, 'Apple/M1/M2/M3': 3}
    gpu_options = {'Intel': 1, 'NVIDIA': 2, 'AMD': 3, 'Apple/M': 4, 'Dahili': 5}

    selected_os = st.selectbox('İşletim Sistemi', list(os_options.keys()))
    selected_cpu = st.selectbox('İşlemci Tipi', list(cpu_options.keys()))
    selected_gpu = st.selectbox('Ekran Kartı', list(gpu_options.keys()))
    ram = st.slider('RAM (GB)', 1, 64, 8)
    ssd_kapasitesi = st.slider('SSD Kapasitesi (GB)', 128, 2048, 256)
    ekran_boyutu = st.slider('Ekran Boyutu (inç)', 10.0, 20.0, 15.6)
    cozunurluk_genislik = st.number_input('Çözünürlük Genişlik (px)', min_value=800, max_value=4000, value=1920)
    cozunurluk_yukseklik = st.number_input('Çözünürlük Yükseklik (px)', min_value=600, max_value=3000, value=1080)

    # Tahmin butonu
    if st.button('Fiyat Tahmini Yap'):
        features = np.array([[os_options[selected_os], cpu_options[selected_cpu],
                              gpu_options[selected_gpu], ram, ssd_kapasitesi,
                              ekran_boyutu, cozunurluk_genislik, cozunurluk_yukseklik]])
        prediction = model.predict(features)
        st.success(f'Tahmini Fiyat: {prediction[0]:.2f} TL')
# Uygulamanın ana fonksiyonu
def main():
    model = load_model()

    st.sidebar.title('Navigasyon')
    selected_page = st.sidebar.selectbox('Sayfayı Seçin', ["Ana Sayfa", "Fiyat Tahmini Yap"])

    if selected_page == "Ana Sayfa":
        show_home()
    elif selected_page == "Fiyat Tahmini Yap":
        show_prediction_page(model)

if __name__ == "__main__":
    main()
