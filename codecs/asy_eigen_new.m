(* ::Package:: *)

(* ::Input:: *)
(*cd10 = {1,0,1,0};*)
(*cd20 = {0,1,0,1};*)
(*cd30 ={-Cos[\[Sqrt]\[Lambda]],-Sin[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]]};*)
(*cd40 ={Sin[\[Sqrt]\[Lambda]],-Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]};*)
(*cd0={cd10,cd20,cd30,cd40};*)
(*Det[cd0]//Simplify;*)
(*bd0 = {1,0,0,0};*)
(*coeff0 =LinearSolve[cd0,bd0]/.{Cosh[Sqrt[\[Lambda]]]^2-Sinh[Sqrt[\[Lambda]]]^2->1,Cos[Sqrt[\[Lambda]]]^2+Sin[Sqrt[\[Lambda]]]^2->1}//Simplify*)
(*coeff0.cd1//Simplify*)
(*coeff0.cd2//Simplify*)
(*coeff0.cd3//Simplify*)
(*coeff0.cd4//Simplify*)


cd11 = {1,0,1,0};
cd21 = {0,1,0,1};
cd31 ={-Cos[\[Sqrt]\[Lambda]],-Sin[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]]};
cd41 ={Sin[\[Sqrt]\[Lambda]],-Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]};
cd5 = {-Sin[\[Sqrt]\[Lambda]],Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]};
cd1={cd11,cd21,cd31,cd41};
Det[cd1]//Simplify;
bd1 = {0,0,1,0};
coeff0.cd5//Simplify
coeff1 =LinearSolve[cd1,bd1]/.{Cosh[Sqrt[\[Lambda]]]^2-Sinh[Sqrt[\[Lambda]]]^2->1,Cos[Sqrt[\[Lambda]]]^2+Sin[Sqrt[\[Lambda]]]^2->1}//Simplify
coeff1 = coeff1* (-coeff0.cd5) * I \[Beta] Sqrt[\[Lambda]]/(1 + I \[Beta] \[Lambda])//Simplify
coeff1.cd11//Simplify
coeff1.cd21//Simplify
coeff1.cd31//Simplify
coeff1.cd41//Simplify


cd12 = {1,0,1,0};
cd22 = {0,1,0,1};
cd32 ={-Cos[\[Sqrt]\[Lambda]],-Sin[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]]};
cd42 ={Sin[\[Sqrt]\[Lambda]],-Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]};
cd5 = {-Sin[\[Sqrt]\[Lambda]],Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]};
cd2 = {cd12,cd22,cd32,cd42};
Det[cd2]//Simplify;
bd2 = {0,0,1,0};
coeff1.cd5//Simplify
coeff2 =LinearSolve[cd2,bd2]/.{Cosh[Sqrt[\[Lambda]]]^2-Sinh[Sqrt[\[Lambda]]]^2->1,Cos[Sqrt[\[Lambda]]]^2+Sin[Sqrt[\[Lambda]]]^2->1}//Simplify
coeff2 = coeff2*(-coeff1.cd5) * I \[Beta] Sqrt[\[Lambda]]/(1 + I \[Beta] \[Lambda])/.{Cosh[Sqrt[\[Lambda]]]^2-Sinh[Sqrt[\[Lambda]]]^2->1}//Simplify
coeff2.cd12//Simplify
coeff2.cd22//Simplify
coeff2.cd32//Simplify
coeff2.cd42//Simplify




