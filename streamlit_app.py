import streamlit as st
from datetime import datetime

def generate_receipt():
    # CSS styling - using proper string formatting
    st.markdown("""
    <style>
        .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            font-family: Arial, sans-serif;
            line-height: 1.2;
        }
        .header {
            text-align: center;
            margin-bottom: 10px;
        }
        .logo {
            font-size: 24px;
            font-weight: bold;
            color: #007bff;
        }
        .title {
            font-size: 18px;
            font-weight: bold;
            margin: 5px 0;
        }
        .subheader {
            font-size: 12px;
            margin: 2px 0;
            display: flex;
            justify-content: space-between;
        }
        .details, .location, .payment {
            margin: 10px 0;
        }
        .details dt {
            font-weight: bold;
            margin-top: 5px;
        }
        .details dd {
            margin-left: 20px;
            margin-bottom: 5px;
        }
        .location p {
            margin: 2px 0 2px 20px;
        }
        .location .bold {
            margin-left: 0;
        }
        .table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }
        .table th, .table td {
            border: 1px solid #000;
            padding: 5px;
            text-align: left;
        }
        .table th {
            background-color: #f2f2f2;
        }
        .payment {
            display: flex;
            justify-content: space-between;
            margin-top: 15px;
        }
        .bold {
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    # Receipt data - you could make these dynamic with Streamlit inputs
    invoice_number = "PE2508052313221hzl"
    current_date = datetime.now().strftime("%B %d, %Y")
    customer_name = "Kenny Mendo"
    ride_type = "Viaje urbano"
    driver_name = "Jhonny Francisco Pumallocia Romero"
    car_details = "black Toyota Rush BXM660"
    pickup_location = "Jr. Centenario 159, Lima, Lima Province, Peru"
    dropoff_location = "Av. Alfredo Mendiola 3697, Lima, Lima Province, Peru"
    pickup_time = "6:23 PM, August 5, 2025"
    dropoff_time = "8:11 PM, August 5, 2025"
    distance = "21.2 km"
    ride_fare = "S/ 78.00"
    payment_method = "Transferencia"
    total_amount = "S/ 78.00"

    # Receipt HTML
    receipt_html = f"""
    <div class="container">
        <div class="header">
            <div class="logo">inDrive</div>
            <div class="title">Recibo por tu servicio</div>
            <div class="subheader">Número de factura: {invoice_number} <span>Fecha: {current_date}</span></div>
        </div>

        <div class="details">
            <p class="bold">Para: {customer_name}</p>
            <dl>
                <dt>Tipo de solicitud:</dt><dd>{ride_type}</dd>
                <dt>Nombre del conductor:</dt><dd>{driver_name}</dd>
                <dt>Detalles del auto:</dt><dd>{car_details}</dd>
                <dt>Fecha del viaje:</dt><dd>{current_date}</dd>
            </dl>
        </div>

        <div class="location">
            <p class="bold">Recogida:</p>
            <p>{pickup_location}</p>
            <p>{pickup_time}</p>
        </div>

        <div class="location">
            <p class="bold">Dejada:</p>
            <p>{dropoff_location}</p>
            <p>{dropoff_time}</p>
        </div>

        <div class="location">
            <p class="bold">Distancia:</p>
            <p>{distance}</p>
        </div>

        <table class="table">
            <tr>
                <th>Descripción</th>
                <th>Monto</th>
            </tr>
            <tr>
                <td>Tarifa del viaje (incluye impuestos)</td>
                <td>{ride_fare}</td>
            </tr>
        </table>

        <div class="payment">
            <p class="bold">Método de pago: {payment_method}</p>
            <p class="bold">Monto total: {total_amount}</p>
        </div>
    </div>
    """

    # Display the receipt
    st.markdown(receipt_html, unsafe_allow_html=True)

# Streamlit app layout
st.set_page_config(page_title="Generador de Recibos", layout="centered")
st.title("Generador de Recibos inDrive")
generate_receipt()