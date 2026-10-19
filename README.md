# 🔬 LPBF Porosity Prediction Using Machine Learning

### Machine Learning × Additive Manufacturing × Materials Science

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-red?logo=streamlit)](https://lpbf-porosity-prediction-nzegmuulkkbpjf6llxtc9cz.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange?logo=scikitlearn)](https://scikit-learn.org/)

**An end-to-end Machine Learning project that investigates the relationship between Laser Powder Bed Fusion (LPBF) processing parameters and XCT-measured porosity in AlSi10Mg components.**

🚀 **Live Application:** [Try the Porosity Prediction App](https://lpbf-porosity-prediction-nzegmuulkkbpjf6llxtc9cz.streamlit.app/)

💻 **GitHub Repository:** [View Source Code](https://github.com/aditya4444-star/LPBF-Porosity-Prediction)

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Engineering Background](#-engineering-background)
- [Project Objectives](#-project-objectives)
- [Dataset](#-dataset)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [Model Performance](#-model-performance)
- [Feature Importance](#-feature-importance)
- [Error Analysis](#-error-analysis)
- [Interactive Web Application](#-interactive-web-application)
- [Installation and Usage](#-installation-and-usage)
- [Project Structure](#-project-structure)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Technologies Used](#-technologies-used)
- [Author](#-author)

---

## 🔍 Project Overview

Additive manufacturing enables the production of complex components with greater geometric flexibility than many conventional manufacturing processes.

However, defects such as porosity can affect the quality and mechanical performance of additively manufactured components.

This project applies supervised Machine Learning to investigate whether selected LPBF processing parameters can be used to estimate the porosity measured using X-ray Computed Tomography (XCT).

A Random Forest Regressor is used as the primary prediction model and is integrated into an interactive Streamlit application.

The project covers the complete workflow, from exploratory data analysis and model development to evaluation and deployment.

## ⚙️ Engineering Background

### Laser Powder Bed Fusion (LPBF)

LPBF is an additive manufacturing process in which a laser selectively melts regions of a powder bed to produce a component layer by layer.

The resulting material quality depends on several interacting process parameters and material characteristics.

Porosity can arise through different mechanisms, including insufficient fusion between neighbouring melt tracks or layers and gas-related pore formation.

The relationship between processing parameters and porosity is nonlinear and depends on the material, machine, and experimental conditions.

Machine Learning provides a way to investigate these relationships using experimental data.

### Parameters Investigated

| Parameter | Symbol | Unit |
|---|---|---|
| Laser Power | P | W |
| Scanning Speed | v | mm/s |
| Hatch Spacing | h | mm |

**Prediction target:** XCT-measured porosity.

The interpretation and units of the target must follow the documentation of the original dataset.

## 🎯 Project Objectives

- Investigate relationships between LPBF processing parameters and measured porosity.
- Perform exploratory data analysis and visualisation.
- Develop and compare multiple regression algorithms.
- Evaluate predictive performance using appropriate regression metrics.
- Investigate feature importance and prediction errors.
- Build an interactive application for estimating porosity from user-provided processing parameters.
- Demonstrate an end-to-end Machine Learning workflow applied to Materials Engineering.

## 📊 Dataset

| Property | Description |
|---|---|
| Material | AlSi10Mg |
| Manufacturing process | Laser Powder Bed Fusion |
| Number of observations | 60 |
| Input features | Laser power, scanning speed, hatch spacing |
| Target variable | XCT-measured porosity |
| Problem type | Supervised regression |

The dataset contains processing parameters and their corresponding porosity measurements.

Because the dataset contains only 60 observations, the findings should be treated as preliminary. Additional experimental data would be required to establish how well the models generalise to new manufacturing conditions.

## 🧠 Machine Learning Workflow

The project follows these stages:

1. **Data Preparation**
   - Load and inspect the dataset.
   - Check data types and missing values.
   - Prepare the input features and target variable.

2. **Exploratory Data Analysis**
   - Examine distributions of the processing parameters.
   - Investigate relationships between individual parameters and porosity.
   - Identify unusual observations and potential nonlinear relationships.

3. **Model Development**
   - Linear Regression
   - Random Forest Regression
   - Gradient Boosting Regression

4. **Model Evaluation**
   - Mean Absolute Error (MAE)
   - Root Mean Squared Error (RMSE)
   - Coefficient of Determination (R²)

5. **Validation and Tuning**
   - Cross-validation
   - Random Forest hyperparameter tuning
   - Comparison of training, validation, and test performance

6. **Model Interpretation**
   - Feature importance analysis
   - Prediction error analysis
   - Investigation of errors for different porosity groups

7. **Deployment**
   - Save the trained model.
   - Build an interactive Streamlit application.
   - Deploy the application online.

## 📈 Model Performance

The following results were obtained on the held-out test split during development.

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 2.1210 | 2.8399 | 0.3114 |
| Random Forest Regressor | 1.5188 | 2.5707 | 0.4357 |
| Gradient Boosting Regressor | 1.7838 | 2.9890 | 0.2372 |

### Interpretation

- **Random Forest achieved the best test-set performance** among the three evaluated models.
- It produced the lowest MAE and RMSE and the highest R².
- Its test-set R² of 0.4357 indicates that the model explains approximately 43.6% of the variation in the target values for this evaluation split.
- The results indicate that the selected processing parameters alone do not fully explain the observed porosity variation.

These results are preliminary and depend on the dataset and evaluation split. They do not establish that the model will perform equally well on new experimental data.

### Cross-Validation

The original Random Forest model also produced the following cross-validation results during development:

| Metric | Value |
|---|---:|
| Mean cross-validation MAE | 1.6732 |
| Standard deviation of cross-validation MAE | 0.5382 |

The variation across folds highlights the uncertainty associated with evaluating a model on a small dataset.

Cross-validation results should be interpreted separately from the held-out test results.

## 🔬 Feature Importance

Feature importance analysis was performed to investigate the contribution of the processing parameters to the model's predictions.

The analysis considered:

- Laser power
- Scanning speed
- Hatch spacing

Feature importance can help identify which inputs the model relies on most heavily.

However, importance scores do not establish causation or prove that changing a particular parameter will improve material quality.

The relationship between processing parameters and porosity should also be interpreted using metallurgical principles and experimental evidence.

## 🧪 Error Analysis

Prediction errors were examined by comparing actual XCT-measured porosity with the model's predictions.

The analysis revealed that some high-porosity observations were substantially underestimated.

This is an important limitation because errors may not be uniform across the target range.

Possible reasons include:

- The small number of observations.
- Limited representation of high-porosity conditions.
- Nonlinear interactions between processing parameters.
- Additional physical variables not included in the dataset.

These possibilities require further investigation and should not be treated as established causes.

## 🌐 Interactive Web Application

The trained Random Forest model is integrated into a Streamlit application.

### Features

- Interactive input controls for laser power, scanning speed, and hatch spacing.
- On-demand porosity prediction.
- Display of the selected processing parameters and predicted result.
- Browser-based access without requiring users to run the notebook.

### Try the Application

**[🚀 Open the Live Porosity Prediction Application](https://lpbf-porosity-prediction-nzegmuulkkbpjf6llxtc9cz.streamlit.app/)**

The application is intended as an educational and experimental demonstration of Machine Learning applied to additive manufacturing.

Its predictions should not be used as manufacturing recommendations without further validation.

## 💻 Installation and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/aditya4444-star/LPBF-Porosity-Prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd LPBF-Porosity-Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application will be available at the local address displayed in the terminal, usually:

`http://localhost:8501`

The saved model file must be present in the expected location, and compatible library versions must be installed.

## 📁 Project Structure

```text
LPBF-Porosity-Prediction/
│
├── AMinML.ipynb
│   └── Exploratory analysis and machine learning experiments
│
├── app.py
│   └── Streamlit application
│
├── lpbf_porosity_cleaned.csv
│   └── Cleaned dataset
│
├── lpbf_porosity_model.pkl
│   └── Saved Random Forest model
│
├── requirements.txt
│   └── Project dependencies
│
├── README.md
│   └── Project documentation
│
└── .gitignore
    └── Files excluded from version control
```

## ⚠️ Limitations

- The dataset contains only 60 observations.
- The test-set R² is approximately 0.44, indicating limited predictive performance.
- Some high-porosity observations were substantially underestimated.
- The model uses only three processing parameters.
- Other factors, including layer thickness, material condition, machine characteristics, and scanning strategy, may influence porosity.
- The model has not been established as reliable for processing conditions outside those represented in the dataset.
- The physical meaning and units of the target must be interpreted according to the original dataset documentation.

**This project is a research and learning prototype, not a validated process-optimisation or manufacturing-quality assurance system.**

## 🚀 Future Improvements

Potential extensions include:

- Collecting a larger and more representative experimental dataset.
- Investigating additional LPBF parameters and material characteristics.
- Evaluating feature interactions and physically motivated features.
- Comparing additional regression algorithms.
- Using more robust validation strategies where the data structure permits.
- Quantifying prediction uncertainty.
- Investigating performance across different porosity ranges.
- Validating predictions against independent experimental measurements.
- Integrating physical knowledge of melt-pool behaviour into feature engineering and model interpretation.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit
- Git and GitHub

## 👨‍💻 Author

**Aditya Rajput**

This project explores the intersection of Materials Engineering, Additive Manufacturing, and Machine Learning.

### Project Links

- **GitHub:** [LPBF Porosity Prediction Repository](https://github.com/aditya4444-star/LPBF-Porosity-Prediction)
- **Live Application:** [Streamlit Porosity Prediction App](https://lpbf-porosity-prediction-nzegmuulkkbpjf6llxtc9cz.streamlit.app/)

---

*Built as a Machine Learning project exploring porosity prediction in Laser Powder Bed Fusion of AlSi10Mg.*