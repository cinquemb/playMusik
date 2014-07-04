from subprocess import Popen
import subprocess
import sys
import re
import random

"""
CREATE A PLAYLIST FROM ANY DIRECTORY WITH MUSIC FILES

command: python play_filt_music.py {search term} {1|0}

Where search term is a possible name of artist/song inside directory
1 is randomized list
0 is not randomized list
"""

def execute_cmd(cmd):
	try:
		proc = Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=None, close_fds=True)
		proc_data = proc.communicate()[0]

		if '*' in cmd:
			data = [re.escape(string) for string in proc_data.split('\n')[:-1]]
		elif 'afplay' in cmd:
			data = 0
		elif len(proc_data) > 0 in proc_data:
			data = 0
		else:
			data = 1
	
	except Exception, e:
		data = e
	return data


def show_play_matches(match_string, is_random):
	cmd = 'find . -iname "*%s*.mp*"'% (match_string)
	match_check = execute_cmd(cmd)

	if match_check != 0 and match_check !=1:
		if is_random == 1:
			random.shuffle(match_check)

		if len(match_check) > 0:
			for song in match_check:
				print 'Now Playing: %s' % (song)
				cmd_1 = 'afplay %s' % (song)
				play_check = execute_cmd(cmd_1)
				if play_check == 0:
					continue
				else:
					print 'Song Failed To Play: %s' % (song)
					break
		else:
			print 'No Songs That Match The Search Term: %s' % (match_string)

if len(sys.argv) > 1:
    match_string = str(sys.argv[1])

    if sys.argv[2]:
    	is_random = int(sys.argv[2])
    else:
    	is_random = 0

    show_play_matches(match_string, is_random)
