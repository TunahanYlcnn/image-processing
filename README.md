# \# 🖐️ MediaPipe ile Gelişmiş El Takibi ve Parmak Analiz Sistemleri

# 

# Bu depo, OpenCV ve MediaPipe kütüphanelerini kullanarak gerçek zamanlı el takibi (Hand Tracking), eklem tespiti (Landmark Detection) ve parmak sayma algoritmalarını içeren Python projelerini barındırmaktadır. Projeler, Windows 11 Pro ortamında ve Lenovo Gaming PC donanımı üzerinde optimize edilmiştir.

# 

# 

# 

# \## 📁 Proje Modülleri ve Özellikler

# 

# \### 1. Temel El Takip Sistemi (`temel\_el\_takip.py`)

# \* \*\*İşlev:\*\* Kameradan gelen görüntüde eli tespit eder ve 21 temel eklem noktasını (landmark) belirler.

# \* \*\*Görselleştirme:\*\* El eklemlerini ve parmaklar arasındaki bağlantıları (skeleton) anlık olarak çizer.

# 

# \### 2. Akıllı Parmak Sayma ve Analiz (`parmak\_sayma\_v2.py`)

# \* \*\*Gelişmiş Algoritma:\*\* Baş parmak ve diğer parmaklar için farklı morfolojik kontrol mantıkları kullanır.

# \* \*\*Ekran Geri Bildirimleri:\*\* Tespit edilen parmak sayısını ve toplam eklem (landmark) sayısını doğrudan video penceresine yansıtır.

# \* \*\*Doğruluk:\*\* `min\_detection\_confidence=0.7` parametresi ile kararlı bir takip sunar.

# 

# 

# 

# \## 🛠️ Kurulum ve Gereksinimler

# 

# Sisteminizde aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

# 

# ```bash

# pip install opencv-python mediapipe numpy

