tld_tables = []

class DNSSearch:
    def __init__(self, url: str, locations: list[str]):
        self.url = url
        self.locations = locations
        self._url_split = self.url.split(".")

        # Extract TLD
        self.tld = self._url_split.pop()
        self.tld_hash = hash(self.tld)
        # Extract SLD (second-level domain)
        self.sld = self._url_split.pop() + "." + self.tld
        self.sld_hash = hash(self.sld)
        # The remaining parts are subdomains (from right to left)
        self.subdomains = self._url_split[::-1]  # Reversed for right-to-left logic

    def __str__(self):
        return (f"URL: {self.url}\n"
                f"TLD: {self.tld}\n"
                f"SLD: {self.sld}\n"
                f"Subdomains: {self.subdomains}")
  
        
dns = DNSSearch("blog.shop.example.co.za", locations=[])
print(dns)
