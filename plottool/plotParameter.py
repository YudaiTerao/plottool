
import os
import glob
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import rcParams

#----- pdf設定 -----#
width = 21.0
height = 29.7
margin = 2.2
header = 3.5
bd_single_margin = 5
bd_table_margin = 2.2
bd_detail_margin = 2
bdp_single_margin = 1.5
bdp_table_margin = 1.5
bdp_detail_margin = 1.8
#axes_column_width, axes_row_height
bd_single_width = [10]
bd_single_height = [10]
bd_table_width = [10, 10]
bdp_table_width = [10, 7]
bdp_table_height = [10, 10, 10]
bd_table_height = [10, 10, 10]
bd_detail_width = [18]
bd_detail_height = [30]
#default EneScale(for pdf)
bd_table_ESl = [[0.5,3,3], [1,3,3],\
                [2,4,4]  , [5,4,4] ,\
                [10,3,3] , [20,3,3]]
bd_detail_ESl = [1,7,7]
#######

#----- plot関連 -----#
K_ticks_pad=7
D_ticks_pad=7
E_ticks_pad=7
E_label_pad=1.5

Fermi_line_width = 1.3
K_line_width = 1
Band_line_width = 1.1
Dos_line_width = 1.1
detail_majorgrid_lw = 0.6
detail_minorgrid_lw = 0.3
########

def filelist(dirpath):
##ディレクトリを与えるとディレクトリ内のfileのpathをリストで出力
    files = []
    if dirpath[-1] != '/': files.extend( glob.glob("{}/*".format(dirpath)) )
    else : files.extend( glob.glob("{}*".format(dirpath)) )
    return files

def is_under_ssh_connection():
    # The environment variable `SSH_CONNECTION` exists only in the SSH session.
    # https://qiita.com/take_me/items/f91a3ffcee4c103a9a03
    return 'SSH_CONNECTION' in os.environ.keys()

def Colorlist(i):
    color_list=('#3288bd', '#d53e4f', '#fdae61', '#abdda4', '#f46d43', '#66c2a5', '#fee08b', '#5e4fa2', '#9e0142', '#e6f598')
    return color_list[i]

def mpl_init():

    if is_under_ssh_connection(): 
        mpl.use('TkAgg')
        #----- Default Font in remote -----#
        rcParams["mathtext.fontset"] = "cm"   #texfont
        rcParams['font.size']=14
        # zodiacにTimes New Romanがない...?
    else :
        #----- Default Font in local -----#
        rcParams["font.serif"] = "Times New Roman"
        rcParams["font.sans-serif"] = 'Arial'
        rcParams["font.family"] = "serif"
        rcParams["mathtext.fontset"] = "cm"   #texfont
        rcParams['font.size']=14

    rcParams["axes.linewidth"] = 1.7 # 枠線の太さ
    for axis in ['x', 'y']:
        rcParams["{}tick.direction".format(axis)] = "in"      # 目盛の向き
        rcParams["{}tick.major.width".format(axis)] = 1.3     # 軸の線の線幅
        rcParams["{}tick.major.size".format(axis)] = 3.5      # 目盛の長さ
        rcParams["{}tick.minor.visible".format(axis)] = False # 副目盛の表示
        rcParams["{}tick.minor.width".format(axis)] = 0.6     # 副目盛の線幅
        rcParams["{}tick.minor.size".format(axis)] = 2.0      # 副目盛の長さ
        rcParams["{}tick.labelsize".format(axis)] = 12        # 目盛のfontsize

    rcParams["xtick.top"] = True            # 上部に目盛iを描くかどうか
    rcParams["xtick.bottom"] = True         # 下部に目盛を描くかどうか
    rcParams["ytick.left"] = True           # 左部に目盛を描くかどうか
    rcParams["ytick.right"] = True          # 右部に目盛を描くかどうか

#pdfのtitle
fontdict_title = {
    'color' : '#000000',
    'size' : 20
}
#Eaxisのlabel用
fontdict_Elabel = {
    'color' : '#000000',
    'size' : 16
}
#Kaxisの目盛用
fontdict_Kticks = { 
    'color' : '#000000', 
    'size' : 13
}
#fontdict_Eticks = {
#    'family' : 'Times New Roman',
#    'color' : '#000000',
#    'size' : 13
#}
#fontdict_Dticks = {
#    'family' : 'Times New Roman',
#    'color' : '#000000',
#    'size' : 13
#}
#fontdict_legend = {
#    'family' : 'Times New Roman',
#    'color' : '#000000',
#    'size' : 16
#}
