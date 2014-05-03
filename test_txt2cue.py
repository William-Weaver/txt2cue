import unittest
from StringIO import StringIO
from txt2cue import parse_input


class TestTxt2Cue(unittest.TestCase):
    def setUp(self):
        self.input_file = StringIO('''
# This is a comment
artist=James Taylor
album=Sweet Baby James
file=/home/user/Music/James_Taylor/Sweet_Baby_James/test.flac
01|Sweet Baby James|00:00:00
02|Lo And Behold|02:54:00
''')
	
    def test_parsing(self):
        result = parse_input(self.input_file)
        expected_output = '''PERFORMER "James Taylor"
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
INDEX 01 02:54:00'''
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
