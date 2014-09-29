import unittest
import sys, os

sys.path.append("/Library/Python/2.7/site-packages/")
import mock

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from guoid import SnowFlake

class TestUtils(unittest.TestCase):
    def setUp(self):
        pass

    @mock.patch("guoid.utils.time.time")
    def test_SnowFlake_time_is_0(self, time):
        time.return_value = 0
        epoch = 0
        guid = SnowFlake(0, 0, epoch)
        guoidvalue = guid.next()
        self.assertEqual(0, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_SnowFlake_time_is_1(self, time):
        time.return_value = 1
        epoch = 0
        guid = SnowFlake(0, 0, epoch)
        guoidvalue = guid.next()
        self.assertEqual(4194304000, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_SnowFlake_time_is_1_and_epoch_is_1(self, time):
        time.return_value = 1
        epoch = 1
        guid = SnowFlake(0, 0, epoch)
        guoidvalue = guid.next()
        self.assertEqual(0, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_SnowFlake_time_is_1_and_epoch_is_0_and_datacenterid_is_1(self, time):
        time.return_value = 1
        epoch = 1
        guid = SnowFlake(1, 0, epoch)
        guoidvalue = guid.next()
        self.assertEqual(131072, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_SnowFlake_time_is_1_and_epoch_is_0_and_workerid_1(self, time):
        time.return_value = 1
        epoch = 1
        guid = SnowFlake(0, 1, epoch)
        guoidvalue = guid.next()
        self.assertEqual(4096, guoidvalue)

if __name__=="__main__":
    sys.exit(unittest.main())

