import streamlit as st

st.title('Loan Eligibility Prediction')

col1, col2, col3 = st.columns(3)

with col1:
    current_loan_amount = st.number_input('Current Loan Amount', min_value=0, max_value=100)
    term = st.selectbox('Term', options = ['Short Term', 'Long Term'])
    credit_score = st.number_input('Credit Score', min_value=0, max_value=100)
    year_in_job = st.selectbox('Year in Current Job', options = ['< 1 year', '1 year', '2 years', '3 years', '4 years', '5 years', '6 years',  '7 years', '8 years', '9 years', '10+ years'])
    home_ownership = st.selectbox('Home Ownership', options=['Rent', 'Home Mortgage', 'Own Home', 'HaveMortgage'])

with col2:
    purpose = st.selectbox('Purpose', options=['Debt Consolidation', 'Home Improvements', 'other',
       'Business Loan', 'small_business', 'Other', 'moving', 'Buy a Car',
       'Medical Bills', 'Buy House', 'Take a Trip', 'vacation',
       'major_purchase', 'Educational Expenses', 'wedding',
       'renewable_energy'])
    annual_income = st.number_input('Annual Income', min_value=0, max_value=100)
    maximum_open = st.number_input('Maximum open credit', min_value=0, max_value=1000)
    monthly_debt = st.number_input('Monthly debt', min_value=0, max_value=1000)
    current_credit_balance = st.number_input('Current credit balance', min_value=0, max_value=100)

with col3:
    year_of_credit_history = st.number_input('Year of credit history', min_value=0, max_value=1000)
    month_since_last_delinquent = st.number_input('Months Since last delinquent', min_value=0, max_value=10)
    number_of_open_account = st.number_input('Number of open account', min_value=0, max_value=100)
    number_of_credit_problem = st.number_input('Number of credit problems', min_value=0, max_value=10)
    bankrupties = st.number_input('Bankruptcies', min_value=0, max_value=7)

tax_liens = st.number_input('Tax Liens', min_value=0, max_value=15)

submit_button = st.button(label='Prediction', type='primary')

if submit_button:
    st.write(tax_liens)



