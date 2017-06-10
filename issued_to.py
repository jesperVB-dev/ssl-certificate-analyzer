from OpenSSL import crypto

cert_file = 'D:\pem.pem'
cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
subject = cert.get_subject()
issued_to = subject.CN    # the Common Name field

print issued_to