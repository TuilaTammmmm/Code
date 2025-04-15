; 8086 Assembly Program to Identify Computer Type
; Reads byte at ROM BIOS address F000:FFFE and determines computer model

.MODEL SMALL
.STACK 100h
.DATA
    ; Messages for each computer type
    msg_ps2_70_80  DB 'Computer Type: PS/2 models 70 and 80$', 0
    msg_ps2_30     DB 'Computer Type: PS/2 model 30$', 0
    msg_pcxt       DB 'Computer Type: PC/XT (later model, 101 keyboard)$', 0
    msg_pcat       DB 'Computer Type: PC/AT$', 0
    msg_pcjr       DB 'Computer Type: PCJR$', 0
    msg_pcat_early DB 'Computer Type: PC/AT (early model)$', 0
    msg_pc         DB 'Computer Type: PC classic$', 0
    msg_unknown    DB 'Computer Type: Unknown$', 0

.CODE
MAIN PROC
    ; Initialize data segment
    MOV AX, @DATA
    MOV DS, AX

    ; Set ES to F000h (ROM BIOS segment)
    MOV AX, 0F000h
    MOV ES, AX

    ; Read byte at F000:FFFE into AL
    MOV BX, 0FFFEh
    MOV AL, ES:[BX]

    ; Compare AL with known values and jump to corresponding label
    CMP AL, 0F8h
    JE  IS_PS2_70_80
    CMP AL, 0FAh
    JE  IS_PS2_30
    CMP AL, 0FBh
    JE  IS_PCXT
    CMP AL, 0FCh
    JE  IS_PCAT
    CMP AL, 0FDh
    JE  IS_PCJR
    CMP AL, 0FEh
    JE  IS_PCAT_EARLY
    CMP AL, 0FFh
    JE  IS_PC
    JMP IS_UNKNOWN

IS_PS2_70_80:
    LEA DX, msg_ps2_70_80
    JMP SHOW_MSG

IS_PS2_30:
    LEA DX, msg_ps2_30
    JMP SHOW_MSG

IS_PCXT:
    LEA DX, msg_pcxt
    JMP SHOW_MSG

IS_PCAT:
    LEA DX, msg_pcat
    JMP SHOW_MSG

IS_PCJR:
    LEA DX, msg_pcjr
    JMP SHOW_MSG

IS_PCAT_EARLY:
    LEA DX, msg_pcat_early
    JMP SHOW_MSG

IS_PC:
    LEA DX, msg_pc
    JMP SHOW_MSG

IS_UNKNOWN:
    LEA DX, msg_unknown

SHOW_MSG:
    MOV AH, 09h
    INT 21h

    ; Print newline
    MOV DL, 0Dh
    MOV AH, 02h
    INT 21h
    MOV DL, 0Ah
    INT 21h

    ; Terminate program
    MOV AH, 4Ch
    INT 21h

MAIN ENDP
END MAIN