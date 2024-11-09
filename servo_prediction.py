import random
import math

class LinearRegression:
    def __init__(self):
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        n_samples = len(X)
        
        # Calculate means
        x_mean = sum(X) / n_samples
        y_mean = sum(y) / n_samples
        
        # Calculate coefficients
        numerator = sum((X[i] - x_mean) * (y[i] - y_mean) for i in range(n_samples))
        denominator = sum((X[i] - x_mean) ** 2 for i in range(n_samples))
        
        self.weights = numerator / denominator
        self.bias = y_mean - self.weights * x_mean
    
    def predict(self, X):
        return [self.weights * x + self.bias for x in X]

def generate_servo_data(n_samples=100):
    """Generate synthetic servo data"""
    X = []
    y = []
    
    for _ in range(n_samples):
        # Input features: voltage (0-5V)
        voltage = random.uniform(0, 5)
        
        # Target: angle (0-180 degrees) with some noise
        angle = (voltage * 36) + random.gauss(0, 2)  # 36 = 180/5 for linear mapping
        
        X.append(voltage)
        y.append(angle)
    
    return X, y

def calculate_metrics(y_true, y_pred):
    """Calculate MSE and R2 score"""
    mse = sum((y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true))) / len(y_true)
    
    y_mean = sum(y_true) / len(y_true)
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    ss_res = sum((y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true)))
    
    r2 = 1 - (ss_res / ss_tot)
    
    return mse, r2

def main():
    # Generate synthetic servo data
    X_train, y_train = generate_servo_data(100)
    X_test, y_true = generate_servo_data(20)
    
    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate and display metrics
    mse, r2 = calculate_metrics(y_true, y_pred)
    
    print("\nServo Position Prediction Results:")
    print("-" * 30)
    print(f"Model Parameters:")
    print(f"Weight: {model.weights:.4f}")
    print(f"Bias: {model.bias:.4f}")
    print("\nModel Performance:")
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R² Score: {r2:.4f}")
    
    # Display some sample predictions
    print("\nSample Predictions:")
    print("Voltage (V) | Actual Angle (°) | Predicted Angle (°)")
    print("-" * 50)
    for i in range(5):
        print(f"{X_test[i]:10.2f} | {y_true[i]:14.2f} | {y_pred[i]:17.2f}")

if __name__ == "__main__":
    main()