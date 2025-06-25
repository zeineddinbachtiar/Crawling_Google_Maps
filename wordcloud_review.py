
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Baca file CSV
df = pd.read_csv(r"D:\KULIAH\SEMESTER\BIG DATA\New folder\crawl_and_train\dataset\review.csv")  # Ganti nama file sesuai kebutuhan
reviews = df['review'].astype(str)

# Gabungkan semua review jadi satu string dan ubah ke huruf kecil
text = ' '.join(reviews).lower()

# Buat Word Cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(text)

# Tampilkan Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud Review", fontsize=16)
plt.show()
