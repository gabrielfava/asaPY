import string
import random
import mysql.connector
import database_conf as cfg
import team


def select_teams(cursor):
	query = ("SELECT team_number, team_name from TEAMS")
	cursor.execute(query)
	return cursor

def update_passwords(cnx, cursor):
	for(team_number, team_name) in cursor:
		new_pass = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
		cursor.execute = ("""
			UPDATE TEAMS
			SET password=%s
			WHERE team_number=%s
		""", (new_pass, team_number))
		print(team_number, team_name, new_pass)
	cnx.commit()



def main():
	cnx = mysql.connector.connect(**cfg.mysql)
	cursor = cnx.cursor()
	select_teams(cursor)
	update_passwords(cnx, cursor)
	cursor.close()
	cnx.close()

if __name__ == "__main__":
	main()




# [user]
# usernumber=900
# usersitenumber=1
# username=time1
# usertype=team
# userenabled=t
# usermultilogin=f
# userfullname=[TIME 1]ASAP
# userdesc=[TIME 1]ASAP
# userpassword=20194143