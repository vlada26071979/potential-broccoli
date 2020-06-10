import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


premier_league = pd.read_csv("premier_league.csv")
results = pd.read_csv("results_12seasons.csv")


premier_league.groupby("season").goals.agg(["min","max","mean"]).plot(kind="bar",
title="Minimum,maksimum i prosek postignutih golova u sezonama PL 2006-2018",figsize=(16,10))
plt.savefig("Minimum,maksimum i prosek postignutih golova u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,9))
plt.title("Broj ucesca svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.team.value_counts().plot(kind="barh",fontsize=7,xticks=(np.arange(1,13)))
plt.xlabel("broj sezona u PL")
plt.savefig("Broj ucesca svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,9))
plt.title("Broj pobeda timova u PL po sezonama 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("season").wins.sum().plot(kind="bar")
plt.xticks(rotation=60)
plt.savefig("Broj pobeda timova u PL po sezonama 2006-2018",dpi=300)
plt.show() 

plt.figure(figsize=(15,9))
plt.title("Broj golova u PL u sezonama 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("season").goals.sum().plot(kind="bar",color=["b","r","g","y","cyan","purple"])
plt.xticks(rotation=60)
plt.savefig("Broj golova u PL u sezonama 2006-2018",dpi=300)
plt.show() 

plt.figure(figsize=(15,9))
plt.title("Broj poraza timova u PL po sezonama 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("season").losses.sum().plot(kind="bar",color=["b","r","g","y","cyan","purple","brown","black","orange"])
plt.xticks(rotation=60)
plt.savefig("Broj poraza timova u PL po sezonama 2006-2018",dpi=300)
plt.show() 


plt.figure(figsize=(15,9))
plt.title("Broj crvenih kartona u PL po sezonama 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("season").total_red_card.sum().plot(kind="bar",color="r")
plt.xticks(rotation=60)
plt.savefig("Broj crvenih kartona u PL po sezonama 2006-2018",dpi=300)
plt.show()   

plt.figure(figsize=(15,9))
plt.title("Broj zutih kartona u PL po sezonama 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("season").total_yel_card.sum().plot(kind="bar",color="y")
plt.xticks(rotation=60)
plt.savefig("Broj zutih kartona u PL po sezonama 2006-2018",dpi=300)
plt.show()  


plt.figure(figsize=(15,8))
plt.title("Prosek broja golova svakog tima postignutih u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").goals.mean().plot(kind="barh",fontsize=7)
plt.ylabel("broj golova")
plt.savefig("Prosek broja golova svakog tima postignutih u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Prosek broja pobeda svakog tima postignutih u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").wins.mean().plot(kind="barh",fontsize=7)
plt.ylabel("broj pobeda")
plt.savefig("Prosek broja pobeda svakog tima postignutih u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Prosek broja poraza svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").losses.mean().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.ylabel("broj poraza")
plt.savefig("Prosek broja poraza svakog tima postignutih u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj golova svakog tima postignutih u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").goals.sum().plot(kind="barh",fontsize=7,
color=['r', 'g', 'b', 'k', 'm', 'y'],xticks=(np.arange(0,1000,step=50)))
plt.ylabel("broj golova")
plt.savefig("Ukupan broj golova svakog tima postignutih u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj primljenih golova svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").goals_conceded.sum().plot(kind="barh",fontsize=7,
color=['r', 'g', 'b', 'k', 'm', 'y'],xticks=(np.arange(0,800,step=50)))
plt.xlabel("broj primljenih golova")
plt.savefig("Ukupan broj primljenih golova svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(16,10))
plt.title("Ukupan broj utakmica svakog tima bez primljenog gola u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").clean_sheet.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj utakmica bez primljenog gola")
plt.savefig("Ukupan broj utakmica svakog tima bez primljenog gola u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(16,10))
plt.title("Ukupan broj golova svakog tima postignut van kaznenog prostora u sezonama PL 2006-2018",
fontdict={"fontweight":"bold"})
premier_league.groupby("team").att_obox_goal.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj golova")
plt.savefig("Ukupan broj golova svakog tima postignut van kaznenog prostora u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(16,10))
plt.title("Ukupan broj golova svakog tima postignut iz kaznenog prostora u sezonama PL 2006-2018",
fontdict={"fontweight":"bold"})
premier_league.groupby("team").att_ibox_goal.sum().plot(kind="barh",fontsize=7,
color=['r', 'g', 'b', 'k', 'm', 'y'],xticks=(np.arange(0,1000,step=50)))
plt.xlabel("broj golova")
plt.savefig("Ukupan broj golova svakog tima postignut iz kaznenog prostora u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(16,9))
plt.title("Ukupan broj golova svakog tima postignut iz penala u sezonama PL 2006-2018",
fontdict={"fontweight":"bold"})
premier_league.groupby("team").att_pen_goal.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj golova")
plt.savefig("Ukupan broj golova svakog tima postignut iz penala u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(16,9))
plt.title("Ukupan broj golova svakog tima postignut glavom u sezonama PL 2006-2018",
fontdict={"fontweight":"bold"})
premier_league.groupby("team").att_hd_goal.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj golova")
plt.savefig("Ukupan broj golova svakog tima postignut glavom u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(16,9))
plt.title("Ukupan broj golova svakog tima postignut iz slobodnih udaraca u sezonama PL 2006-2018",
fontdict={"fontweight":"bold"})
premier_league.groupby("team").att_freekick_goal.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj golova")
plt.savefig("Ukupan broj golova svakog tima postignut iz slobodnih udaraca u sezonama PL 2006-2018",dpi=300)
plt.show()


plt.figure(figsize=(16,9))
plt.title("Ukupan broj golova svakog tima postignut iz kontranapada u sezonama PL 2006-2018",
fontdict={"fontweight":"bold"})
premier_league.groupby("team").goal_fastbreak.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj golova")
plt.savefig("Ukupan broj golova svakog tima postignut iz kontranapada u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(16,9))
plt.title("Ukupan broj autogolova svakog tima sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").own_goals.sum().plot(kind="barh",fontsize=7,
color=['r', 'g', 'b', 'k', 'm', 'y'],xticks=np.arange(0,31,step=2))
plt.xlabel("broj autogolova")
plt.savefig("Ukupan broj autogolova svakog tima sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(16,9))
plt.title("Ukupan broj stativa i precki svakog tima u sezonama PL 2006-2018",
fontdict={"fontweight":"bold"})
premier_league.groupby("team").hit_woodwork.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj pogodjenih stativa i precki")
plt.savefig("Ukupan broj stativa i precki svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(16,9))
plt.title("Ukupan broj odbranjenih penala svakog tima u sezonama PL 2006-2018",
fontdict={"fontweight":"bold"})
premier_league.groupby("team").penalty_save.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj odbranjenih penala")
plt.savefig("Ukupan broj odbranjenih penala svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Broj pobeda svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").wins.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj pobeda")
plt.savefig("Broj pobeda svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Broj poraza svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").losses.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj poraza")
plt.savefig("Broj poraza svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Broj suteva u okvir gola svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").ontarget_scoring_att.sum().plot(kind="barh",fontsize=7)
plt.xlabel("broj suteva u okvir gola")
plt.savefig("Broj poraza svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Broj dodavanja svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").total_pass.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj dodavanja")
plt.savefig("Broj dodavanja svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Broj dugackih lopti svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").total_long_balls.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj dugackih lopti")
plt.savefig("Broj dugackih lopti svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj zutih kartona svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").total_yel_card.sum().plot(kind="barh",fontsize=7,color="y")
plt.xlabel("broj zutih kartona")
plt.savefig("Ukupan broj zutih kartona svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj crvenih kartona svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").total_red_card.sum().plot(kind="barh",fontsize=7,color="r")
plt.xlabel("broj crvenih kartona")
plt.savefig("Ukupan broj crvenih kartona svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj presecenih dodavanja svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").interception.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj presecenih dodavanja")
plt.savefig("Ukupan broj presecenih dodavanja svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj dodira sa loptom svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").touches.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj dodira")
plt.savefig("Ukupan broj dodira sa loptom svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj izvedenih kornera svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").corner_taken.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj kornera")
plt.savefig("Ukupan broj izvedenih kornera svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj centarsuteva svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").total_cross.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj centarsuteva")
plt.savefig("Ukupan broj centarsuteva svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj ofsajda svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").total_offside.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj ofsajd pozicija")
plt.savefig("Ukupan broj ofsajda svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj startova svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").total_tackle.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj startova")
plt.savefig("Ukupan broj startova svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj startova poslednjeg igraca u odbrani svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").last_man_tackle.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj startova poslednjeg igraca u odbrani")
plt.savefig("Ukupan broj startova poslednjeg igraca u odbrani svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

plt.figure(figsize=(15,8))
plt.title("Ukupan broj blokiranih suteva svakog tima u sezonama PL 2006-2018",fontdict={"fontweight":"bold"})
premier_league.groupby("team").outfielder_block.sum().plot(kind="barh",fontsize=7,color=['r', 'g', 'b', 'k', 'm', 'y'])
plt.xlabel("broj blokova")
plt.savefig("Ukupan broj blokiranih suteva svakog tima u sezonama PL 2006-2018",dpi=300)
plt.show()

