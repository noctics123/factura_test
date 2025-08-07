<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recibo por tu servicio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            line-height: 1.2;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            margin-bottom: 10px;
        }
        .logo {
            font-size: 40px;
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
            margin: 0 0 5px 20px;
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
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">inDrive</div>
            <div class="title">Recibo por tu servicio</div>
            <div class="subheader">Número de factura: PE2508052313221hzl <span>Fecha: August 5, 2025</span></div>
        </div>

        <div class="details">
            <p class="bold">Para: Kenny Mendo</p>
            <dl>
                <dt>Tipo de solicitud:</dt><dd>Viaje urbano</dd>
                <dt>Nombre del conductor:</dt><dd>Jhonny Francisco Pumallocia Romero</dd>
                <dt>Detalles del auto:</dt><dd>black Toyota Rush BXM660</dd>
                <dt>Fecha del viaje:</dt><dd>August 5, 2025</dd>
            </dl>
        </div>

        <div class="location">
            <p class="bold">Recogida:</p>
            <p>Jr. Centenario 159, Lima, Lima Province, Peru</p>
            <p>6:23 PM, August 5, 2025</p>
        </div>

        <div class="location">
            <p class="bold">Dejada:</p>
            <p>Av. Alfredo Mendiola 3697, Lima, Lima Province, Peru</p>
            <p>8:11 PM, August 5, 2025</p>
        </div>

        <div class="location">
            <p class="bold">Distancia:</p>
            <p>21.2 km</p>
        </div>

        <table class="table">
            <tr>
                <th>Descripción</th>
                <th>Monto</th>
            </tr>
            <tr>
                <td>Tarifa del viaje (incluye impuestos)</td>
                <td>S/ 78.00</td>
            </tr>
        </table>

        <div class="payment">
            <p class="bold">Método de pago: Transferencia</p>
            <p class="bold">Monto total: S/ 78.00</p>
        </div>
    </div>

    <script>
        // Optional: Ensure layout adjusts on load
        window.onload = function() {
            document.body.style.margin = '20px';
        };
    </script>
</body>
</html>