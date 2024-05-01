"""

To run from MayaSkeleton Dir
python -m unittest test.test_core_functionality

"""

# Built-in
import os
import unittest

# Internal
import core_functionality
import batching_core


TEST_DATA_DIR = 'test_data'
SKEL_TYPES = [ 'Fiend', 'Bird', 'Human' ]
ALL_CMD_KWARGS = dict(flags=True, parent_name=True, name=True, color=True, radius=True,
                      length=True, mirror_index=True, model_space=True)


def get_test_data_path(data_folder=None):
    """ Acquire add test data folder to current dir """
    if not data_folder:
        data_folder = TEST_DATA_DIR
    return os.path.join(core_functionality.get_real_path(os.path.dirname(__file__)), data_folder)


def get_result_names():
    """ Add the standard file name to the types """
    return [x + '_SKEL_0000.skeleton.uc' for x in SKEL_TYPES]


class TestCore(unittest.TestCase):

    def test_read_default(self):
        """ Ensure read is getting all files """
        dc = core_functionality.DataCore()
        dc.read()
        test_results = get_result_names()
        self.assertEquals(dc.data_store.keys(), test_results)

    def test_read_custom(self):
        """ Ensure custom read works from different location """
        dc = core_functionality.DataCore(file_path=get_test_data_path())
        dc.read()
        test_results = ['Test{}'.format(x) for x in get_result_names()]
        self.assertEquals(dc.data_store.keys(), test_results)

    def test_file_comms(self):
        # clean up last test...usually would mock file read/write, but not part of standard lib
        test_out_file_path = os.path.join(get_test_data_path("write_test"), 'file_out.txt')
        if os.path.exists(test_out_file_path):
            os.remove(test_out_file_path)

        dc = core_functionality.DataCore()
        dc.communicate(file_path=test_out_file_path, **ALL_CMD_KWARGS)
        self.assertTrue(os.path.exists(test_out_file_path))


if __name__ == "__main__":
    unittest.main()
