from OpenSSL import crypto

cert_file = 'D:\pem.pem'
cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
SAN = cert.get_extension(7)
SAN = str(SAN).split('CA ')

print SAN[0]