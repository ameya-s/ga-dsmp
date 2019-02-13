# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

# code starts here

bank = pd.read_csv(path)

categorical_var = bank.select_dtypes('object')
print(categorical_var)

numerical_var = bank.select_dtypes('number')
print(numerical_var)



# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID', axis=1)

missing_values = banks.isnull().sum()
print(missing_values)

bank_mode = banks.mode()

banks.fillna(bank_mode.transpose().to_dict()[0], inplace=True)

print(banks.isnull().sum())
#code ends here



# --------------
# Code starts here

avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc='mean')
print(avg_loan_amount)


# code ends here



# --------------
# code starts here

loan_approved_se = banks.loc[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]

loan_approved_nse = banks.loc[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]

percentage_se = len(loan_approved_se)*100.00/len(banks)
percentage_nse = len(loan_approved_nse)*100.00/len(banks)

# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term']/12

big_loan_term = len(loan_term[loan_term >= 25])



# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()


# code ends here


