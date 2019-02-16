# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()

fig, ax = plt.subplots(figsize=(14,8))
loan_status.plot(kind='bar', ax=ax)


# --------------
#Code starts here

fig, ax = plt.subplots(figsize=(16,8))

property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False, ax=ax)
ax.set_xlabel('Property Area', fontsize=14)
ax.set_ylabel('Loan Status', fontsize=14)
ax.tick_params(axis='x', labelrotation=45)



# --------------
#Code starts here

fig, ax = plt.subplots(figsize=(16,8))

education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=True, ax=ax)
ax.set_xlabel('Education', fontsize=14)
ax.set_ylabel('Loan Status', fontsize=14)
ax.tick_params(axis='x', labelrotation=45)


# --------------
#Code starts here

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(20,10))
xlim, ylim = (-300, 1000), (0,0.015)

graduate = data.loc[data['Education'] == 'Graduate']
not_graduate = data.loc[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind='density', ax=ax1)
ax1.set_ylim(ylim)
ax1.set_xlim(xlim)
ax1.set_xlabel('Graduate - Loan Amount')

not_graduate['LoanAmount'].plot(kind='density', ax=ax2)
ax2.set_ylim(ylim)
ax2.set_xlim(xlim)
ax2.set_xlabel('Non Graduate - Loan Amount')











#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here


fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(20,10))

ax_1.scatter(data['ApplicantIncome'], data['LoanAmount'])
ax_1.set_title('Applicant Income')
ax_1.set_ylabel('Loan Amount')

ax_2.scatter(data['CoapplicantIncome'], data['LoanAmount'])
ax_2.set_title('Coapplicant Income')
ax_2.set_ylabel('Loan Amount')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'], data['LoanAmount'])
ax_3.set_title('Total Income')
ax_3.set_ylabel('Loan Amount')


