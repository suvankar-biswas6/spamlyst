# download_nltk_data.py
import nltk, os

# Target a folder inside your app (e.g. /app/nltk_data)
target_dir = os.path.join(os.getcwd(), "nltk_data")

# Make sure the folder exists
if not os.path.isdir(target_dir):
    os.makedirs(target_dir)

# Download “punkt” into that folder
nltk.download("punkt", download_dir=target_dir)
