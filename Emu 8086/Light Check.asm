MOV DX, 02C0h
START:
  MOV AL, 00h       ; Tất cả đèn sáng
  OUT DX, AL
  CALL DELAY_1000
  MOV AL, 0FFh      ; Tất cả đèn tắt
  OUT DX, AL
  CALL DELAY_1000
  JMP START

DELAY_1000:
  MOV CX, 1000
DELAY_LOOP:
  NOP
  LOOP DELAY_LOOP
  RET
