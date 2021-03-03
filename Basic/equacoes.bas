10 INPUT "Digite o valor para a:"; a
20 INPUT "Digite o valor para b:"; b
30 INPUT "Digite o valor para c:"; c

31 LET a = VAL(a)
32 LET b = VAL(b)
33 LET c = VAL(c)

35 IF a = 0 THEN GOTO 130

40 LET delta = b*b - 4*a*c

41 IF delta < 0 THEN GOTO 130 ELSE IF delta = 0 THEN GOTO 100

50 LET respA = (-b+SQR(delta))/(2*a)
60 LET respB = (-b-SQR(delta))/(2*a)
70 PRINT "Resposta 1 = " + respA
80 PRINT "Resposta 2 = " + respB
90 END

100 LET deltaNeg = (-b)/(2*a)
110 PRINT " = " + deltaNeg
120 END

130 PRINT "Sem solução"
140 END