from data_processing import load_data, preprocess_data, feature_engineering
from model_building import train_model, evaluate_model
from sklearn.model_selection import train_test_split

def main():
    # Load data
    data = load_data('data.csv')
    
    # Preprocess data
    preprocessed_data = preprocess_data(data)
    
    # Perform feature engineering
    engineered_features = feature_engineering(preprocessed_data)
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(engineered_features, data['target'], test_size=0.2, random_state=42)
    
    # Train model
    model = train_model(X_train, y_train)
    
    # Evaluate model
    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Model accuracy: {accuracy}")
    
if __name__ == "__main__":
    main()
