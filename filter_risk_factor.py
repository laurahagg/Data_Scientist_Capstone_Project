
import pandas as pd
import numpy as np

SEPSIS_DATA = "Maternal_Sepsis_by_Select_Risk_Factors__SPARCS__2016-2018.csv"

# provide lists with the options for cities, months and days
maternal_window = ["Pregnancy", "Delivery", "Postpartum"]
risk_factor= ['diabetes', 'high blood pressure']
sepsis_type = ["any sepsis", "severe sepsis"]


def get_filters():
    """
    Asks user to specify the maternal status, risk factor and sepsis to analyze.

    Returns:
        (str) maternal_window
        (str) risk_factor
        (str) sepsis
    """
    print('Hello! Let\'s explore the risk factors during maternity for a significant risk of sepsis!')

    # get user input for maternal_window
    while True:
        maternal = input("Would you like to see the risk factor for Pregnancy, Delivery or Postpartum?\n")
        if maternal in maternal_window:
            break
        else:
            print("You made a typing error. Please enter the right Maternal Window.")




    # get user input for risk factor
    while True:
        risk = input("In Which Risk Factor are you interested in?\n Here is a List of the Risk Factors you can choose:\n - Diabetes\n - High Blood Pressure\n ")
        if risk in risk_factor:
            break
        else:
            print("You made a typing error. Please enter the right Risk Factor.")


    # get user input for sepsis
    while True:
        sepsis = input("Would you like to have the risk for Any Sepsis or for a Severe Sepsis \n")
        if sepsis in sepsis_type:
            break
        else:
            print("You made a typing error. Please enter the right type of the sepsis.")

    print('-'*40)
    return maternal, risk, sepsis


def load_data(maternal, risk, sepsis):
    """
    Loads data for the specified maternal window and filters by risk factor and sepsis type.

    Args:
        (str) maternal -maternal window to analyze
        (str) risk - filtered risk factor
        (str) sepsis - filtered type of the sepsis: any sepsis or severe sepsis
    Returns:
        df - Pandas DataFrame containing maternal data filtered by risk factor and sepsis type
    """
     # load data file into a dataframe
    df = pd.read_csv(SEPSIS_DATA[maternal])






     

     # filter by risk_factor
    df = df[df["Risk_Factor"] == risk]

    return df





def main():
    while True:
        maternal, risk, sepsis = get_filters()
        df = load_data(maternal, risk, sepsis)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
