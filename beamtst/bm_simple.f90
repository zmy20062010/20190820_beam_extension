!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
! bm_simple : A linear ODE eigenvalue problem for a cantilever beam
!      note : In this piece of code, we reproduce the various eigenvalues 
!             and the corresponding eigenmode for a cantilever beam.
!
!             The eigenvalues for the problem are all real
!             It is fairly simple to use the bifurcation method to locate
!             eigenvalues and corresponding eigenmodes
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
      SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP)
!-------------------------------------------------------------------------------
      IMPLICIT NONE
      INTEGER, INTENT(IN) :: NDIM, ICP(*), IJAC
      DOUBLE PRECISION, INTENT(IN) :: U(NDIM), PAR(*)
      DOUBLE PRECISION, INTENT(OUT) :: F(NDIM)
      DOUBLE PRECISION, INTENT(INOUT) :: DFDU(NDIM,NDIM), DFDP(NDIM,*)

        F(1) = U(2)
        F(2) = U(3)
        F(3) = U(4)
        F(4) = ( PAR(1) )**2 * U(1)

      END SUBROUTINE FUNC

      SUBROUTINE STPNT(NDIM,U,PAR,T)
!-------------------------------------------------------------------------------
      IMPLICIT NONE
      INTEGER, INTENT(IN) :: NDIM
      DOUBLE PRECISION, INTENT(INOUT) :: U(NDIM),PAR(*)
      DOUBLE PRECISION, INTENT(IN) :: T

        PAR(1) = 0.0
        PAR(2) = 0.0
        PAR(3) = 0.0

        U(1) = 0.0
        U(2) = 0.0
        U(3) = 0.0
        U(4) = 0.0

      END SUBROUTINE STPNT

      SUBROUTINE BCND(NDIM,PAR,ICP,NBC,U0,U1,FB,IJAC,DBC)
!-------------------------------------------------------------------------------
      IMPLICIT NONE
      INTEGER, INTENT(IN) :: NDIM, ICP(*), NBC, IJAC
      DOUBLE PRECISION, INTENT(IN) :: PAR(*), U0(NDIM), U1(NDIM)
      DOUBLE PRECISION, INTENT(OUT) :: FB(NBC)
      DOUBLE PRECISION, INTENT(INOUT) :: DBC(NBC,*)

        FB(1) = U0(1) - PAR(2)
        FB(2) = U0(2)
        FB(3) = U1(3)
        FB(4) = U1(4)

      END SUBROUTINE BCND

      SUBROUTINE ICND(NDIM,PAR,ICP,NINT,U,UOLD,UDOT,UPOLD,FI,IJAC,DINT)
!-------------------------------------------------------------------------------
      IMPLICIT NONE
      INTEGER, INTENT(IN) :: NDIM, ICP(*), NINT, IJAC
      DOUBLE PRECISION, INTENT(IN) :: PAR(*)
      DOUBLE PRECISION, INTENT(IN) :: U(NDIM), UOLD(NDIM), UDOT(NDIM), UPOLD(NDIM)
      DOUBLE PRECISION, INTENT(OUT) :: FI(NINT)
      DOUBLE PRECISION, INTENT(INOUT) :: DINT(NINT,*)

        FI(1) = U(1)*U(1) - PAR(3)

      END SUBROUTINE ICND

      SUBROUTINE FOPT
      END SUBROUTINE FOPT

      SUBROUTINE PVLS
      END SUBROUTINE PVLS
