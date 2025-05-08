# Student Performance Predictor

A Flask-based web application that allows teachers to log in, add student data in real-time, and predict student exam performance using a trained machine learning model.

## Features

- Secure teacher login
- Real-time student data entry
- Performance prediction using machine learning
- Dashboard to view all student data

## Setup Instructions

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Initialize the database:
- Create `students.db` in the `database/` directory.
- Create `users` and `students` tables.
4. Train the model:
   python models/train_model.py
5. Run the application:


## License

MIT License