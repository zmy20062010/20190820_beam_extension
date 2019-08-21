!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
! bm_onepiezo_free : 
!        A linear ODE eigenvalue problem for a piezo cantilever uniphorm beam
!
! note1 :    For a piezoelectric composite cantilever beam, the original
!            real beam eigenproblem is converted into a complex one because
!            of the external connection of an electrical load.
!            
! note2 :    In this piece of code, we have to use the push-pull method to
!            get the eigenvalue and eigenfunction of the underlying 
!            boundary value problem.
!            
! note3 :    Results show that in the case of short-circuit condition, where
!            the externally connected resistance is zero, the resulting
!            eigenfunction(at least the first mode) is the same to that of a
!            pure elastic beam. With the increase of connected resistance,
!            the eigenfrequency will increase to an ultimate value 
!            corresponding to the open-circuit condition.
!            
! note4 :    It seems that we should be able to use a real version of this
!            code and use the bifurcation trick to identify all the eigen
!            modes at the same time. But validation should be considered.
!            
! note5 :    Using this code, we are able to investigate the dependence of 
!            eigenmode characteristics upon the system piezoelectric, 
!            mechanical, or electrical parameters. The generally used base
!            excitation case for an energy harvester is treated in a another
!            code.
!            
! note6 :    The parameter value and basic model used in this code comes from
!            the classic paper by (Erturk & Inman 2008)
!            "A distributed parameter electromechanical model for cantilevered 
!            piezoelectric energy harvesters".
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
      REAL*8     alpha, beta, nur, nui
      COMPLEX*16 nu

      alpha = PAR(1)
      beta  = PAR(2)
      nur   = PAR(3)
      nui   = PAR(4)
      nu    = COMPLEX(nur, nui)

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
      REAL*8 nur, nui, newBCr, newBCi, pushpull

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
      Rl   = 900.0

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

      nur      = 1.0d0
      nui      = 0.0d0

      newBCr   = 0.0d0
      newBCi   = 0.0d0
      pushpull = 0.0d0

      PAR(1) = alpha
      PAR(2) = beta
      ! PAR(3) = nu
      PAR(3) = nur
      PAR(4) = nui
      PAR(5) = newBCr
      PAR(6) = newBCi
      PAR(7) = pushpull

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

      REAL*8 alpha, beta
      REAL*8 nur, nui, newBCr, newBCi, pushpull

      COMPLEX*16 u10, u1x0, u1xx0, u1xxx0
      COMPLEX*16 u11, u1x1, u1xx1, u1xxx1

      COMPLEX*16 jnu, nu, newBC


      alpha    = PAR(1)
      beta     = PAR(2)
      ! nu    = PAR(3)
      nur      = PAR(3)
      nui      = PAR(4)
      nu       = COMPLEX(nur, nui)
      jnu      = COMPLEX(0.0d0, 1.0d0) * nu
      newBCr   = PAR(5)
      newBCi   = PAR(6)
      newBC    = COMPLEX(newBCr, newBCi)
      pushpull = PAR(7)

      u10    = U0(1)
      u1x0   = U0(2)
      u1xx0  = U0(3)
      u1xxx0 = U0(4)

      u11    = U1(1)
      u1x1   = U1(2)
      u1xx1  = U1(3)
      u1xxx1 = U1(4)

      FB(1) = u10 - pushpull
      FB(2) = u1x0
      FB(3) = u1xx1 + jnu * beta / ( jnu * beta + 1 ) * alpha**(2.0d0) * u1x1
      ! FB(3) = u1xx1
      FB(4) = u1xxx1
      FB(5) = u1xx1 - newBC

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
