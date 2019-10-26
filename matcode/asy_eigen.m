(* ::Package:: *)

(* ::Input:: *)
(*cd1 = {1,0,1,1};*)
(*cd2 = {0,1,1,-1};*)
(*cd3s = \[Lambda]{-Cos[\[Sqrt]\[Lambda]],-Sin[\[Sqrt]\[Lambda]],Exp[\[Sqrt]\[Lambda]],Exp[-\[Sqrt]\[Lambda]]};*)
(*cd3t=\[Sqrt]\[Lambda] {-Sin[\[Sqrt]\[Lambda]],Cos[\[Sqrt]\[Lambda]],Exp[\[Sqrt]\[Lambda]],-Exp[-\[Sqrt]\[Lambda]]};*)
(*cd3 = cd3s+I \[Lambda] \[Beta]/(1+I \[Lambda] \[Beta]) \[Alpha]^2 cd3t;*)
(*cd4 ={Sin[\[Sqrt]\[Lambda]],-Cos[\[Sqrt]\[Lambda]],Exp[\[Sqrt]\[Lambda]],-Exp[-\[Sqrt]\[Lambda]]};*)
(*cd={cd1,cd2,cd3,cd4};*)
(*Det[cd]//Simplify*)


(* ::Input:: *)
(**)


Fall = (E^-Sqrt[\[Lambda]] (2 E^Sqrt[\[Lambda]] (-I+\[Beta] \[Lambda])+(-I - \[Epsilon] \[Beta] Sqrt[\[Lambda]]+\[Beta] \[Lambda]+E^(2 Sqrt[\[Lambda]]) (-I + \[Epsilon] \[Beta] Sqrt[\[Lambda]]+\[Beta] \[Lambda])) Cos[Sqrt[\[Lambda]]]+(1+E^(2 Sqrt[\[Lambda]])) \[Epsilon] \[Beta] Sqrt[\[Lambda]] Sin[Sqrt[\[Lambda]]]))/(-I+\[Beta] \[Lambda]);
\[Lambda]  = \[Lambda]0 + \[Epsilon] \[Lambda]1 + \[Epsilon]^2 \[Lambda]2 + + \[Epsilon]^3 \[Lambda]3;
Fall/.{\[Epsilon]->0}//Simplify
D[Fall,{\[Epsilon],1}]/.{\[Epsilon]->0}//Simplify
D[Fall,{\[Epsilon],2}]/.{\[Epsilon]->0}//Simplify


s0 = 2+(E^-Sqrt[\[Lambda]0]+E^Sqrt[\[Lambda]0]) Cos[Sqrt[\[Lambda]0]];
s1 = (E^-Sqrt[\[Lambda]0] ((-1+E^(2 Sqrt[\[Lambda]0])) (-I \[Lambda]1+\[Beta] \[Lambda]0 (2+\[Lambda]1)) Cos[Sqrt[\[Lambda]0]]-(1+E^(2 Sqrt[\[Lambda]0])) (\[Beta] \[Lambda]0 (-2+\[Lambda]1)-I \[Lambda]1) Sin[Sqrt[\[Lambda]0]]))/(2 Sqrt[\[Lambda]0] (-I+\[Beta] \[Lambda]0));
s2 = 1/(4 \[Lambda]0^(3/2) (-I+\[Beta] \[Lambda]0)^2) E^-Sqrt[\[Lambda]0] (((-1+E^(2 Sqrt[\[Lambda]0])) (\[Lambda]1^2-4 \[Lambda]0 \[Lambda]2)-2 I \[Beta] \[Lambda]0 (2 (-1+E^(2 Sqrt[\[Lambda]0]) (1+2 Sqrt[\[Lambda]0])+2 Sqrt[\[Lambda]0]) \[Lambda]1-(-1+E^(2 Sqrt[\[Lambda]0])) \[Lambda]1^2+4 (-1+E^(2 Sqrt[\[Lambda]0])) \[Lambda]0 \[Lambda]2)+\[Beta]^2 \[Lambda]0^2 ((4+E^(2 Sqrt[\[Lambda]0]) (-4+8 Sqrt[\[Lambda]0])+8 Sqrt[\[Lambda]0]) \[Lambda]1-(-1+E^(2 Sqrt[\[Lambda]0])) \[Lambda]1^2+4 (-1+E^(2 Sqrt[\[Lambda]0])) \[Lambda]0 \[Lambda]2)) Cos[Sqrt[\[Lambda]0]]-((1+E^(2 Sqrt[\[Lambda]0]) (1-2 Sqrt[\[Lambda]0])+2 Sqrt[\[Lambda]0]) \[Lambda]1^2-4 (1+E^(2 Sqrt[\[Lambda]0])) \[Lambda]0 \[Lambda]2-2 I \[Beta] \[Lambda]0 (-2 (1+E^(2 Sqrt[\[Lambda]0])) \[Lambda]1+(-1+E^(2 Sqrt[\[Lambda]0]) (-1+2 Sqrt[\[Lambda]0])-2 Sqrt[\[Lambda]0]) \[Lambda]1^2+4 (1+E^(2 Sqrt[\[Lambda]0])) \[Lambda]0 \[Lambda]2)+\[Beta]^2 \[Lambda]0^2 (4 (1+E^(2 Sqrt[\[Lambda]0])) \[Lambda]1+(-1+E^(2 Sqrt[\[Lambda]0]) (-1+2 Sqrt[\[Lambda]0])-2 Sqrt[\[Lambda]0]) \[Lambda]1^2+4 (1+E^(2 Sqrt[\[Lambda]0])) \[Lambda]0 \[Lambda]2)) Sin[Sqrt[\[Lambda]0]]);
lam0 = FindRoot[s0==0,{\[Lambda]0,1.0}]
lam1 = Solve[s1==0,{\[Lambda]1}]//Simplify;
lam1 = lam1[[1]]
lam2 = Solve[s2==0,{\[Lambda]2}]/.lam1//Simplify;
lam2 = lam2[[1]]
lam1 = lam1/.lam0//Simplify
lam2 = lam2/.lam1/.lam0//Simplify



