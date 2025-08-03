from model import load_data, train_model, save_model, evaluate_model

# Step 1: Load data
df = load_data('data/final.csv')

# Step 2: Train model
model, x_train, x_test, y_train, y_test = train_model(df)

# Step 3: Evaluate (optional but good for debugging)
mae = evaluate_model(model, x_test, y_test)
print(f"📊 Model Test MAE: ${mae:,.2f}")

# Step 4: Save the trained model
save_model(model, 'models/RE_Model.pkl')

print("✅ Model trained and saved successfully as models/RE_Model.pkl")
