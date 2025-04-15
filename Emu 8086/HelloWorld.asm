.model small
.stack 100h

.data
    msg db 'Hello, world!$'

.code
main:
    mov ax, @data
    mov ds, ax

    mov ah, 09h     ; Hàm 09h của interrupt 21h để in chuỗi kết thúc bằng '$'
    lea dx, msg     ; Đưa địa chỉ chuỗi vào thanh ghi DX
    int 21h         ; Gọi interrupt để in chuỗi

    mov ah, 4Ch     ; Hàm thoát chương trình
    int 21h

end main
