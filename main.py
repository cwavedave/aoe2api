import requests

# SET PARAMS
GAME = "aoe2de"
OLD = "aoe2hd"
LANGUAGE = "en"

# End Points
STRINGS_USED = "https://aoe2.net/api/strings"
# Request a list of strings used by the API.

ALL_LOBBIES = "https://aoe2.net/api/lobbies"
#

LEADERBOARD = "https://aoe2.net/api/leaderboard" #Needs leaderboard id, start & count
# Request the current leaderboards

LAST_MATCH = "https://aoe2.net/api/player/lastmatch"
# Request the last match the player started playing, this will be the current match if they are still in game

PLAYERS_ONLINE = "https://aoe2.net/api/stats/players"
# Number of players in game and an estimate of the number current playing multiplayer

PLAYER_MATCH_HISTORY = "https://aoe2.net/api/player/matches?game=aoe2de&steam_id=76561199003184910&count=5"
# Request the match history for a player

PLAYER_RATING_HISTORY = "https://aoe2.net/api/player/ratinghistory" #Requires Steam ID, Leaderboard id, count
MATCHES = "https://aoe2.net/api/matches"


response = requests.get()





# Match




# Number of Players Online




