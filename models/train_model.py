import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv('student_dataset.csv')

features = ['Student_Age', 'Weekly Study Hours', 'Attendance',
            'Reading', 'Notes', 'Listening in Class', 'Project Work']
target = 'Grade'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, 'models/performance_model.pkl')