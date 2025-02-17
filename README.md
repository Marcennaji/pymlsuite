# **PyMLSuite - Automated Machine Learning Pipeline**

## **👤 Author**
Marc Ennaji 
[🔗 LinkedIn Profile](https://www.linkedin.com/in/marcennaji/)

## **🛠️ WORK IN PROGRESS**
Project development has started in **February 2025**, and core features are planned to be completed in **May 2025**.

## **📌 Project Overview (For Non-Technical Users)**

### **What is PyMLSuite?**
PyMLSuite is an open-source **Machine Learning Automation tool** that helps businesses and developers **train, compare, deploy, and monitor machine learning models** efficiently. It provides an easy way to select the best model for structured/tabular data and deploy it as an API.

### **Why is it useful?**
- **Reduces manual ML work**: Automates model training, selection, and deployment.
- **Ensures accuracy**: Picks the best model based on real-world performance.
- **Simplifies ML adoption**: Allows businesses to use ML without deep expertise.
- **Open-source & flexible**: Easily customizable for various industries.

### **Real-World Use Cases**
- **Fraud Detection**: Detect fraudulent transactions using historical patterns.
- **Customer Churn Prediction**: Identify users likely to stop using a service.
- **Healthcare Risk Analysis**: Predict diseases or health risks from patient data.
- **E-commerce Recommendations**: Suggest products based on user behavior.

### **Cloud Deployment**
PyMLSuite will be deployed on **Heroku**, providing easy access via a REST API.

#### **Deploying to Heroku**
To deploy PyMLSuite to Heroku, use the following commands:
```bash
heroku create pymlsuite-app
git push heroku main
heroku ps:scale web=1
heroku open
```
This ensures that the ML models are accessible via a **cloud-based API** without requiring local setup.

---

## **🚀 Quick Start Guide (For Developers & Data Scientists)**

### **Installation**
#### ✅ Using `pip` (Local Installation)
```bash
pip install fastapi uvicorn scikit-learn xgboost pandas numpy mlflow requests khiops wandb dvc python-dotenv pytest pytest-xdist requests datasets
```

#### ✅ Using Docker
```bash
# Clone the repository
git clone https://github.com/marcennaji/PyMLSuite.git
cd PyMLSuite

# Build and run the Docker container
docker build -t pymlsuite .
docker run -p 8000:8000 pymlsuite
```

#### **Installing Khiops (Optional but Recommended)**
To compare **Khiops vs. Scikit-Learn models**, you must install the **Khiops binaries**.  
Follow the official [🔗 Khiops installation guide](https://khiops.org/setup/).
When you will have installed the Khiops application (containing the binaries), then you will be able to install the Khiops Python library with pip, as described in the Khiops installation guide.

#### ✅ Running Tests Locally
```bash
pytest
```

#### ✅ Running Tests in Parallel (For Speed Optimization)
```bash
pytest -n auto
```

---

## **🛠️ Technical Overview**

### **Tech Stack**
| Component | Technology Used |
|-----------|----------------|
| **Backend API** | FastAPI |
| **Model Training** | Khiops, Scikit-Learn, XGBoost |
| **Data Processing** | Pandas, NumPy |
| **Model Tracking** | MLflow, Weights & Biases |
| **Testing** | Pytest, Pytest-xdist (Parallelization) |
| **CI/CD** | GitHub Actions |
| **Containerization** | Docker, Docker Compose |
| **Dataset Management** | DVC (Data Version Control) |
| **Cloud Deployment** | Heroku |
| **Code Formatting & Linting** | Black, Ruff (pre-commit hooks) |
| **Data Validation & Models** | Pydantic |

### **Core Features**
1. **Automated Model Selection**: Compares Khiops, RandomForest, and XGBoost to choose the best-performing model.
2. **API Deployment**: The selected model is deployed as a REST API via FastAPI.
3. **Continuous Integration (CI)**: Every code change is tested using GitHub Actions.
4. **Parallelized Testing**: Ensures fast and scalable model validation.
5. **Real-World Dataset Support**: Prepares and trains models on large-scale tabular datasets.
6. **Cloud Deployment**: Runs on **Heroku** for easy access.
7. **Data Validation with Pydantic**: Ensures API request validation and structured data handling.

---

## **📚 Contributing & Support**
We welcome contributions! If you’d like to enhance PyMLSuite, please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## **📩 Contact**
For questions or contributions, reach out via [LinkedIn](https://www.linkedin.com/in/marcennaji) or open an issue on GitHub.

---

## **📜 License**
PyMLSuite is licensed under the MIT License. See `LICENSE` for details.

