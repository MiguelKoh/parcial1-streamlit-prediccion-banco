import datetime
import streamlit as st
import accessAPI as servicio

st.set_page_config(
    page_title="Mi aplicación"
)
st.title("Formulario")
with st.form('my_form'):

    age = st.number_input("Age", min_value=17, max_value=100)

    job = st.selectbox(
        'Job',
        ('','admin', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services',
         'student','technician', 'unemployed', 'unknown'))

    marital = st.selectbox(
        'Marital',
        ('','married', 'divorced', 'single', 'unknown'))

    education = st.selectbox(
        'Education',
        ('','basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree',
         'unknown'))
    default = st.selectbox(
        'Default',
        ('','yes', 'no', 'unkown'))

    housing = st.selectbox(
        'Casa',
        ('','yes', 'no', 'unkown'))

    loan = st.selectbox(
        'Loan',
        ('','yes', 'no', 'unkown'))

    contact = st.selectbox(
        'Contact',
        ('','cellular', 'telephone'))

    month = st.selectbox(
        'Month',
        ('','apr', 'aug','dec','jul','jun','mar','mar','mar','may','nov','oct','sep'))

    dayOfWeek = st.selectbox(
        'Day of Week',
        ('','mon', 'tue', 'wed', 'thu', 'fri'))

    duration = st.number_input("Duration", min_value=1, max_value=5000, value=1)

    campaign = st.number_input("Campaing", min_value=1, max_value=100, value=1)

    pdays = st.number_input("pdays", min_value=1, max_value=999)

    previous = st.number_input("previous", min_value=0, max_value=7)

    poutcome = st.selectbox(
        'poutcome',
        ('','failure', 'nonexistent', 'success'))

    empVarRate = st.number_input("EmpVarRate", min_value=-10.0, max_value=10.0, value=0.0)

    consPriceIdx = st.number_input("Cons Price Idx", min_value=-1.000, max_value=100.000,value=1.000)

    consConfIdx = st.number_input("Cons Conf Idx", min_value=-100.0, max_value=100.0,value=0.0)

    euribor3m = st.number_input("Euribor3m", min_value=0.000, max_value=10.000,value=0.000)

    nrEmployed = st.number_input("Nr.employedx", max_value=6000.0,value=0.0)

    submitted = st.form_submit_button("llamar servicio")

    if submitted:
        result = servicio.llamarServicio(age,job,marital,education,default,housing,loan,contact,month,dayOfWeek,duration,campaign,pdays,previous,poutcome
                   ,empVarRate,consPriceIdx,consConfIdx,euribor3m,nrEmployed)
        if result == "no":
         st.write("Resultado: ", result," se aprueba el credito")
        elif result == "yes":
            st.write("Resultado: si se aprueba el credito")




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
