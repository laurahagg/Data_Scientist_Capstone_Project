# Data_Scientist_Capstone_Project
Maternal Sepsis by Select Risk Factors


## Libraries
for the project the following libraries had been used:
Numpy, Pandas, Matplotlib, Seaborn


## Files in the Repository
The following files are in the repository:

Capstone_Project_Maternal_Health_Dicussion.pdf
In this text are discussed serveral questions about the dataset

Sepsis.ipynb
The jupyter notebook to answer the questions of the disussion file

risk_factor_filter.py
The programm to try yourself, if the risk factor is signicant

Maternal_Sepsis_by_Select_Risk_Factors__SPARCS__2016-2018.csv
The dataset

HDNY_MaternalSepsis_RiskFactors_DataDictionary_v2.pdf
The dictionary of the columns in the dataset

rows.json
a json file with further informations about the dataset

## Source of the dataset
I collected the data from the follwing homepage:
https://healthdata.gov/State/Maternal-Sepsis-by-Select-Risk-Factors-SPARCS-2016/gy4j-ef7j

## The dataset
The dataset contains information on the occurrence of maternal sepsis among live births during the pregnancy, delivery, and postpartum periods from 2016 to 2018. It provides counts, rates, and measures of association related to specific risk factors and the incidence of maternal sepsis, identified through administrative means.

## Questions to analyze
•	What are the ten most risk factors to get a sepsis during the maternal window?	
•	From this top ten, which are statistically significant (p-value < 0.05)?
•	What are the top ten risk factors with the highest incidence for a statistically significant sepsis (any or severe)?	
•	Is there a relationship between the Number of Live Births and the Sepsis Incidence?
•	Do other Risk Factors have a significant risk of getting a sepsis?

## Methods to answer the question:
Viusals (barplots, scatterplots)
Lists to compare the risk factors between the visuals


## Summary of the results of the Analysis
In total, 94 risk factors were examined in this dataset to determine if there is a statistically significant risk for any or severe sepsis. Here are the key insights from my exploration:
1.	None of the risk factors in the statistically significant top ten list are included in the list of most common risk factors. This indicates that the risk factors that are most commonly significant (represented by red bars) are not the same as the most frequently occurring risk factors.

2.	Demographic factors exhibit varying influences on the significance of developing sepsis. Younger women and those who initiate prenatal care after the first trimester appear to be as-sociated with significant risks of sepsis. Additionally, factors such as education, race/ethnicity, and region of residence have distinct impacts on sepsis significance. Further investigations are required to determine if any patterns exist within these factors.

3.	Risk factors with a very high incidence are rare, indicating a low number of live births associ-ated with them.


## Interactive programm
To analyze the statistical significance of a specific combination of maternal window, risk factor, and sepsis type in relation to the risk of developing sepsis, an interactive program is provided.

To run the program, follow the steps below:

1. Install Anaconda Prompt, if not already installed.
2. Open Anaconda Prompt.
3. Navigate to the directory where the program file "filter_risk_factor.py" is located.
4. Run the command python filter_risk_factor.py in the Anaconda Prompt.
5. Follow the prompts and provide the necessary inputs for the maternal window, risk factor, and sepsis type.
6. The program will analyze the combination and determine if it is statistically significant in relation to sepsis risk.
7. The program will provide the result indicating whether the combination is significant or not.

Enjoy using the program and exploring the significance of different combinations!

Please note that the accuracy and reliability of the program's results depend on the underlying data and statistical analysis methods used.

