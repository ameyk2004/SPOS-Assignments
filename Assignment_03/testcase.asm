MACRO
M1 &X &Y &B= &A=AREG
MOVER &A &X
ADD &A ='1'
MOVER &B &Y
ADD &A ='5'
MEND
MACRO
M1 &P &Q &R &U=CREG &V=DREG
MOVER &U &P
MOVER &V &Q
ADD &U ='15'
ADD &V ='10'
MEND
M1 10 20 &B=CREG
M1 100 200 300 &V=AREG &U=BREG