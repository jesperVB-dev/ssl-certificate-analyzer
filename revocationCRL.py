from OpenSSL import crypto

cert_file = 'D:\pem.pem'
cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
SAN = cert.get_extension(5)
SAN = str(SAN).split('Full ')

print SAN[1]