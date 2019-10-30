(* ::Package:: *)

(* ::Input:: *)
(*cd1 ={1,0,1,1};*)
(*cd2 ={0,1,1,-1};*)
(*cd3 ={-Cos[\[Sqrt]\[Lambda]],-Sin[\[Sqrt]\[Lambda]],Exp[\[Sqrt]\[Lambda]],Exp[-\[Sqrt]\[Lambda]]};*)
(*cd4 ={Sin[\[Sqrt]\[Lambda]],-Cos[\[Sqrt]\[Lambda]],Exp[\[Sqrt]\[Lambda]],-Exp[-\[Sqrt]\[Lambda]]};*)
(*cd={cd1,cd2,cd3,cd4};*)
(*bd1 ={1,0,0,0};*)
(*sol1e=LinearSolve[cd,bd1]//Simplify*)
(*bd2 ={0,0,1,0};*)
(*sol2e=LinearSolve[cd,bd2]//Simplify*)
(**)
(*sol1u = {Cos[\[Sqrt]\[Lambda]],Sin[\[Sqrt]\[Lambda]],Exp[\[Sqrt]\[Lambda]],Exp[-\[Sqrt]\[Lambda]]}*)
(*sol1=Dot[sol1e,sol1u ]//Simplify*)
(**)
(*sol2=Dot[sol2e,sol1u ]//Simplify*)


sol1=DotProduct[sol1e,sol1u]




