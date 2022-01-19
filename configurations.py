from productions.P1 import P1
from productions.P2 import P2
from productions.P7 import P7
from productions.P10 import P10
from productions.P11 import P11
from productions.P12 import P12


def p12_big_up():
    P1(0)
    P2(5)
    P10(10)
    P2(25)
    P2(20)
    P2(15)
    P11(29, 90, 100)
    P7(75, 50, 85, 60)
    P7(100, 105, 50, 55)
    P12(29, 70, 75)


def p12_big_down():
    P1(0)
    P2(5)
    P10(20)
    P2(25)
    P2(10)
    P2(15)
    P11(29, 50, 60)
    P7(75, 90, 85, 100)
    P7(100, 105, 50, 55)
    P12(80, 85, 29)


def p12_big_left():
    P1(0)
    P2(5)
    P10(20)
    P2(25)
    P2(10)
    P2(15)
    P7(100, 105, 50, 55)
    P7(75, 90, 85, 100)
    P11(80, 85, 29)
    P12(29, 50, 60)


def p12_big_right():
    P1(0)
    P2(5)
    P10(25)
    P2(15)
    P2(10)
    P2(20)
    P11(60, 65, 29)
    P7(80, 85, 90, 95)
    P7(75, 50, 85, 60)
    P12(95, 29, 105)
