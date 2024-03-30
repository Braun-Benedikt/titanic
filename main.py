from data_cleaning import clean_data
from feature_engineering import feature_engineering
from model_training import evaluate_model, grid_search_logistic_regression
from sklearn.model_selection import train_test_split
import seaborn as sns


# Load Dataset
titanic_df = sns.load_dataset('titanic')

# Clean data
train_data = clean_data(titanic_df)

# Feature engineering
train_data = feature_engineering(train_data)

# Model and training
relevant_features = ['pclass', 'sex', 'age', 'family_size', 'fare']
X_train, X_val, y_train, y_val = train_test_split(train_data[relevant_features], train_data['survived'], test_size=0.2)
model = grid_search_logistic_regression(X_train, y_train)
evaluate_model(model, X_val, y_val)