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
		configuration = ConfigParser.ConfigParser()
		configuration.read(self.config_file)

		self.db_config['database'] = configuration.get('DatabaseInfo', 'hostname')
		self.db_config['username'] = configuration.get('DatabaseCredentials', 'username')
		self.db_config['password'] = configuration.get('DatabaseCredentials', 'password')


	def _write_config(self, hostname, username, password):
		# Create the configuration file. This will overwrite any existing file.
		config_file = open(self.config_file, 'w')
		
		# Encrypt and the password
		password = security._encrypt_val(password)

		# Create configuration file settings.
		Config.add_section('DatabaseInfo')
		Config.set('DatabaseInfo', 'hostname', hostname)
		
		Config.add_section('DatabaseCredentials')
		Config.set('DatabaseCredentials', 'username', username)
		Config.set('DatabaseCredentials', 'password', password)

		# Write the configuration to the file. 
		Config.write(config_file)
		config_file.close()
