# **ClustXpert: Easy and Flexible Clustering**

## **👤 Author**
Marc Ennaji 
[🔗 LinkedIn Profile](https://www.linkedin.com/in/marcennaji/)

## **🛠️ WORK IN PROGRESS**
Project development has started in **February 2025**, and core features are planned to be completed in **July 2025**.

## **📌 Project Overview (For Non-Technical Users)**

ClustXpert is a **powerful yet user-friendly** clustering tool that makes advanced data clustering **accessible to everyone**.  

This project is a fork of **Khiops Enneade**, an application I originally developed under the supervision of **Vincent Lemaire (Research Scientist and Research Program Manager at Orange Labs)**. While the original **Enneade** remains available *as-is* on the Khiops website (based on an **older, unsupported version of Khiops**), **ClustXpert is built on the latest version of Khiops**, bringing improved performance, stability, and compatibility.  

ClustXpert is designed to be **easy to use for beginners**, while still offering **high configurability** for advanced users.  

---

## 📌 **Why Use ClustXpert?**  

✅ **Super easy to use** → Start clustering with just **one command**!  
✅ **No need for one-hot encoding** → Native support for categorical variables.  
✅ **Works with relational data (multi-table support)** → No need to merge tables manually.  
✅ **Highly flexible** → Fine-tune clustering settings if needed.  
✅ **Optimized cluster initialization** → Get better, more stable results.  
✅ **Modern & scalable** → Built with MLOps best practices (data versioning, experiment tracking, CI/CD).  

---

## 📅 Quick Start Guide
### Installation
✅ **Using pip (Local Installation)**  
```bash
pip install fastapi uvicorn scikit-learn pandas numpy mlflow requests wandb dvc python-dotenv pytest pytest-xdist matplotlib seaborn
```
✅ **Using Docker**  
```bash
# Clone the repository
git clone https://github.com/marcennaji/clustxpert.git
cd clustxpert

# Build and run the Docker container
docker build -t clustxpert .
docker run -p 8000:8000 clustxpert
```

### **Training and evaluating on a dataset**
If you just want to **run clustering with the best default settings**, simply use:  

```bash
python clustxpert/clustering.py --dataset datasets/sample.csv
```
---

### ⚙️ Flexible Customization (For Advanced Users)
If you want more control, ClustXpert lets you fine-tune your clustering, for example:

```bash
python clustxpert/clustering.py --dataset datasets/sample.csv --n_clusters 5 --init_method "kmeans++" --max_iter 200
```
You can configure:
✔ Number of clusters
✔ Initialization strategy (e.g., smart heuristics, custom seeds)
✔ Max iterations, distance metrics, categorical handling...
✔ Pre-processing methods


### 🚀 Deploying to Heroku (Optional, for API Integration)
```bash
heroku create clustxpert-app
git push heroku main
heroku ps:scale web=1
heroku open
```
This makes clustering models accessible via a FastAPI-based REST API.

### ✅ Running Tests Locally
#### ✅ Unit tests for benchmarking scripts:

```bash
pytest
```
#### ✅ Parallelized testing (for speed optimization):

```bash
pytest -n auto
```


## 🛠️ Technical Overview
| **Component**          | **Technology Used**              |
|----------------------|--------------------------------|
| **Data Processing** | Pandas, NumPy                 |
| **Experiment Tracking** | MLflow, Weights & Biases  |
| **Visualization**   | Matplotlib, Seaborn           |
| **Testing & Validation** | Pytest, Pytest-xdist    |
| **CI/CD**          | GitHub Actions                |
| **Containerization** | Docker, Docker Compose     |
| **Dataset Management** | DVC (Data Version Control) |
| **API & Deployment** | FastAPI, Heroku             |
| **Code Quality**    | Black, Ruff (pre-commit hooks) |



## **📚 Contributing & Support**
We welcome contributions! If you’d like to enhance clustxpert, please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## **📩 Contact**
For questions or contributions, reach out via [LinkedIn](https://www.linkedin.com/in/marcennaji) or open an issue on GitHub.

---

### 📜 License & Credits
ClustXpert is licensed under BSD-3.

Original Enneade: I developed the first version of Enneade under the supervision of Vincent Lemaire (Research Scientist and Research Program Manager at Orange Labs). This original version is still available as-is on the Khiops website, but it is not maintained and runs on an older version of Khiops.

ClustXpert is a fork that brings Enneade to the latest Khiops version, improving performance, maintainability, and usability.



