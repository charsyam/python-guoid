import unittest
import sys
import mock

from guoid.guoid import snowflake
from guoid.guoid import init_guoid

class TestUtils(unittest.TestCase):
    def setUp(self):
        init_guoid()

    @mock.patch("guoid.utils.time.time")
    def test_snowflake_time_is_0(self, time):
        time.return_value = 0
        epoch = 0
        guoidvalue = snowflake(0, 0, epoch)
        self.assertEqual(0, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_snowflake_time_is_1(self, time):
        time.return_value = 1
        epoch = 0
        guoidvalue = snowflake(0, 0, epoch)
        self.assertEqual(4194304000, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_snowflake_time_is_1_and_epoch_is_1(self, time):
        time.return_value = 1
        epoch = 1
        guoidvalue = snowflake(0, 0, epoch)
        self.assertEqual(0, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_snowflake_time_is_1_and_epoch_is_0_and_datacenterid_is_1(self, time):
        time.return_value = 1
        epoch = 1
        guoidvalue = snowflake(1, 0, epoch)
        self.assertEqual(131072, guoidvalue)

    @mock.patch("guoid.utils.time.time")
    def test_snowflake_time_is_1_and_epoch_is_0_and_workerid_1(self, time):
        time.return_value = 1
        epoch = 1
        guoidvalue = snowflake(0, 1, epoch)
        self.assertEqual(4096, guoidvalue)

if __name__=="__main__":
    sys.exit(unittest.main())

