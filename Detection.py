import socket
import concurrent.futures
import time

def check_dns(domain, dns_server):
    try:
        # 設定 DNS 伺服器
        original_nameserver = socket.gethostbyname_ex(domain)[2]
        
        print(f"DNS 伺服器 {dns_server} 的解析結果：")
        print(f"域名：{domain}")
        print(f"IP 位址：{original_nameserver}")
        return original_nameserver
    except Exception as e:
        print(f"查詢 {dns_server} 時發生錯誤：{str(e)}")
        return None

def main():
    domain = "example.com"
    dns_servers = [
        "8.8.8.8",        # Google DNS
        "1.1.1.1",        # Cloudflare DNS
        "208.67.222.222", # OpenDNS
        "9.9.9.9"         # Quad9 DNS
    ]
    
    results = {}
    for server in dns_servers:
        result = check_dns(domain, server)
        results[server] = result
    
    # 比較結果
    reference_result = results[dns_servers[0]]
    if reference_result:
        for server, ips in results.items():
            if ips != reference_result:
                print(f"\nDNS劫持警告：{server} 返回的IP地址與參考DNS服務器不一致")
                print(f"{server} 返回的IP地址：{ips}")
                print(f"參考IP地址：{reference_result}")
            else:
                print(f"\n{server} 返回的IP地址一致：{ips}")

if __name__ == "__main__":
    main()