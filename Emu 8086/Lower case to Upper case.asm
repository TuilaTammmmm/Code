; Assembly program: Convert input letter case using XOR trick
; Note: '@' = label, '$' = procedure (custom style)

.model small           
.stack 100h            

.data                  

n_line           db    0ah,0dh,"$"                        
input_msg        db    "Input",20h,": $"                  
output_msg       db    0ah,0dh,"Output: $"
stop_msg         db    "Press 'esc' to Stop this Programme.",0ah,0dh,"$"   
end_msg          db    0ah,0dh,"Proramme Terminated. $"

.code                  

main proc
    mov ax,@data       
    mov ds,ax          

    lea dx,stop_msg
    mov ah,9
    int 21h 

@input: 
    mov cx,0
       
    lea dx,input_msg
    mov ah,9
    int 21h 

    mov ah,1           
    int 21h        
    
    cmp al,27d         
    je @terminate   
    
    call $check_constraints    
       
    cmp cx,1           
    je @input           ; N?u không h?p l? thì nh?p l?i
    
    xor bx,bx          
    mov bl,al
    xor bl,32d         ; Ð?i ch? hoa/thu?ng b?ng XOR trick
                      
@output:            
    lea dx,output_msg
    mov ah,9
    int 21h 
     
    mov dl,bl          
    mov ah,2
    int 21h
            
    lea dx,n_line      
    mov ah,9
    int 21h 
    
    jmp @input
    
@terminate: 
    lea dx,end_msg  
    mov ah,9
    int 21h
      
    mov ah,4ch         
    int 21h            
main endp              

; ===== PROCEDURE =====

$check_constraints proc
    ; Ki?m tra xem ký t? có ph?i là ch? cái hay không (A-Z ho?c a-z)
    mov cx,1           ; m?c d?nh không h?p l?

    cmp al,'A'
    jl @end_function
    cmp al,'Z'
    jle @valid

    cmp al,'a'
    jl @end_function
    cmp al,'z'
    jg @end_function

@valid:
    mov cx,0           ; h?p l?

@end_function:
    ret
$check_constraints endp

end main
