import pandas as pd 
import matplotlib.pyplot as plt 
from functions import display_gen_stats
from functions import display_team_play_stats
from functions import display_att_stats
from functions import display_def_stats
from functions import display_other_stats

pd.show_versions()

premier_league = pd.read_csv("premier_league.csv")
print(premier_league.head())
results = pd.read_csv("results_12seasons.csv")
print(results.tail())

city_data = premier_league[premier_league["team"] == "Manchester City"]
print(city_data)
print(city_data.shape)
print(city_data.describe())
print(city_data.info())
print(city_data.dtypes)
print(city_data.index)
print(city_data.columns)
print(city_data.isnull().sum())


display_gen_stats()
display_team_play_stats()
display_att_stats()
display_def_stats()
display_other_stats()


season_shots_wins = ["season","ontarget_scoring_att","wins"]
print(city_data[season_shots_wins])

city_results = results.loc[(results["home_team"] == "Manchester City") | (results["away_team"] == "Manchester City")]
print(city_results.head())
print(city_results["result"].value_counts())

home_games = city_results[city_results["home_team"] == "Manchester City"]
away_games =  city_results[city_results["away_team"] == "Manchester City"]
print(home_games.head())
print(away_games.head())
print(home_games.shape)
print(away_games.shape)
home_wins = home_games.loc[home_games["result"] == "H"]
home_draws = home_games.loc[home_games["result"] == "D"]
home_losses = home_games.loc[home_games["result"] == "A"]
print(home_wins.head())
print(home_wins.shape)
print(home_draws.tail())
print(home_draws.shape)
print(home_losses.head())
print(home_losses.shape)

num_of_home_wins = home_wins.shape[0]
num_of_home_draws = home_draws.shape[0]
num_of_home_losses = home_losses.shape[0]

home_wdl = [num_of_home_wins,num_of_home_draws,num_of_home_losses]
labels = ["wins","draws","losses"]
colors = ["blue","yellow","red"]
plt.figure(figsize=(12,9))
plt.title("Manchester City overall home performances (2006-2018)",fontdict={"fontweight":"bold","fontsize":15})
plt.pie(home_wdl,labels=labels,colors=colors,autopct="%1.2f%%",explode=(0.01,0.01,0.01))
plt.savefig("Manchester City overall home performances (2006-2018)",dpi=300)
plt.show()

away_wins = away_games.loc[away_games["result"] == "A"]
away_draws = away_games.loc[away_games["result"] == "D"]
away_losses = away_games.loc[away_games["result"] == "H"]
print(away_wins.head())
print(away_draws.head())
print(away_losses.head())

num_of_away_wins = away_wins.shape[0]
num_of_away_draws = away_draws.shape[0]
num_of_away_losses = away_losses.shape[0]
print(num_of_away_wins,num_of_away_draws,num_of_away_losses)

away_wdl = [num_of_away_wins,num_of_away_draws,num_of_away_losses]
labels = ["wins","draws","losses"]
colors = ["blue","yellow","red"]
plt.figure(figsize=(12,9))
plt.title("Manchester City overall away performances (2006-2018)",fontdict={"fontweight":"bold","fontsize":15})
plt.pie(away_wdl,labels=labels,colors=colors,autopct="%1.2f%%",explode=(0.01,0.01,0.01))
plt.savefig("Manchester City overall away performances (2006-2018)",dpi=300)
plt.show()


derby_of_manchester = city_results[(city_results["home_team"] == "Manchester City")
 & (city_results["away_team"] =="Manchester United")
 | (city_results["home_team"] == "Manchester United") & (city_results["away_team"] == "Manchester City")]
print(derby_of_manchester)
city_derby_wins = derby_of_manchester[(derby_of_manchester["home_team"] == "Manchester City") &
 (derby_of_manchester["result"] == "H") 
 | (derby_of_manchester["away_team"] == "Manchester City") & (derby_of_manchester["result"] == "A")]
print(city_derby_wins)
derby_draws = derby_of_manchester[derby_of_manchester["result"] == "D"]
print(derby_draws)
united_derby_wins = derby_of_manchester[(derby_of_manchester["home_team"] == "Manchester United") & 
(derby_of_manchester["result"] == "H") 
 | (derby_of_manchester["away_team"] == "Manchester United") & (derby_of_manchester["result"] == "A")]
print(united_derby_wins)

city_vs_pool = city_results[(city_results["home_team"] == "Manchester City") & (city_results["away_team"] == "Liverpool")
| (city_results["home_team"] == "Liverpool") & (city_results["away_team"] == "Manchester City")]
print(city_vs_pool)



zero_goals_games = city_results.loc[results["home_goals"] + results["away_goals"] == 0 ]
print(zero_goals_games.head())
one_to_two = city_results.loc[(results["home_goals"] + results["away_goals"] >= 1) & (results["home_goals"] +
results["away_goals"] <= 2) ]
print(one_to_two.head())
three_to_six = city_results.loc[(results["home_goals"] + results["away_goals"] >= 3) & (results["home_goals"] +
results["away_goals"] <= 6) ]
print(three_to_six.head())
seven_up = city_results.loc[results["home_goals"] + results["away_goals"] >= 7 ]
print(seven_up.head())

utakmice_bez_golova = zero_goals_games.shape[0]
utakmice_jedan_do_dva = one_to_two.shape[0]
utakmice_tri_do_sest = three_to_six.shape[0]
utakmice_sedam_plus = seven_up.shape[0]

parametri = [utakmice_bez_golova,utakmice_jedan_do_dva,utakmice_tri_do_sest,utakmice_sedam_plus]
etikete = ["bez golova","1-2 gola","3-6 golova","7+ golova"]
boje = ["red","green","blue","orange"]
plt.figure(figsize=(12,9))
plt.title("Broj golova na utakmicama Manchester City-ja u sezonama 2006-2018",fontdict={"fontweight":"bold"})
plt.pie(parametri,labels=etikete,colors=boje,autopct="%1.2f%%",explode=(0.01,0.01,0.01,0.01))
plt.savefig("Broj golova na utakmicama Manchester City-ja u sezonama 2006-2018",dpi=300)
plt.show()


city_results["score"] = city_results["home_goals"].astype("str") + ":" + city_results["away_goals"].astype("str")

print(city_results["score"].mode())
print(city_results["score"].value_counts())

home_one_null_wins = city_results[(city_results["home_team"] == "Manchester City") & (city_results["score"] == "1:0")]
away_one_null_defeats = city_results[(city_results["score"] == "1:0") & (city_results["away_team"] == "Manchester City")]
print(home_one_null_wins.head())
print(home_one_null_wins.shape)

print(away_one_null_defeats.head())
print(away_one_null_defeats.shape)

print(max(city_results["home_goals"] + city_results["away_goals"]))
most_goals_games =city_results[(city_results["home_goals"] + city_results["away_goals"])  == 9]
print(most_goals_games)

home_games_clean_sheet = home_games.loc[home_games["away_goals"] == 0]
print(home_games_clean_sheet.tail())
home_games_clean_sheet_wins = home_games.loc[(home_games["away_goals"] == 0) & (home_games["home_goals"] > 0 )]
print(home_games_clean_sheet_wins.head())