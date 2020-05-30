# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle


#dataset = pd.read_csv('AirQualityUCI.csv')

#dataset = pd.read_excel('AirQualityUCI.xlsx')
dataset = pd.read_csv('placements.csv')

'''import seaborn as sns
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
sns.set(style='whitegrid', context='notebook')
features_plot = ['C6H6(GT)', 'RH', 'AH', 'PT08.S1(CO)']


data_to_plot = dataset[features_plot]
data_to_plot = scalar.fit_transform(data_to_plot)
data_to_plot = pd.DataFrame(data_to_plot)

sns.pairplot(data_to_plot, size=2.0);
plt.tight_layout()
plt.show()
'''




#dataset['Date'].fillna(0, inplace=True)

#dataset['Time'].fillna(dataset['test_score'].mean(), inplace=True)

dataset.dropna(axis=0, how='all')

#X = dataset.iloc[:, :17]




features = dataset.values[:,:4]

'''features = features.drop('Date', axis=1)
features = features.drop('Time', axis=1)
features = features.drop('C6H6(GT)', axis=1)
features = features.drop('PT08.S4(NO2)', axis=1)'''

labels = dataset['Company Tier'].values

#features = features.values

#from sklearn.cross_validation import train_test_split


#X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
#regressor.fit(X_train, y_train)
regressor.fit(features, labels)





# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(int(model.predict([[2, 9, 7, 7]])))
