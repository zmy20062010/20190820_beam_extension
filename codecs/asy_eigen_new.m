(* ::Package:: *)

(* ::Input:: *)
(*cd1 = {1,0,1,0};*)
(*cd2 = {0,1,0,1};*)
(*cd3 ={-Cos[\[Sqrt]\[Lambda]],-Sin[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]]};*)
(*cd4 ={Sin[\[Sqrt]\[Lambda]],-Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]};*)
(*cd={cd1,cd2,cd3,cd4};*)
(*Det[cd]//Simplify*)
(*bd0 = {1,0,0,0};*)
(*coeff0 =LinearSolve[cd,bd0]/.{Cosh[Sqrt[\[Lambda]]]^2-Sinh[Sqrt[\[Lambda]]]^2->1,Cos[Sqrt[\[Lambda]]]^2+Sin[Sqrt[\[Lambda]]]^2->1}//Simplify*)
(*coeff0.cd1//Simplify*)
(*coeff0.cd2//Simplify*)
(*coeff0.cd3//Simplify*)
(*coeff0.cd4//Simplify*)
(*sol0 = coeff0*)


bd1 = {0,0,-1,0};
coeff1 =LinearSolve[cd,bd1]/.{Cosh[Sqrt[\[Lambda]]]^2-Sinh[Sqrt[\[Lambda]]]^2->1,Cos[Sqrt[\[Lambda]]]^2+Sin[Sqrt[\[Lambda]]]^2->1}//Simplify
coeff1.cd1//Simplify
coeff1.cd2//Simplify
coeff1.cd3//Simplify
coeff1.cd4//Simplify
sol0.{-Sin[\[Sqrt]\[Lambda]],Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]}//Simplify
cmultiple1 = I \[Beta] Sqrt[\[Lambda]]/(1 + I \[Beta] \[Lambda])* (sol0.{-Sin[\[Sqrt]\[Lambda]],Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]})/.{Cosh[Sqrt[\[Lambda]]]^2-Sinh[Sqrt[\[Lambda]]]^2->1,Cos[Sqrt[\[Lambda]]]^2+Sin[Sqrt[\[Lambda]]]^2->1}//Simplify
sol1 = (coeff1 * cmultiple1)//Simplify





bd2 = {0,0,-1,0};
coeff2 =LinearSolve[cd,bd2]/.{Cosh[Sqrt[\[Lambda]]]^2-Sinh[Sqrt[\[Lambda]]]^2->1,Cos[Sqrt[\[Lambda]]]^2+Sin[Sqrt[\[Lambda]]]^2->1}//Simplify
coeff2.cd1//Simplify
coeff2.cd2//Simplify
coeff2.cd3//Simplify
coeff2.cd4//Simplify
sol1.{-Sin[\[Sqrt]\[Lambda]],Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]}//Simplify
cmultiple2 = I \[Beta] Sqrt[\[Lambda]]/(1 + I \[Beta] \[Lambda])* (sol1.{-Sin[\[Sqrt]\[Lambda]],Cos[\[Sqrt]\[Lambda]],Sinh[\[Sqrt]\[Lambda]],Cosh[\[Sqrt]\[Lambda]]})/.{Cosh[Sqrt[\[Lambda]]]^2-Sinh[Sqrt[\[Lambda]]]^2->1,Cos[Sqrt[\[Lambda]]]^2+Sin[Sqrt[\[Lambda]]]^2->1}//Simplify
sol2 = (coeff2 * cmultiple2)//Simplify



