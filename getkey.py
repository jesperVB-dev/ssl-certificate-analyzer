import sys
import chilkat

victem = str(raw_input("Enter victem adress: "))
victem_port = int(raw_input("Enter victem port: "))

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

print("SPKI Fingerprint with algorithm sha256 and encoding base64: " + sslCert.getSpkiFingerprint("sha256","base64"))
print("SPKI Fingerprint with algorithm sha256 and encoding hex: " + sslCert.getSpkiFingerprint("sha256","hex"))
print("SPKI Fingerprint with algorithm sha384 and encoding base64: " + sslCert.getSpkiFingerprint("sha384","base64"))
print("SPKI Fingerprint with algorithm sha384 and encoding hex: " + sslCert.getSpkiFingerprint("sha384","hex"))
print("SPKI Fingerprint with algorithm sha512 and encoding base64: " + sslCert.getSpkiFingerprint("sha512","base64"))
print("SPKI Fingerprint with algorithm sha512 and encoding hex: " + sslCert.getSpkiFingerprint("sha512","hex"))
print("SPKI Fingerprint with algorithm sha1 and encoding base64: " + sslCert.getSpkiFingerprint("sha1","base64"))
print("SPKI Fingerprint with algorithm sha1 and encoding hex: " + sslCert.getSpkiFingerprint("sha1","hex"))
print("SPKI Fingerprint with algorithm md2 and encoding base64: " + sslCert.getSpkiFingerprint("md2","base64"))
print("SPKI Fingerprint with algorithm md2 and encoding hex: " + sslCert.getSpkiFingerprint("md2","hex"))
print("SPKI Fingerprint with algorithm md5 and encoding base64: " + sslCert.getSpkiFingerprint("md5","base64"))
print("SPKI Fingerprint with algorithm md5 and encoding hex: " + sslCert.getSpkiFingerprint("md5","hex"))
