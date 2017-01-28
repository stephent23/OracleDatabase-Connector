from oracledb_configuration import DBConfiguration
from oracledb_password import PasswordSecurity
import cx_Oracle as database

class Database(object):
	
	def __init__(self):
		self.configuration_file = DBConfiguration()
		self.security = PasswordSecurity()
		self.db_connection = self._connect_to_database()

	
	def _connect_to_database(self):
		config = self.configuration_file._get_config()
		plain_password = self.security._decrypt_val(config['password'])
		connection_string = str(config['hostname'] + '/' + plain_password + '@' + config['hostname'])
		
		# Establish connection
		self.db_connection = database.connect(connection_string) 