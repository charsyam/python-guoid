import unittest
import sys, os

sys.path.append("/Library/Python/2.7/site-packages/")
import mock

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from guoid import Instagram

class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    def get_id(self, id):
        return abs(hash(id))%17

    @mock.patch("guoid.utils.time.time")
    def test_Instagram_time_is_0(self, time):
        time.return_value = 0
        epoch = 0
        guoid = Instagram(epoch)
        guoidvalue = guoid.next(self.get_id("charsyam"))
        self.assertEqual(49152, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_Instagram_time_is_1(self, time):
        time.return_value = 0
        epoch = 0
        guoid = Instagram(epoch)
        guoidvalue = guoid.next(self.get_id("charsyam2"))
        self.assertEqual(57344, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_Instagram_time_is_2(self, time):
        time.return_value = 1
        epoch = 0
        guoid = Instagram(epoch)
        guoidvalue = guoid.next(self.get_id("charsyam"))
        self.assertEqual(4194353152, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_Instagram_time_is_1_and_epoch_is_1(self, time):
        time.return_value = 1
        epoch = 1
        guoid = Instagram(epoch)
        guoidvalue = guoid.next(self.get_id("charsyam"))
        self.assertEqual(49152, guoidvalue)

if __name__=="__main__":
    sys.exit(unittest.main())
