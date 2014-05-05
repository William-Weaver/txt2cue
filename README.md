Python script to read a simple text file from stdin
containing the Artist, Album Title, Flac audio file full path
and track listings, one per line and output to stdout a cue sheet
in a format suitable for split2flac.

Input example:
```yaml
artist: James Taylor
album: Sweet Baby James
file: /home/user/Music/James_Taylor/Sweet_Baby_James/test.flac
tracks:
    - Sweet Baby James | 00:00:00
    - Lo And Behold | 02:54:00
```

Output from the above:
```
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
```
