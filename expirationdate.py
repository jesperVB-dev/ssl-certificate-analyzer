from datetime import datetime
from OpenSSL import crypto as c

cert = c.load_certificate(c.FILETYPE_PEM, file('pem.pem').read())
a=datetime.strptime(cert.get_notAfter(),"%Y%m%d%H%M%SZ")

print a