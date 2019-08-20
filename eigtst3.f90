!---------------------------------------------------------------------
!---------------------------------------------------------------------
!   eigtst3: 
!    test for the linear eigenvalue problem with complex variables
!   note:
!       In AUTO package, for this example, if we change the involved
!       dependent variables to be complex, no bifurcation point can 
!       be detected using the same numerical continuation method
!       
!       It is generally supposed the eigenvalue for this problem
!       is real, but not calculated.
!---------------------------------------------------------------------
!---------------------------------------------------------------------
    SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP)
!-------------------------------------------------------------------------------
    IMPLICIT NONE
    INTEGER NDIM, ICP(*), IJAC
    REAL*8 PAR(*)
    ! REAL*8 DFDP, DFDU, F, U
    COMPLEX*16 DFDP, DFDU, F, U
    DIMENSION U(NDIM), F(NDIM)

    REAL*8 PI

    PI=4*ATAN(1.0D0)
    F(1) = U(2)
    F(2) = -( PAR(1)*PI )**2 * U(1)

    END SUBROUTINE FUNC

    SUBROUTINE STPNT(NDIM,U,PAR,T)
!-------------------------------------------------------------------------------
    IMPLICIT NONE
    INTEGER NDIM
    ! REAL*8 U
    COMPLEX*16 U
    REAL*8 T, PAR(*)
    DIMENSION U(NDIM)

    PAR(1)=0.
    PAR(2)=0.

    U(1)=0.0
    U(2)=0.0

    END SUBROUTINE STPNT

    SUBROUTINE BCND(NDIM,PAR,ICP,NBC,U0,U1,FB,IJAC,DBC)
!-------------------------------------------------------------------------------
    IMPLICIT NONE
    INTEGER NDIM, ICP(*), NBC, IJAC
    REAL*8 PAR(*)
    ! REAL*8 U0, U1, FB, DBC
    COMPLEX*16 U0, U1, FB, DBC
    DIMENSION U0(NDIM), U1(NDIM), FB(NBC)

    FB(1)=U0(1)-PAR(2)
    FB(2)=U1(1)

    END SUBROUTINE BCND

    ! SUBROUTINE ICND(NDIM,PAR,ICP,NINT,U,UOLD,UDOT,UPOLD,FI,IJAC,DINT)
    SUBROUTINE ICND
!       ---------- ----
!     IMPLICIT NONE
!     INTEGER, INTENT(IN) :: NDIM, ICP(*), NINT, IJAC
!     DOUBLE PRECISION, INTENT(IN) :: PAR(*)
!     DOUBLE PRECISION, INTENT(IN) :: U(NDIM), UOLD(NDIM), UDOT(NDIM), UPOLD(NDIM)
!     DOUBLE PRECISION, INTENT(OUT) :: FI(NINT)
!     DOUBLE PRECISION, INTENT(INOUT) :: DINT(NINT,*)

!     FI(1)=U(1)*U(1)-PAR(3)

    END SUBROUTINE ICND

    SUBROUTINE FOPT
    END SUBROUTINE FOPT

    SUBROUTINE PVLS
    END SUBROUTINE PVLS