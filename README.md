## spark-world

A personal environment for learning and experimenting with Apache Spark.

This repository is structured for project-based practice using PySpark, Jupyter, and Docker.

Explore, preprocess, and analyze large-scale data with scalable tools.

<br>

### 📁 Folder Structure
```
spark-world/
├── docs/                      # Spark-related study notes and concepts
│
├── projects/                  # Individual Spark-based projects
│   └── churn-prediction/      # Example project for customer churn prediction
│       ├── data/              # Raw and preprocessed datasets
│       ├── notebooks/         # Jupyter notebooks for EDA and experimentation
│       ├── scripts/           # PySpark scripts for ETL, modeling, evaluation
│       ├── Dockerfile         # Project-specific Docker environment
│       └── Makefile           # Automation commands for build/run/clean
│
├── docker-compose.yml         # Jupyter + PySpark development environment
├── requirements.txt           # Shared Python dependencies
└── README.md                  # Repository overview and usage instructions
```

<br>

### 💼 Projects

- **churn-prediction**: Predicting customer churn using PySpark-based preprocessing and Spark MLlib models.
