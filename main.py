from OpenSSL import crypto
from datetime import datetime
import chilkat

victem = "www.facebook.com"
victem_port = 443
chilkatGlob = chilkat.CkGlobal()
success = chilkatGlob.UnlockBundle("Anything for 30-day trial.")
if (success != True):
    print(chilkatGlob.lastErrorText())
    sys.exit()

http = chilkat.CkHttp()

sslCert = http.GetServerSslCert(victem,victem_port)
if (sslCert == None ):
    print(http.lastErrorText())
    sys.exit()

cert_file = 'D:\pem.pem'
cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())

def GetSAN(cert):
	SAN = cert.get_extension(2)
	print SAN

def GetCompany(cert):
	subject = cert.get_subject()
	company = subject.O
	print company

def Expiration(cert):
	expiration = datetime.strptime(cert.get_notAfter(),"%Y%m%d%H%M%SZ")

	print expiration

def SPKI(cert):
	print "SPKI Fingerprint with algorithm sha256 and encoding base64: " + sslCert.getSpkiFingerprint("sha256","base64")
	#print "SPKI Fingerprint with algorithm sha256 and encoding hex: " + sslCert.getSpkiFingerprint("sha256","hex")
	#print "SPKI Fingerprint with algorithm sha384 and encoding base64: " + sslCert.getSpkiFingerprint("sha384","base64")
	#print "SPKI Fingerprint with algorithm sha384 and encoding hex: " + sslCert.getSpkiFingerprint("sha384","hex")
	#print "SPKI Fingerprint with algorithm sha512 and encoding base64: " + sslCert.getSpkiFingerprint("sha512","base64")
	#print "SPKI Fingerprint with algorithm sha512 and encoding hex: " + sslCert.getSpkiFingerprint("sha512","hex")
	#print "SPKI Fingerprint with algorithm sha1 and encoding base64: " + sslCert.getSpkiFingerprint("sha1","base64")
	#print "SPKI Fingerprint with algorithm sha1 and encoding hex: " + sslCert.getSpkiFingerprint("sha1","hex")
	#print "SPKI Fingerprint with algorithm md2 and encoding base64: " + sslCert.getSpkiFingerprint("md2","base64")
	#print "SPKI Fingerprint with algorithm md2 and encoding hex: " + sslCert.getSpkiFingerprint("md2","hex")
	#print "SPKI Fingerprint with algorithm md5 and encoding base64: " + sslCert.getSpkiFingerprint("md5","base64")
	#print "SPKI Fingerprint with algorithm md5 and encoding hex: " + sslCert.getSpkiFingerprint("md5","hex")

def Issuer(cert):
	subject = cert.get_subject()
	issuer = cert.get_issuer()
	issued_by = issuer.CN

	print issued_by

def CommonName(cert):
	subject = cert.get_subject()
	issued_to = subject.CN

	print issued_to

def StartDate():
	start = datetime.strptime(cert.get_notBefore(),"%Y%m%d%H%M%SZ")
	
	print start

def main(cert):
	CommonName(cert)
	print "unknown fingerprint SHA256 (coming soon)"
	SPKI(cert)
	CommonName(cert)
	GetSAN(cert)
	StartDate()
	Expiration(cert)
	Issuer(cert)

main(cert)