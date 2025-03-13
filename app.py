from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

POPULAR_PKL_URL = "https://drive.google.com/file/d/1gG-bY1onkFc3TLV6WXvB7pQKkSeyGKz0/view?usp=sharing"
BOOKS_PKL_URL = "https://drive.google.com/file/d/12GK9HyE2bVZLdORAQzlR1Y8LHjaTs2rB/view?usp=sharing"
PT_PKL_URL = "https://drive.google.com/file/d/1RcjKQayVVD4DSs_tqo58RBGYCabIjkSJ/view?usp=sharing"
SIMILARITY_SCORES_PKL_URL = "https://drive.google.com/file/d/18MNTJ8Sq3R22R4IoU1LafjbNEIw8KRXb/view?usp=sharing"

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)

download_file(POPULAR_PKL_URL, "popular.pkl")
download_file(BOOKS_PKL_URL, "books.pkl")
download_file(PT_PKL_URL, "pt.pkl")
download_file(SIMILARITY_SCORES_PKL_URL, "similarity_scores.pkl")

# Load data
popular_df = pd.read_pickle(open(r'popular.pkl','rb'))
books = pd.read_pickle(open(r'C:\CODES\BookRecommendationSystem\books.pkl','rb'))
pt = pd.read_pickle(open(r'pt.pkl','rb'))
similarity_scores = pd.read_pickle(open(r'similarity_scores.pkl','rb'))

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/Recommender')
def recommend():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommender():
    userinput = request.form.get('userinput')
    
    # Check if the input is in the index
    if userinput in pt.index:
        index = np.where(pt.index == userinput)[0]
        index = index[0]

        similar_items = sorted(enumerate(similarity_scores[index]), key=lambda x: x[1], reverse=True)[:10]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-L'].values))
            data.append(item)

        print(data)  # Debugging statement to check data
        return render_template('recommend.html', data=data)
    else:
        return render_template('recommend.html', data=[], error="Book not found")  # Handle book not found

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def handler(event, context):
    return app(event, context)

if __name__ == "__main__":
    app.run(debug=True)

    