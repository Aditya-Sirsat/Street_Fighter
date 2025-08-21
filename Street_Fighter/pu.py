import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data from Excel file
data = pd.read_excel(r"C:\Users\DELL\OneDrive\Attachments\FDS5.xlsx",header=None)

# Assuming the Excel file has two columns 'X' and 'Y'
X = data['X'].values.reshape(-1, 1)  # Feature
y = data['Y'].values                  # Target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Coefficients
print('Coefficients:', model.coef_)

# Intercept
print('Intercept:', model.intercept_)