🎓 Student Performance Predictor

A web-based machine learning application that predicts student exam performance based on real-time inputs like study hours, attendance, past scores, and participation. Built to assist educators in identifying students at academic risk and offering timely intervention.

🚀 Features

- Predicts student exam scores using a trained ML model
- Real-time student data entry through web forms
- Secure teacher login with hashed credentials
- Dashboard displaying all student records and predictions
- Model explainability with SHAP (optional)
- SQLite database integration (lightweight and extendable)

📌 How to Use

- Clone the repository
- Install dependencies: pip install -r requirements.txt
- Train the ML model: python models/train_model.py
- Run the server: python run.py
- Open http://localhost:5000/login

📄 License
This project is licensed under the MIT License.
