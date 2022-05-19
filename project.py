from pip._vendor import requests as r


class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.formation = ''
        self.available_pos = [0, 0, 0, 0]
        self.fieldability = True
        self.active_roster = []


class Player:
    def __init__(self, name, position, team, playability):
        self.name = name
        self.position = position
        self.team = team
        self.playability = playability


class Run:
    def api_request(self):
        self.request = r.get(
            'https://foxes90-prempundit.herokuapp.com/players')
        self.players_api = self.request.json()

    def team_creation(self):
        self.teams = {}
        x = set()
        for i in (range(len(self.players_api['Players']))):
            x.add(self.players_api['Players'][i]['team'])
        x = list(x)
        for i in x:
            k = Team(i)
            self.teams[i] = k

    def player_creation(self):
        for i in (range(len(self.players_api['Players']))):
            first_name = (self.players_api['Players'][i]['first_name'])
            last_name = (self.players_api['Players'][i]['last_name'])
            pos_ = (self.players_api['Players'][i]['position'])
            team_name = (self.players_api['Players'][i]['team'])
            playability = True
            if (self.players_api['Players'][i]['injured']) == True or (self.players_api['Players'][i]['suspended']) == True:
                playability = False
            last_name = Player(f'{first_name} {last_name}',
                               pos_, team_name, playability)
            if last_name.playability == True:
                self.teams[last_name.team].active_roster.append(last_name)

    def player_position(self):
        for i in self.teams:
            for k in range(len(self.teams[i].active_roster)):
                x = self.teams[i].active_roster[k].position
                if x == 'Keeper':
                    self.teams[i].available_pos[0] += 1
                elif x == 'Defender':
                    self.teams[i].available_pos[1] += 1
                elif x == 'Midfielder':
                    self.teams[i].available_pos[2] += 1
                elif x == 'Striker':
                    self.teams[i].available_pos[3] += 1

    def valid_lineup(self):
        for i in self.teams:
            if sum(self.teams[i].available_pos) < 11:
                self.teams[i].fieldability = False
            elif self.teams[i].available_pos[0] == 0:
                self.teams[i].fieldability = False
            elif self.teams[i].available_pos[1] < 3 or self.teams[i].available_pos[1] > 5:
                self.teams[i].fieldability = False
            elif self.teams[i].available_pos[2] < 3 or self.teams[i].available_pos[2] > 5:
                self.teams[i].fieldability = False
            elif self.teams[i].available_pos[3] < 1 or self.teams[i].available_pos[3] > 3:
                self.teams[i].fieldability = False

    def whosyourteam(self):
        team_name = set()
        for i in self.teams:
            team_name.add(i)
        print (f'These are the current teams in the Champions League:\n{team_name}')
        x = input(
            'Tell me your team, Ill tell you if they can field for their upcoming game this Champions Weekend\n').title()
        if x in team_name:
            if self.teams[x].fieldability == False:
                print(f'Sorry bud {x} is not going to be able to play this weekend')
            else:
                print(f'Lucky you {x} will be able to play this weekend.')
        else:
            print(f'Input "{x}" Is Invalid')


run_ = Run()
run_.api_request()
run_.team_creation()
run_.player_creation()
run_.player_position()
run_.valid_lineup()
run_.whosyourteam()
