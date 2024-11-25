# Write your solution here

import json

class Player:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.__name = name
        self.__nationality = nationality
        self.__assists = assists
        self.__goals = goals
        self.__penalties = penalties
        self.__team = team
        self.__games = games
        self.__points = goals + assists

    @property
    def name(self):
        return self.__name

    @property
    def nationality(self):
        return self.__nationality

    @property
    def assists(self):
        return self.__assists

    @property
    def goals(self):
        return self.__goals

    @property
    def penalties(self):
        return self.__penalties

    @property
    def team(self):
        return self.__team

    @property
    def games(self):
        return self.__games

    @property
    def points(self):
        return self.__points


class PlayerList:
    def __init__(self):
        self.__players = []

    def add_player(self, player: Player):
        self.__players.append(player)

    def search_player(self, name: str):
        for player in self.__players:
            if player.name == name:
                return player

    def get_teams_list(self):
        return sorted(list(set([player.team for player in self.__players])))

    def get_countries_list(self):
        return sorted(list(set([player.nationality for player in self.__players])))

    def get_team_players(self, team: str):
        return sorted([player for player in self.__players if player.team == team], key=lambda x: x.points, reverse=True)

    def get_country_players(self, country: str):
        return sorted([player for player in self.__players if player.nationality == country], key=lambda x: x.points, reverse=True)
    
    def points_ranking(self, ammount: int):
        all_players = sorted(self.__players, key=lambda x: (x.points, x.goals), reverse=True)
        return all_players[:ammount]
    
    def goals_ranking(self, ammount: int):
        all_players = sorted(self.__players, key=lambda x: (x.goals, -x.games), reverse=True)
        return all_players[:ammount]


class Application:
    def __init__(self):
        self.__player_list = PlayerList()

    def load_data(self):
        filename = input("file name: ")

        with open(filename, "r") as file:
            json_data = file.read()

        data = json.loads(json_data)
        print(f"read the data of {len(data)} players\n")
        return data
    
    def process_data(self, data: list):
        for player in data:
            to_add = Player(player["name"], player["nationality"], player["assists"], player["goals"], player["penalties"], player["team"], player["games"])
            self.__player_list.add_player(to_add)

    def print_player(self, player: Player):
        print(f"{player.name:<21}{player.team:<4}{player.goals:>3} + {player.assists:>2} = {player.points:>3}")

    def search_player(self):
        name = input("name: ")
        player = self.__player_list.search_player(name)

        if player == None:
            print("player not found.")
        else:
            self.print_player(player)

    def show_teams(self):
        teams = self.__player_list.get_teams_list()
        for team in teams:
            print(team)

    def show_countries(self):
        countries = self.__player_list.get_countries_list()
        for country in countries:
            print(country)

    def show_players_in_team(self):
        team = input("team: ")
        players = self.__player_list.get_team_players(team)

        if len(players) == 0:
            print("team not found.")
        else:
            for player in players:
                self.print_player(player)

    def show_players_from_country(self):
        country = input("country: ")
        players = self.__player_list.get_country_players(country)

        if len(players) == 0:
            print("country not found.")
        else:
            for player in players:
                self.print_player(player)

    def show_ranking_by_points(self):
        ammount = int(input("how many: "))
        ranking = self.__player_list.points_ranking(ammount)

        for player in ranking:
            self.print_player(player)

    def show_ranking_by_goals(self):
        ammount = int(input("how many: "))
        ranking = self.__player_list.goals_ranking(ammount)

        for player in ranking:
            self.print_player(player)

    def menu(self):
        print("""commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals""")

    def execute(self):
        data = self.load_data()
        self.process_data(data)

        self.menu()
        
        while True:
            command = int(input("\ncommand: "))

            if command == 0:
                break
            elif command == 1:
                self.search_player()
            elif command == 2:
                self.show_teams()
            elif command == 3:
                self.show_countries()
            elif command == 4:
                self.show_players_in_team()
            elif command == 5:
                self.show_players_from_country()
            elif command == 6:
                self.show_ranking_by_points()
            elif command == 7:
                self.show_ranking_by_goals()
            else:
                print("invalid command!\n")
                self.menu()


main = Application()
main.execute()