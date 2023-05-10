from Statistics_Functions import *
from mean_Player_Functions import *
import seaborn
import matplotlib.pyplot as plt

#function_list = [(mean_pC, "pC"), (mean_pD, "pD"), (mean_r, "r"), (mean_c, "c"), (mean_cprm,"c'"), (mean_piCC, "piCC"), (mean_piCD, "piCD"), (mean_piDC, "piDC"), (mean_piDD, "piDD"), (mean_score_Prisoner, "sPr"), (mean_scoreprm_Prisoner, "sPr'"), (mean_score_Snowdrift, "sSn"), (mean_scoreprm_Snowdrift, "sSn'"), (mean_nice, "n"), (mean_rec, "t"), (mean_recprm, "t'")]

#scoreList = [(mean_score_Prisoner, "sPr"), (mean_score_Snowdrift, "sSn")]

#probabilityList = [(mean_pC, "pC"), (mean_pD, "pD"), (mean_c, "c"), (mean_piCC, "piCC"), (mean_piCD, "piCD"), (mean_piDC, "piDC"), (mean_piDD, "piDD"), (mean_nice, "n"), (mean_rec, "t")]

extraList = [(mean_piCD, "piCD")]

#Given a function in two variables x and y, and a name for the functions, returns a heat map of it
def plotHeatmap(f, name, N = 100, scale_min = 0, scale_max = 1):#, scale_min = 0, scale_max = 1):
    #We generate our plot
    data = [[f(k1/N,k2/N)  for k1 in range(0,N+1)] for k2 in range(0,N+1)]
    heat_map = seaborn.heatmap(data, cmap="BuPu", cbar_kws={'orientation': 'vertical'}, vmin = scale_min, vmax = scale_max)

    heat_map.invert_yaxis()
    #We want to have fewer ticks than we have data points
    increment = 5
    heat_map.set_xticks([k*(N+1)/increment for k in range(0,increment+1)])
    heat_map.set_yticks([k*(N+1)/increment for k in range(0,increment+1)])
    #We want these ticks labeled appropriately
    heat_map.set_xticklabels([k/increment for k in range(0,increment+1)])
    heat_map.set_yticklabels([k/increment for k in range(0,increment+1)])
    #We label our graph
    plt.xlabel('$\mathrm{p}_\mathrm{C}$')
    plt.ylabel('$\mathrm{p}_\mathrm{D}$')
    #plt.title(name)
    #We save our plot
    #filelocation = 'Plot_Data/'
    filetype = '.png'
    #savefile_name = filelocation + name + filetype
    savefile_name = name + filetype
    plt.savefig(savefile_name)
    plt.close()
    return 0

N = 6*10**3

#for f in scoreList:
#    plotHeatmap(f[0], f[1], N, 1.5, 3)
#    print(f[1])

#for f in probabilityList:
#    plotHeatmap(f[0], f[1], N, 0, 1)
#    print(f[1])

for f in extraList:
    plotHeatmap(f[0], f[1], N, 0, 0.5)
    print(f[1])
#print(cov(function_list[0], function_list[1]))
