#!/usr/bin/env python

'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

import glob
import os

if __name__=="__main__":
    WEBSITE_DIR = '/Users/Zaaron/Code/bzreinhardt.github.io'
    post_dir = os.path.join(WEBSITE_DIR,'_posts/')
    tag_dir = os.path.join(WEBSITE_DIR, 'tag/')

    filenames = glob.glob(post_dir + '*md')

    total_tags = []


    for filename in filenames:
        f = open(filename, 'r')
        crawl = False
        tag_section = False
        for line in f:
            if crawl:
                current_tags = line.strip().split()
                if current_tags[0] == 'tags:':
                    tag_section = True
                    # new style tags on the same line
                    print(len(current_tags))
                    if len(current_tags) > 1:
                        for tag in current_tags[1:]:
                            tag = tag.translate(None, '[],')
                            total_tags.append(tag)
                        crawl = False
                        break
                else:
                    if tag_section:
                        tag = '-'.join(line.strip().split()[1:])
                        total_tags.append(tag)
                    if current_tags[0] == 'meta:':
                        tag_section = False
                        break


            if line.strip() == '---':
                if not crawl:
                    crawl = True
                else:
                    crawl = False
                    break
        f.close()
    total_tags = set(total_tags)

    old_tags = glob.glob(tag_dir + '*.md')
    for tag in old_tags:
        os.remove(tag)

    if not os.path.exists(tag_dir):
        os.makedirs(tag_dir)

    for tag in total_tags:
        tag_filename = tag_dir + tag + '.md'
        f = open(tag_filename, 'a')
        write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
        f.write(write_str)
        f.close()
    print("Tags generated, count", total_tags.__len__())
