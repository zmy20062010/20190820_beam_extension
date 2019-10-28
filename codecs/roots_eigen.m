(* ::Package:: *)

(* ::Input:: *)
(*fdet[\[Lambda]_] := 1+Cosh[Sqrt[\[Lambda]]]Cos[Sqrt[\[Lambda]]]+I \[Beta] Sqrt[\[Lambda]]/(1+I \[Beta] \[Lambda])\[Epsilon](Sinh[Sqrt[\[Lambda]]]Cos[Sqrt[\[Lambda]]]+Cosh[Sqrt[\[Lambda]]]Sin[Sqrt[\[Lambda]]]);*)
(*FindRoot[fdet[\[Lambda]]/.{\[Epsilon]-> 20, \[Beta]->0.01},{\[Lambda],3.0+0.0 I}]*)


Plot[1 + Cosh[Sqrt[\[Lambda]]] Cos[Sqrt[\[Lambda]]] + 0.1(Sinh[Sqrt[\[Lambda]]]Cos[Sqrt[\[Lambda]]]+Cosh[Sqrt[\[Lambda]]] Sin[Sqrt[\[Lambda]]]),{\[Lambda], 1, 150}]


Plot3D[1+Cosh[Sqrt[\[Lambda]]]Cos[Sqrt[\[Lambda]]]+I \[Beta] Sqrt[\[Lambda]]/(1+I \[Beta] \[Lambda])(Sinh[Sqrt[\[Lambda]]]Cos[Sqrt[\[Lambda]]]+Cosh[Sqrt[\[Lambda]]]Sin[Sqrt[\[Lambda]]]),{\[Lambda], 1, 20},{\[Beta], 0, 1}]


Plot3D[Sin[x + y^2], {x, -3, 3}, {y, -2, 2}]

