# questions
# 1. is the remove functionality only required to work with coach_ID and team_ID?
# 2. in project specification you mention the requirement to make sure there aren't any digits in our coaches names
# however in the example input output you proceed to load the coach John Proba1 into the database
# 3. First team Begin fuuls has BEGIN as the team id in the input/output file and BEG in the file given to load. Which one is final one?

from coach import Coach
from team import Team
import csv

# coaches_by_name is the query structured as first_name=John or just john?
coach_list = []
team_list = []


def print_help():
	print('1. To add a coach to the table of coaches\n'
	      'EX:          pythonistaDMBS?>>add_coach COACH_ID SEASON FIRST_NAME LAST_NAME SEASON_WIN SEASON_LOSS'
	      ' PLAYOFF_WIN PLAYOFF_LOSS TEAM\n'
	      '2. To add a team to the table of teams\n'
	      'EX:          pythonistaDMBS?>>add_team TEAM_ID, LOCATION, NAME, LEAGUE\n'
	      '3. To load coaches to the table using csv file.\n'
	      'EX:          pythonistaDMBS?>>load_coaches FILENAME.ext\n'
	      '4. To load teams to the table using csv file.\n'
	      'EX:          pythonistaDMBS?>>load_teams FILENAME.ext'
	      '5. To remove an existing record in coaches table\n'
	      'EX:          pythonistaDMBS?>>remove_coach coach_id=COACH_ID'
	      '6. To remove an existing record in teams table\n'
	      'EX:          pythonistaDMBS?>>remove_team team_id=TEAM_ID\n'
	      '7. To print a list of all coaches, with info about one coach\'s performance in one season in a line\n'
	      'EX:          pythonistaDMBS?>print_coaches>\n'
	      '8. To print a list of all teams, with info about one team per line\n'
	      'EX:          pythonistaDMBS?>>print_teams\n'
	      '9. To print the information of coach(es) with the specified first name\n'
	      'EX:          pythonistaDMBS?>>coaches_by_name John\n'
	      '10. To print the information of teams in the city and league specified by the arguments\n'
	      'EX:          pythonistaDMBS?>>teams_by_city_league Los+Angeles A\n'
	      '11. To print the name of the coach who has the most net wins in a season specified by the only argument.\n'
	      'EX:          pythonistaDMBS?>>best_coach\n'
	      '12. To print the info of coaches with the specified properties, which are given by the arguments in the '
	      'following format: field=VALUE where field represents the name of a search criterion and \'VALUE\' is '
	      'the value of that field you want the query results to match.\n'
	      'EX:          pythonistaDMBS?>>search_coaches\n')


def add_coach(raw_coach_query_list):
	"""Takes in a list of split data by space"""
	stripped_list = [element.strip() for element in raw_coach_query_list]

	raw_coach_query_list = stripped_list

	# validation for coach_id
	coach_id = raw_coach_query_list[1]
	letters = sum(char.isalpha() for char in coach_id)
	if letters > 7:
		print('invalid number of characters in coach_id. MAX is 7')
		return
	numbers = sum(char.isdigit() for char in coach_id)
	if numbers > 2:
		print('invalid number of numbers in coach_id. MAX is 2')
		return
	# validation for year.
	season_year = raw_coach_query_list[2]
	numbers = sum(char.isdigit() for char in season_year)
	if numbers != 4:
		print('invalid number of numbers in coach_id. Must be 4 digit number')
		return

	# processing of first name -> removing any + characters
	first_name = raw_coach_query_list[3]
	first_name = first_name.replace('+', ' ')

	# processing of last name -> removing any + characters
	last_name = raw_coach_query_list[4]
	last_name = last_name.replace('+', ' ')

	# processing of the rest of data wins/losses
	try:
		season_win = int(raw_coach_query_list[5])
	except:
		print("You must pass in a valid integer to season win!")
		return
	finally:
		if season_win < 0:
			print('Invalid. Season win must be >= 0')

	try:
		season_loss = int(raw_coach_query_list[6])
	except:
		print("You must pass in a valid integer to season loss.")
	finally:
		if season_loss < 0:
			print('Invalid. Season loss must be >= 0')

	try:
		playoff_win = int(raw_coach_query_list[7])
	except:
		print("You must pass in a valid integer to playoff win!")
	finally:
		if playoff_win < 0:
			print('Invalid. Playoff win must be >= 0')

	try:
		playoff_loss = int(raw_coach_query_list[8])
	except:
		print("You must pass in a valid integer to playoff loss!")
	finally:
		if playoff_loss < 0:
			print('Invalid. Playoff loss must be >= 0')

	# processing of team
	team = raw_coach_query_list[9]

	# append the added coach to the table (list) of coaches)
	coach = Coach(coach_id, season_year, first_name, last_name, season_win, season_loss, playoff_win, playoff_loss,
	              team)
	coach_list.append(coach)


def add_team(raw_team_query_list):
	stripped_list = [element.strip() for element in raw_team_query_list]

	raw_team_query_list = stripped_list

	team_id = raw_team_query_list[1]

	# processing for team location
	location = raw_team_query_list[2]
	location = location.replace('+', ' ')

	name = raw_team_query_list[3]

	# league processing
	league = raw_team_query_list[4]
	if len(league) != 1:
		print('Invalid league name. Must be represented by a singular character')
		return

	team = Team(team_id, location, name, league)
	team_list.append(team)


def load_coaches(file_name):
	with open(file_name, 'r') as csv_file:
		coach_reader = csv.reader(csv_file, delimiter=',')
		# to skip the header of the file
		next(coach_reader)
		for row in coach_reader:
			# need to insert the dummy first command element to the row before processing.
			row.insert(0, 'load_coaches')
			add_coach(row)


def load_teams(file_name):
	with open(file_name, 'r') as csv_file:
		team_reader = csv.reader(csv_file, delimiter=',')
		# to skip the header of the file
		next(team_reader)
		for row in team_reader:
			# need to insert the dummy first command element to the row before processing.
			row.insert(0, 'load_teams')
			add_team(row)


def print_coaches(coaches):
	for coach in coaches:
		print(coach)


def print_teams(teams):
	for team in teams:
		print(team)


def remove_coach(coach_id_deletable):
	# filter the new coach list from the current coach list by not having the coaches with ID to remove
	new_coaches_list = [coach for coach in coach_list if coach.coach_id != coach_id_deletable]
	if new_coaches_list == coach_list:
		print('The coach id was not found in the database.')
	return new_coaches_list


def remove_team(team_id_deletable):
	# filter the new team list from the current tem list by not having the teams with ID to remove
	new_teams_list = [team for team in team_list if team.team_id != team_id_deletable]
	if new_teams_list == team_list:
		print('The team id was not found in the database.')
	return new_teams_list


def coaches_by_name(first_name_to_find):
	"""coaches_by_name van+Gundy"""
	# filter out the coaches by name find matching ones
	coaches_list_by_name = [coach for coach in coach_list if coach.first_name.lower() == first_name_to_find.lower()]
	# if any coaches populated the new list, we print them out
	if coaches_list_by_name:
		print_coaches(coaches_list_by_name)
	else:
		print('No coaches with specified first name were found.')


def teams_by_city_league(city_input, league_input):
	"""teams_by_city_league Los+Angeles A"""
	# list comprehension to filter out teams with matching city and location
	teams_by_city_league_list = [team
	                             for team
	                             in team_list
	                             if team.location.lower() == city_input.lower()
	                             and team.league.lower() == league_input.lower()]

	# if any teams populated the new list, we print them out, otherwise notify user that no search results present
	if teams_by_city_league_list:
		print_teams(teams_by_city_league_list)
	else:
		print('No teams with specified city (location) and league were found.')


def best_coach(year):
	# filter coaches from that year
	coaches_from_the_year = [coach for coach in coach_list if coach.season == year]
	"""(season_win - season_loss) + (playoff_win - playoff_loss)"""
	# setup the initial score
	current_best_score = -1000
	# iterate through the list of coaches at the moment
	if coaches_from_the_year:
		for coach in coaches_from_the_year:
			# determine score
			score = (coach.season_win - coach.season_loss) + (coach.playoff_win - coach.playoff_loss)
			# if the score we are looking at is better than previous one we reinstate the current
			# best score and setup the coach to be the best coach
			if score >= current_best_score:
				current_best_score = score
				best_c = coach
		print(f'{best_c.first_name} {best_c.last_name}')
	else:
		print('No coaches were found from the season specified')


def search_coaches(search_criteria_dict):
	filtered_list = coach_list
	for key in search_criteria_dict.keys():
	# for i in range(len(search_criteria_dict)):
		print('prior iteration...')
		print_coaches(filtered_list)
		# key = str(next(iter(search_criteria_dict)))
		print(f"The key we look into is: {key}")
		new_filter = [coach for coach in filtered_list if getattr(coach, key) == search_criteria_dict[key]]
		filtered_list = new_filter
		print('after iteration...')
		print_coaches(new_filter)

	print('final list....')
	print_coaches(filtered_list)


print('Welcome to the Pythonista Database Management System.\n'
      'Please type your query.\n'
      'Type "help" for list of available queries.\n'
      'Type "q" to exit the program.\n')

query = input('pythonistaDBMS?>>')
while query != 'q':
	query_list = query.split()
	# print(query_list)
	leading_command = query_list[0]
	# help command
	if leading_command == 'help':
		print_help()
	# adding a coach
	elif leading_command == 'add_coach':
		# check if the number of arguments is enough for the file processing.
		if len(query_list) == 10:
			add_coach(query_list)
		else:
			print("Invalid amount of arguments to add the coach to the database.")
	# adding a team
	elif leading_command == 'add_team':
		if len(query_list) == 5:
			add_team(query_list)
		else:
			print("Invalid amount of arguments to add the team to the database.")
	elif leading_command == 'load_coaches':
		if len(query_list) == 2:
			filename = query_list[1]
			load_coaches(filename)
		else:
			print("Invalid amount of arguments to load coaches from file to the database.")
	elif leading_command == 'load_teams':
		if len(query_list) == 2:
			filename = query_list[1]
			load_teams(filename)
		else:
			print("Invalid amount of arguments to load teams from file to the database.")
	elif leading_command == 'remove_coach':
		# we split the query list item 1 (coach_id=BLAH) by '=' character and get the item 1 which is the actual id.
		coach_id_to_remove = query_list[1].split('=')[1]
		coach_list = remove_coach(coach_id_to_remove)
	elif leading_command == 'remove_team':
		team_id_to_remove = query_list[1].split('=')[1]
		team_list = remove_team(team_id_to_remove)
	elif leading_command == 'print_coaches':
		print_coaches(coach_list)
	elif leading_command == 'print_teams':
		print_teams(team_list)
	elif leading_command == 'coaches_by_name':
		# modify the name character + to be space
		name = query_list[1].replace('+', ' ')
		coaches_by_name(name)
	elif leading_command == 'teams_by_city_league':
		city = query_list[1].replace('+', ' ')
		league = query_list[2]
		teams_by_city_league(city, league)
	elif leading_command == 'best_coach':
		season_year = query_list[1]
		best_coach(season_year)
	# TODO
	elif leading_command == 'search_coaches':
		field_list = query_list[1:]
		field_dictionary = {}
		for field in field_list:
			buffer = field.split('=')
			field_dictionary[buffer[0]] = buffer[1]
		search_coaches(field_dictionary)
	else:
		print('invalid command')

	query = input('pythonistaDBMS?>>')
