# Machine Learning Predictive Analytics for Diabetes

## Overview
This project leverages advanced machine learning techniques to predict diabetes risk using patient health data. It provides a robust pipeline for data preprocessing, model training, evaluation, and deployment. The solution is designed for scalability, reproducibility, and real-world applicability.

## Features
- Data preprocessing and feature scaling
- Model training and hyperparameter optimization
- Performance evaluation with metrics and visualizations
- Model serialization for deployment
- Interactive prediction via web or notebook
- Result saving and analysis

## Dataset
- **Source:** `diabetes_dataset.csv`
- **Description:** Contains patient health metrics and diabetes diagnosis labels.

## Installation
```bash
# Clone the repository
git clone https://github.com/Devnath03/Machine_Learning-Predictive-Analytics-for-Diabetes.git
cd Machine_Learning-Predictive-Analytics-for-Diabetes

# (Optional) Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
### Run the Application
```bash
python app.py
```
### Jupyter Notebook
Open `Diabetic Prediction.ipynb` for step-by-step analysis and interactive predictions.

## Model Architecture
- **Preprocessing:** StandardScaler
- **Model:** (e.g., RandomForestClassifier, LogisticRegression)
- **Serialization:** Models saved as `model.pickle`, scaler as `scaler.pickle`

## Graphical Analysis
Below are sample visualizations generated during analysis:

![Feature Importance](docs/feature_importance.png)
*Feature importance plot showing the most influential health metrics.*

![ROC Curve](docs/roc_curve.png)
*ROC curve illustrating model performance.*

## Results Overview
Results from model evaluation and predictions are saved for further analysis:
- **Accuracy:** 77.%

Saved results can be found in the `results/` directory or as output in the notebook.

## How to Save Results
Results and predictions can be saved using the following code snippet:
```python
import pandas as pd
results = pd.DataFrame({'Prediction': y_pred, 'Actual': y_test})
results.to_csv('results/predictions.csv', index=False)
```

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License.

## Contact
For questions or collaboration, contact [Devnath03](https://github.com/Devnath03).
