import unittest
import sys
import mock

from guoid.guoid import instagram
from guoid.guoid import init_guoid

class TestUtils(unittest.TestCase):
    def setUp(self):
        init_guoid()

    @mock.patch("guoid.utils.time.time")
    def test_instagram_time_is_0(self, time):
        time.return_value = 0
        epoch = 0
        guoidvalue = instagram("charsyam", epoch)
        self.assertEqual(1212416, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_instagram_time_is_0(self, time):
        time.return_value = 0
        epoch = 0
        guoidvalue = instagram("charsyam2", epoch)
        self.assertEqual(3186688, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_instagram_time_is_1(self, time):
        time.return_value = 1
        epoch = 0
        guoidvalue = instagram("charsyam", epoch)
        self.assertEqual(4195516416, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_instagram_time_is_1_and_epoch_is_1(self, time):
        time.return_value = 1
        epoch = 1
        guoidvalue = instagram("charsyam", epoch)
        self.assertEqual(1212416, guoidvalue)

if __name__=="__main__":
    sys.exit(unittest.main())

