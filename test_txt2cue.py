import unittest
from io import StringIO
from txt2cue import parse_input, process_key_val_pair


class TestTxt2Cue(unittest.TestCase):
    def setUp(self):
        self.input_file = StringIO('''
# This is a comment
artist=James Taylor
album=Sweet Baby James
file=/home/user/Music/James_Taylor/Sweet_Baby_James/test.flac
Sweet Baby James|00:00:00
Lo And Behold|02:54:00
''')
    def test_process_key_val_pair(self):
        self.assertEqual(
            process_key_val_pair('hello=world'),
            ('hello', 'world'))
        self.assertEqual(
            process_key_val_pair('goodbye =  world  '),
            ('goodbye', 'world'))

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
