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


def check_data(key, input):
    try:
        if key not in input:
            sys.stderr.write(
                'Error in input: "' + key + '" not present.\n')
            return False
        else:
            return True
    except TypeError:
        sys.stderr.write(
            'Error in input: "' + key + '" not well formed.\n')
        return False


def parse_input(file_obj):
    try:
        data = yaml.load(file_obj)
    except yaml.YAMLError as e:
        sys.stderr.write("Error in yaml input file:" + e)
    else:
        try:
            has_artist = check_data('artist', data)
            has_album = check_data('album', data)
            has_file = check_data('file', data)
            has_tracks = check_data('tracks', data)
            if has_artist and has_album and has_file and has_tracks:
                album = data['album']
                artist = data['artist']
                file = data['file']
                tracks = data['tracks']
            else:
                sys.stderr.write('Malformed data - exiting\n')
                sys.stderr.write(data)
                sys.exit(1)
        except TypeError:
            sys.stderr.write('Data was:\n')
            sys.stderr.write(data)
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
    except:
        sys.stderr.write('Done')
