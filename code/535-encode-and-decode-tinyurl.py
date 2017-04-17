url_map = {}
ID = 1

class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        global ID
        encoded = hex(ID).lstrip('0xX')
        url_map[ID] = longUrl
        ID += 1
        return 'http://shorturl.com/' + encoded


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        encoded = shortUrl.split('/')[-1]
        decoded = int(encoded, 16)
        if decoded in url_map:
            return url_map[decoded]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
if __name__ == '__main__':
    url = 'https://leetcode.com/problems/design-tinyurl'
    codec = Codec()
    assert codec.decode(codec.encode(url)) == url
