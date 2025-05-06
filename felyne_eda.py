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


def distribution_of_other_cats_column():
    # Distribution of Other Cats Column
    plt.figure()
    ax = sns.countplot(data=data, x='other_cats', palette='crest', hue='other_cats', legend=False)
    for p in ax.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height()/4316)
        x = p.get_x() + p.get_width() / 2
        y = p.get_height() + 15
        ax.text(x, y, percentage, ha='center')
        
    plt.xlabel('Is there other cats in the household?')
    plt.ylabel('Count')
    plt.title('Distribution of "Other Cats" Column Before Imputing Missing Data')
    plt.show()

def cats_per_breed_group():
    
    total_male = data[data['sex'] == 'Male'].shape[0]
    total_female = data[data['sex'] == 'Female'].shape[0]
    
    plt.figure(figsize=(20, 8))
    ax = sns.countplot(data=data, x=data['breed_group'], palette='crest', hue='sex')
    
    legend = ax.legend(
        labels=[f'Male ({total_male})', f'Female({total_female})'],
        loc='upper right',
        
    )
    
    plt.setp(ax.get_legend().get_texts(), fontsize = '14')
    ax.set_xticklabels(ax.xaxis.get_majorticklabels(), ha='right', rotation=45)
    
    plt.title('Number of Cats Per Breed Group', fontsize=16)
    plt.xlabel('Breed Group')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.show()
    
def cats_age_scatter_plot():
    
    ages = [0, 3.4, 6.8, 10.2, 13.6, 17]
    labels = ['0 - 3.4', '3.4 - 6.8', '6.8 - 10.2', '10.2 - 13.6', '13.6 - 17']
    data['age_group'] = pd.cut(data['age'], bins=ages, labels=labels)
    
    plt.figure(figsize=(12, 6))
    ax = sns.scatterplot(data=data, x='age', y='activity_playfulness', hue='age_group', palette='crest')
    
    legend = ax.legend(
        title='Age Group',
        loc='upper right',
    )
    
    plt.title('Activity/Playfulness of the Cats Based on Their Age', fontsize=16)
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Activity/Playfulness Score', fontsize=12)
    
    plt.show()

def human_sociability_other_cats():
    data_long = data.melt(id_vars='other_cats', 
                      value_vars=['human_sociability', 'cat_sociability'],
                      var_name='variable', 
                      value_name='score')

    plt.figure(figsize=(15, 6))
    ax = sns.violinplot(
        x='other_cats', 
        y='score', 
        hue='variable', 
        data=data_long, 
        palette={'human_sociability': '#a7cda7', 'cat_sociability': '#408390'},
        split=True,  
        inner='quartile',
        bw_method=0.2,
        gap=.1
    )
    
    handles, labels = ax.get_legend_handles_labels()
    new_labels = ['Human Sociability', 'Cat Sociability']
    ax.legend(handles, new_labels, title='Sociability Type')

    plt.title("Comparison of Sociability with Humans and Cats Based on Whether or Not There Are Other Cats in the Household", fontsize=14)
    plt.xlabel("Is There Other Cats in The Household?", fontsize=12)
    plt.ylabel("Score", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.show()

# ---------------------------------------------------- FEATURE ENGINEERING ----------------------------------------------------

# Impute missing ages (127) with the mean of all existing values, then drops all ages older than 17.72 (6)
age_imp = SimpleImputer(missing_values=np.nan, strategy='mean')
data.age = age_imp.fit_transform(data[['age']])
data = data.drop(data[data.age >= 17.72].index)

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

# ---------------------------------------------------- HYPOTHESIS ----------------------------------------------------

# Mann Whitney U test to compare the human sociability score of the group of households with just one cat 
# and a sample of similar size of the group of households with more than one cat

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
