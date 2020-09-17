import sys
import importlib.abc
import imp
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser


# Debugging
import logging

log = logging.getLogger(__name__)

# Get links from a given URL
def _get_links(url):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == "a":
                attrs = dict(attrs)
                links.add(attrs.get("href").rstrip("/"))

    links = set()
    try:
        log.debug(f"Getting links from {url}")
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode("utf-8"))
    except Exception as e:
        log.debug(f"Could not get links. {e}")
    log.debug("links: %r", links)

    return links
