import base64
from Crypto.Cipher import AES

class PasswordSecurity(object):
	
	def __init__(self):
		self.key = self._generate_key()
		self.password = None

	
	def _generate_key(self):
		master_key = 'blahblahblahblahblahblah'
		return AES.new(master_key[:32])

	
	def _encrypt_val(self, cleartext):
		tag_string = (str(cleartext) +
						(AES.block_size -
						len(str(cleartext)) % AES.block_size) * "\0")
		cipher_text = base64.b64encode(self.key.encrypt(tag_string))

		return cipher_text

	
	def _decrypt_val(self, cipher_text):
		raw_decrypted = self.key.decrypt(base64.b64decode(cipher_text))
		clear_text = raw_decrypted.rstrip("\0")
		return clear_text
