# questions
# 1. is the remove functionality only required to work with coach_ID and team_ID?
from coach import Coach
# coaches_by_name is the query structured as first_name=John or just john?

def print_help():
    print('1. To add a coach to the table of coaches\n'
          'EX:          pythonistaDMBS?>>add_coach COACH_ID, SEASON, FIRST_NAME, LAST_NAME, SEASON_WIN, SEASON_LOSS, '
          'PLAYOFF_WIN, PLAYOFF_LOSS, TEAM\n'
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


print('Welcome to the Pythonista Database Management System.\n'
      'Please type your query.\n'
      'Type "help" for list of available queries.\n'
      'Type "q" to exit the program.\n')

query = input('pythonistaDBMS?>>')
while query != 'q':
    if query == 'help':
        print_help()
    query = input('pythonistaDBMS?>>')