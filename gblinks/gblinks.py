# -*- coding: utf-8 -*-

import fnmatch
import markdown
import os
import re
import sys
import urlparse

from lxml import html

reload(sys)
sys.setdefaultencoding('utf8')

def is_url(url):
    return urlparse.urlparse(url).scheme != ''

def get_link_dict(file, link_text, link_url, link_path):
     data = {}
     data['file'] = os.path.normpath(file)
     data['link_text'] = link_text
     data['link_url'] = link_url
     data['link_path'] = os.path.normpath(link_path)

     return data;


class Gblinks:

    def __init__(self, path):
        if not os.path.isdir(path):
            raise ValueError('the given path is not valid')

        self.__mdfiles = self._get_markdown_files(path)

        if not self.__mdfiles:
            raise ValueError('the given path does not contain MarkDown files')

    def _files_iterator(self, path, pattern='*.md'):
        for root, dirs, files in os.walk(path):
            for file in fnmatch.filter(files, pattern):
                yield root, file

    def _get_markdown_files(self, path):
        return list(self._files_iterator(path))

    def _link_iterator(self, markdown_file):
        with open(markdown_file, 'r') as file:
            data = file.read()

            doc = html.fromstring(markdown.markdown(data))
            for link in doc.xpath('//a'):
                href = link.get('href')

                if href and not bool(re.search('{{.*}}', href)):
                  yield link.text, href

    def check_broken_links(self):
        return self.get_links(only_broken=True, only_local=True)

    def get_links(self, only_broken=False, only_local=False):
        links = []

        for path, file in self.__mdfiles:
            markdown_file = os.path.join(path, file)
            for link_text, link_url in self._link_iterator(markdown_file):
                if not only_local or not is_url(link_url):
                    link_path = os.path.join(path, link_url)
                    if not only_broken or not os.path.exists(link_path):
                        links.append(get_link_dict(markdown_file, link_text, link_url, link_path))

        return links
