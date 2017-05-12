import time
import sys
import re
from bs4 import BeautifulSoup
import requests
import html.parser
import jinja2
import codecs
import os
from collections import Counter
from string import ascii_uppercase as letters
import subprocess
from ftplib import FTP

loader = jinja2.FileSystemLoader(os.getcwd())
jenv = jinja2.Environment(loader=loader)
template = jenv.get_template('room_info.j2')

urlMK = 'https://wiimmfi.de/mkw'
h = html.parser.HTMLParser()

player = '5284-6991-7807'


def room_info():
    dot = str('.')
    while 1 > 0:
        try:
            wiimmfii_page = requests.get(urlMK)

            soup = BeautifulSoup(wiimmfii_page.content, "lxml")
            player_list = []

            global room_top_text
            room_top = soup.find(text=player).find_previous('th', {'class': 'tc'})
            room_top_text = room_top.text
            room_bottom = soup.find(text=player).find_next('th', {'class': 'tc'})

            for tag in soup.find(text=player).find_previous('th', {'class': 'tc'}).next_elements:
                if tag == room_bottom:
                    break
                else:
                    player_list.append(tag)

            player_list = [str(i) for i in player_list]
            player_string = ''.join(player_list)
            soup2 = BeautifulSoup(player_string, 'lxml')
            rows = soup2.find_all('tr')

            if 'class="tc"' in str(player_list[-1]):
                rows = rows[1:-1]
            else:
                rows = rows[1:]

            player_codes = [td.contents[1].text for td in rows]
            player_names = [td.contents[16].text for td in rows]
            player_conn_fails = [td.contents[10].text for td in rows]
            player_regions = [td.contents[5].text for td in rows]
            player_roles = [td.contents[3].text for td in rows]
            player_points = [td.contents[12].text for td in rows]
            player_values = zip(player_names, player_conn_fails, player_regions, player_roles, player_points, player_codes)
            player_values = [list(i) for i in player_values]

            regex_2p = re.compile(r'[1.]\s.+[2.]\s.+')

            viewer_2p = len([i for i in player_values if re.search(regex_2p, i[0]) and "viewer" in str(i[3])])

            two_player = [i for i in player_names if re.search(regex_2p, i)]

            viewers = len([i for i in player_roles if "viewer" in str(i)]) + viewer_2p

            room_size = str(len(player_names) + len(two_player) - viewers)

            global main_dict
            main_dict = dict(zip(player_codes, player_values))

            template_vars = {"main_dict": main_dict,
                             "room_top_text": room_top_text,
                             "room_size": room_size,
                             "viewers": viewers}
            web_output = template.render(template_vars)
            web_writer = codecs.open("Room_Info.html", "w", 'utf-8')
            web_writer.write(web_output)
            web_writer.close()
            print(room_top_text, flush=True)

        except:
            sys.stdout.write('\r' + dot)
            sys.stdout.flush()
            dot += '.'

        time.sleep(5)

room_info()
