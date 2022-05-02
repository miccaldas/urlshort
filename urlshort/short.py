"""URL Shortener stolen in almost all entirety."""
from __future__ import with_statement
import contextlib
from urllib.parse import urlencode
from urllib.request import urlopen
from colr import color


#  Defining the function to shorten a URL
def make_shorten(url):
    # we append the escaped url to the end of tinyurl’s api url. Then we open the request_url using urlopen.
    request_url = "http://tinyurl.com/api-create.php?" + urlencode({"url": url})
    with contextlib.closing(urlopen(request_url)) as response:
        # The urlopen function returns a stream of bytes rather than a string so in order to print it and alter it we have to convert it into utf-8.
        return response.read().decode("utf-8")


url = input(color("What is your url? ", fore="#f37735"))
url_short = make_shorten(url)
print(color("+------------------------------+", fore="#f7d0cb"))
print(color("| ", fore="#f7d0cb") + color(url_short, fore="#f37735") + color(" |", fore="#f7d0cb"))
print(color("+------------------------------+", fore="#f7d0cb"))


# https://tinyurl.com/y9m7998w
