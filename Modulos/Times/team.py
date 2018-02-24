#team.py
class Team(object):
	"""docstring for Team"""
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

	seq = 0
	objects = []
	
	def __init__(team_number, team_site, team_name, enabled, type, multi_login, team_full_name, password ):
		super(Team, self).__init__()
		self.team_number = team_number
		self.team_site = team_site
		self.team_name = team_name
		self.enabled = enabled
		self.type = type
		self.multi_login = multi_login
		self.team_full_name = team_full_name
		self.password = password

	def save(self):
		self.__class__.seq += 1
		self.team_number = self.__class__.seq
		self.__class__.objects.append(self)

	@classmethod
	def all(cls):
		return cls.objects		