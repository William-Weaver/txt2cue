#!/usr/bin/python3
'''
 Python script to read a simple yaml file from stdin
 containing the Artist, Album Title, Flac audio file full path
 and track listings, one per line and output to stdout a cue sheet
 in a format suitable for split2flac.

 Input example:
    artist: James Taylor
    album: Sweet Baby James
    file: /home/user/Music/James_Taylor/Sweet_Baby_James/test.flac
    tracks:
        - Sweet Baby James | 00:00:00
        - Lo And Behold | 02:54:00

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
'''
import sys
import yaml


def parse_input(file_obj):
    try:
        data = yaml.load(file_obj)
    except yaml.YAMLError as e:
        sys.stderr.write("Error in yaml input file:" + e)
    else:
        try:
            last = 'artist'
            artist = data['artist']
            last = 'album'
            album = data['album']
            last = 'file'
            file = data['file']
            last = 'tracks'
            tracks = data['tracks']
        except TypeError:
            sys.stderr.write(
                'Error in input: "' + last + '" not well formed.\n')
            sys.stderr.write('Data was:\n' + data)
            sys.exit(1)
        else:
            output = [
                'PERFORMER "{}"'.format(artist),
                'TITLE "{}"'.format(album),
                'FILE {}'.format(file)]
            for num, track_info in enumerate(tracks, start=1):
                title, start_time = track_info.split('|')
                title = title.strip()
                start_time = start_time.strip()
                output.append(
                    'TRACK {num:02d} AUDIO\n'
                    'FLAGS PRE\n'
                    'TITLE "{title}"\n'
                    'PERFORMER "{artist}"\n'
                    'INDEX 01 {start_time}'.format(
                        num=num, title=title, artist=data['artist'],
                        start_time=start_time))
    return '\n'.join(output)

if __name__ == '__main__':
    try:
        sys.stdout.write(parse_input(sys.stdin))
    except ValueError as e:
        sys.stderr.write('Invalid input: ' + e)
