# ShipSail_EDA

## Full Name and Email Address
- Full Name: [Full Name]
- Email Address: [Email Address]

## Overview
This repository contains code for Task 2, which involves data preprocessing, model training, and evaluation for cruise data. The folder structure is as follows:
- `constants.py`: Defines constants used in the pipeline.
- `Preprocessing.py`: Contains functions for data ingestion and preprocessing.
- `Data_Cleaning_pipeline.py`: Implements the data cleaning pipeline.
- `Model.py`: Defines functions for creating MLP and Decision Tree classifiers.
- `training.py`: Executes the training process and evaluates the models.

## Instructions for Executing the Pipeline
To execute the pipeline:
1. Ensure all required libraries are installed (`pandas`, `numpy`, `scikit-learn`, `sqlite3`, `re`, `typing`, `matplotlib`, `seaborn`).
2. Run the `training.py` script.

## Description of Logical Steps/Flow
1. Data Ingestion: Load cruise data from SQLite databases using predefined paths.
2. Data Cleaning Pipeline: Perform data cleaning and preprocessing steps including cleaning cruise distance, imputing null values, encoding categorical variables, and splitting data into train and test sets.
3. Model Training: Train Multi-Layer Perceptron (MLP) and Decision Tree classifiers.
4. Model Evaluation: Evaluate the trained models using accuracy score.

## Overview of Key Findings from EDA
The EDA conducted in Task 1 revealed several insights:
- Distribution of genders across different ticket types.
- Relationship between ease of online booking ratings and ticket types.

## Processing of Features
The features in the dataset are processed as follows:
- Cleaned cruise distance column to extract numeric values.
- Imputed null values with mode for object columns and with mean for numerical columns.
- Dropped unnecessary columns such as logging and date of birth.
- Encoded categorical variables using LabelEncoder.
- Split data into train and test sets and standardized features.

## Choice of Models
Two models were chosen for training:
1. Multi-Layer Perceptron (MLP) Classifier: Suitable for complex non-linear relationships in the data.
2. Decision Tree Classifier: Provides interpretability and handles non-linear relationships well.

## Evaluation of Models
Both models were evaluated based on accuracy score:
- MLP Classifier achieved an accuracy score of [accuracy]%.
- Decision Tree Classifier achieved an accuracy score of [accuracy]%.
Both models performed well on the task.

## Other Considerations for Deploying Models
Additional considerations for deploying models may include:
- Model interpretability and explainability.
- Handling of missing data in real-time scenarios.
- Model performance monitoring and maintenance.
