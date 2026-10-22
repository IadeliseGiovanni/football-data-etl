import pandas as pd

def transform_matches(raw_matches: list) -> pd.DataFrame:
    cleaned_data = []
    
    for match in raw_matches:
        home_score = match['score']['fullTime']['home']
        away_score = match['score']['fullTime']['away']
        
        if home_score is not None and away_score is not None:
            if home_score > away_score:
                winner = match['homeTeam']['name']
            elif away_score > home_score:
                winner = match['awayTeam']['name']
            else:
                winner = 'DRAW'
        else:
            winner = 'PENDING'

        cleaned_data.append({
            'match_id': match['id'],
            'home_team': match['homeTeam']['name'],
            'away_team': match['awayTeam']['name'],
            'home_score': home_score,
            'away_score': away_score,
            'winner': winner,
            'match_date': match['utcDate'],
            'status': match['status']
        })
        
    df = pd.DataFrame(cleaned_data)
    return df