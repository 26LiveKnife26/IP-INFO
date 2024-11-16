import requests

def ip_info(ip):
    ips = requests.get(url=f"http://ip-api.com/json/{ip}").json()

    ip_infos = {
        "Status" : ips.get('status'),
        "IP" : ips.get('query'),
        "Country": ips.get('country'),
        "Region" : ips.get('regionName'),
        "City" : ips.get('city'),
        "ZIP(почтовый адр.)" : ips.get('zip'),
        "Lat(ширина)" : ips.get('lat'),
        "Lon(длина)" : ips.get('lon'),
        "TimeZone" : ips.get('timezone'),
        "ISP(интернет-провайдер)": ips.get('isp'),
        "Organization" : ips.get('org'),
        "AS" : ips.get('as')
    }

    for i, i2 in ip_infos.items():
        print(f"{i} : {i2}")