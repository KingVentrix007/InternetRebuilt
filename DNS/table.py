
master_table = {}
def add_dns_entry(url,ip:list[str]):
    broken_url = url.split(".")[::-1]
    current_table = master_table
    for part in broken_url:
        next_table = current_table.get(part,None)
        if(next_table == None):
            current_table[part] = {}
            next_table = current_table.get(part,None)
        current_table = next_table
    if(current_table.get("ip",None) == None):
        current_table["ip"] = ip
    else:
        for i in ip:
            current_table["ip"].append(i)

def search(url):
    broken_url = url.split(".")[::-1]
    current_table = master_table
    for part in broken_url:
        next_table = current_table.get(part,None)
        if(next_table == None):
            return None
        current_table = next_table
    return current_table["ip"]
def test():
    add_dns_entry("example.co.za",["1.1.1.1"])
    add_dns_entry("example.za",["3.2.1.0"])

    print(search("example.za"))

test()