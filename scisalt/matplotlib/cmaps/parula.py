import os as _os
on_rtd = _os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    import matplotlib.pyplot as _plt
    import matplotlib.colors as _mc


def _x(val):
    return (val-1)/63


def _y(val):
    return val/255

cdict = {'red':   [(_x(1)  , 0.0     , _y(53))   ,
                   (_x(4)  , _y(53)  , _y(53))   ,
                   (_x(5)  , _y(50)  , _y(50))   ,
                   (_x(6)  , _y(43)  , _y(43))   ,
                   (_x(7)  , _y(32)  , _y(32) )  ,
                   (_x(8)  , _y(15)  , _y(15) )  ,
                   (_x(9)  , _y(3)   , _y(3)  )  ,
                   (_x(10) , _y(1)   , _y(1)  )  ,
                   (_x(11) , _y(4)   , _y(4)  )  ,
                   (_x(17) , _y(20)  , _y(20) )  ,
                   (_x(18) , _y(19)  , _y(19) )  ,
                   (_x(21) , _y(9)   , _y(9)  )  ,
                   (_x(22) , _y(7)   , _y(7)  )  ,
                   (_x(26) , _y(7)   , _y(7)  )  ,
                   (_x(27) , _y(10)  , _y(10) )  ,
                   (_x(53) , _y(248) , _y(248))  ,
                   (_x(54) , _y(253) , _y(253))  ,
                   (_x(55) , _y(255) , _y(255))  ,
                   (_x(62) , _y(245) , _y(245))  ,
                   (_x(64) , _y(249) , _y(249))] ,

         'green': [(_x(1)  , 0.0     , _y(42))   ,
                   (_x(4)  , _y(61)  , _y(61))   ,
                   (_x(5)  , _y(67)  , _y(67))   ,
                   (_x(6)  , _y(74)  , _y(74))   ,
                   (_x(7)  , _y(83)  , _y(83) )  ,
                   (_x(8)  , _y(92)  , _y(92) )  ,
                   (_x(9)  , _y(99)  , _y(99) )  ,
                   (_x(10) , _y(104) , _y(104))  ,
                   (_x(11) , _y(109) , _y(109))  ,
                   (_x(17) , _y(133) , _y(133))  ,
                   (_x(18) , _y(137) , _y(137))  ,
                   (_x(21) , _y(152) , _y(152))  ,
                   (_x(22) , _y(156) , _y(156))  ,
                   (_x(26) , _y(169) , _y(169))  ,
                   (_x(27) , _y(172) , _y(172))  ,
                   (_x(53) , _y(186) , _y(186))  ,
                   (_x(54) , _y(190) , _y(190))  ,
                   (_x(55) , _y(195) , _y(195))  ,
                   (_x(62) , _y(235) , _y(235))  ,
                   (_x(64) , _y(251) , _y(251))] ,

         'blue':  [(_x(1)  , 0.0     , _y(135))   ,
                   (_x(4)  , _y(173) , _y(173))   ,
                   (_x(5)  , _y(185) , _y(185))   ,
                   (_x(6)  , _y(199) , _y(199))   ,
                   (_x(7)  , _y(212) , _y(212))   ,
                   (_x(8)  , _y(221) , _y(221))   ,
                   (_x(9)  , _y(225) , _y(225))   ,
                   (_x(10) , _y(225) , _y(225))   ,
                   (_x(11) , _y(224) , _y(224))   ,
                   (_x(17) , _y(212) , _y(212))   ,
                   (_x(18) , _y(211) , _y(211))   ,
                   (_x(21) , _y(209) , _y(209))   ,
                   (_x(22) , _y(207) , _y(207))   ,
                   (_x(26) , _y(194) , _y(194))   ,
                   (_x(27) , _y(189) , _y(189))   ,
                   (_x(53) , _y(68)  , _y(68) )   ,
                   (_x(54) , _y(61)  , _y(61) )   ,
                   (_x(55) , _y(55)  , _y(55) )   ,
                   (_x(62) , _y(24)  , _y(24) )   ,
                   (_x(64) , _y(14)  , _y(14) )]}

parula = _mc.LinearSegmentedColormap('parula', cdict)
_plt.register_cmap(cmap=parula)
