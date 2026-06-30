# 🚗 Car Price Prediction Web Application

A Flask-based Machine Learning web application that predicts the estimated selling price of a used car based on user inputs.

This project deploys a **Multiple Linear Regression** model through a clean and responsive web interface, allowing users to get real-time predictions directly from their browser.

---



## ✨ Features

- 🚗 Predict used car selling prices instantly
- 🤖 Machine Learning powered prediction
- 🌐 Flask backend
- 🎨 Modern responsive user interface
- 📱 Mobile-friendly design
- ⚡ Fast prediction using a pre-trained model
- ✅ Input validation
- ⚠️ Handles invalid and negative predictions gracefully

---

## 🛠️ Technologies Used

### Backend

- Python
- Flask
- Joblib
- Scikit-learn

### Frontend

- HTML5
- CSS3
- JavaScript
- Font Awesome

### Machine Learning

- Multiple Linear Regression
- Pandas
- NumPy
- Scikit-learn

---

# 📂 Project Structure

```text
car-price-prediction-webapp/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/NADEEMAHMED770/car-price-prediction-webapp.git
```

Move into the project folder

```bash
cd car-price-prediction-webapp
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 🧠 Machine Learning Model

This application uses a **Multiple Linear Regression** model trained on a used car dataset.

The deployed model predicts the selling price using the following features:

- Manufacturing Year
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission

The trained model is loaded using **Joblib** and used to generate predictions in real time.

---

# 🔗 Related Project

The machine learning model used in this application was developed in a separate project that focuses on:

- Data Cleaning
- Data Preprocessing
- Feature Engineering
- Model Training
- Model Evaluation

👉 **Machine Learning Repository:**

Replace this with your repository link:

```
https://github.com/NADEEMAHMED770/car_price_prediction 
```

---

# 🎯 Future Improvements

- Deploy using Render
- Compare multiple ML models
- Add model confidence information
- Support additional vehicle features
- Store prediction history
- REST API for predictions
- Docker support

---

# 🤝 Acknowledgements

This project was developed as part of my Machine Learning learning journey.

The deployed machine learning model was trained by me in a separate project. During the development of this web application, I used AI coding assistants to help with frontend design, UI implementation, and code refinement. I integrated, tested, customized, and understood the complete Flask application and machine learning deployment workflow.

---

# 👨‍💻 Author

**Nadeem Ahmed**

BS Artificial Intelligence Student

GitHub: https://github.com/NADEEMAHMED770


---

## ⭐ If you found this project interesting, consider giving it a star!
