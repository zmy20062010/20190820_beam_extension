!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
! bm_onepiezo_free_real0 and bm_onepiezo_free_real1 : 
!        A linear ODE eigenvalue problem for a piezo cantilever unimorph beam
!            
! note1 :    In bm_onepiezo_free_real0, we treat the unimorph piezo beam
!            problem considering electrical connections.
!            
! note2 :    In bm_onepiezo_free_real1, we treat the usual elastic beam
!            problem. This is a classic comparison reference.
!            
! note2 :    For the piezo beam, we did not find any non-trivial solution. 
!            This tells us that the bifurcation method is not appropriate to
!            deal with the eigenproblem of this kind.
!            
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
      SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP)
!-------------------------------------------------------------------------------
      IMPLICIT NONE
      INTEGER NDIM, ICP(*), IJAC
      REAL*8 PAR(*)
      COMPLEX*16 DFDP, DFDU, F, U
      DIMENSION U(NDIM), F(NDIM)

      COMPLEX*16 u1, u1x, u1xx, u1xxx
      REAL*8     alpha, beta, nu

      alpha = PAR(1)
      beta  = PAR(2)
      nu    = PAR(3)

      u1    = U(1)
      u1x   = U(2)
      u1xx  = U(3)
      u1xxx = U(4)

      F(1) = u1x
      F(2) = u1xx
      F(3) = u1xxx
      F(4) = nu**(2.0d0) * u1

      END SUBROUTINE FUNC

      SUBROUTINE STPNT(NDIM,U,PAR,T)
!-------------------------------------------------------------------------------
      IMPLICIT NONE
      INTEGER NDIM
      COMPLEX*16 U
      REAL*8 T, PAR(*)
      DIMENSION U(NDIM)

      REAL*8 b, lp, Ys, Yp, rhos, rhop, hs, hp
      REAL*8 ep33S, e31, d31, Rl
      REAL*8 Cp, Bp, ep, mp
      REAL*8 fr, PI

      REAL*8 nY, hpa, hsa, hpc, ya, yb, yc

      REAL*8 alpha, beta, nu

      PI = 4.0d0 * ATAN(1.0d0)

!     beam base structure material constants
      lp   =  100.0d-3
      Ys   =  10.0d10
      rhos =  7.165d3
      hs   =  0.5d-3
      b    =  20.0d-3
!     piezo layer material constants
      Yp   = 66.0d9
      rhop = 7.80d3
      hp   = 0.4d-3
      ep33S= 15.93d-9
      d31  = -190d-12
      e31  = d31 * Yp
!     external circuit and excitation
      fr   = 1
      Rl   = 900.0d3

!     positions from the neutral axis as a reference
      nY  = Ys / Yp
      hpa = ( hp*hp + 2*nY*hp*hs + nY*hs*hs) / (hp+nY*hs) / 2.0d0
      hsa = ( hp*hp + 2*hp*hs + nY*hs*hs) / (hp+nY*hs) / 2.0d0
      hpc = nY*hs*(hp + hs) / (hp+nY*hs) / 2.0d0
      ya  = -hsa
      yb  = hpa - hp
      yc  = hpa

!     structural, electrical, and piezoelectric parameters
      Bp = b/3.0d0*( Ys*(yb*yb*yb - ya*ya*ya) + Yp*(yc*yc*yc - yb*yb*yb) )
      Cp = ep33S * b * lp / hp
      ep = b * Yp * d31 * (yc*yc - yb*yb) / 2.0d0 / hp
      mp = b * ( rhos * hs + rhop * hp )

      alpha = ep * SQRT(lp / Cp / Bp)
      beta  = Rl * Cp * SQRT(Bp / mp / lp**4.0d0)
      nu    = 2 * PI * fr * SQRT(mp * lp**4.0d0 / Bp)


      PAR(1) = alpha
      PAR(2) = beta
      PAR(3) = nu

      U(1)   = 0.0d0
      U(2)   = 0.0d0
      U(3)   = 0.0d0
      U(4)   = 0.0d0

      END SUBROUTINE STPNT

      SUBROUTINE BCND(NDIM,PAR,ICP,NBC,U0,U1,FB,IJAC,DBC)
!-------------------------------------------------------------------------------
      IMPLICIT NONE
      INTEGER NDIM, ICP(*), NBC, IJAC
      REAL*8  PAR(*)
      COMPLEX*16 U0, U1, FB, DBC
      DIMENSION U0(NDIM), U1(NDIM), FB(NBC)

      REAL*8 alpha, beta, nu

      COMPLEX*16 u10, u1x0, u1xx0, u1xxx0
      COMPLEX*16 u11, u1x1, u1xx1, u1xxx1

      COMPLEX*16 jnu


      alpha    = PAR(1)
      beta     = PAR(2)
      nu       = PAR(3)

      u10    = U0(1)
      u1x0   = U0(2)
      u1xx0  = U0(3)
      u1xxx0 = U0(4)

      u11    = U1(1)
      u1x1   = U1(2)
      u1xx1  = U1(3)
      u1xxx1 = U1(4)

      FB(1) = u10
      FB(2) = u1x0
      FB(3) = u1xx1 + jnu * beta / ( jnu * beta + 1 ) * alpha**(2.0d0) * u1x1
      FB(3) = u1xx1
      FB(4) = u1xxx1

      END SUBROUTINE BCND

      SUBROUTINE ICND
      ! SUBROUTINE ICND(NDIM,PAR,ICP,NINT,U,UOLD,UDOT,UPOLD,FI,IJAC,DINT)
!-------------------------------------------------------------------------------
      ! IMPLICIT NONE
      ! INTEGER NDIM, ICP(*), NINT, IJAC
      ! REAL*8  PAR(*)
      ! COMPLEX*16 U, UOLD, UDOT, UPOLD, FI, DINT
      ! DIMENSION U(NDIM), UOLD(NDIM), UDOT(NDIM), UPOLD(NDIM), FI(NINT)

      ! print *, "here3"
      ! FI(1) = REALPART(U(1) * CONJG(U(1))) - PAR(4)

      END SUBROUTINE ICND

      SUBROUTINE FOPT
      END SUBROUTINE FOPT

      SUBROUTINE PVLS
      END SUBROUTINE PVLS
