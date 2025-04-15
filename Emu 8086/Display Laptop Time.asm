.MODEL SMALL
.DATA
    msg  DB 'Bây giờ là: $'
.CODE
    START:  MOV  AX,@DATA
            MOV  DS,AX

            LEA  DX, msg     ; Load the address of the message into DX
            MOV  AH, 09H     ; DOS function to display a string
            INT  21H         ; Call DOS interrupt

    HOUR:   
            MOV  AH,2CH      ; To get System Time
            INT  21H
            MOV  AL,CH       ; Hour is in CH
            AAM
            MOV  BX,AX
            CALL DISP

            MOV  DL,':'
            MOV  AH,02H      ; To Print : in DOS
            INT  21H

    MINUTES:
            MOV  AH,2CH      ; To get System Time
            INT  21H
            MOV  AL,CL       ; Minutes is in CL
            AAM
            MOV  BX,AX
            CALL DISP

            MOV  DL,':'      ; To Print : in DOS
            MOV  AH,02H
            INT  21H

    Seconds:
            MOV  AH,2CH      ; To get System Time
            INT  21H
            MOV  AL,DH       ; Seconds is in DH
            AAM
            MOV  BX,AX
            CALL DISP

            MOV  AH,4CH      ; To Terminate the Program
            INT  21H

DISP PROC
            MOV  DL,BH       ; Since the values are in BX, BH Part
            ADD  DL,30H      ; ASCII Adjustment
            MOV  AH,02H      ; To Print in DOS
            INT  21H
            MOV  DL,BL       ; BL Part
            ADD  DL,30H      ; ASCII Adjustment
            MOV  AH,02H      ; To Print in DOS
            INT  21H
            RET
DISP ENDP                    ; End Disp Procedure

END START      ; End of MAIN