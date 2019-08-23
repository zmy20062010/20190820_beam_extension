!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
!   Axisymmetric jet profile using viscous force as the reference
!   Dimensional parameters:
!     rho              = density
!     R0               = nozzle radius
!     L                = fall height
!     Q                = volume flow rate
!     U0 = Q/(Pi R0^2) = injection velocity
!     mu               = dynamic viscosity
!     nu = mu / rho    = kinematic viscosity
!     sigma            = surface tension
!     g                = gravitational acceleration
!   Independent varables:
!     ha, hap, hw, hn3
!     pa, pap, pw, px2, px3, pq0, pq1, pom2, pu1, pu3, pn1, pn3, pm2
!-------------------------------------------------------------------------------
!-------------------------------------------------------------------------------
    SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP) 
!-------------------- 
    IMPLICIT NONE
    INTEGER NDIM, ICP(*), IJAC
    REAL*8 PAR(*)
    COMPLEX*16 DFDP, DFDU, F, U
    DIMENSION U(NDIM), F(NDIM)
    ! steady variables
    COMPLEX*16 ha, hap, hw, hn3
    ! perturbation variables
    COMPLEX*16 pa, pap, pw, pn3
    !   continuation variables
    REAL*8 ep, Su, Re, Bu, Cg, Cr, Ch
    !   intermediate variables
    REAL*8 eps, Pi

    COMPLEX*16 sig
    REAL*8 sigr, sigi

!---Parameters
    ep   = PAR(1)
    Su   = PAR(2)
    Re   = PAR(3)
    Bu   = PAR(4)
    eps  = 1.0d0 / ep
    Cg   = PAR(5)
    Ch   = PAR(6)
    Cr   = PAR(7)
    Pi   = 4.0d0*DATAN(1.0d0)

    sigr = PAR(15)
    sigi = PAR(16)
    sig  = COMPLEX(sigr, sigi)

!---State variables
    ha    = U(1)
    hap   = U(2)
    hw    = U(3)
    hn3   = U(4)
!---Perturbation variables
    pa    = U(5)
    pap   = U(6)
    pw    = U(7)
    pn3   = U(8)

    ! Steady equations
    F(1) = hap
    F(2) = ((1 + eps**2*hap**2)*(eps*Sqrt(1 + eps**2*hap**2)*(hn3 &
           + 6*ha*hap*hw*Pi) + ha*Pi*Su))/(eps**2*ha**2*Pi*Su)
    F(3) = (-2*hap*hw)/ha
    F(4) = (2*hap*hn3)/ha - (Bu*Cg*ha**2*Pi)/eps**2 + 12*hap**2*hw*Pi &
           - (2*ha*hap*hw**2*Pi*Re)/eps
    ! Perturbation equations
    F(5)  = 0.0d0
    F(6)  = 0.0d0
    F(7)  = 0.0d0
    F(8)  = 0.0d0

    END SUBROUTINE FUNC

    SUBROUTINE STPNT(NDIM,U,PAR,T) 
!---------------------------------
    IMPLICIT NONE
    INTEGER NDIM
    COMPLEX*16 U
    REAL*8 T, PAR(*)
    DIMENSION U(NDIM)

    !   steady variables
    COMPLEX*16 ha, hap, hw, hn3
    !   perturbation variables
    COMPLEX*16 pa, pap, pw, pn3
    ! constants
    COMPLEX*16 one, zero

    !   physical parameters
    REAL*8 a0, H, g, rho, mu, gamma, U0
    !   continuation variables
    REAL*8 ep, Su, Re, Bu, Cg, Cr, Ch
    !   intermediate variables
    REAL*8 eps, Pi

    a0    = 0.3d-3
    H     = 0.15d-3
    U0    = 0.428d0
    g     = 9.81d0
    rho   = 1.0d3
    mu    = 1.0d-3
    gamma = 72.7d-3
    ep    = H / a0
    Su    = gamma / (mu * U0)
    Re    = rho * U0 * a0 / mu 
    BU    = rho * g * a0**2 / (mu * U0)
    eps   = 1.0d0 / ep
    Cg    = 0.0d0
    Cr    = 0.0d0
    Ch    = 0.0d0
    Pi    = 4.0d0*DATAN(1.0d0)
    one   = COMPLEX(1.0d0, 0.0d0)
    zero  = COMPLEX(0.0d0, 0.0d0)

    PAR(1) = ep
    PAR(2) = Su
    PAR(3) = Re
    PAR(4) = Bu
    PAR(5) = Cg
    PAR(6) = Ch
    PAR(7) = Cr

    PAR(12)= 0.0      ! PUSHPULL
    PAR(13)= 0.0      ! NEWBCr
    PAR(14)= 0.0      ! NEWBCi

    PAR(15)= 1.0      ! sigr
    PAR(16)= 1.0      ! sigi

    ha   = one
    hap  = zero
    hw   = one
    hn3  = - Pi * ha * Su / eps

    pa    = zero
    pap   = zero
    pw    = zero
    pn3   = zero

    ! Steady State
    U(1) = ha
    U(2) = hap
    U(3) = hw
    U(4) = hn3
    ! Perturbation
    U(5)  = pa
    U(6)  = pap
    U(7)  = pw
    U(8)  = pn3

    END SUBROUTINE STPNT

    SUBROUTINE BCND(NDIM,PAR,ICP,NBC,U0,U1,FB,IJAC,DBC) 
!---------------------------------------------------
    IMPLICIT NONE
    INTEGER NDIM, ICP(*), NBC, IJAC
    REAL*8 PAR(*)
    COMPLEX*16 U0, U1, FB, DBC
    DIMENSION U0(NDIM), U1(NDIM), FB(NBC)

    ! steady state variables
    COMPLEX*16 ha0, hap0, hw0, hn30
    COMPLEX*16 ha1, hap1, hw1, hn31
    ! perturbation variables
    COMPLEX*16 pa0, pap0, pw0, pn30
    COMPLEX*16 pa1, pap1, pw1, pn31

    COMPLEX*16 hhm1, phm1
    COMPLEX*16 one, zero
    !   continuation variables
    REAL*8 ep, Su, Re, Bu, Cg, Cr, Ch
    REAL*8 eps, Pi

    COMPLEX*16 NEWBC
    REAL*8 PUSHPULL, NEWBCr, NEWBCi

    !---Parameters
    ep   = PAR(1)
    Su   = PAR(2)
    Re   = PAR(3)
    Bu   = PAR(4)
    eps  = 1.0d0 / ep
    Cg   = PAR(5)
    Ch   = PAR(6)
    Cr   = PAR(7)

    PUSHPULL = PAR(12)
    NEWBCr   = PAR(13)
    NEWBCi   = PAR(14)
    NEWBC    = COMPLEX(NEWBCr, NEWBCi)
    Pi    = 4.0d0*DATAN(1.0d0)
    one   = 1.0d0
    zero  = 0.0d0
    
!  ha0, hap0, hn30, hw0
    ha0   = U0(1)
    hap0  = U0(2)
    hw0   = U0(3)
    hn30  = U0(4)

    pa0   = U0(5)
    pap0  = U0(6)
    pw0   = U0(7)
    pn30  = U0(8)
!  ha1, hap1, hn31, hw1
    ha1   = U1(1)
    hap1  = U1(2)
    hw1   = U1(3)
    hn31  = U1(4)

    pa1   = U1(5)
    pap1  = U1(6)
    pw1   = U1(7)
    pn31  = U1(8)

    hhm1  = (eps*(hn31 + 6*ha1*hap1*hw1*Pi))/(ha1**2*Pi*Su)
    phm1  = (eps*(-2*hn31*pa1 + ha1*(-6*hap1*hw1*pa1*Pi + 6*ha1*hw1*pap1*Pi &
            + pn31 + 6*ha1*hap1*Pi*pw1)))/(ha1**3*Pi*Su)

    FB(1) = ha0 - one 
    FB(2) = -hhm1 - one - Ch*(0.0d0 - 1.0d0) 
    FB(3) = ha1 - one - Cr*(5.0d0 - 1.0d0) 
    FB(4) = hw0 - one 

    FB(5)  = pa0
    FB(6)  = pap0
    FB(7)  = pw0
    FB(8)  = pn30
    
    END SUBROUTINE BCND

    SUBROUTINE ICND
    END SUBROUTINE ICND

    SUBROUTINE FOPT 
    END SUBROUTINE FOPT

    SUBROUTINE PVLS
    END SUBROUTINE PVLS

! !-------------------------------------------------------------------------------
! !-------------------------------------------------------------------------------
! !   Axisymmetric jet profile using viscous force as the reference
! !   Dimensional parameters:
! !     rho              = density
! !     R0               = nozzle radius
! !     L                = fall height
! !     Q                = volume flow rate
! !     U0 = Q/(Pi R0^2) = injection velocity
! !     mu               = dynamic viscosity
! !     nu = mu / rho    = kinematic viscosity
! !     sigma            = surface tension
! !     g                = gravitational acceleration
! !   Independent varables:
! !     ha, hap, hw, hn3
! !     pa, pap, pw, px2, px3, pth, pom2, pu1, pu3, pn1, pn3, pm2
! !     pq0 = -Sqrt(2) * Sin(hth) * pth
! !     pq1 = Sqrt(2) * Cos(hth) * pth
! !-------------------------------------------------------------------------------
! !-------------------------------------------------------------------------------
!     SUBROUTINE FUNC(NDIM,U,ICP,PAR,IJAC,F,DFDU,DFDP) 
! !-------------------- 
!     IMPLICIT NONE
!     INTEGER NDIM, ICP(*), IJAC
!     REAL*8 PAR(*)
!     COMPLEX*16 DFDP, DFDU, F, U
!     DIMENSION U(NDIM), F(NDIM)

!     ! Steady variables
!     COMPLEX*16 ha, hap, hn3, hw
!     ! perturbation variables
!     COMPLEX*16 pa, pap, pw, px2, px3
!     COMPLEX*16 pth, pq0, pq1
!     COMPLEX*16 pom2, pu1, pu3
!     COMPLEX*16 pn1, pn3, pm2
!     !   continuation variables
!     REAL*8 ep, Su, Re, Bu, Cg, Cr, Ch, ld
!     !   intermediate variables
!     REAL*8 eps, Pi
!     INTEGER it

!     COMPLEX*16 sig
!     REAL*8 sigr, sigi

! !---Parameters
!     ep   = PAR(1)
!     Su   = PAR(2)
!     Re   = PAR(3)
!     Bu   = PAR(4)
!     eps  = 1.0d0 / ep
!     Cg   = PAR(5)
!     Ch   = PAR(6)
!     Cr   = PAR(7)
!     ld   = PAR(8)  !  Length of the jet axis  ld = l/H
!     Pi   = 4.0d0*DATAN(1.0d0)
!     ! Pi   = 1.0d0

!     sigr = PAR(15)
!     sigi = PAR(16)
!     sig  = COMPLEX(sigr, sigi)

! !---Steady State variables
!     ha    = U(1)
!     hap   = U(2)
!     hw    = U(3)
!     hn3   = U(4)
! !---Perturbation variables
!     ! pa    = U(5)
!     ! pap   = U(6)
!     ! pw    = U(7)
!     ! px2   = U(8)
!     ! px3   = U(9)
!     ! pth   = U(10)
!     ! pom2  = U(11)
!     ! pu1   = U(12)
!     ! pu3   = U(13)
!     ! pn1   = U(14)
!     ! pn3   = U(15)
!     ! pm2   = U(16)
!     ! pq0   = -pth * Sqrt(0.5d0)
!     ! pq1   = pth * 0.0d0

!     ! Steady equations
!     F(1)  = hap
!     F(2)  = ((1 + eps**2*hap**2)*(eps*Sqrt(1 + eps**2*hap**2)*(hn3 &
!             + 6*ha*hap*hw*Pi) + ha*Pi*Su))/(eps**2*ha**2*Pi*Su)
!     F(3)  = -2  * hap * hw / ha
!     F(4)  = (2*hap*hn3)/ha - (Bu*Cg*ha**2*Pi)/eps**2 &
!             + 12*hap**2*hw*Pi - (2*ha*hap*hw**2*Pi*Re)/eps
!     ! Perturbation equations
!     ! F(5)  = 0.0d0
!     ! F(6)  = 0.0d0
!     ! F(7)  = 0.0d0
!     ! F(8)  = 0.0d0
!     ! F(9)  = 0.0d0
!     ! F(10) = 0.0d0
!     ! F(11) = 0.0d0
!     ! F(12) = 0.0d0
!     ! F(13) = 0.0d0
!     ! F(14) = 0.0d0
!     ! F(15) = 0.0d0
!     ! F(16) = 0.0d0
!     ! DO it = 5, 16
!     !      F(it) = ld * F(it)
!     ! ENDDO

!     END SUBROUTINE FUNC

!     SUBROUTINE STPNT(NDIM,U,PAR,T) 
! !---------------------------------
!     IMPLICIT NONE
!     INTEGER NDIM
!     COMPLEX*16 U
!     REAL*8 T, PAR(*)
!     DIMENSION U(NDIM)

!     ! Steady variables
!     COMPLEX*16 ha, hap, hn3, hw
!     ! perturbation variables
!     COMPLEX*16 pa, pap, pw, px2, px3
!     COMPLEX*16 pth, pq0, pq1
!     COMPLEX*16 pom2, pu1, pu3
!     COMPLEX*16 pn1, pn3, pm2

!     COMPLEX*16 one, zero

!     !   physical parameters
!     REAL*8 a0, H, g, rho, mu, gamma, U0
!     !   continuation variables
!     REAL*8 ep, Su, Re, Bu, Cg, Cr, Ch, ld
!     !   intermediate variables
!     REAL*8 eps, Pi

!     a0    = 0.3d-3
!     H     = 0.15d-3
!     U0    = 0.428d0
!     g     = 9.81d0
!     rho   = 1.0d3
!     mu    = 1.0d-3
!     gamma = 72.7d-3
!     ep    = H / a0
!     Su    = gamma / (mu * U0)
!     Re    = rho * U0 * a0 / mu 
!     BU    = rho * g * a0**2 / (mu * U0)
!     eps   = 1.0d0 / ep
!     Cg    = 0.0d0
!     Cr    = 0.0d0
!     Ch    = 0.0d0
!     ld    = 1.0d0
!     ! Pi    = 4.0d0*DATAN(1.0d0)
!     Pi    = 1.0d0
!     one   = COMPLEX(1.0d0, 0.0d0)
!     zero  = COMPLEX(0.0d0, 0.0d0)

!     PAR(1) = ep
!     PAR(2) = Su
!     PAR(3) = Re
!     PAR(4) = Bu
!     PAR(5) = Cg
!     PAR(6) = Ch
!     PAR(7) = Cr
!     PAR(8) = ld 

!     PAR(12)= 0.0      ! PUSHPULL
!     PAR(13)= 0.0      ! NEWBCr
!     PAR(14)= 0.0      ! NEWBCi

!     PAR(15)= 1.0      ! sigr
!     PAR(16)= 1.0       ! sigi

!     ha    = one
!     hap   = zero
!     hw    = one
!     hn3   = - Pi * ha * Su / eps

!     pa    = zero
!     pap   = zero
!     pw    = zero
!     px2   = zero
!     px3   = zero
!     pth   = zero
!     ! pq0   = zero
!     ! pq1   = zero
!     pom2  = zero
!     pu1   = zero
!     pu3   = zero
!     pn1   = zero
!     pn3   = zero
!     pm2   = zero

!     ! Steady State
!     U(1)  = ha
!     U(2)  = hap
!     U(3)  = hw
!     U(4)  = hn3
!     ! Perturbation
!     ! U(5)  = pa
!     ! U(6)  = pap
!     ! U(7)  = pw
!     ! U(8)  = px2
!     ! U(9)  = px3
!     ! U(10) = pth
!     ! ! U(10) = pq0
!     ! ! U(11) = pq1
!     ! U(11) = pom2
!     ! U(12) = pu1
!     ! U(13) = pu3
!     ! U(14) = pn1
!     ! U(15) = pn3
!     ! U(16) = pm2

!     END SUBROUTINE STPNT

!     SUBROUTINE BCND(NDIM,PAR,ICP,NBC,U0,U1,FB,IJAC,DBC) 
! !---------------------------------------------------
!     IMPLICIT NONE
!     INTEGER NDIM, ICP(*), NBC, IJAC
!     REAL*8 PAR(*)
!     COMPLEX*16 U0, U1, FB, DBC
!     DIMENSION U0(NDIM), U1(NDIM), FB(NBC)

!     !  Steady variables
!     COMPLEX*16 ha0, hap0, hn30, hw0
!     COMPLEX*16 ha1, hap1, hn31, hw1
!     ! perturbation variables
!     COMPLEX*16 pa0, pap0, pw0, px20, px30
!     COMPLEX*16 pth0, pq00, pq10
!     COMPLEX*16 pom20, pu10, pu30
!     COMPLEX*16 pn10, pn30, pm20
!     COMPLEX*16 pa1, pap1, pw1, px21, px31
!     COMPLEX*16 pth1, pq01, pq11
!     COMPLEX*16 pom21, pu11, pu31
!     COMPLEX*16 pn11, pn31, pm21

!     COMPLEX*16 hm1, pm1
!     COMPLEX*16 one, zero
!     !   continuation variables
!     REAL*8 ep, Su, Re, Bu, Cg, Cr, Ch, ld
!     REAL*8 eps, Pi

!     COMPLEX*16 NEWBC
!     REAL*8 PUSHPULL, NEWBCr, NEWBCi

!     !---Parameters
!     ep   = PAR(1)
!     Su   = PAR(2)
!     Re   = PAR(3)
!     Bu   = PAR(4)
!     eps  = 1.0d0 / ep
!     Cg   = PAR(5)
!     Ch   = PAR(6)
!     Cr   = PAR(7)
!     ld   = PAR(8)  !  Length of the jet axis  ld = l/H

!     PUSHPULL = PAR(12)
!     NEWBCr   = PAR(13)
!     NEWBCi   = PAR(14)
!     NEWBC    = COMPLEX(NEWBCr, NEWBCi)
!     ! Pi    = 4.0d0*DATAN(1.0d0)
!     Pi   = 1.0d0
!     one   = COMPLEX(1.0d0, 0.0d0)
!     zero  = COMPLEX(0.0d0, 0.0d0)
    
! !  ha0, hap0, hn30, hw0
!     ha0   = U0(1)
!     hap0  = U0(2)
!     hw0   = U0(3)
!     hn30  = U0(4)

!     ! pa0   = U0(5)
!     ! pap0  = U0(6)
!     ! pw0   = U0(7)
!     ! px20  = U0(8)
!     ! px30  = U0(9)
!     ! pth0  = U0(10)
!     ! ! pq00  = U0(10)
!     ! ! pq10  = U0(11)
!     ! pom20 = U0(11)
!     ! pu10  = U0(12)
!     ! pu30  = U0(13)
!     ! pn10  = U0(14)
!     ! pn30  = U0(15)
!     ! pm20  = U0(16)
! !  ha1, hap1, hn31, hw1
!     ha1   = U1(1)
!     hap1  = U1(2)
!     hw1   = U1(3)
!     hn31  = U1(4)

!     ! pa1   = U1(5)
!     ! pap1  = U1(6)
!     ! pw1   = U1(7)
!     ! px21  = U1(8)
!     ! px31  = U1(9)
!     ! pth1  = U1(10)
!     ! ! pq01  = U1(10)
!     ! ! pq11  = U1(11)
!     ! pom21 = U1(11)
!     ! pu11  = U1(12)
!     ! pu31  = U1(13)
!     ! pn11  = U1(14)
!     ! pn31  = U1(15)
!     ! pm21  = U1(16)

!     hm1  =  (eps*(hn31 + 6*ha1*hap1*hw1*Pi))/(ha1**2*Pi*Su)
!     pm1  =  ((1 + eps**2*hap1**2)**1.5*pa1*Pi*Su &
!             + eps*(Sqrt(1 + eps**2*hap1**2)*pn31 &
!             - eps*hap1*pap1*(3*eps*(hn31 + 6*ha1*hap1*hw1*Pi) &
!             + 3*eps**3*hap1**2*(hn31 + 6*ha1*hap1*hw1*Pi) &
!             + 2*ha1*Sqrt(1 + eps**2*hap1**2)*Pi*Su)))/((ha1 &
!             + eps**2*ha1*hap1**2)**2*Pi*Su)

!     FB(1)  = ha0 - one 
!     FB(2)  = -hm1 - one - Ch*(0.0d0 - 1.0d0) 
!     FB(3)  = ha1 - one - Cr*(5.0d0 - 1.0d0) 
!     FB(4)  = hw0 - one 

!     ! FB(5)  = px20
!     ! FB(6)  = px30
!     ! FB(7)  = pth0
!     ! FB(8)  = pa0
!     ! FB(9)  = pw0
!     ! FB(10) = pu10
!     ! FB(11) = pu30
!     ! FB(12) = px31
!     ! FB(13) = pth1
!     ! FB(14) = pa1
!     ! FB(15) = pu11
!     ! FB(16) = pm1

!     END SUBROUTINE BCND

!     SUBROUTINE ICND
!     END SUBROUTINE ICND

!     SUBROUTINE FOPT 
!     END SUBROUTINE FOPT

!     SUBROUTINE PVLS
!     END SUBROUTINE PVLS
