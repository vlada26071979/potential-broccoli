import pandas as pd 


premier_league = pd.read_csv("premier_league.csv")
results = pd.read_csv("results_12seasons.csv")

def display_gen_stats():
    team_summary = premier_league.groupby("team").sum()
    general_stats = ["wins","losses","goals","total_yel_card","total_red_card"]
    print(team_summary[general_stats])

def display_team_play_stats():
    team_summary = premier_league.groupby("team").sum()
    team_play_stats = ["total_pass","total_through_ball","total_long_balls",
    "backward_pass","total_cross", "corner_taken"]
    print(team_summary[team_play_stats])

def display_att_stats():
    team_summary = premier_league.groupby("team").sum()
    attacking_stats = ["total_scoring_att","ontarget_scoring_att","hit_woodwork","att_hd_goal",
    "att_pen_goal", "att_freekick_goal","att_ibox_goal","att_obox_goal", "goal_fastbreak", "total_offside"]
    print(team_summary[attacking_stats])

def display_def_stats():
    team_summary = premier_league.groupby("team").sum()
    defensive_stats = ['clean_sheet','goals_conceded', 'saves', 'outfielder_block', 'interception',
    'total_tackle', 'last_man_tackle', 'total_clearance', 'head_clearance','own_goals', 'penalty_conceded',
    'pen_goals_conceded']
    print(team_summary[defensive_stats])

def display_other_stats():
    team_summary = premier_league.groupby("team").sum()
    other_stats = ['touches', 'big_chance_missed','clearance_off_line', 'dispossessed', 'penalty_save',
    'total_high_claim', 'punches']
    print(team_summary[other_stats])

