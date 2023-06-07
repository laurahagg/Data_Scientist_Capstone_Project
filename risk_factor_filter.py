import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

SEPSIS_DATA = "Maternal_Sepsis_by_Select_Risk_Factors__SPARCS__2016-2018.csv"

maternal_window = ["Pregnancy", "Delivery", "Postpartum"]

risk_factors = ['3rd or 4th degree tears',
 'ART',
 'Abnormal placentation',
 'Acute myocardial infarction',
 'Acute renal failure',
 'Adult respiratory distress syndrome',
 'Age Group',
 'Air and thrombotic embolism',
 'Alcohol abuse',
 'Amniotic fluid embolism',
 'Aneurysm',
 'Asthma',
 'Blood loss anaemia',
 'Blood products transfusion',
 'Cardiac arrest/ventricular fibrillation',
 'Cardiac arrhythmias',
 'Cardiac valvular disease',
 'Cerclage (rescue>prophylactic)',
 'Cesarean Delivery',
 'Chronic congestive heart failure',
 'Chronic ischemic heart disease',
 'Chronic pulmonary disease',
 'Chronic renal disease',
 'Coagulopathy',
 'Congenital heart disease',
 'Conversion of cardiac rhythm',
 'Cystic fibrosis',
 'Deficiency anaemia',
 'Depression',
 'Disseminated intravascular coagulation',
 'Drug abuse',
 'Eclampsia',
 'Education',
 'Episiotomy',
 'Fluid and electrolyte disorders',
 'Gestational diabetes mellitus',
 'Gestational hypertension',
 'Group B Strep Carrier',
 'Heart failure/arrest during surgery or procedure',
 'History of Sepsis (w/in 1yr prior to start of pregnancy)',
 'Human immunodeficiency virus',
 'Hypothyroidism',
 'Hysterectomy',
 'Illegal Drug Use',
 'Induction of Labor',
 'Liver disease',
 'Lymphoma',
 'Metastatic cancer',
 'Mild preeclampsia or unspecified preeclampsia',
 'Multiple Gestation',
 'Multiple gestation',
 'Nulliparity',
 'Obesity',
 'Obstetric Trauma',
 'Operative Vaginal Delivery',
 'Organ Transplant',
 'Other Immunosupression',
 'Other neurological disorders',
 'Paralysis',
 'Peptic ulcer disease, excluding bleeding',
 'Peripheral vascular disorders',
 'Placenta previa',
 'Postpartum hemorrhage',
 'Preexisting diabetes mellitus',
 'Preexisting hypertension',
 'Premature rupture of membranes',
 'Preterm Delivery',
 'Previous cesarean delivery',
 'Prolonged labor',
 'Psychoses',
 'Puerperal cerebrovascular disorders',
 'Pulmonary circulation disorders',
 'Pulmonary edema / Acute heart failure',
 'Pulmonary hypertension',
 'Race/Ethnicity',
 'Region of Residence',
 'Renal failure',
 'Retained Products of Conception',
 'Rheumatoid arthritis/collagen vascular diseases',
 'Severe anesthesia complications',
 'Severe preeclampsia/eclampsia',
 'Shock',
 'Sickle cell disease',
 'Sickle cell disease with crisis',
 'Solid tumour without metastasis',
 'Stillbirth',
 'Systemic lupus erythematosus',
 'Temporary tracheostomy',
 'Tobacco use',
 'Trimester Beginning Prenatal Care',
 'Uterine rupture',
 'Valvular disease',
 'Ventilation',
 'Weight loss']

sepsis_type = ["Any Sepsis", "Severe Sepsis"]

def get_filters():
    """
    Asks user to specify the maternal status, risk factor and sepsis to analyze.

    Returns:
        (str) maternal_window
        (str) risk_factor
        (str) sepsis
    """
    print("Hello! Let's explore the risk factors during maternity for a significant risk of sepsis!")

    # Get user input for maternal_window
    while True:
        maternal = input("Would you like to see the risk factor for Pregnancy, Delivery, or Postpartum?\n")
        if maternal in maternal_window:
            break
        else:
            print("Please enter a valid maternal window (Pregnancy, Delivery, or Postpartum).")

    # Get user input for risk factor
    while True:
        print("Available risk factors:")
        for index, factor in enumerate(risk_factors, start=1):
            print(f"{index}. {factor}")
        risk_index = input("Enter the index of the risk factor you are interested in: ")
        try:
            risk_index = int(risk_index)
            risk = risk_factors[risk_index - 1]
            break
        except (ValueError, IndexError):
            print("Please enter a valid index.")

    # Get user input for sepsis
    while True:
        sepsis = input("Would you like to analyze Any Sepsis or Severe Sepsis?\n")
        if sepsis in sepsis_type:
            break
        else:
            print("Please enter a valid sepsis type (Any Sepsis, Severe Sepsis).")

    print('-' * 40)
    return maternal, risk, sepsis


def load_data(maternal, risk):
    """
    Loads data for the specified maternal window and filters by risk factor and sepsis type.

    Args:
        (str) maternal -maternal window to analyze
        (str) risk - filtered risk factor
        (str) sepsis - filtered type of the sepsis: any sepsis or severe sepsis
    Returns:
        df - Pandas DataFrame containing maternal data filtered by risk factor and sepsis type
    """
    # Load data file into a DataFrame
    df = pd.read_csv(SEPSIS_DATA)
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace(',', '', regex=False)

    # Cleaning data types
    # Change the datatype of the p-value (any sepsis and severe sepsis) to a float
    df['Any_Sepsis_p-value'] = df['Any_Sepsis_p-value'].str.replace('<.0001', '0.0001').astype(float)
    df['Severe_Sepsis_p-value'] = df['Severe_Sepsis_p-value'].str.replace('<.0001', '0.0001').astype(float)

    # Filter by maternal_window
    df = df[df["Maternal_Window"] == maternal]

    # Filter by risk_factor
    df = df[df["Risk_Factor"] == risk]

    # Create 'Sepsis_Prediction' column and initialize with False
    df['Sepsis_Prediction'] = False

    return df



def risk_filter(df, sepsis_type):
    """
    Filters the data if the p-value < 0.05

    Args:
        (str) sepsis_type
        (DataFrame) df - Pandas DataFrame containing maternal data
    Returns:
        df - Pandas DataFrame containing maternal data filtered by risk factor and sepsis type
        Prediction if significant or not
    """

    # Define a significance threshold
    significance_threshold = 0.05

    # Predict sepsis probability based on the p-value
    if sepsis_type == 'Any Sepsis':
        df['Sepsis_Prediction'] = df['Any_Sepsis_p-value'] < significance_threshold
    elif sepsis_type == 'Severe Sepsis':
        df['Sepsis_Prediction'] = df['Severe_Sepsis_p-value'] < significance_threshold


    if df['Sepsis_Prediction'].any():
        print('With this combination there is a statistically significant risk of getting sepsis.')
    else:
        print('With this combination there is no statistically significant risk of getting sepsis.')

    # Display the resulting DataFrame
    return df


def main():
    while True:
        maternal, risk, sepsis = get_filters()
        df = load_data(maternal, risk)

        # Perform data analysis or display the filtered DataFrame as desired

        df = risk_filter(df, sepsis)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
