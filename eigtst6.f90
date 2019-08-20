!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!   eigtst6: 
!    test for the linear eigenvalue problem with complex variables
!   note:
!       In this test, we use the so-called push-pull method
!       We add an extra boundary condition to the previous problem
!       and change the existing boundry condition to include a 
!       controlling parameter
!                                                                               
!       In the continuation process
!       we first push, to change the controlling parameter to a nonzero number
!                      to make the eivenvalue problem inhomogeneous, so that
!                      we could get the added boundry condtions and make them
!                      inhomogeneous
!       then we pull, to change the controlling parameter back to zero, but
!                     remaining the added boundary conditions unchanged, so 
!                     that the problem is still inhomogeneous. In this way,
!                     an eivenvalue can generally be founded near the initial
!                     guess. Note that sometimes we cannot find any final
!                     eigenvalue with a given initial guess and sometimes the
!                     method itself encounters some problems.
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
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
    F(2) = -( COMPLEX(PAR(1),PAR(2)) * PI )**2 * U(1)

    END SUBROUTINE FUNC

    SUBROUTINE STPNT(NDIM,U,PAR,T)
!-------------------------------------------------------------------------------
    IMPLICIT NONE
    INTEGER NDIM
    ! REAL*8 U
    COMPLEX*16 U
    REAL*8 T, PAR(*)
    DIMENSION U(NDIM)

    PAR(1) = 0.5
    PAR(2) = 0.
    PAR(3) = 0.
    PAR(4) = 0.
    PAR(5) = 0.

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

    FB(1)=U0(1)- COMPLEX(PAR(5), 0.0d0)
    FB(2)=U1(1)
    FB(3)=U1(2) - COMPLEX(PAR(3), PAR(4))

    END SUBROUTINE BCND

    ! SUBROUTINE ICND(NDIM,PAR,ICP,NINT,U,UOLD,UDOT,UPOLD,FI,IJAC,DINT)
    SUBROUTINE ICND
!-------------------------------------------------------------------------------
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