import requests
import statesofplay
import time
import json


# Test API (currently the top 25 rankings)
# If this is about getting the team information, then from the API I must get all the info relating to the team
espn_api_url = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/rankings"

def get_team_Dictionary(url):
    espn_api_url = url
    response = requests.get(espn_api_url)
    if response.status_code == 200:
        team_data = response.json()
        print("Recieved API-------------------")
        team_json_data = json.loads(response.content)
        print("This response contains {0} properties".format(len(team_json_data)))
        print("\n")
        for key in team_json_data:
            if key == "rankings": # rankings key
                tier_of_leagues = team_json_data[key] # seperated by NCAA League           
    else:
        response.raise_for_status()

# link for scoreboard_api
espn_scoreboard_url = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard"

# gets the scoreboard from the scoreboard api
def call_scoreboard():
    response = requests.get(espn_scoreboard_url)
    response.raise_for_status()
    return response.json()

def print_games(data):
    events = data.get("events", [])

    if not events:
        print("No games are currently available")
        return
    
    for event in events:
        competition = event["competitions"][0]
        competitors = competition["competitors"]

        # Getting each team in the game
        home_team = None
        away_team = None

        for team in competitors:
            if team["homeAway"] == "home":
                home_team = team
            else:
                away_team = team

        home_name = home_team["team"]["displayName"]
        away_name = away_team["team"]["displayName"]

        home_score = home_team["score"]
        away_score = away_team["score"]

        # Time and Quarter in game
        status = competition["status"]["type"]["shortDetail"]
            # competition[clock][period]
        
        # Situation Info (wrap in if statement if game has started)
        situation = competition.get("situation", {})
        down_distance = situation.get("downDistanceText", "N/A")
        possession_id = situation.get("possession")

        possession_team = "N/A"
        if possession_id:
            if possession_id == home_team["team"]["id"]:
                possession_team = home_name
            elif possession_id == away_team["team"]["id"]:
                possession_team = away_name

        # Infomation that is shown
        print("--------------------------------")
        print(f"{away_name} @ {home_name}")
        print(f"Score: {away_score} - {home_score}")
        print(f"Status: {status}")
        print(f"Down & Distance: {down_distance}")
        print(f"Possession: {possession_team}")
        print("--------------------------------")




if __name__ == "__main__":
    while True:
        print("\n\n===refreshing scoreboard===\n")
        data = call_scoreboard()
        print_games(data)
        time.sleep(100) # refreshing every 1m40






