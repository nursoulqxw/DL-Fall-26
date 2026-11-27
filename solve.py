import socket, re, math, time

HOST = "challenge01.root-me.org"
PORT = 52002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)
s.connect((HOST, PORT))

buf = ""
m = None
start = time.time()
while m is None and time.time() - start < 1.8:
    try:
        chunk = s.recv(4096).decode(errors="ignore")
    except socket.timeout:
        break
    if not chunk:
        break
    buf += chunk
    m = re.search(r"square root of (\d+) and multiply by (\d+)", buf)

print("SERVER:", buf)

num1 = int(m.group(1))
num2 = int(m.group(2))
answer = math.sqrt(num1) * num2
msg = "{:.2f}\n".format(answer)
print("SENDING:", msg.strip())
s.sendall(msg.encode())

time.sleep(0.3)
try:
    print("RESPONSE:", s.recv(4096).decode(errors="ignore"))
except socket.timeout:
    print("нет ответа")
s.close()