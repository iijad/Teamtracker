

previous_games = {}

def detect_scoring_event(old_score, new_score):
    diff = new_score - old_score
    if diff >= 6:
        return "TOUCHDOWN"
    if diff == 3:
        return "FIELD GOAL"
    elif diff == 2:
        return "SAFETY"
    # add logic for 2 point conversions
    return None

def process_games(data):
    events = data.get("events", [])

    for event in events:
        event_id = event["id"]
        competition = event["competitions"][0]
        competitors = competition["competitors"]

        home_team = next(t for t in competitors if t["homeAway"] == "home")
        away_team = next(t for t in competitors if t["homeAway"] == "away")

        home_name = home_team["team"]["displayName"]
        away_name = away_team["team"]["displayName"]

        home_score = int(home_team["score"])
        away_score = int(away_team["score"])

        situation = competition.get("situation", {})
        possession = situation.get("possession")

        # Initializing the game state if it's the first time seeing it
        if event_id not in previous_games:
            previous_games[event_id] = {
                "home_score": home_score,
                "away_score": away_score,
                "possession": possession
            }
            continue

        old_game = previous_games[event_id]

        # Detecting scoring changes
        if home_score != old_game["home_score"]:
            event_type = detect_scoring_event(old_game["home_score"], home_score)
            print(f"{home_name} - {event_type}")
        
        if away_score != old_game["away_score"]:
            event_type = detect_scoring_event(old_game["away_score"], away_score)
            print(f"{away_name} - {event_type}")

        # Possession change (basic change, review for TURNOVER)
        if possession != old_game["possession"] and old_game["possession"] is not None:
            if possession == home_team["team"]["id"]:
                new_pos_team = home_name
            elif possession == away_team["team"]["id"]:
                new_pos_team = away_name
            else:
                new_pos_team = "Unknown"

        # Update the state
        previous_games[event_id] = {
            "home_score": home_score,
            "away_score": away_score,
            "possession": possession
        }

