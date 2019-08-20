      PROGRAM Complex_Kind
        IMPLICIT NONE
        DOUBLE PRECISION xr, xi
        COMPLEX*16 x
        COMPLEX(KIND(1.0D0)) y
        INTEGER    xkind

        xr = 2.0D0
        xi = 3.0D0
        xkind = KIND(1.0D0)
        x = COMPLEX(xr, xi)
        y = COMPLEX(xr, xi) + COMPLEX(1.0d0, 2.0d0)

        print *, xkind
        print *, x
        print *, y
        print *, xr
        print *, xi


      END PROGRAM Complex_Kind
