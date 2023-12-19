
import numpy as np
from matplotlib import axes as a

import plottool.plotParameter as Pm
import plottool.plotUtils as Md
Pm.mpl_init()

########################
# ===== BandPlot ===== #
########################

def BandSinglePlot(ax: a.Axes, values, kpoints, EneScale, Ecenter=0, detailgrid=False, MinorScale=-1, dn=-1, bdcolor=""):
    #----- add values -----#
    for i, value in enumerate(values):
        if i == dn : break
        if bdcolor == 'rainbow': color = Pm.Colorlist(i%5)  #n本ごとに色を変える
        elif bdcolor == "": color = 'gray'
        else : color = bdcolor
        ax.plot( value[0], value[1], c=color, lw=Pm.Band_line_width ) #灰色

    #----- axes config -----#
    Md.Kaxis(ax, 'x', kpoints)
    Md.Eaxis(ax, 'y', EneScale, Ecenter=Ecenter, detailgrid=detailgrid, MinorScale=MinorScale)

def ProjBandPlot(ax: a.Axes, fig, values, kpoints, EneScale, Ecenter=0, detailgrid=False, MinorScale=-1, dn=-1, cmap='viridis_r', cmax=0.8, cmin=0.0, ms=2):
    #----- add values -----#
    for i, value in enumerate(values):
        if i == dn : break
        ax.scatter( value[0], value[1], c=value[2], s=ms, cmap=cmap, vmax=cmax, vmin=cmin)

    #----- axes config -----#
    Md.Kaxis(ax, 'x', kpoints)
    Md.Eaxis(ax, 'y', EneScale, Ecenter=Ecenter, detailgrid=detailgrid, MinorScale=MinorScale)

def BandComparePlot(ax: a.Axes, values1, values2, kpoints, EneScale, Ecenter=0, detailgrid=False, MinorScale=-1, dn=-1):
    #-----values-----#\
    for i, value1 in enumerate(values1):
        if i == dn : break
        color=Pm.Colorlist(0)
        ax.plot( value1[0], value1[1], c=color, lw=Pm.Band_line_width)
    for i, value2 in enumerate(values2):
        if i == dn : break
        color=Pm.Colorlist(1)
        ax.plot( value2[0], value2[1], c=color, lw=Pm.Band_line_width)

    Md.Kaxis(ax, 'x', kpoints)
    Md.Eaxis(ax, 'y', EneScale, Ecenter=Ecenter, detailgrid=detailgrid, MinorScale=MinorScale)

def AdjustXvalue(x_source, x_source_max: float, x_ref_max: float):
    x_new=[ float(xs*x_ref_max/x_source_max) for xs in x_source ]
    return x_new

#######################
# ===== DosPlot ===== #
#######################

def DosPlot(ax: a.Axes, values, EneScale, Eaxis='y', Ecenter=0, detailgrid=False, MinorScale=-1):
    # values:[[e1,d1],[e2,d2]....[en,dn]]
    #   nmax: 10 (colorlistを10までしか登録してない)
    #   e: Energy, d: Dos  e1,d1などはすべてlist

    if Eaxis == 'x' :
        for i, value in enumerate(values):
            ax.plot( value[0], value[1], c=Pm.Colorlist(i), lw=Pm.Dos_line_width )
        Md.Eaxis(ax, 'x', EneScale, Ecenter=Ecenter, detailgrid=detailgrid, MinorScale=MinorScale)
        Md.Daxis(ax, 'y', EneScale, values, Ecenter=Ecenter)

    elif Eaxis == 'y' :
        for i, value in enumerate(values):
            ax.plot( value[1], value[0], c=Pm.Colorlist(i), lw=Pm.Dos_line_width )
        Md.Eaxis(ax, 'y', EneScale, Ecenter=Ecenter, detailgrid=detailgrid, MinorScale=MinorScale)
        Md.Daxis(ax, 'x', EneScale, values, Ecenter=Ecenter)

######################

def AHCplot(ax: a.Axes, Ene, AHC):
    ax.plot( Ene, AHC, c='black' )
    Md.Eaxis(ax, 'x', [0.1, 3, 3])
    ax.set_ylabel(r"$\sigma_{ij}\;\;\rm{[S/cm]}$")

def ANCplot(ax: a.Axes, Ene, ANC):
    ax.plot( Ene, ANC, c='black' )
    Md.Eaxis(ax, 'x', [0.1, 3, 3])
    #Md.addgrid(ax, 'y')
    ax.set_ylabel(r"$\alpha_{ij}$")














