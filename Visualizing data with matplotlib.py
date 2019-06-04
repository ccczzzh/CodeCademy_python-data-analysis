# Load modules
import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv('page_visits.csv')

# Calculate survey results
survey_results = df.groupby('website_goal')\
  	.first_name.count()
  
# Make a pie chart
plt.pie(survey_results.values,
        labels=survey_results.index,
        autopct='%d%%'
       )
plt.title('Why do citizens visit our website?')
plt.axis('equal')

# Paste code here:
plt.show()
