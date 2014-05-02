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

word = "junk"
for line in sys.stdin.readlines():
    if line[0] == "#":
        #sys.stdout.write("Ignoring Comment")
        next
    elif line[0:6] == "album=":
        words = line.split('=')
        album = words[1].rstrip('\n')
        sys.stdout.write('TITLE "' + album + '"\n')
    elif line[0:7] == "artist=":
        words = line.split('=')
        artist = words[1].rstrip('\n')
        sys.stdout.write('PERFORMER "' + artist + '"\n')
    elif line[0:5] == "file=":
        words = line.split('=')
        file = words[1].rstrip('\n')
        sys.stdout.write('FILE ' + file + '\n')
    else:
        words = line.split('|')
        track = words[0].rstrip('\n')
        title = words[1].rstrip('\n')
        start_time = words[2].rstrip('\n')
        sys.stdout.write('TRACK ' + track + ' AUDIO\n')
        sys.stdout.write('FLAGS PRE\n')
        sys.stdout.write('TITLE "' + title + '"\n')
        sys.stdout.write('PERFORMER "' + artist + '"\n')
        sys.stdout.write('INDEX 01 ' + start_time + '\n')
