# **PyMLSuite - Automated Machine Learning Pipeline**

## **🛠️ WORK IN PROGRESS 
Project development has started on February 2025, core features are planned to be completed in May 2025

## **👤 Author**
Marc Ennaji  
[🔗 LinkedIn Profile](https://www.linkedin.com/in/marcennaji/)


## **📌 Project Overview **

### **What is PyMLSuite?**
PyMLSuite is an open-source **Machine Learning Automation tool** that helps businesses and developers **train, compare, deploy, and monitor machine learning models** efficiently. It provides an easy way to select the best model for structured/tabular data and deploy it as an API.

### **Why is it useful?**
- **Reduces manual ML work**: Automates model training, selection, and deployment.
- **Ensures accuracy**: Picks the best model based on real-world performance.
- **Simplifies ML adoption**: Allows businesses to use ML without deep expertise.
- **Open-source & flexible**: Easily customizable for various industries.

### **Some real-World Use Cases :**
- **Fraud Detection**: Detect fraudulent transactions using historical patterns.
- **Customer Churn Prediction**: Identify users likely to stop using a service.
- **Healthcare Risk Analysis**: Predict diseases or health risks from patient data.
- **E-commerce Recommendations**: Suggest products based on user behavior.

---

## **🚀 Quick Start Guide **

## 🔹 Prerequisites
Install Khiops manually, by following these [🔗 instructions ](https://khiops.org/setup/)


### **Installation**
#### ✅ Using `pip` (Local Installation)
```bash
pip install fastapi uvicorn scikit-learn xgboost pandas numpy mlflow requests wandb dvc python-dotenv pytest pytest-xdist requests datasets
```

#### ✅ Using Docker
```bash
# Clone the repository
git clone https://github.com/YOUR_GITHUB_USERNAME/PyMLSuite.git
cd PyMLSuite

# Build and run the Docker container
docker build -t pymlsuite .
docker run -p 8000:8000 pymlsuite
```

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

### **Core Features**
1. **Automated Model Selection**: Compares Khiops, RandomForest, and XGBoost to choose the best-performing model.
2. **API Deployment**: The selected model is deployed as a REST API via FastAPI.
3. **Continuous Integration (CI)**: Every code change is tested using GitHub Actions.
4. **Parallelized Testing**: Ensures fast and scalable model validation.
5. **Real-World Dataset Support**: Prepares and trains models on large-scale tabular datasets.

---

## **📚 Contributing & Support**
For now, the development is still ongoing. When the main features will be completed, contributions will be welcome.

---

## **📜 License**
PyMLSuite is licensed under the MIT License. See `LICENSE` for details.


