ORG 0000H

; Định nghĩa địa chỉ cổng
SENSOR  EQU 3FDh  ; Cổng cảm biến nhiệt
HEATER  EQU 3FEh  ; Cổng đèn sưởi
FAN     EQU 3FFh  ; Cổng quạt

; Giá trị ngưỡng nhiệt độ
TEMP_LOW  EQU 22  ; Ngưỡng dưới 22°C
TEMP_HIGH EQU 25  ; Ngưỡng trên 25°C

; Giá trị điều khiển
ON  EQU 0FFh      ; Bật: tất cả bit là 1
OFF EQU 00h       ; Tắt: tất cả bit là 0

START:
    ; Đọc nhiệt độ từ cảm biến
    IN A, (SENSOR)    ; Đọc giá trị nhiệt độ vào thanh ghi A

    ; So sánh nhiệt độ với ngưỡng dưới (22°C)
    CPI TEMP_LOW      ; So sánh A với 22
    JC TURN_ON_HEATER ; Nếu A < 22, bật đèn sưởi

    ; So sánh nhiệt độ với ngưỡng trên (25°C)
    CPI TEMP_HIGH     ; So sánh A với 25
    JNC TURN_ON_FAN   ; Nếu A > 25, bật quạt

    ; Nếu 22°C <= nhiệt độ <= 25°C, tắt cả đèn và quạt
    MVI A, OFF
    OUT (HEATER), A   ; Tắt đèn sưởi
    OUT (FAN), A      ; Tắt quạt
    JMP DELAY         ; Chuyển đến phần trễ

TURN_ON_HEATER:
    MVI A, ON
    OUT (HEATER), A   ; Bật đèn sưởi
    MVI A, OFF
    OUT (FAN), A      ; Tắt quạt
    JMP DELAY

TURN_ON_FAN:
    MVI A, ON
    OUT (FAN), A      ; Bật quạt
    MVI A, OFF
    OUT (HEATER), A   ; Tắt đèn sưởi
    JMP DELAY

DELAY:
    ; Tạo trễ 1 phút (600 lệnh NOP)
    MVI B, 0FFh       ; Vòng lặp ngoài
DELAY_LOOP1:
    MVI C, 0FFh       ; Vòng lặp trong
DELAY_LOOP2:
    NOP               ; Lệnh NOP
    DCR C             ; Giảm C
    JNZ DELAY_LOOP2   ; Lặp nếu C != 0
    DCR B             ; Giảm B
    JNZ DELAY_LOOP1   ; Lặp nếu B != 0

    ; Sau khi trễ, quay lại kiểm tra nhiệt độ
    JMP START

END