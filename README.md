# Teamtracker
Allows for a user to choose a team and get specific updates from that team when they play; structured like ESPN SCOREBOARD

# Details
Takes an API (ESPN, other free sports api that shows live updates)
shows the current games going on
And the main information
	- who's playing (home, away)
	- the current score
	- who has the ball (possession)
	- the quarter, down + distance, and time remaining
	- any special indicators (A SCORE (TD, FG), UNEXPECTED CHANGE IN POSSESSION(TO), if current score qualifies for upset (UPSET ALERT), CLOSE GAME for a close game

ALL displayed in a viewable box on the side of the screen

Process:
 - Welcome screen that allows user to choose favorite team to follow (maybe multiple, but try just one first)
 - Show sch of team of when they play (like show current calendar and the team of when they play and who they play)
 - Then for when they play, have the box show live updates of the team (refer to beginning)


## 2/8/26
 - Found ESPN hidden API to use for project (https://gist.github.com/bhaidar/b2fdd34004250932a4a354a2cc15ddd4)
        - Contains: 
            - Team Name, nickname, logo, abbreviation, 
            - shortName : FBS, NCAA DIVISION II, NCAA DIVISION III
            - isConference : True (in conference), false (not in conference)
            - keys = sports, leagues, rankings, 
            - for team_Json_Data, it's split up by NCAA Leagues, [0] == FBS, [1] == Div. II, [2] == Division III
           - Link for all teams (https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams)


Phase 1

Pull scoreboard (done)

Print live games in terminal (done)

Phase 2

Track state changes (done for now)

Detect scoring events (done for now)

Phase 3

Store rankings locally

Add upset logic

Phase 4

Build UI boxes

Phase 5

Add favorite team selection
