![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Focused-blue?style=for-the-badge)

# 🌾 AgriPredict: ML-Powered Crop Yield Forecasting

AgriPredict is a precision agriculture tool developed to predict crop yields across various Indian states. By leveraging historical government data, the project helps stakeholders anticipate production levels based on seasonal, regional, and environmental parameters.

## 📂 Dataset Overview
The project utilizes the **"Crop Production Statistics"** provided by the **Government of India**.
- **Source:** [Ministry of Agriculture and Farmers Welfare (Agricultural Statistics at a Glance)](https://agriwelfare.gov.in/en/Agricultural_Statistics_at_a_Glance) / [Open Government Data (OGD) Platform India](https://www.data.gov.in/)
- **Scope:** Includes comprehensive records of Year, State, District, Season, and Crop-wise production.
- **Preprocessing:** High-variance entries and outliers were filtered to ensure model reliability for staple food grains and commercial crops.

## 🚀 Technical Highlights
* **Model:** Random Forest Regressor (Chosen for its robustness and ability to capture non-linear relationships).
* **Feature Engineering:** - One-Hot Encoding for categorical features (State, District, Season, Crop).
  - Log-Transformation ($y' = \log(1 + y)$) of the target variable to handle the heavy skewness of yield data.
* **Interface:** Interactive Streamlit dashboard for real-time inference.

## 📥 Model Download (Required)
The trained model (`rf_model_no_coconut.pkl`) is **2.18 GB**, which exceeds GitHub's standard file limits.
1. **Download the model:** [PASTE YOUR GOOGLE DRIVE LINK HERE]
2. **Placement:** Place the downloaded `.pkl` file in the root directory before running the application.

## 🛠 Installation & Usage
```bash
# Clone the repository
git clone [https://github.com/harshitchauhann95/AgriPredict-Machine-Learning-Based-Crop-Yield-Forecasting.git](https://github.com/harshitchauhann95/AgriPredict-Machine-Learning-Based-Crop-Yield-Forecasting.git)

# Install dependencies
pip install -r requirements.txt

# Run the web app
streamlit run app.py
```
## 📸 Interface Preview
<img width="1440" height="820" alt="AgriPredict App Screenshot" src="https://github.com/user-attachments/assets/7e8ff77a-fb2b-47a7-8cdc-6d99f0a1d95d" />

---

## 📊 Machine Learning Workflow
To ensure high prediction accuracy, the following pipeline was implemented:

1. **Exploratory Data Analysis (EDA):** Analyzed historical trends in crop production across various Indian agro-climatic zones.
2. **Data Cleaning:** Removed missing values and filtered out high-variance outliers that degraded model $R^2$ performance.
3. **Training:** Evaluated various regressor models; **Random Forest** yielded the best balance between training speed and predictive accuracy.
4. **Serialization:** Saved the finalized model using `pickle` for low-latency deployment in the web interface.

---

## 🔮 Future Roadmap
- **IoT Integration:** Connecting live soil health data from **ESP8266 sensors** to provide real-time field inputs.
- **Hyperparameter Tuning:** Implementing **Bayesian Optimization** for finer model control and improved error metrics.
- **Deep Learning:** Testing **LSTM (Long Short-Term Memory)** models for advanced time-series yield forecasting.

---

## 📄 License
Distributed under the **MIT License**. See `LICENSE` for more information.
