#!/usr/bin/python3
"""
 Python script to read a simple text file from stdin
 containing the Artist, Album Title, Flac audio file full path
 and track listings, one per line and output to stdout a cue sheet
 in a format suitable for split2flac.

 Input example:
    # This is a comment
    artist=James Taylor
    album=Sweet Baby James
    file=/home/user/Music/James_Taylor/Sweet_Baby_James/test.flac
    01|Sweet Baby James|00:00:00
    02|Lo And Behold|02:54:00

 Output from the above:
    PERFORMER "James Taylor"
    TITLE "Sweet Baby James"
    FILE /home/user/Music/James_Taylor/Sweet_Baby_James/test.flac
    TRACK 01 AUDIO
    FLAGS PRE
    TITLE "Sweet Baby James"
    PERFORMER "James Taylor"
    INDEX 01 00:00:00
    TRACK 02 AUDIO
    FLAGS PRE
    TITLE "Lo And Behold"
    PERFORMER "James Taylor"
    INDEX 01 02:54:00
"""
import sys

def process_key_val_pair(line):
    key, value = line.split('=')
    return key.strip(), value.strip()

def parse_input(file_obj):
	output = []
	for line in file_obj.readlines():
            line = line.strip()
	    if line.startswith("#"):
		# Ignore comments
		continue
	    elif line.startswith("album="):
		_, album = process_key_val_pair(line)
		output.append('TITLE "{}"'.format(album))
	    elif line.startswith("artist="):
		_, artist = process_key_val_pair(line)
		output.append('PERFORMER "{}"'.format(artist))
	    elif line.startswith("file="):
		_, file_name = process_key_val_pair(line)
		output.append('FILE ' + file_name)
	    elif line:
		words = line.split('|')
		track = words[0]
		title = words[1]
		start_time = words[2]
		output.append('TRACK ' + track + ' AUDIO')
		output.append('FLAGS PRE')
		output.append('TITLE "' + title + '"')
		output.append('PERFORMER "' + artist + '"')
		output.append('INDEX 01 ' + start_time + '')
        return '\n'.join(output)

if __name__ == '__main__':
    sys.stdout.write(parse_input(sys.stdin))
