import requests
import pandas as pd
import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def load_nhl_teams_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)['data']

def fetch_play_by_play_data(game_id):
    url = f"https://api-web.nhle.com/v1/gamecenter/{game_id}/play-by-play"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve data: {response.status_code}")

def get_team_abbreviation(team_id, nhl_teams_data):
    for team in nhl_teams_data:
        if team['id'] == team_id:
            return team['triCode']
    return None

def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def process_play(play, nhl_teams_data, last_event_details):
    event_type = play.get('typeDescKey')
    period = play.get('periodDescriptor', {}).get('number')
    time_on_clock_str = play.get('timeInPeriod')
    time_on_clock_seconds = time_to_seconds(time_on_clock_str)
    
    coordinates = play.get('details', {})
    x_coord = coordinates.get('xCoord')
    y_coord = coordinates.get('yCoord')
    shot_type = coordinates.get('shotType')
    shooting_player_id = coordinates.get('shootingPlayerId')
    goalie_in_net_id = coordinates.get('goalieInNetId')
    event_owner_team_id = coordinates.get('eventOwnerTeamId')
    event_owner_team_abbreviation = get_team_abbreviation(event_owner_team_id, nhl_teams_data)
    
    result = {
        'goal': 'goal',
        'shot-on-goal': 'save',
        'missed-shot': 'missed'
    }.get(event_type, 'other')
    
    if last_event_details['time_seconds'] is not None and period == last_event_details['period']:
        time_since_last_event_seconds = time_on_clock_seconds - last_event_details['time_seconds']
    else:
        time_since_last_event_seconds = None
    
    event_data = {
        'period': period,
        'time': time_on_clock_str,
        'x': x_coord,
        'y': y_coord,
        'type': event_type,
        'team': event_owner_team_abbreviation,
        'result': result,
        'time_since_last_event_seconds': time_since_last_event_seconds,
        'last_event_type': last_event_details['type']
    }
    
    last_event_details.update({
        'time_seconds': time_on_clock_seconds,
        'period': period,
        'type': event_type
    })
    
    return event_data

def generate_dataframe(game_id):
    nhl_teams_data = load_nhl_teams_data('nhl_teams.json')
    data = fetch_play_by_play_data(game_id)
    
    plays = data.get('plays', [])
    plays_sorted = sorted(plays, key=lambda x: (x.get('periodDescriptor', {}).get('number'), x.get('timeInPeriod')))
    
    last_event_details = {'time_seconds': None, 'period': None, 'type': None}
    events = [process_play(play, nhl_teams_data, last_event_details) for play in plays_sorted]
    
    df = pd.DataFrame(events)
    filtered_df = df[df['type'].isin(['missed-shot', 'goal', 'shot-on-goal'])]
    
    return filtered_df

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        game_id = request.form['game_id']
        try:
            df = generate_dataframe(game_id)
            result = df.to_dict(orient='records')
            return render_template('index.html', data=result, game_id=game_id)
        except Exception as e:
            return render_template('index.html', error=str(e), game_id=game_id)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
