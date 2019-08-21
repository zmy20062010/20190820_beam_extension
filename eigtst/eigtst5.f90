!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!   eigtst5: 
!    here in this example we investigate the eigenvalue problem from 
!    the paper:
!         (JGNACE  I.  KOLODNER 1955),  Heavy Rotating String - 
!                                      A  Nonlinear Eigenvdue  Problem
!    The model is formulated as follows:
!             u'' + lambda*sqrt(u*u + x*x) * u = 0
!                 u(0) = u'(1) = 0
!    where lambda = omega^2 l /g
!      ---- omega: rotating angular velocity
!           l    : length of the string
!           g    : gravitational velocity
!   note:
!       The simulation results show that
!            a string can rotate  at  any velocity  w  >  w1  ,  
!            and  that  for  each  w  in the range  w_n  <  w  < w_n+1
!            there are exactly  n  distinct  modes  of rotation.
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
    SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP)
!-------------------------------------------------------------------------------
    IMPLICIT NONE
    INTEGER NDIM, ICP(*), IJAC
    REAL*8 PAR(*)
    REAL*8 DFDP, DFDU, F, U
    ! COMPLEX*16 DFDP, DFDU, F, U
    DIMENSION U(NDIM), F(NDIM)

    F(1) = U(2)
    F(2) = - PAR(1) * SQRT( U(1)**2.0 + U(3)**2.0 ) * U(1)
    F(3) = 1.0d0
    ! F(3) = U(4)
    ! F(4) = -( PAR(1)*PI )**2 * U(3)


    END SUBROUTINE FUNC

    SUBROUTINE STPNT(NDIM,U,PAR,T)
!-------------------------------------------------------------------------------
    IMPLICIT NONE
    INTEGER NDIM
    REAL*8 U
    ! COMPLEX*16 U
    REAL*8 T, PAR(*)
    DIMENSION U(NDIM)

    PAR(1)=0.

    U(1)=0.0
    U(2)=0.0
    U(3)= T
    ! U(3)=0.0
    ! U(4)=0.0

    END SUBROUTINE STPNT

    SUBROUTINE BCND(NDIM,PAR,ICP,NBC,U0,U1,FB,IJAC,DBC)
!-------------------------------------------------------------------------------
    IMPLICIT NONE
    INTEGER NDIM, ICP(*), NBC, IJAC
    REAL*8 PAR(*)
    REAL*8 U0, U1, FB, DBC
    ! COMPLEX*16 U0, U1, FB, DBC
    DIMENSION U0(NDIM), U1(NDIM), FB(NBC)

    FB(1)=U0(1)
    FB(2)=U1(2)
    FB(3)=U0(3)
    ! FB(3)=U0(3)-PAR(2)
    ! FB(4)=U1(3)

    END SUBROUTINE BCND

    SUBROUTINE ICND(NDIM,PAR,ICP,NINT,U,UOLD,UDOT,UPOLD,FI,IJAC,DINT)
!     SUBROUTINE ICND
!      ---------- ----
    IMPLICIT NONE
    INTEGER, INTENT(IN) :: NDIM, ICP(*), NINT, IJAC
    DOUBLE PRECISION, INTENT(IN) :: PAR(*)
    DOUBLE PRECISION, INTENT(IN) :: U(NDIM), UOLD(NDIM), UDOT(NDIM), UPOLD(NDIM)
    DOUBLE PRECISION, INTENT(OUT) :: FI(NINT)
    DOUBLE PRECISION, INTENT(INOUT) :: DINT(NINT,*)

    FI(1)=U(1)*U(1)-PAR(3)

    END SUBROUTINE ICND

    SUBROUTINE FOPT
    END SUBROUTINE FOPT

    SUBROUTINE PVLS
    END SUBROUTINE PVLS