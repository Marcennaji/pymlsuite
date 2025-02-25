# **PyMLSuite: K-Means Benchmarking Tool**

## **👤 Author**
Marc Ennaji 
[🔗 LinkedIn Profile](https://www.linkedin.com/in/marcennaji/)

## **🛠️ WORK IN PROGRESS**
Project development has started in **February 2025**, and core features are planned to be completed in **May 2025**.

## **📌 Project Overview (For Non-Technical Users)**

PyMLSuite: K-Means Benchmarking Tool
🚀 Compare K-Means from Scikit-learn vs. Enneade (Khiops K-Means)
PyMLSuite is an open-source benchmarking suite designed to compare Scikit-learn's K-Means with Enneade (Khiops' K-Means implementation). It provides automated tools for evaluating clustering performance, execution speed, and scalability on structured/tabular data.

📌 Why Use PyMLSuite?
✅ Compare K-Means implementations → Evaluate accuracy, speed, and scalability.
✅ Automated Experiments → Run multiple tests with MLflow logging.
✅ Data Versioning & Reproducibility → Track datasets using DVC.
✅ Visual Benchmarking → Generate clustering reports with matplotlib & seaborn.
✅ Deploy an API → Run clustering on new data via a FastAPI service.

🔹 Real-World Use Cases
🔹 Customer Segmentation → Identify user clusters based on behavior.
🔹 Anomaly Detection → Detect unusual patterns in financial or security data.
🔹 Image Compression → Cluster pixel values for reducing image sizes.
🔹 Genetic Data Clustering → Group similar genetic sequences for research.

🛠️ Technical Overview
Tech Stack
Component	Technology Used
Benchmarking	Khiops (Enneade), Scikit-learn (K-Means)
Data Processing	Pandas, NumPy
Experiment Tracking	MLflow, Weights & Biases
Visualization	Matplotlib, Seaborn
Testing & Validation	Pytest, Pytest-xdist
CI/CD	GitHub Actions
Containerization	Docker, Docker Compose
Dataset Management	DVC (Data Version Control)
API & Deployment	FastAPI, Heroku
Code Quality	Black, Ruff (pre-commit hooks)
📌 Core Features
✅ K-Means Algorithm Comparison → Benchmark Scikit-learn vs. Enneade with real datasets.
✅ Performance Metrics → Compute Silhouette Score, Davies-Bouldin Index, Execution Time.
✅ Experiment Logging → Track results with MLflow & Weights & Biases.
✅ Visualization & Reporting → Generate clustering plots & performance reports.
✅ API for Predictions → Deploy a FastAPI service for clustering on new datasets.
✅ Cloud-Ready Deployment → Run benchmarks locally or deploy on Heroku.

📅 Quick Start Guide
Installation
✅ Using pip (Local Installation)

bash
Copier
Modifier
pip install fastapi uvicorn scikit-learn pandas numpy mlflow requests khiops wandb dvc python-dotenv pytest pytest-xdist matplotlib seaborn
✅ Using Docker

bash
Copier
Modifier
# Clone the repository
git clone https://github.com/marcennaji/PyMLSuite.git
cd PyMLSuite

# Build and run the Docker container
docker build -t pymlsuite .
docker run -p 8000:8000 pymlsuite
🛠 Running Benchmarks (Scikit-learn K-Means vs. Enneade)
1️⃣ Train & Compare Clustering Models
Run the benchmark script to compare both implementations:

bash
Copier
Modifier
python pymlsuite/benchmark_kmeans.py --dataset datasets/sample.csv
The script will:
✅ Train K-Means (Scikit-learn) and Enneade (Khiops K-Means).
✅ Compute performance metrics (Silhouette score, inertia, execution time).
✅ Log results in MLflow and generate visual reports.

🚀 Deploying to Heroku (Optional, for API Integration)
bash
Copier
Modifier
heroku create pymlsuite-app
git push heroku main
heroku ps:scale web=1
heroku open
This makes clustering models accessible via a FastAPI-based REST API.

✅ Running Tests Locally
✅ Unit tests for benchmarking scripts:

bash
Copier
Modifier
pytest
✅ Parallelized testing (for speed optimization):

bash
Copier
Modifier
pytest -n auto

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

