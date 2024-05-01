""" 
Intended to provide a small utility the data core can use for formatting json output and writing to a file

For reference http://code.activestate.com/recipes/580667-json-formatted-logging/

Logging will also need to be configured by the interface

Author: Chris Penny
"""
# Built-in
import json
import logging
from collections import defaultdict


def filter_data(input_data, interesting_fields=None):
    """ Filter input data by interesting fields 

    Note:
        Consider moving to core

    Args:
        input_data (dict): to filter
        interesting_fields (list): to be filtered by

    Returns:
        (defaultdict)
    """
    if interesting_fields is None:
        interesting_fields = []
    out_data = defaultdict(dict)
    for data_file, data_value in input_data.items():
        for skel_data in data_value['skeletons']:
            bone_list = []
            for bone_data in skel_data['uc_data']['bones']:
                sub_out_data = {}
                for field in interesting_fields:
                    if field == 'parent_name':
                        sub_out_data['parent_name'] = bone_data['debug_data']['parent_name']
                    else:
                        try:
                            sub_out_data[field] = bone_data[field]
                        except KeyError:
                            LOG.warning("Requested field '%s' not found ...skipping.", field)
                if sub_out_data:
                    bone_list.append(sub_out_data)
            if bone_list:  # only add if bones found
                out_data[data_file]['header'] = data_value['header']
                out_data[data_file][skel_data['uc_name']] = bone_list 
    return out_data


def logger(name, handler, record_fields=[], level=logging.INFO):
    """ Custom Logger to handle output """
    handler.setFormatter(JSONFormatter(record_fields))
    log = logging.getLogger(name)
    log.addHandler(handler)  # Persistant uses will need to check/set handlers to prevent multiple being applied during same session
    log.setLevel(level)
    return log


def file_log(log_name, record_fields=[], file_name='json.log', level=logging.INFO):
    """ Convenience function to return a JSON file logger for simple situations.

    Args:
         log_name: name of the logger - to allow for multiple logs, and levels of logs in an application
         record_fields: metadata fields to add to the JSON record created by the logger
         file_name: name of the file to be used in the logger

    Returns:
        JSON file logger
    """
    return logger(log_name, logging.FileHandler(file_name,'w'), record_fields, level)


def stream_log(log_name, record_fields=[], output_stream=None, level=logging.INFO):
    """
    A convenience function to return a JSON stream logger for simple situations.

    Args:
        log_name: name of the logger - to allow for multiple logs, and levels of logs in an application
        record_fields: metadata fields to add to the JSON record created by the logger
        output_stream: to be used by the logger. sys.stderr is used when output_stream is None.

    Returns:
        JSON stream logger
    """
    return logger(log_name, logging.StreamHandler(output_stream), record_fields, level)


class JSONFormatter(logging.Formatter):
    def __init__(self, record_fields=None, datefmt=None, custom_json=None):
        """
        JSONFormatter class outputs Python log records in JSON format. 

        Attrs:
            record_fields (list): strings referring to metadata fields on the record object. It can be empty.
            datefmt (str): date time format
            custom_json: JSONEncoder subclass to enable writing of custom JSON objects.

        """
        logging.Formatter.__init__(self, None, datefmt)
        self.record_fields = record_fields or []
        self.custom_json = custom_json

    def _get_json_data(self, record):
        """ 
        Combines supplied record_fields with the log record msg field into an object to convert to JSON 

        Args:
            record (logger): log record output to JSON log

        Returns:
            (object) to convert to JSON - filtered dict if record_fields are supplied or record.msg attribute
        """

        if self.record_fields:
            return filter_data(record.msg, interesting_fields=self.record_fields)
        else:
            return record.msg

    def format(self, record):
        """
        Overridden to take a log record and output a JSON formatted string.

        Args:
            record (logger): log record output to JSON log

        Returns:
           (str) in JSON format
        """
        return json.dumps(self._get_json_data(record), cls=self.custom_json, indent=4)
