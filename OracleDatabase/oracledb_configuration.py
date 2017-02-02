from oracledb_password import PasswordSecurity
import ConfigParser
import os.path

class DBConfiguration(object):

	def __init__(self):
		self.db_config = dict()
		self.config_file = 'db_conf.ini'


	def _check_config_exists(self):
		config_file_exists = os.path.isfile(self.config_file)
		return config_file_exists


	def _get_config(self):
		return self.db_config


	def _get_config_from_file(self):
		parser = ConfigParser.ConfigParser()
		parser.read(self.config_file)

		self.db_config['hostname'] = parser.get('DatabaseInfo', 'hostname')
		self.db_config['username'] = parser.get('DatabaseCredentials', 'username')
		self.db_config['password'] = parser.get('DatabaseCredentials', 'password')


	def _write_config(self, hostname, username, password):
		# Create the configuration file. This will overwrite any existing file.
		config_file = open(self.config_file, 'w')
		
		# Encrypt and the password
		password = PasswordSecurity()._encrypt_val(password)

		# Create configuration file settings.
		config = ConfigParser.RawConfigParser()
		config.add_section('DatabaseInfo')
		config.set('DatabaseInfo', 'hostname', hostname)
		
		config.add_section('DatabaseCredentials')
		config.set('DatabaseCredentials', 'username', username)
		config.set('DatabaseCredentials', 'password', password)

		# Write the configuration to the file. 
		config.write(config_file)
		config_file.close()
