C----------------------------------------------------------------------
C   Complex eigenvalue in a boundary value problem
c   y'' = (lambda-i) y, y(0) = y(1) = 0  [i = sqrt(-1)]
c   (p1,p2) = complex eigenvalue lambda
c   (p3,0) = continuation parameter to take y(1) away from zero and back
c   (p4,p5) = y'(0) used to keep y nontrivial when y(1)->0
c   Solution procedure:
c     (1) specify initial value of lambda (= guess for the eigenvalue) in subroutine stpnt
c     (2) run test.f with constants file c.test.away. During this step, 
c            p3 increases from 0 to 1, resulting in an "incorrect" boundary condition on y(1)
c            p1, p2 remain fixed at their initial values
c            p4, p5 vary freely
c     (3) run test.f with constants file c.test.back. During this step,
c            p3 decreases from 1 to 0, recovering the correct boundary condition y(1) = 0
c            p4, p5 remain fixed at their values from step (2)
c            p1, p2 vary freely and converge to the nearest eigenvalue
c         NB: remember to change IRS in c.test.back to the appropriate solution label
C----------------------------------------------------------------------
C----------------------------------------------------------------------
C
      SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP)
C     ---------- ----
      IMPLICIT COMPLEX*16 (A-H,O-Z)
      REAL*8 PAR(*)
      DIMENSION U(NDIM),F(NDIM)

       F(1) = U(2)
       F(2) = U(1)*(PAR(1) + PAR(2)*(0d0,1d0) - (0d0,1d0))
C
      RETURN
      END
C
      SUBROUTINE STPNT(NDIM,U,PAR,T)
C     ---------- -----
C
      IMPLICIT COMPLEX*16 (A-H,O-Z)
      REAL*8 PAR(*)
      DIMENSION U(NDIM)
C
       U(1)=0
       U(2)=0
C  starting guess for eigenvalue
       PAR(1) = -43.0d0
       PAR(2) = 1.2d0
C
      RETURN
      END
C
      SUBROUTINE BCND(NDIM,PAR,ICP,NBC,U0,U1,F,IJAC,DBC)
C     ---------- ----
      IMPLICIT COMPLEX*16 (A-H,O-Z)
      REAL*8 PAR(*)
      DIMENSION ICP(*),U0(NDIM),U1(NDIM),F(NBC)
C
       F(1)=U0(1)
C        F(2)=U1(1)-PAR(3)*(1d0,0d0)
       F(2)=U1(1)
c "Extra" boundary condition on y'(0), to keep the solution nontrivial as PAR(3) -> 0 in step (2)   
C        F(3)=U0(2)-PAR(4)*(1d0,0d0)-PAR(5)*(0d0,1d0)
C
      RETURN
      END
C     
      SUBROUTINE ICND(NDIM,PAR,ICP,NINT,U,UOLD,UDOT,UPOLD,FI,IJAC,DINT)
C     ---------- ----
      IMPLICIT COMPLEX*16 (A-H,O-Z)
      REAL*8 PAR(*)
      DIMENSION U(NDIM), UOLD(NDIM), UDOT(NDIM), UPOLD(NDIM), FI(NINT)

      FI(1)=U(1)*CONJG(U(1)) - (PAR(3), 0d0)


      RETURN
      END
C
      SUBROUTINE FOPT
      RETURN
      END
C 
      SUBROUTINE PVLS
      RETURN 
      END 
