streamlit
matplotlib
numpy
pandas
pip install -r requirements.txt
pip install matplotlib
pip uninstall streamlit matplotlib
pip install streamlit matplotlib



import pandas as pd
import numpy as np
import warnings
import os
import joblib
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split, cross_val_predict, KFold
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier, RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, KFold
import numpy as np
import pandas as pd
from joblib import load
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
