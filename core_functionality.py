""" 
Intended to provide a clas that will read and write the fromat defined by the files in the `data` directory 

Author: Chris Penny
"""
# Built-in
import os
import json
import logging

# Internal
from batching_core import stream_log, file_log


DEFAULT_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
DEFAULT_WRITE_PATH = os.path.join(os.path.dirname(__file__), 'write')


def get_real_path(path):
    """ Get to the heart of the path matter """
    return os.path.realpath(os.path.abspath(os.path.expanduser(path)))


class DataCore(object):
    def __init__(self, file_path=None):
        self._data_path = file_path or DEFAULT_DATA_PATH
        self.data_store = {}
        self.out_data = {}

    @property 
    def data_path(self):
        """ Path to the location of the data """
        return self._data_path

    @data_path.setter
    def data_path(self, input_path):
        """ Provides symnlink, and absolute path resolution """
        self._data_path = get_real_path(input_path)

    def read(self):
        """ Using the data_path, read and store the content of the directory.

        Returns:
            (dict) containing data read/stored
        """
        self.data_store = {}
        for data_file in os.listdir(self.data_path):
            with open(os.path.join(self.data_path, data_file), "r") as open_file:
                self.data_store[data_file] = json.load(open_file)
        return self.data_store
    
    def communicate(self, std_out=False, file_path=None, **kwargs):
        """ Gather the data, intrepret kwargs, and log to either std or file

        Args:
            std_out (bool): communicate through std out
            file_path (str): path to file to save output

        """
        if not self.data_store:
            self.read()
        record_fields = [x for x, y in kwargs.items() if y]  # intrepret kwargs from CLI 
        if std_out:
            stream_name = "str_{}".format(__name__)
            stream_log(stream_name, record_fields=record_fields).info(self.data_store)
        if file_path:
            stream_name = "file_{}".format(__name__)
            file_log(__name__, record_fields=record_fields, file_name=file_path).info(self.data_store)


class CoreException(Exception):
    """ Custom exeception for the Core module """
