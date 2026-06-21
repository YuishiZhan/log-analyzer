log_data = """10:00 5.5.5.5 80 blocked
10:01 10.0.0.2 22 allowed
10:02 5.5.5.5 443 blocked
10:03 192.168.1.1 80 allowed
10:04 5.5.5.5 22 blocked
10:05 10.0.0.2 443 allowed
10:06 5.5.5.5 80 blocked
10:07 10.0.0.2 22 blocked
10:08 192.168.1.1 443 blocked
10:09 5.5.5.5 80 blocked"""

lines = log_data.splitlines()
ip_attacks = {}
port_attacks = {}

for line in lines:
    parts = line.split()
    ip = parts[1]
    port = int(parts[2])
    
    if ip in ip_attacks:
        ip_attacks[ip] += 1
    else:
        ip_attacks[ip] = 1
    
    if port in port_attacks:
        port_attacks[port] += 1
    else:
        port_attacks[port] = 1

max_ip = max(ip_attacks, key=ip_attacks.get)
max_port = max(port_attacks, key=port_attacks.get)

print("📊 ОТЧЕТ ПО ЛОГАМ")
print(f"Всего событий: {len(lines)}")
print(f"Самый активный IP: {max_ip} (атак: {ip_attacks[max_ip]})")
print(f"Самый частый порт: {max_port} (раз: {port_attacks[max_port]})")
