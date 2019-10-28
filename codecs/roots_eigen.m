(* ::Package:: *)

(* ::Input:: *)
(*fdet = 1+Cosh[Sqrt[\[Lambda]]]Cos[Sqrt[\[Lambda]]]+I \[Beta] Sqrt[\[Lambda]]/(1+I \[Beta] \[Lambda])\[Epsilon](Sinh[Sqrt[\[Lambda]]]cos[Sqrt[\[Lambda]]]+Cosh[Sqrt[\[Lambda]]]Sin[Sqrt[\[Lambda]]])*)


fdet1[\[Lambda]_]:= 1+Cosh[Sqrt[\[Lambda]]]Cos[Sqrt[\[Lambda]]] + \[Epsilon](Sinh[Sqrt[\[Lambda]]]cos[Sqrt[\[Lambda]]]+Cosh[Sqrt[\[Lambda]]]Sin[Sqrt[\[Lambda]]]);
(*Nsolve[(fdet1[\[Lambda]]/.{\[Epsilon]->0.001} )== 0 && 0 < Re[\[Lambda]] < 10, \[Lambda]]*)
FindRoot[fdet1[\[Lambda]],{\[Lambda],3.0+1.0 I}]


FindRoot[(Cos[z + I] - 2) (z + 2), {z, 1}]
FindRoot[x^2 + 1 == 0, {x, 1 + 1. I}]


FindRoot[1+Cosh[Sqrt[\[Lambda]]]Cos[Sqrt[\[Lambda]]] + 0.1(Sinh[Sqrt[\[Lambda]]]cos[Sqrt[\[Lambda]]]+Cosh[Sqrt[\[Lambda]]]Sin[Sqrt[\[Lambda]]]), {\[Lambda] , 1.0 + 1.0 I}]


Plot[1 + Cosh[Sqrt[\[Lambda]]] Cos[Sqrt[\[Lambda]]] + 0.1(Sinh[Sqrt[\[Lambda]]]Cos[Sqrt[\[Lambda]]]+Cosh[Sqrt[\[Lambda]]] Sin[Sqrt[\[Lambda]]]),{\[Lambda], 1, 20}]
