REM Exemplo calculadora

10 INPUT "Digite o primeiro valor:";a
20 INPUT "Digite o segundo valor:";b
30 INPUT "Digite a operação (+ - * /):";op

31 LET a = VAL(a)
32 LET b = VAL(b)

40 IF op = "+" THEN GOTO 50 ELSE IF op = "-" THEN GOTO 60 ELSE IF op = "*" THEN GOTO 70 ELSE IF op = "/" THEN GOTO 80 ELSE GOTO 90

50 PRINT "Soma: " + (a+b)
51 END

60 PRINT "Subtração: " + (a-b)
61 END

70 PRINT "Multiplicação: " + (a*b)
71 END

80 PRINT "Divisão: " + (a/b)
81 END

90 PRINT "Operação invelida: "
91 PRINT "Digite a operação novamente: " 
92 GOTO 30