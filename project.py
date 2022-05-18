from pip._vendor import requests as r

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.formation = ''
        self.available_pos = [1, 1, 1, 1]
        self.fieldability = True
        self.roster = []

    def valid_lineup(self):
        if sum(self.available_pos) < 11:
            self.fieldability = False
        elif self.available_pos[0] == 0:
            self.fieldability = False
        elif self.available_pos[1] < 3 or self.available_pos[1] > 5:
            self.fieldability = False
        elif self.available_pos[2] < 3 or self.available_pos[2] > 5:
            self.fieldability = False
        elif self.available_pos[3] < 1 or self.available_pos[3] > 3:
            self.fieldability = False
    
#    def pos_assignment(self):


class Player:
    def __init__(self, name, position,team, playable):
        self.name = name
        self.position = position
        self.team = team
        self.playable = None

class Run:
    def api_request(self):
        self.request = r.get('https://foxes90-prempundit.herokuapp.com/players')
        self.players_api = self.request.json()
    
    def team_creation(self):
        x = set()
        for i in (range(len(self.players_api['Players']))):
            x.add(self.players_api['Players'][i]['team'])
        x = list(x)
        for i in x:
            i = Team(i)
            

    def player_creation(self):
        for i in (range(len(self.players_api['Players']))):
            first_name = (self.players_api['Players'][i]['first_name'])
            last_name = (self.players_api['Players'][i]['last_name'])
            pos_ = (self.players_api['Players'][i]['position'])
            team_name = (self.players_api['Players'][i]['team'])
            playability = True
            if (self.players_api['Players'][i]['injured']) == True or (self.players_api['Players'][i]['suspended']) == True:
                playability = False
            last_name = Player(f'{first_name} {last_name}',pos_,team_name,playability)
#            if last_name.playability == True:
#                append
    


    



run_ = Run()
run_.api_request()
run_.team_creation()
run_.player_creation()
print(Aston.__dict__)


