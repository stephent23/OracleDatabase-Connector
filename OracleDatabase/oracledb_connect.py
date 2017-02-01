from oracledb_configuration import DBConfiguration
from oracledb_password import PasswordSecurity
import cx_Oracle as database

class Database(object):
	
	def __init__(self):
		self.configuration_file = DBConfiguration()
		self.security = PasswordSecurity()
		self.db_connection = self._connect_to_database()

	
	def _connect_to_database(self):
		self.configuration_file._get_config()
		config = self.configuration_file.db_config
		plain_password = self.security._decrypt_val(config['password'])
		connection_string = str(config['hostname'] + '/' + plain_password + '@' + config['hostname'])
		
		# Establish connection
		self.db_connection = database.connect(connection_string)


	def _query_fetch_one(self, sql_query):
		cursor = self.db_connection.database.cursor()
		cursor.database.execute(sql_query)
		result = cursor.database.fetchone()
		return result

	
	def _query_fetch_many(self, sql_query, number_of_rows):
		cursor = self.db_connection.database.cursor()
		cursor.database.execute(sql_query)
		result = cursor.database.fetchmany(numRows=number_of_rows)
		return result


	def _query_fetch_all(self, sql_query):
		cursor = self.db_connection.database.cursor()
		cursor.database.execute(sql_query)
		result = cursor.database.fetchall()
		return result


	def _close_database_connection(self):
		self.db_connection.close()