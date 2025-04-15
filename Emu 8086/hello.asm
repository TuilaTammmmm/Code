; hello.asm (Windows 64-bit)
extern _printf
extern _ExitProcess

section .data
    message db "Hello, World!", 0

section .text
    global _main
_main:
    ; Gọi printf để in chuỗi
    lea rcx, [message]  ; Tham số 1: con trỏ đến chuỗi
    call _printf

    ; Thoát chương trình
    xor rcx, rcx        ; Mã thoát = 0
    call _ExitProcess