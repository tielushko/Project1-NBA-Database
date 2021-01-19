class Coach:
    def __init__(self, coach_id, season, first_name, last_name, season_win, season_loss, playoff_win, playoff_loss, team):
        self.coach_id = coach_id
        self.season = season
        self.first_name = first_name
        self.last_name = last_name
        self.season_win = season_win
        self.season_loss = season_loss
        self.playoff_win = playoff_win
        self.playoff_loss = playoff_loss
        self.team = team

    def __repr__(self):
        return "{0:<10} {1:<10} {2:<10} {3:<10} {4:<10} {5:<10} {6:<10} {7:<10} {8:<10}".format(self.coach_id, self.season, self.first_name, self.last_name, self.season_win, self.season_loss, self.playoff_win, self.playoff_loss, self.team)


