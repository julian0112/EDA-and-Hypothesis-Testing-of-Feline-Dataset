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
The initial plan for the data exploration was to check the different columns and review which were relevant to work with. After that transform features like the “OTHER_CAT”
column with One-Hot encoding and “problematic_behavior” into a range using ordinal encoder. Once all the relevant features are into a better format, start to work with the missing data, reviewing the best ways to impute the data of the different types of features, then check for skew data and outliers, finally check for correlation between the different attributes using plots.

