import requests
import zipfile
import io
import os

def download_data():
    url = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
    print("Adatok letöltése folyamatban...")
    
    # Letöltés
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    
    # Kicsomagolás a data mappába
    print("Kicsomagolás...")
    z.extractall("data")
    
    print("Kész! Az adatok a 'data/ml-latest-small' mappában találhatóak.")

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")
    download_data()