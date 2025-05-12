**<h1>Exploratory Data Analysis for Machine Learning: Honors Peer-graded Assignment**</h1>
<h2>Main Objective</h2>
The main objective of this project is to explore the dataset given and try to find characteristics and relationships between the diferent parameters in the data with the objective to prove or not a hypothesis. The subject of the dataset that was used was the "Reliability and Validity of Seven Feline Behavior and Personality Traits" and its objective was to study the different personalities and behavior of over 4300 cats based on the answers of their owners using an online questionnaire, and study its validity and reliability. The feline personality and behavior include seven traits: 
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
  <li><b>other_cats:</b> there was 997 missing values, in this case we combined the <i>fillna</i> method from Pandas and the Numpy method <i>numpy.random.choice</i> using the parameter p, this allow us to add a distribution when filling the missing data, in this case the distribution was around 80/20, where "YES" is the majority of the data as seen in Figure 2, then the data was map to make a nominal transformation and change the values to True and False</li>
  <li><b>problematic_behavior:</b> once again there was 997 missing entries for this column, the values of this feature were a range of: No, A_little, Some, A_lot and np.nan, so first we transform the data into a range of numbers using Ordinal Encoder, now to impute the missing data we used the <i>KNN Imputer</i> from Scikit-Learn with two neighbors, and including the Seven Personality Traits in the input samples when fitting, this was done because out of all the columns those seven parameters didn't have missing data or needed any type of imputation</i></li>
</ol>
<div align="center">
  
  ![imagen](https://github.com/user-attachments/assets/889b0c32-b9b7-477a-9485-ffeabf706d77)<br>
  <i>Figure 1: console print showing that there is missing date in the columns age, other_cats and problematic_behavior</i><br><br>
</div>
<div align="center">

  ![Distribution of other cats](https://github.com/user-attachments/assets/aa2c23b7-f336-4c6a-9788-d5e4e757885f)
<br>
  <i>Figure 2: distribution of "other_cats" column before imputing the missing data</i><br><br>
</div>

In the case of the sex column we are going to leave the data as "Male" and "Female", this is done because the focus of the project is to prove or disprove a hypothesis, not to develop a model, so to facilitate readability we are going to leave the Strings, that is the sa,me reason why in the case of other_cats we change the values to a boolean and not to 1 and 0. The last seven columns represent the values of the traits, these were calculated based on the answers of the questionnaire and the ranges of each vary greatly as shown in the Figure 3, we decided to not normalize this data, mostly for lack of context, we don't know if a value of 0.5 is the same in humman_aggression as in activity_playfulness, the range in each one is very different and the calculations that were used for each are unknown, however for the hypothesis testing we are not going to need normalized columns, so this should not affect the result at the end.

Inspecting the skewness of the data it was decided to not change it, being the nature of the dataset a questionnaire for the owners of the cat, the skew or outliers that generate were from the bias of the owner and not that much about the data itself, for example: most owners didn’t feel like their cat had any problematic behavior, that caused a positive skew within that feature, changing that to a normal distribution would make that most cats have some problematic behavior and would ignore the input of the owners. In case of outliers, they were also untouched, most of the features with values that could be considered outliers were the factor scores, and those being calculation based on the behavior attributes means that they could provide valuable data and insight about special cases.
<div>

  ![imagen](https://github.com/user-attachments/assets/96ff3f92-79c0-4b0a-bc8c-ad827108da98)
<br>
  <i>Figure 3: description of the values of each of the seven traits of cats personality</i>
</div>

<h2>Insights</h2>
First by checking the different breed groups we can see that there are some much more common than others, for example Landrace Cat Shorthair is the most common one, followed by the House Cat, on the other hand, some breeds like the Turkish Van and the Persian and Exotic rarely appear, we also checked the distribution of the sex of the cats, showing that there is a more male cats that females, but with a difference of just 115, so there isn't really a inbalance problem, as seen in Figure 4.

<div align="center">

  ![Number of cats per breed group](https://github.com/user-attachments/assets/eb2fb5ac-db35-4119-a79b-27b4dd80ac81)
<br>
  <i>Figure 4: number of cats for each group order by their sex</i><br><br>
</div>

We then decided to check the relationship between the Activity/Playfulness Score and the Age of the cat, as seen in Figure 5, there is a line of the same value in the scatter plot around the age of 5, which was the data imputation for missing values ​​and the activity score of these cats varies between 1.5 and -4, this could mean that some of these cats could be much older than the given age, given that that lower score is much more common in cats in the 13.6 to 17 age group. Overall we can see that the older the cat gets, the lower is its score.

<div align="center">

 ![Activity of cats based on age](https://github.com/user-attachments/assets/3f0e1b9b-9afc-421a-b78d-1435bbdd2ef5)
<i>Figure 5: Activity/Playfulness Score based on the age of the cat</i>
</div>

Finally we checked how the Human and Cat Sociability Score changes based on whether or not there is another cat in the household, we found that in both cases, when there is another cat or not, the Human Sociability seems to be similar, but there is a considerable change with the Cat Sociability when there is more than one cat at home as seen in Figure 6.

<div align="center">

 ![Human Sociability based on other cats](https://github.com/user-attachments/assets/f4911eb5-0ae4-4778-8281-2bd530a7089a)
<i>Figure 6: Comparison of Sociability with Humans and Cats Based on Whether or Not There Are Other Cats in the Household</i>
</div>

<h2>Hypothesis and Significance Test</h2>
Having other cats in the household affects the “human sociability” score of the cat.
<ol>
	<li>
		 H0: Having other cat in the household doesn't affect the “human sociability” score.
	</li>
	<li>
		HA: Having other cat in the household affects the “human sociability” score of the cat.
	</li>
</ol>
<br>
The p-value for the significance level is going to be 0.05 and for the test we are going to use the Mann Whitney U test, this allows us to compare whether there is a difference between the two groups, with and without multiple cats in the household, is statistically significant and we don't have to worry about the normalization of the Human Sociability column. First we created two variable the dataset in two groups, this datasets store the Human Sociability score whether are more cats or not, but because of the difference in size between the groups, where there is more than five times the amount of household with more than one cat that those with just one, we are going to created multiple subsamples of 700 entries with the larger group. We are going to run the Man Whitney U Test multiple times and sum the p-value of each loop to a variable so we can get the mean of the p-value at the end, also we are going to compare the median of the Human Sociability Score of group with more than one cat and the one with just one cat, that way in each loop we can check if the sociability is also better or worse without being affected by outliers.

<div align="center">

 ![imagen](https://github.com/user-attachments/assets/2bc43d9b-18da-4cf8-ab94-c426012c847e)
<i>Figure 7: Code for the significant test</i>
</div>
<br>
The result of running the test 5 times were a a p-value between ~5.83e-08 and ~5.39e-05 with the mean being 1.25e-05. This means that in all the cases the p-value was smaller than the significance level p-value of 0.05, in other words, we can reject the null hypothesis and say that having another cat in the household affects the human sociability score of the cat. When comparing the median of each sample in the loop, all of them gave the same result, the median of the households with just one cat, 0.25, was greater that the household with multiple cats, that means that the human sociability score is better when there is just one cat.
<h2>Next Steps for Analyzing the Data </h2>
The results from the significance test may suggest that the household where cats have the company of other cats are not that dependent of their owners or humans, that doesn’t have to mean they don’t like their owners, but instead, that their social necessities can be satisfied by a feline companion. To further study this we could check the correlation of the groups with and without other cats, and the cat sociability feature, we could also check based on the age or breed group, the necessities of the cat may change depending of their age or if they need special cares for their health, for example: Sphynx cats doesn’t have hair, so they need special care for their skin like applying oils or even put clothes on them when the temperature drops, this could make a stronger bond with their owner even if there were other cats.
<h2>Quality of Dataset</h2>
There was enough to work with and impute the ones that were missing, the problem was maybe in columns like “other_cats”, being Boolean data the best option for imputing was to map while trying to maintain the same ratio, this means it’s likely that some data for cats that lived alone has been lost, this also adds skewness to that feature, also with the factor scores attributes there was some skewness and outliers, those being calculations means that the information is still valuable so there was no change for those values, but if we had the data of the equation used to calculate each score based on the answers of the behavioral question of the survey, then we could have a better insight of that data and even be able to change it imputing some missing data of the multiple behavioral questions.

<h2>Bibliography</h2>
Mikkola, S., Salonen, M., Hakanen, E., Sulkama, S., & Lohi, H. (2021). Feline behavior and personality survey data (Version 2). figshare. https://doi.org/10.6084/m9.figshare.14899077.v2
