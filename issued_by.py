from OpenSSL import crypto

cert_file = 'D:\pem.pem'
cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
subject = cert.get_subject()
issuer = cert.get_issuer()
issued_by = issuer.CN

print issued_by