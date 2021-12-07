"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "sjak3"
__version__ = "2021.12.07"

import rhinoscriptsyntax as rs
obj = Crv
if rs.IsCurve(obj):
    a = rs.OffsetCurve( obj, [0,0,0], 0.01 )
    A_1 = rs.CurveArea(obj)                     #A_1 is original crv.
    A_2 = rs.CurveArea(a)                       #A_2 is Offsetted crv.
    if(A_2 >=  A_1):
        C = rs.OffsetCurve(obj, [0,0,0], D)
    else :                                      
        d2 = D*(-1)
        C = rs.OffsetCurve(obj, [0,0,0], d2)
        
       
       
#If offsetted crv is larger than original one, there is no need to flip crv.
#Otherwise, Crv needs to be flipped.
#Comparison Crv (a) is offsetted 0.01.