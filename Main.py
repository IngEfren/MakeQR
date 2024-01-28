# MODULOS PARA QUE EL CODIGO FUNCIONE
# pip install qrcode

# Importamos el modulo para trabajar con QRs
import qrcode

# Almacenamos el texto que queremos convertir a QR
TextToQR = "Prueba de funcionamiento"

# Generamos un codigo QR
qr = qrcode.make(TextToQR)

# Almacenamos la imagen del codigo QR
qr.save("Codigo.png")

# SECCION DE LINEA NO FUNCIONAL VISTA EN DOCUMENTACION ANTIGUA
# Mostramos el codigo QR
# qr.show("Codigo.png")