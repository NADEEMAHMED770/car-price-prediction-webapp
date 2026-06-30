# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import joblib
import sys
import io
import warnings

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Suppress scikit-learn version warnings (optional)
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

app = Flask(__name__)

# Load the model
try:
    model = joblib.load("model.pkl")
    print("✅ Model loaded successfully!")
except Exception as e:
    model = None
    print(f"⚠️ Model not found. Error: {e}")

@app.route("/")
def home():
    return render_template("index.html", reset_form=True)

@app.route("/predict", methods=["POST"])
def predict():
    errors = []
    
    # --- Get and validate Year ---
    year_str = request.form.get("year", "").strip()
    if not year_str:
        errors.append("Year is required.")
    else:
        try:
            year = int(year_str)
            if year < 1980:
                errors.append("Year must be at least 1980.")
            elif year > 2026:
                errors.append("Year cannot be in the future. Please enter a valid year.")
        except ValueError:
            errors.append("Year must be a valid number.")
    
    # --- Get and validate Present Price ---
    price_str = request.form.get("present_price", "").strip()
    if not price_str:
        errors.append("Present price is required.")
    else:
        try:
            present_price = float(price_str)
            if present_price <= 0:
                errors.append("Present price must be greater than 0.")
            elif present_price > 100:
                errors.append("Present price seems too high. Please enter a valid price in Lakhs.")
        except ValueError:
            errors.append("Present price must be a valid number.")
    
    # --- Get and validate Kilometers Driven ---
    kms_str = request.form.get("kms_driven", "").strip()
    if not kms_str:
        errors.append("Kilometers driven is required.")
    else:
        try:
            kms_driven = int(kms_str)
            if kms_driven < 0:
                errors.append("Kilometers driven cannot be negative.")
            elif kms_driven > 1000000:
                errors.append("Kilometers driven seems too high. Please enter a valid value.")
        except ValueError:
            errors.append("Kilometers driven must be a valid number.")
    
    # --- Get Fuel Type ---
    fuel_type = request.form.get("fuel_type", "Petrol")
    Fuel_Petrol = 1 if fuel_type == "Petrol" else 0
    Fuel_Diesel = 1 if fuel_type == "Diesel" else 0
    
    # --- Get Seller Type ---
    seller_type = request.form.get("seller_type", "Dealer")
    Selling_type = 0 if seller_type == "Dealer" else 1
    
    # --- Get Transmission ---
    transmission = request.form.get("transmission", "Manual")
    Transmission = 1 if transmission == "Manual" else 0
    
    # --- If errors exist, return to form with error messages ---
    if errors:
        return render_template(
            "index.html",
            errors=errors,
            year=year_str if 'year' in locals() else '',
            present_price=price_str if 'price_str' in locals() else '',
            kms_driven=kms_str if 'kms_str' in locals() else '',
            fuel_type=fuel_type,
            seller_type=seller_type,
            transmission=transmission,
            reset_form=False
        )
    
    # --- Check if model exists ---
    if model is None:
        errors.append("Model not loaded. Please check server logs.")
        return render_template(
            "index.html",
            errors=errors,
            year=year,
            present_price=present_price,
            kms_driven=kms_driven,
            fuel_type=fuel_type,
            seller_type=seller_type,
            transmission=transmission,
            reset_form=False
        )
    
    # --- Make prediction ---
    try:
        features = [[
            year,
            present_price,
            kms_driven,
            Selling_type,
            Transmission,
            Fuel_Diesel,
            Fuel_Petrol
        ]]
        
        prediction = model.predict(features)
        predicted_price = round(prediction[0], 2)
        is_negative = predicted_price < 0
        
        return render_template(
            "index.html",
            prediction=predicted_price,
            is_negative=is_negative,
            year=year,
            present_price=present_price,
            kms_driven=kms_driven,
            fuel_type=fuel_type,
            seller_type=seller_type,
            transmission=transmission,
            reset_form=False,
            show_result=True
        )
    except Exception as e:
        errors.append(f"An error occurred while predicting: {str(e)}")
        return render_template(
            "index.html",
            errors=errors,
            year=year,
            present_price=present_price,
            kms_driven=kms_driven,
            fuel_type=fuel_type,
            seller_type=seller_type,
            transmission=transmission,
            reset_form=False
        )

@app.route("/reset")
def reset():
    return render_template("index.html", reset_form=True)

if __name__ == "__main__":
    app.run(debug=True)