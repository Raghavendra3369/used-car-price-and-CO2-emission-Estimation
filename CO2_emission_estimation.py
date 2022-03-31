import streamlit as st
import pickle
import numpy
import pandas as pd

model1 = pickle.load(open('model of CO2 Emission estimation.pkl', 'rb'))

def show_CO2_emission_estimation_page():
    st.title("CO2 Emission Estimation")
    st.write("""### Enter the details to estimate the CO2 emitted by the car""")

    names1 = ('Acura', 'Aston Martin', 'Audi', 'BMW', 'Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge',
            'Fiat', 'Ford', 'GMC', 'Honda', 'Hyundai', 'Infiniti', 'Jaguar', 'Jeep', 'Kia', 'Land Rover',
            'Lexus', 'Lincoln', 'Maserati', 'Mazda', 'Mercedes-Benz', 'Mini-Cooper', 'Mitsubishi', 'Nissan',
            'Porsche', 'RAM', 'Scion', 'Subaru', 'Toyota', 'Volkswagen', 'Volvo')

    fuel_types1 = ('Diesel', 'Petrol', 'Ethanol', 'Natural Gas')

    Name1 = st.selectbox("Select the Manufacturer", names1)
    Engine_size = st.number_input("Enter the size of the Engine in Liters", min_value=1.00, max_value=8.00, step=1.0, format="%.2f")
    Cylinder = st.number_input("Enter the number of Cylinder", min_value=4, max_value=10)
    Fuel_Type1 = st.selectbox("Select the Fuel type", fuel_types1)
    Mileage1 = st.number_input("Enter the Mileage in Kmpl", min_value=4.00, max_value=20.00, step=1.0, format="%.2f")

    FUELCONSUMPTION_COMB = 100 / Mileage1

    estimate1 = st.button("Estimate the CO2 Emitted")

    name1 = {'Acura': 0, 'Aston Martin': 1, 'Audi': 2 ,'BMW': 3, 'Buick': 4, 'Cadillac': 5, 'Chevrolet': 6,
             'Chrysler': 7, 'Dodge': 8, 'Fiat': 9, 'Ford': 10, 'GMC': 11, 'Honda': 12, 'Hyundai': 13,
             'Infiniti': 14, 'Jaguar': 15, 'Jeep': 16, 'Kia': 17, 'Land Rover': 18, 'Lexus': 19, 'Lincoln': 20,
             'Maserati': 21, 'Mazda': 22, 'Mercedes-Benz': 23, 'Mini-Cooper': 24, 'Mitsubishi': 25, 'Nissan': 26,
             'Porsche': 27, 'RAM': 28, 'Scion': 29, 'Subaru': 30, 'Toyota': 31, 'Volkswagen': 32, 'Volvo': 33}

    fuel_type1 = {'Diesel': 0, 'Ethanol': 1, 'Natural Gas': 2, 'Petrol': 3}

    if estimate1:
        input_query1 = pd.DataFrame(
            [[name1[Name1], float(Engine_size), int(Cylinder), fuel_type1[Fuel_Type1], float(FUELCONSUMPTION_COMB)]],
            columns=['MAKE', 'ENGINESIZE', 'CYLINDERS', 'FUELTYPE', 'FUELCONSUMPTION_COMB'])

        carbon_value = model1.predict(input_query1)[0]

        st.subheader(f"The estimated emission of CO2 by the car is {carbon_value:.2f} g/Km")
