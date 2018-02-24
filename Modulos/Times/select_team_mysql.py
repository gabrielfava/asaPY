import mysql.connector
import database_conf as cfg

cnx = mysql.connector.connect(**cfg.mysql)

cursor = cnx.cursor()
query = ("SELECT team_number, team_name FROM teams")

cursor.execute(query)

for(team_number, team_name) in cursor:
	print("{} -> {}".format(team_number, team_name))

cursor.close()
cnx.close()
