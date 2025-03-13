# Book Recommendation System

## 📌 Overview
The **Book Recommendation System** is a web-based application built using **Flask** that provides personalized book recommendations. Users can input a book title, and the system suggests similar books based on collaborative filtering.

## 📂 Project Structure
```
BookRecommendationSystem/
│-- templates/            # HTML templates for frontend
│   │-- about.html        # About page
│   │-- contact.html      # Contact page
│   │-- index.html        # Homepage with search functionality
│   │-- login.html        # Login page
│   │-- recommend.html    # Book recommendation results
│   │-- register.html     # Registration page
│-- static/               # Static files (CSS, images, etc.)
│   │-- style.css         # Styling for the web app
│-- app.py                # Main Flask application
│-- popular.pkl           # Precomputed popular books data
│-- books.pkl             # Dataset containing book details
│-- pt.pkl                # Pivot table for collaborative filtering
│-- similarity_scores.pkl # Similarity matrix for recommendations
│-- requirements.txt      # Python dependencies (if applicable)
```

## 🚀 Features
- User-friendly interface to search for books.
- Provides book recommendations based on similarity scores.
- Uses **Flask** for backend routing and **HTML/CSS** for frontend design.
- Displays book details such as title, author, and cover image.
- Includes About, Contact, Login, and Registration pages.

## 🔧 Setup Instructions
### Prerequisites
Ensure you have Python installed on your system.

### 1️⃣ Install Dependencies
Navigate to the project directory and install required dependencies:
```bash
pip install flask pandas numpy pickle5
```

### 2️⃣ Run the Application
Execute the following command to start the Flask server:
```bash
python app.py
```
The application will run on **http://127.0.0.1:5000/**.

### 3️⃣ Using the System
1. Open the browser and go to `http://127.0.0.1:5000/`
2. Search for a book title in the search bar.
3. Get personalized book recommendations.

## 🛠 Technologies Used
- **Python** (Flask, Pandas, NumPy, Pickle)
- **HTML, CSS** (Frontend design)
- **Machine Learning** (Collaborative Filtering-based Recommendations)

---
✅ Developed with ❤️ by Kalyani Satish Uparkar

