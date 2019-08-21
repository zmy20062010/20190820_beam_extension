!---------------------------------------------------------------------
!---------------------------------------------------------------------
!   eigtst4: 
!    test for the linear eigenvalue problem with complex variables
!   note:
!       In this test, we decompose the problem shown in eigtst3
!       to form a completely real eigenvalue problem.
!       Every variable is decomposed into its real and imaginary part.
!                                                                         
!       As a result, we reach a general linear real eigenvalue problem
!                                                                         
!       However, we found that the new problem still fails to reach 
!       any feasible bifurcation point.
!---------------------------------------------------------------------
!---------------------------------------------------------------------
    SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP)
!-------------------------------------------------------------------------------
    IMPLICIT NONE
    INTEGER NDIM, ICP(*), IJAC
    REAL*8 PAR(*)
    REAL*8 DFDP, DFDU, F, U
    ! COMPLEX*16 DFDP, DFDU, F, U
    DIMENSION U(NDIM), F(NDIM)

    REAL*8 PI

    PI=4*ATAN(1.0D0)
    F(1) = U(2)
    F(2) = -( PAR(1)*PI )**2 * U(1)
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
    PAR(2)=0.

    U(1)=0.0
    U(2)=0.0
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

    FB(1)=U0(1)-PAR(2)
    FB(2)=U1(1)
    ! FB(3)=U0(3)-PAR(2)
    ! FB(4)=U1(3)

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