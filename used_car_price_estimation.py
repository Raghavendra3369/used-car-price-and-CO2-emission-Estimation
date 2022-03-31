import streamlit as st
import pickle
import numpy
import pandas as pd

model = pickle.load(open('model of used car price estimation.pkl', 'rb'))

def show_used_car_price_estimation_page():
    st.title("Used Car Price Estimation")
    st.write("""### Enter the details to estimate the price of the car""")

    names = ('Audi', 'BMW', 'Chevrolet', 'Datsun', 'Fiat', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 'Jeep',
             'Land Rover','Mahindra', 'Maruti', 'Mercedes Benz', 'Mini Cooper', 'Mitsubishi', 'Nissan',
             'Porsche', 'Renault', 'Skoda', 'Tata', 'Toyota', 'Volkswagen', 'Volvo')

    fuel_types = ('Diesel', 'Petrol', 'LPG', 'CNG')

    owner_types = ('First', 'Second', 'Third', 'Fourth & above')

    Name = st.selectbox("Select the Manufacturer", names)
    Kilometers_Driven = st.number_input("Enter the Kilometers driven", min_value=1000, max_value=500000, step=500)
    Fuel_Type = st.selectbox("Select the Fuel type", fuel_types)
    Owner_Type = st.selectbox("Select the type of Owner", owner_types)
    Mileage = st.number_input("Enter the Mileage in Kmpl",min_value=1.00,max_value=35.00,step=1.0, format="%.2f")
    Engine = st.number_input("Enter the Size of the Engine in cc", min_value=620, max_value=5400)
    Power = st.number_input("Enter the Power in bhp",min_value=30.00,max_value=500.00,step=10.0, format="%.2f")
    Seats = st.number_input("Enter the number of Seats", min_value=1, max_value=10, step=1)
    Car_age = st.number_input("Enter the Age of the car in years", min_value=3, max_value=22, step=1)

    estimate = st.button("Estimate the price")

    name = {'Audi': 0, 'BMW': 1, 'Chevrolet': 2, 'Datsun': 3, 'Fiat': 4, 'Ford': 5, 'Honda': 6, 'Hyundai': 7,
            'Jaguar': 8, 'Jeep': 9,'Land Rover': 10, 'Mahindra': 11, 'Maruti': 12, 'Mercedes Benz': 13,
            'Mini Cooper': 14, 'Mitsubishi': 15, 'Nissan': 16, 'Porsche': 17, 'Renault': 18, 'Skoda': 19,
            'Tata': 20, 'Toyota': 21, 'Volkswagen': 22, 'Volvo': 23}

    fuel_type = {'CNG': 0, 'Diesel': 1, 'LPG': 2, 'Petrol': 3}

    owner_type = {'First': 0, 'Fourth & above': 1, 'Second': 2, 'Third': 3}

    if estimate:
        input_query = pd.DataFrame([[name[Name], int(Kilometers_Driven), fuel_type[Fuel_Type], owner_type[Owner_Type],
                                     float(Mileage), int(Engine), float(Power), int(Seats), int(Car_age)]],
                                   columns=['Name', 'Kilometers_Driven', 'Fuel_Type', 'Owner_Type', 'Mileage', 'Engine',
                                            'Power', 'Seats', 'Car_age'])

        price = model.predict(input_query)[0]

        st.subheader(f"The estimated Price of the car is {price:.2f} lakh rupees")


