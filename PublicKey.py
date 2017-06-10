from OpenSSL import crypto
from OpenSSL._util import lib as cryptolib


def pem_publickey(pkey):
    """ Format a public key as a PEM """
    bio = crypto._new_mem_buf()
    cryptolib.PEM_write_bio_PUBKEY(bio, pkey._pkey)
    return crypto._bio_to_string(bio)


key = crypto.PKey()
key.generate_key(crypto.TYPE_RSA, 2048)
print pem_publickey(key)