import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler

# Reads the dataset and saves only the features that are going to be worked on
data = pd.read_excel('Feline_dataset.xlsx', 'Dataset')
data = data.iloc[:, [1, 2, 3, 4, 5, 144, 145, 146, 147, 148, 149, 150]]

# Rename the first four columns and changes the "unkown" values for numpy nan
data = data.rename(columns={'BREEDGROUP':'breed_group', 'SEX': 'sex', 'AGE_BEHAVIOUR': 'age', 'OTHER_CATS': 'other_cats'})
data.replace('unknown', np.nan, inplace=True)

# Impute missing ages (127) with the mean of all existing values, then drops all ages older than 17.72 (6)
age_imp = SimpleImputer(missing_values=np.nan, strategy='mean')
data.age = age_imp.fit_transform(data[['age']])
data = data.drop(data[data.age >= 17.72].index)

# Distribution of Other Cats Column
# plt.figure()
# ax = sns.countplot(data=data, x='other_cats', palette='flare', hue='other_cats', legend=False)
# for p in ax.patches:
#     percentage = '{:.1f}%'.format(100 * p.get_height()/4316)
#     x = p.get_x() + p.get_width() / 2
#     y = p.get_height() + 15
#     ax.text(x, y, percentage, ha='center')
    
# plt.title('Distribution of "Other Cats" Column Before Imputing Missing Data')
# plt.show()

# Impute missing other_cats data (995) in a ratio of 80% YES and 20% NO, this to maintain the distribution of the existing data
data.other_cats = data['other_cats'].fillna(pd.Series(np.random.choice(['YES', 'NO'], p=[0.8, 0.2], size=len(data))))
data.other_cats = data['other_cats'].fillna('NO')
data.other_cats = data['other_cats'].map({'YES' : True, 'NO' : False})

# Transforms the problematic behavior column into a range of number using Ordinal Encoder
behaviors = ['No', 'A_little', 'Some', 'A_lot', np.nan]
enc = OrdinalEncoder(categories= [behaviors])
data.problematic_behavior = enc.fit_transform(data[['problematic_behavior']])

# Impute missing problematic_behavior data (995) using KNN imputation and the last seven features
knn = KNNImputer(n_neighbors=2)
data.iloc[:, 4:12] = knn.fit_transform(data.iloc[:, 4:12])
data.problematic_behavior = np.round(data.problematic_behavior)

# # Mann Whitney U test to compare the human sociability score of the group of households with just one cat 
# # and a sample of similar size of the group of households with more than one cat

total_p_values= 0
for i in range(5):
    no_cat = data[data['other_cats'] == False]['human_sociability']
    other_cat = data[data['other_cats'] == True]['human_sociability'].sample(700)
    stat, p_value = mannwhitneyu(other_cat, no_cat, alternative='two-sided')
    total_p_values += p_value
    print(f'Estadistico: {stat}')
    print(f'P-value: {p_value}')

    if (no_cat.median() > other_cat.median()):
        print(f'The median of the households with just one cat, {no_cat.median()}, is greater than the households with multiple cats, {other_cat.median()}')
        
    else:
        print(f'The median of the households with multiple cats, {other_cat.median()}, is greater than the households with just one cat, {no_cat.median()}')
        
print('Mean of P-value:', total_p_values/5)
