!---------------------------------------------------------------------
!---------------------------------------------------------------------
!  extension :  Analysis of the piezo beam with flexible extension
!---------------------------------------------------------------------
!---------------------------------------------------------------------

      SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP)
!-------------------- 
      IMPLICIT NONE
      INTEGER NDIM, ICP(*), IJAC
      REAL*8 PAR(*)
      COMPLEX*16 DFDP, DFDU, F, U
      DIMENSION U(NDIM), F(NDIM)

      COMPLEX*16 u1, u1x, u1xx, u1xxx
      COMPLEX*16 u2, u2x, u2xx, u2xxx
      REAL*8     alpha, beta, nu, lamB, lamm, laml

      alpha = PAR(1)
      beta  = PAR(2)
      nu    = PAR(3)
      lamB  = PAR(4)
      lamm  = PAR(5)
      laml  = PAR(6)

      u1    = U(1)
      u1x   = U(2)
      u1xx  = U(3)
      u1xxx = U(4)
      u2    = U(5)
      u2x   = U(6)
      u2xx  = U(7)
      u2xxx = U(8)


      F(1) = u1x
      F(2) = u1xx
      F(3) = u1xxx
      F(4) = nu**(2.0d0) * u1
      F(5) = u2x
      F(6) = u2xx
      F(7) = u2xxx
      F(8) = nu**(2.0d0) * lamm * laml**(4.0d0) / lamB * u2

      END SUBROUTINE FUNC

      SUBROUTINE STPNT(NDIM,U,PAR,T)
!---------------------------------
      IMPLICIT NONE
      INTEGER NDIM
      COMPLEX*16 U
      REAL*8 T, PAR(*)
      DIMENSION U(NDIM)

      REAL*8 b, lp, le, Ys, Ye, c11E, rhos, rhoe, rhop, hs, he, hp
      REAL*8 ep33S, e31, Rl
      REAL*8 Cp, Bp, ep, Be, mp, me
      REAL*8 fr, PI

      REAL*8 alpha, beta, nu
      REAL*8 lamB, lamm, laml, lamh

      PI = ATAN(1.0d0) * 4.0d0

      ! beam base structure material constants
      lp   =  50.0d-3
      Ys   =  10.8d10
      rhos =  8.8d3
      hs   =  0.25d-3
      b    =  20.0d-3
      ! piezo layer material constants
      c11E = 12.03d10
      rhop = 7.75d3
      hp   = 0.5d-3
      ep33S= 7.32d-9
      e31  = -5.35
      ! beam extension material constants
      le   = 20d-3
      Ye   = 2.3d9
      rhoe = 1.38d3
      he   = 0.25d-3
      ! external circuit and excitation
      fr   = 120
      Rl   = 900.0d3

      Bp = 2.0d0/3.0d0 * b * ( Ys * hs**3.0d0 &
           + c11E * ( (hs + hp)**3.0d0 - hs**3.0d0) )
      Be = 2.0d0/3.0d0 * b * Ye * he**3.0d0
      Cp = ep33S * b * lp / 2.0d0 / hp
      ep = b * e31 * (hs + hp/2.0d0)
      mp = 2.0d0 * b * ( rhos * hs + rhop * hp )
      me = 2.0d0 * b * rhoe * he

      alpha = ep * SQRT(lp / Cp / Bp)
      beta  = Rl * Cp * SQRT(Bp / mp / lp**4.0d0)
      nu    = 2 * PI * fr * SQRT(mp * lp**4.0d0 / Bp)
      ! nu = 1.1317071070250151 for fr = 120
      lamB  = Be / Bp
      lamm  = me / mp
      laml  = le / lp
      lamh  = 0.0d0

      PAR(1) = alpha
      PAR(2) = beta
      PAR(3) = nu
      PAR(4) = lamB
      PAR(5) = lamm
      PAR(6) = laml
      PAR(7) = lamh

      U(1)   = 0.0d0
      U(2)   = 0.0d0
      U(3)   = 0.0d0
      U(4)   = 0.0d0
      U(5)   = 0.0d0
      U(6)   = 0.0d0
      U(7)   = 0.0d0
      U(8)   = 0.0d0

      END SUBROUTINE STPNT

      SUBROUTINE BCND(NDIM,PAR,ICP,NBC,U0,U1,FB,IJAC,DBC)
!---------------------------------------------------
      IMPLICIT NONE
      INTEGER NDIM, ICP(*), NBC, IJAC
      REAL*8 PAR(*)
      COMPLEX*16 U0, U1, FB, DBC
      DIMENSION U0(NDIM), U1(NDIM), FB(NBC)

      REAL*8 alpha, beta, nu
      REAL*8 lamB, lamm, laml, lamh

      COMPLEX*16 u10, u1x0, u1xx0, u1xxx0
      COMPLEX*16 u11, u1x1, u1xx1, u1xxx1
      COMPLEX*16 u20, u2x0, u2xx0, u2xxx0
      COMPLEX*16 u21, u2x1, u2xx1, u2xxx1

      COMPLEX*16 iu
      iu = COMPLEX(0.0d0, 1.0d0)

      alpha = PAR(1)
      beta  = PAR(2)
      nu    = PAR(3)
      lamB  = PAR(4)
      lamm  = PAR(5)
      laml  = PAR(6)
      ! Parameter used to control the inhomogeneous boundary condition
      lamh  = PAR(7) 

      u10    = U0(1)
      u1x0   = U0(2)
      u1xx0  = U0(3)
      u1xxx0 = U0(4)
      u20    = U0(5)
      u2x0   = U0(6)
      u2xx0  = U0(7)
      u2xxx0 = U0(8)

      u11    = U1(1)
      u1x1   = U1(2)
      u1xx1  = U1(3)
      u1xxx1 = U1(4)
      u21    = U1(5)
      u2x1   = U1(6)
      u2xx1  = U1(7)
      u2xxx1 = U1(8)

      FB(1) = u10 - 1.0d0 * lamh
      FB(2) = u1x0
      FB(3) = u11 - u20
      FB(4) = laml * u1x1 - u2x0
      FB(5) = u1xx1 + iu * nu * beta  / ( iu * nu * beta + 1 ) &
              * alpha**(2.0d0) * u1x1 &
              - lamB / (laml**(2.0d0)) * u2xx0
      FB(6) = u1xxx1 - lamB / (laml**(3.0d0)) * u2xxx0
      FB(7) = u2xx1
      FB(8) = u2xxx1

      END SUBROUTINE BCND

      SUBROUTINE ICND(NDIM,PAR,ICP,NINT,U,UOLD,UDOT,UPOLD,FI,IJAC,DINT)
!     ---------- ----
      ! IMPLICIT NONE
      ! INTEGER, INTENT(IN) :: NDIM, ICP(*), NINT, IJAC
      ! DOUBLE PRECISION, INTENT(IN) :: PAR(*)
      ! DOUBLE PRECISION, INTENT(IN) :: U(NDIM), UOLD(NDIM), UDOT(NDIM), UPOLD(NDIM)
      ! DOUBLE PRECISION, INTENT(OUT) :: FI(NINT)
      ! DOUBLE PRECISION, INTENT(INOUT) :: DINT(NINT,*)

      ! FI(1)=U(1)*U(1)-PAR(3)

      END SUBROUTINE ICND

      SUBROUTINE FOPT
      END SUBROUTINE FOPT

      SUBROUTINE PVLS
      END SUBROUTINE PVLS
