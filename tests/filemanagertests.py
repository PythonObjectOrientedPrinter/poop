import unittest
from src.poop.filemanager import FileManager


class FileManagerTest(unittest.TestCase):
    def setUp(self):
        self.fm = FileManager()
        self.blueprints_path = './tests/blueprints/'

    def tearDown(self):
        del self.fm

    def test_listdir(self):
        listdir = FileManager.listdir('./tests/blueprints/listdirblueprint')
        self.assertListEqual(listdir, ['test.gcode', 'one.txt', 'two.py'])

    def test_can_open_file(self):
        self.fm.open_file('{0}listdirblueprint/{1}'.format(self.blueprints_path, 'one.txt'))
        file_content = self.fm.read_file()
        self.assertEqual(file_content, '#Line One\n#Line Two\n#Line Three')

    def test_can_read_line_one(self):
        self.fm.open_file('{0}listdirblueprint/{1}'.format(self.blueprints_path, 'test.gcode'))
        line_content = self.fm.read_line()
        self.assertEqual(line_content, '; This is a comment\n')

    def test_can_read_line_two_correctly(self):
        self.fm.open_file('{0}listdirblueprint/{1}'.format(self.blueprints_path, 'test.gcode'))
        self.fm.read_line()
        line_content = self.fm.read_line()
        self.assertEqual(line_content, 'G0 X100 Y100 Z0\n')
