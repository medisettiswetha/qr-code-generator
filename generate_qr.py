# qr-code-generator
!pip install qrcode[pil]

import qrcode

# Data to encode
data = "https://www.website.com"

# Generate the QR code
img = qrcode.make(data)

# Save it as an image
img.save("my_qrcode.png")

from IPython.display import Image
Image("my_qrcode.png")
