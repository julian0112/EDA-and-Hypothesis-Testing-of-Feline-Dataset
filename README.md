**<h1>Exploratory Data Analysis for Machine Learning: Honors Peer-graded Assignment**</h1>
<h2>Main Objective</h2>
The main objective of this project is to explore the dataset given and try to find characteristics and relationships between the diferent parameters in the data with the objective to prove or not a hypothesis. The subject of te dataset that was used was the "Reliability and Validity of Seven Feline Behavior and Personality Traits" and its objective was to study the different personalities and behavior of over 4300 cats based on the answers of their owners using an online questionnaire, and study its validity and reliability. The feline personality and behavior include seven traits: 
<br>
<br>
<ol>
  <li>Fearfulness</li>
  <li>Activity/Playfulness</li>
  <li>Aggression Toward Humans</li>
  <li>Sociability Toward Humans</li>
  <li>Sociability Toward Cats</li>
  <li>Excessive Grooming</li>
  <li>Litterbox Issues</li>
</ol>

<h2>Attributes Summary</h2>
The twelve features that are the focus of the project are going to be:
<ol>
  <li><b>Breedgroup:</b> defines the breed group of the cat, there is twenty-six different groups, those being: “Landrace cat shorthair”, “Landrace cat longhair”, “House cat”, “European”, “Maine Coon”, “Bengal”, “Siberian and Neva Masquerade”, “Oriental”, “Sphynx and Devon Rex”, “Abyssinian”, “Ocicat”, “British”, “Norwegian Forest Cat”, “Sacred Birman”, “Cornish Rex”, “Russian Blue”, “American Curl”, “Somali”, “Siamese and Balinese”, “Burmese”, “Turkish Angora”, “Korat”, “Persian and Exotic”, “Turkish Van”, and “Others”.</li>
  <li><b>Sex:</b> defines the sex of the cat where it could be “Male” or “Female.</li>
  <li><b>Age Behavior:</b> defines the age when the personality section was answered, its values are continuous and in years.</li>
  <li><b>Other Cats:</b> defines if there are other cats in the same household, its values could be “Yes” or “No”.</li>
  <li><b>Problematic Behavior:</b> defines if the owner feels if the cat has any problematic or unwanted behavior, its values could be: “No”, “A little”, “Some”, “A lot”.</li>
  <li><b>Fearfulness:</b> one of the personality traits, defines a factor score calculated using the answers from the survey, its values are continuous, where the higher score indicate a higher fearfulness.</li>
  <li><b>Human Aggression:</b> one of the personality traits, defines a factor score calculated using the answers from the survey, its values are continuous, where the higher score indicate a higher aggression towards humans.</li>
  <li><b>Activity/Playfulness:</b> one of the personality traits, defines a factor score calculated using the answers from the survey, its values are continuous, where the higher score indicate a higher activity/playfulness.</li>
  <li><b>Cat Sociability:</b> one of the personality traits, defines a factor score calculated using the answers from the survey, its values are continuous, where the higher score indicate a higher sociability towards cats.</li>
  <li><b>Human Sociability:</b> one of the personality traits, defines a factor score calculated using the answers from the survey, its values are continuous, where the higher score indicate a higher sociability towards humans.</li>
  <li><b>Litterbox Issues:</b> one of the personality traits, defines a factor score calculated using the answers from the survey, its values are continuous, where the higher score indicate more litterbox issues.</li>
  <li><b>Excessive Grooming:</b> one of the personality traits, defines a factor score calculated using the answers from the survey, its values are continuous, where the higher score indicate more excessive grooming.</li>
</ol>
<h2>Initial Plan for Data Exploration</h2>
The initial plan for the data exploration was to check the different columns and review which were relevant to work with. After that transform features like the “other_cats” column with One-Hot encoding and “problematic_behavior” into a range using ordinal encoder. Once all the relevant features are into a better format, start to work with the missing data, reviewing the best ways to impute the data of the different types of features, then check for skew data and outliers, finally check for correlation between the different attributes using plots.

<h2>Data Cleaning and Feature Engineering</h2>
First we created a copy of the dataset with only the features that are going to be used for the project, once this is done we ran the info from Pandas and noticed that there are three columns with missing data as seen in Figure 1, so first we changed the String "unknown" to numpy.nan and made the next changes:
<ol>
  <li><b>age:</b> there was 123 missing entries, so we used the <i>Simple Imputer</i> from Scikit-Learn to replace the missing data with the mean of the column, which was 5.82</li>
  <li><b>other_cats:</b> there was 997 missing values, in this case we combined the <i>fillna</i> method from Pandas and the Numpy method <i>numpy.random.choice</i> using the parameter p, this allow us to add a distribution when filling the missing data, in this case the distribution was around 80/20, where "YES" is the majority of the data as seen in Figure 2, then the data was map to change the value to boolen</li>
  <li><b>problematic_behavior:</b> once again there was 997 missing entries for this column, the values of this feature were a range of: No, A_little, Some, A_lot and np.nan, so first we transform the data into a range of numbers using Ordinal Encoder, now to impute the missing data we used the <i>KNN Imputer</i> from Scikit-Learn with two neighbors, and including the Seven Personality Traits in the input samples when fitting, this was done because out of all the columns those seven parameters didn't have missing data or needed any type of imputation</i></li>
</ol>
<div align="center">
  
  ![imagen](https://github.com/user-attachments/assets/889b0c32-b9b7-477a-9485-ffeabf706d77)<br>
  <i>Figure 1: console print showing that there is missing date in the columns age, other_cats and problematic_behavior</i><br><br>
</div>
<div align="center">

  ![Distribution of other cats before imputing](https://github.com/user-attachments/assets/54245527-85ad-41de-a4cc-87f86af2bb10)<br>
  <i>Figure 2: distribution of "other_cats" column before imputing the missing data</i><br><br>
</div>

Inspecting the skewness of the data it was decided to not change it, being the nature of the dataset a questionnaire for the owners of the cat, the skew or outliers that generate were from the bias of the owner and not that much about the data itself, for example: most owners didn’t feel like their cat had any problematic behavior, that caused a positive skew within that feature, changing that to a normal distribution would make that most cats have some problematic behavior and would ignore the input of the owners. In case of outliers, they were also untouched, most of the features with values that could be considered outliers were the factor scores, and those being calculation based on the behavior attributes means that they could provide valuable data and insight about special cases.

<h2>Insights</h2>




