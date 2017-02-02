from oracledb_configuration import DBConfiguration
from oracledb_password import PasswordSecurity
import cx_Oracle as database

class Database(object):
	
	def __init__(self):
		self.configuration_file = DBConfiguration()
		self.security = PasswordSecurity()
		self.db_connection = self._connect_to_database()

	
	def _connect_to_database(self):
		self.configuration_file._get_config_from_file()
		config = self.configuration_file._get_config()
		plain_password = self.security._decrypt_val(config['password'])
		dsn_tns = database.makedsn(host=config['hostname'], port='1521', service_name=config['service'])
		# Establish connection
		self.db_connection = database.connect(user=config['username'], password=plain_password, dsn=dsn_tns)

	def _query_fetch_one(self, sql_query):
		cursor = self.db_connection.cursor()
		cursor.execute(sql_query)
		result = cursor.fetchone()
		return result

	
	def _query_fetch_many(self, sql_query, number_of_rows):
		cursor = self.db_connection.cursor()
		cursor.execute(sql_query)
		result = cursor.fetchmany(numRows=number_of_rows)
		return result


	def _query_fetch_all(self, sql_query):
		cursor = self.db_connection.cursor()
		cursor.execute(sql_query)
		result = cursor.fetchall()
		return result


	def _close_database_connection(self):
		self.db_connection.close()