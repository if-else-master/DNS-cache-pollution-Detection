import socket
import concurrent.futures
import time

def check_dns(domain, dns_server):
    try:
        # 設定 DNS 伺服器
        server = socket.gethostbyname_ex(domain)[2]
        
        print(f"DNS 伺服器 {dns_server} 的解析結果：")
        print(f"域名：{domain}")
        print(f"IP 位址：{server}")
        return server
    except Exception as e:
        print(f"查詢 {dns_server} 時發生錯誤：{str(e)}")
        return None

def main():
    domain = "example.com"
    dns_servers = [
        "8.8.8.8",        
        "1.1.1.1",        
        "208.67.222.222",
        "9.9.9.9"         
    ]
    
    results = {}
    for server1 in dns_servers:
        result = check_dns(domain, server1)
        results[server1] = result
    
    # 比較結果
    aa = results[dns_servers[0]]
    if aa:
        for server2, ips in results.items():
            if ips != aa:
                print(f"\nDNS劫持警告：{server2} 返回的IP地址與參考DNS服務器不一致")
                print(f"{server2} 返回的IP地址：{ips}")
                print(f"參考IP地址：{aa}")
            else:
                print(f"\n{server2} 返回的IP地址一致：{ips}")

if __name__ == "__main__":
    main()