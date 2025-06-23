# 🚀 Sensor Data Normalization Service – RIFT-AR Internship Challenge

## 📌 Overview

This project is my solution to **Track 2: Data Normalization Service** for the RIFT-AR internship technical challenge. The goal was to implement a cloud-style function that:

- Loads simulated raw sensor data  
- Validates the input data  
- Normalizes it for downstream machine learning tasks  
- Saves the cleaned and scaled dataset in `.csv` format  

The challenge is part of a real-world system to process data from iOS devices — like accelerometer and gyroscope readings — for location intelligence and context inference.

---

## 🧰 Tech Stack

- **Python 3.13.5**
- **pandas** – for data handling
- **scikit-learn** – for data normalization
- **JSON** – to simulate raw input
- **CSV** – output format for normalized results

---

## 📂 Project Structure

```bash
riftar_data_pipeline/
│
├── test_data.json           # Simulated raw sensor input (JSON format)
├── main.py                  # Core script: loads, validates & normalizes data
├── normalized_data.csv      # Output: scaled data ready for ML processing
└── README.md                # Documentation (this file)
```

---

## 🧪 Sample Data

Raw sensor data is stored in `test_data.json` and includes:

- `timestamp`: ISO 8601 timestamp  
- `acc_x`, `acc_y`, `acc_z`: Accelerometer readings  
- `gyro_x`, `gyro_y`, `gyro_z`: Gyroscope readings  

### Example:
```json
[
  {
    "timestamp": "2025-06-18T10:00:00Z",
    "acc_x": 0.01,
    "acc_y": -0.02,
    "acc_z": 9.80,
    "gyro_x": 0.001,
    "gyro_y": -0.005,
    "gyro_z": 0.0008
  },
  ...
]
```

---

## ⚙️ Functionality & Steps

### 1. **Load JSON Data**

The script reads `test_data.json` and converts it into a structured `pandas` DataFrame for analysis.

```python
with open("test_data.json", "r") as file:
    sensor_data = json.load(file)

df = pd.DataFrame(sensor_data)
```

---

### 2. **Data Validation**

Three key checks are performed:
- ✅ No missing values (NaNs)
- ✅ All required columns are present
- ✅ Sensor data columns are all numeric

This ensures the data is clean and consistent before applying ML preprocessing steps.

---

### 3. **Normalization**

Sensor values are scaled using `MinMaxScaler` from `scikit-learn`. This transforms all values to the range `[0, 1]`, which helps machine learning models learn efficiently.

The normalized data is combined with the original timestamp column to preserve time reference.

```python
scaler = MinMaxScaler()
normalized_values = scaler.fit_transform(df[sensor_columns])
```

---

### 4. **Save to CSV**

Final output is saved as `normalized_data.csv` and contains clean, scaled data ready for ingestion by ML pipelines.

---

## 📈 Example Output (normalized)

| timestamp               | acc_x | acc_y | acc_z | gyro_x | gyro_y | gyro_z |
|------------------------|-------|-------|-------|--------|--------|--------|
| 2025-06-18T10:00:00Z   | 0.00  | 0.00  | 1.00  | 0.00   | 0.00   | 0.33   |
| 2025-06-18T10:00:01Z   | 0.50  | 0.50  | 0.00  | 1.00   | 0.50   | 1.00   |
| 2025-06-18T10:00:02Z   | 1.00  | 1.00  | 0.60  | 0.50   | 1.00   | 0.00   |

---

## 📚 Notes & Learnings

- I used `MinMaxScaler` for simplicity, but other scalers (like `StandardScaler`) can be used depending on downstream models.
- The JSON structure mimics real sensor input from a mobile device.
- This setup can be expanded to support real-time cloud APIs, streaming data, or multiple formats.
- I gained hands-on experience in structuring a data pipeline and performing validation for real-world sensor data.

---

## 💡 Why This Track Resonated With Me

I chose Track 2 because I’m deeply interested in how raw environmental data can be transformed into meaningful intelligence for real-world applications. This challenge helped me:

- Handle structured sensor data with confidence  
- Apply preprocessing techniques used in ML pipelines  
- Build a clear, testable, and scalable backend-style system  

---

## 🙋🏽‍♀️ About Me

I'm a final-year Electrical & Electronics Engineering student with growing experience in embedded systems and real-time sensor integration. I love learning hands-on through projects like this, and I'm inspired by RIFT-AR’s mission to build privacy-first, hardware-independent systems.

I’m eager to keep learning fast, adapt to challenges, and eventually contribute to your team full time — building intelligent systems that bridge the physical and digital worlds.

---

## ✅ TODO / Future Ideas

- Real cloud deployment with Firebase or AWS Lambda  
- Support for streaming live data from a mobile device  
- Advanced feature extraction (e.g. peak detection, FFTs)
