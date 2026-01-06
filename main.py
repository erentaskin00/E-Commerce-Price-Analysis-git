import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt

def get_data():
    url = "https://www.akakce.com/arama/?q=iphone+13"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    products = []

    print("Veri toplanmaya çalışılıyor")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('li', class_='p-w')
        for item in items:
            name = item.find('h3').text.strip()
            price_raw = item.find('span', class_='pt_v8').text.strip()
            products.append({'Product': name, 'Price_Raw': price_raw})
    except:
        pass

    if not products:
        print("\n[BİLGİ] Canlı veriyi çekemedik :(")
        products = [
            {'Product': 'iPhone 13 128GB', 'Price_Raw': '28.499,00 TL'},
            {'Product': 'iPhone 13 256GB', 'Price_Raw': '32.150 TL'},
            {'Product': 'iPhone 13 Mini', 'Price_Raw': '25999.00TL'}, 
            {'Product': 'Ucuz İlan', 'Price_Raw': '1.500 TL'},
            {'Product': 'Pahalı İlan', 'Price_Raw': '145.000 TL'},
            {'Product': 'iPhone 13 Yenilenmiş', 'Price_Raw': '21.000,00 TL'},
            {'Product': 'iPhone 13 512GB', 'Price_Raw': '55.000 TL'}
        ]
    return pd.DataFrame(products)

df = get_data()

def clean_price(price):
    price = str(price).upper().replace('TL', '').replace(' ', '')
    if ',' in price and '.' in price:
        price = price.replace('.', '').replace(',', '.')
    elif ',' in price:
        price = price.replace(',', '.')
    elif '.' in price and len(price.split('.')[-1]) > 2:
        price = price.replace('.', '')
    
    return float(price)

df['Price'] = df['Price_Raw'].apply(clean_price)

Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1
df['Is_Anomaly'] = (df['Price'] < (Q1 - 1.5 * IQR)) | (df['Price'] > (Q3 + 1.5 * IQR))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.boxplot(y=df['Price'], color="cyan")
plt.title('Fiyat Dagilimi (Boxplot)')

plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x=df.index, y='Price', hue='Is_Anomaly', palette={True:'red', False:'blue'}, s=100)
plt.title('Anomali Tespiti')

plt.tight_layout()
plt.show()

print("\n--- Temizlenmi veri ve analiz ---")
print(df[['Product', 'Price', 'Is_Anomaly']])
