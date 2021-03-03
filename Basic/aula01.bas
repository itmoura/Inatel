REM Primeiro Programa

10 PRINT "Hello World!"
20 LET x = 42
21 LET y = 10
30 PRINT "Valor: " + x
REM 40 INPUT "Digite um valor: "; y
REM 50 PRINT "Valor Digitado: " + y
60 GOTO 80
70 PRINT "Uma frase!"
80 PRINT "Está chovendo"
90 IF y > 0 THEN GOTO 100 ELSE IF y = 0 THEN GOTO 150 ELSE GOTO 200

100 PRINT "1. O valor do Y é"
110 PRINT "1. Positivo"
111 GOTO 300

150 PRINT "2. O valor do Y é"
160 PRINT "2. nulo"
161 GOTO 300

200 PRINT "3. O valor do Y é"
210 PRINT "3. Negativo"
211 GOTO 300

300 PRINT "Execução normal..."


REM Estrutura de repetição
REM FOR i = 0 TO 10 STEP 1
REM PRINT i
REM NEXT i

400 INPUT "Digite um valor: "; x
410 IF x >= 0 THEN GOTO 430 ELSE GOTO 450
420 PRINT "Valor digitado: " + x
430 GOTO 400

450 PRINT "Linha fora do loop" 