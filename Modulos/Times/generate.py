import string
import random
from mysql.connector import MySQLConnection, Error
import database_conf as cfg
import team

__select_ALL = "SELECT team_number, team_site, team_name, password, team_short_name, enabled, type, multi_login, team_full_name FROM TEAMS"


def select_teams(cursor):
	query = ("SELECT team_number, team_name, password from TEAMS")
	cursor.execute(query)
	return cursor

def update_passwords(cnx, cursor):
	for(team_number, team_name, password) in cursor:
		if(not password):
			new_pass = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
			query = """UPDATE TEAMS
					SET password=%s
					WHERE team_number=%s""" 
			data = (new_pass, team_number)

			try:
				cursor.execute(query,data)
			except Error as error:
				print(error)

	cnx.commit()


def generate_file(cursor):
	cursor.execute(__select_ALL)
	f = open("import.txt", 'w')
	f.write("[user]")
	first_team = True
	for(team_number, team_site, team_name, password, team_short_name, enabled, type, multi_login, team_full_name) in cursor:
		if(first_team):
			f.write('\n')
			first_team = False
		else:
			f.write('\n\n')
		f.write('usernumber=' + str(team_number))	
		f.write('\nusersitenumber=' + team_site)
		f.write('\nusername=' + team_short_name)
		f.write('\nusertype=' + type)
		f.write('\nuserenabled=' + enabled)
		f.write('\nusermultilogin=' + multi_login)
		f.write('\nuserfullname=' + team_full_name)
		f.write('\nuserdesc=' + team_full_name)
		f.write('\nuserpassword=' + str(password))
	f.close()


def main():
	cnx = MySQLConnection(**cfg.mysql)
	cursor = cnx.cursor()
	select_teams(cursor)
	update_passwords(cnx, cursor)
	generate_file(cursor)
	cursor.close()
	cnx.close()

if __name__ == "__main__":
	main()