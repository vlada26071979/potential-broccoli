import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from functions import display_gen_stats
from functions import display_team_play_stats
from functions import display_att_stats
from functions import display_def_stats
from functions import display_other_stats



premier_league = pd.read_csv("premier_league.csv")
results = pd.read_csv("results_12seasons.csv")



print(premier_league.head())
print(premier_league.head())
print(premier_league.columns) 
print(premier_league.shape)
print(premier_league.info())
print(premier_league.describe())
print(premier_league.dtypes)
print(premier_league.select_dtypes(include="object").head())
print(results.select_dtypes(include="object").head())
print(results.select_dtypes(include="number").head())
print(premier_league.isnull().sum())
print()
print("Broj ucesca svakog tima u Premier ligi tokom 12 sezona 2006-2018:")
print(premier_league.team.value_counts())
print(premier_league.goals.nlargest(5))
najvise_golova_u_sezoni = premier_league.loc[premier_league["goals"] == 106]
print(najvise_golova_u_sezoni)
print(premier_league.wins.nlargest(3))
najvise_pobeda_u_sezoni = premier_league.loc[premier_league["wins"] == 32]
print(najvise_pobeda_u_sezoni)


team_summary = premier_league.groupby("team").sum()
print(team_summary)

display_gen_stats()
display_team_play_stats()
display_att_stats()
display_def_stats()
display_other_stats()


zero_goals_games = results.loc[results["home_goals"] + results["away_goals"] == 0 ]
print(zero_goals_games.head())
one_to_two = results.loc[(results["home_goals"] + results["away_goals"] >= 1) & (results["home_goals"] +
results["away_goals"] <= 2) ]
print(one_to_two.head())
three_to_six = results.loc[(results["home_goals"] + results["away_goals"] >= 3) & (results["home_goals"] +
results["away_goals"] <= 6) ]
print(three_to_six.head())
seven_up = results.loc[results["home_goals"] + results["away_goals"] >= 7 ]
print(seven_up.head())

utakmice_bez_golova = zero_goals_games.shape[0]
utakmice_jedan_do_dva = one_to_two.shape[0]
utakmice_tri_do_sest = three_to_six.shape[0]
utakmice_sedam_plus = seven_up.shape[0]

parametri = [utakmice_bez_golova,utakmice_jedan_do_dva,utakmice_tri_do_sest,utakmice_sedam_plus]
etikete = ["bez golova","1-2 gola","3-6 golova","7+ golova"]
boje = ["red","green","blue","orange"]
plt.figure(figsize=(12,9))
plt.title("Broj golova na utakmicama Premier lige u sezonama 2006-2018",fontdict={"fontweight":"bold"})
plt.pie(parametri,labels=etikete,colors=boje,autopct="%1.2f%%",explode=(0.01,0.01,0.01,0.01))
plt.savefig("Broj golova na utakmicama Premier lige u sezonama 2006-2018",dpi=300)
plt.show()

print(results.head())
print(results.shape)
print(results.groupby("season").result.value_counts())

plt.figure(figsize=(15,8))
plt.title("Broj pobeda domacina,remija i pobeda gostujucih timova u PL u sezonama 2006-2018")
results.groupby("season").result.value_counts().plot(kind="barh")
plt.savefig("Broj pobeda,remija i poraza u PL u sezonama 2006-2018",dpi=300)
plt.show()

home_team_wins = results[results["result"] == "H"]
print(home_team_wins.shape)
print(home_team_wins.head())
plt.figure(figsize=(15,8))
plt.title("Broj pobeda domacih timova po sezonama",fontdict={"fontweight":"bold"})
home_team_wins.groupby("season").result.value_counts().plot(kind="barh")
plt.savefig("Broj pobeda domacih timova po sezonama",dpi=300)
plt.show()

draws = results[results["result"] == "D"]
print(draws.head())
print(draws.shape)
plt.figure(figsize=(15,8))
plt.title("Broj neresenih rezultata po sezonama",fontdict={"fontweight":"bold"})
draws.groupby("season").result.value_counts().plot(kind="barh")
plt.savefig("Broj neresenih rezultata po sezonama",dpi=300)
plt.show()

goalless_draws = draws[draws["home_goals"] + draws["away_goals"] == 0]
print(goalless_draws.head())
print(goalless_draws.shape)
scoring_draws = draws[draws["home_goals"] + draws["away_goals"] > 0]
print(scoring_draws.head(20))
print(scoring_draws.shape)

away_team_wins = results[results["result"] == "A"]
print(away_team_wins.head())
print(away_team_wins.shape)
plt.figure(figsize=(15,8))
plt.title("Broj pobeda gostiju po sezonama",fontdict={"fontweight":"bold"})
away_team_wins.groupby("season").result.value_counts().plot(kind="barh")
plt.savefig("Broj pobeda gostiju po sezonama",dpi=300)
plt.show()

number_of_home_team_wins = home_team_wins.shape[0]
number_of_draws = draws.shape[0]
number_of_away_team_wins = away_team_wins.shape[0]

wdl = [number_of_home_team_wins,number_of_draws,number_of_away_team_wins]
labels = ["home wins","draws","away wins"]
colors = ["blue","orange","purple"]
plt.figure(figsize=(12,9))
plt.title("Broj pobeda domacina,broj neresenih i broj pobeda gostiju u PL (2006-2018)",
fontdict={"fontweight":"bold","fontsize":15})
plt.pie(wdl,labels=labels,colors=colors,autopct="%1.2f%%",explode=(0.01,0.01,0.01))
plt.savefig("Broj pobeda domacina,broj neresenih i broj pobeda gostiju u PL (2006-2018)",dpi=300)
plt.show()




































