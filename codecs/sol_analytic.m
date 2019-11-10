(* ::Package:: *)

(* ::Input:: *)
(*s1 = {1,0,1,0};*)
(*s2 = {0,1,0,1};*)
(*s31 ={-Cos[\[Sqrt]\[Sigma]],-Sin[\[Sqrt]\[Sigma]],Cosh[\[Sqrt]\[Sigma]],Sinh[\[Sqrt]\[Sigma]]};*)
(*s32 = {-Sin[\[Sqrt]\[Sigma]],Cos[\[Sqrt]\[Sigma]],Sinh[\[Sqrt]\[Sigma]],Cosh[\[Sqrt]\[Sigma]]};*)
(*s3 = s31 + \[Epsilon] * I  \[Beta] \[Sqrt]\[Sigma]/(1 + I  \[Beta]  \[Sigma]) * s32;*)
(*s4 ={Sin[\[Sqrt]\[Lambda]],-Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]};*)
(*cd={s1,s2,s3,s4};*)
(*Det[cd]//Simplify*)
(*t = {1,0,0,0};*)
(*coeff =LinearSolve[cd,t]/.{Cosh[Sqrt[\[Lambda]]]^2-Sinh[Sqrt[\[Lambda]]]^2->1,Cos[Sqrt[\[Lambda]]]^2+Sin[Sqrt[\[Lambda]]]^2->1}//Simplify*)
(*coeff.s1//Simplify*)
(*coeff.s2//Simplify*)
(*coeff.s3//Simplify*)
(*coeff.s4//Simplify*)


mysol1 = (1+Cos[Sqrt[\[Lambda]]]Cosh[Sqrt[\[Lambda]]]-Sin[Sqrt[\[Lambda]]]Sinh[Sqrt[\[Lambda]]]+(2I \[Beta] Sqrt[\[Lambda]] \[Epsilon])/(1+I \[Beta] \[Lambda]) Cos[Sqrt[\[Lambda]]]Sinh[Sqrt[\[Lambda]]])/(2(1+Cos[Sqrt[\[Lambda]]]Cosh[Sqrt[\[Lambda]]]+(I \[Beta] Sqrt[\[Lambda]] \[Epsilon])/(1 + I \[Beta] \[Lambda]) (Cos[Sqrt[\[Lambda]]]Sinh[Sqrt[\[Lambda]]]+Sin[Sqrt[\[Lambda]]]Cosh[Sqrt[\[Lambda]]])));
coeff1 =(-I + \[Beta] \[Lambda] + (-I+ \[Beta] \[Lambda]) Cos[Sqrt[\[Lambda]]] Cosh[Sqrt[\[Lambda]]]+(2 \[Beta] \[Epsilon] Sqrt[\[Lambda]] Cos[Sqrt[\[Lambda]]]+(I - \[Beta] \[Lambda]) Sin[Sqrt[\[Lambda]]]) Sinh[Sqrt[\[Lambda]]])/(2 (-I + \[Beta] \[Lambda] + Cosh[Sqrt[\[Lambda]]] ((-I + \[Beta] \[Lambda]) Cos[Sqrt[\[Lambda]]]+ \[Beta] \[Epsilon] Sqrt[\[Lambda]] Sin[Sqrt[\[Lambda]]])+ \[Beta] \[Epsilon] Sqrt[\[Lambda]] Cos[Sqrt[\[Lambda]]] Sinh[Sqrt[\[Lambda]]]));
(I Denominator[coeff1]-(1+I \[Beta] \[Lambda])Denominator[mysol1])//Expand//Simplify
(I Numerator[coeff1]-(1+I \[Beta] \[Lambda])Numerator[mysol1])//Expand//Simplify


mysol2 = (Cos[Sqrt[\[Lambda]]]Sinh[Sqrt[\[Lambda]]]+Sin[Sqrt[\[Lambda]]]Cosh[Sqrt[\[Lambda]]]+(2I \[Beta] Sqrt[\[Lambda]] \[Epsilon])/(1+I \[Beta] \[Lambda]) Sin[Sqrt[\[Lambda]]]Sinh[Sqrt[\[Lambda]]])/(2(1+Cos[Sqrt[\[Lambda]]]Cosh[Sqrt[\[Lambda]]]+(I \[Beta] Sqrt[\[Lambda]] \[Epsilon])/(1 + I \[Beta] \[Lambda]) (Cos[Sqrt[\[Lambda]]]Sinh[Sqrt[\[Lambda]]]+Sin[Sqrt[\[Lambda]]]Cosh[Sqrt[\[Lambda]]])));
coeff2 =((-I+\[Beta] \[Lambda]) Cosh[Sqrt[\[Lambda]]] Sin[Sqrt[\[Lambda]]]+((-I+\[Beta] \[Lambda]) Cos[Sqrt[\[Lambda]]]+2 \[Beta] \[Epsilon] Sqrt[\[Lambda]] Sin[Sqrt[\[Lambda]]]) Sinh[Sqrt[\[Lambda]]])/(2 (-I+\[Beta] \[Lambda]+Cosh[Sqrt[\[Lambda]]] ((-I+\[Beta] \[Lambda]) Cos[Sqrt[\[Lambda]]]+\[Beta] \[Epsilon] Sqrt[\[Lambda]] Sin[Sqrt[\[Lambda]]])+\[Beta] \[Epsilon] Sqrt[\[Lambda]] Cos[Sqrt[\[Lambda]]] Sinh[Sqrt[\[Lambda]]]));
(I Denominator[coeff1]-(1+I \[Beta] \[Lambda])Denominator[mysol1])//Expand//Simplify
(I Numerator[coeff1]-(1+I \[Beta] \[Lambda])Numerator[mysol1])//Expand//Simplify






