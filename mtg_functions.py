def opp_mull_win_rate(opponent_mulligans, wins, losses):
    """
    Calculate how often you win when your opponent mulligans.
    Returns a formatted % value.
    """
    total_games = wins + losses
    win_rate = wins / total_games
    opp_mull_win_rate = win_rate * opponent_mulligans
    formatted_win_rate = "{:.2%}".format(opp_mull_win_rate)
    return formatted_win_rate

def player_mull_win_rate(player_mulligans, wins, losses):
    """
    Calculate how often you win when you mulligan.
    Returns a formatted % value.
    """
    total_games = wins + losses
    win_rate = wins / total_games
    player_mull_win_rate = win_rate * player_mulligans
    formatted_win_rate = "{:.2%}".format(player_mull_win_rate)
    return formatted_win_rate