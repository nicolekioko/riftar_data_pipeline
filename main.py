import json
import pandas as pd

# Step 1: Load data from JSON
with open("test_data.json", "r") as file:
    sensor_data = json.load(file)

# Step 2: Convert JSON data to DataFrame for easier processing
df = pd.DataFrame(sensor_data)

# Step 3: Show the raw data
print("📥 Raw Sensor Data:")
print(df)
# Step 4: Validate the data

print("\n✅ Validating Data...")

# Check for missing values (NaNs)
if df.isnull().values.any():
    print("⚠️ Warning: Missing values found in data!")
    print(df.isnull().sum())
else:
    print("✅ No missing values found.")

# Check for expected columns
expected_columns = ["timestamp", "acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z"]
missing_cols = [col for col in expected_columns if col not in df.columns]

if missing_cols:
    print(f"❌ Missing columns: {missing_cols}")
else:
    print("✅ All expected columns are present.")

# Check that sensor data columns are numeric
sensor_columns = ["acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z"]
non_numeric = df[sensor_columns].select_dtypes(exclude=["number"]).columns.tolist()

if non_numeric:
    print(f"❌ Non-numeric sensor columns found: {non_numeric}")
else:
    print("✅ All sensor columns are numeric.")
from sklearn.preprocessing import MinMaxScaler

# Step 5: Normalize the sensor data
print("\n📊 Normalizing Sensor Data...")

# Define columns to normalize
sensor_columns = ["acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z"]

# Create the scaler
scaler = MinMaxScaler()

# Apply scaler to sensor data
normalized_values = scaler.fit_transform(df[sensor_columns])

# Create a new DataFrame with normalized values
normalized_df = pd.DataFrame(normalized_values, columns=sensor_columns)

# Include timestamp in the final normalized data
normalized_df["timestamp"] = df["timestamp"]

# Show the normalized data
print("✅ Normalized Sensor Data:")
print(normalized_df)

# Save to CSV
normalized_df.to_csv("normalized_data.csv", index=False)
print("\n💾 Normalized data saved to 'normalized_data.csv'")
