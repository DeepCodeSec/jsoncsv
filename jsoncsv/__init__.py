# -*- coding: utf-8 -*-
"""Transfers data from JSON-structured data into a CSV file."""

import json
import logging
import unicodecsv as csv
import urllib.request

from jsoncsv import metadata

logger = logging.getLogger(__name__)

__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright


class JsonData(object):
    def __init__(self):
        self.__data = None

    @property
    def json_data(self):
        """
        Returns the latest JSON-formatted data read using this instance.

        This accessor simply returns the JSON data stored within the object, which correspond
        to the latest valid URL or file read.

        :return: JSON-formatted data or None if no data was read from any source.
        """
        return self.__data

    def read_url(self, _url):
        """
        Reads JSON data from the specified URL.

        This function will read the response from the given URL and will
        attempt to parse the results as JSON data. If an exception occurs,
        this function will return None and no data will be loaded in the object.

        :param _url: The URL to JSON-formatted data.
        :return: The JSON data loaded from the URL provided.
        """
        assert _url is not None

        logger.info("Connecting to '{u:s}'...".format(u=_url))

        with urllib.request.urlopen(_url) as fp:
            try:
                self.__data = json.loads(fp.read().decode('utf-8'))
                logger.info("Successfully read {nb:d} byte(s) from '{u:s}'...".format(nb=len(self.__data), u=_url))
            except Exception as e:
                logger.error("Failed to read data from '{u:s}':".format(u=_url))
                logger.error(str(e))
                self.__data = None

        return self.__data

    def read_file(self, _file):
        assert _file is not None

        with open(_file, "r") as fp:
            self.__data = json.loads(fp.read().decode('utf-8'))

    def write_dict_to_csv(self, _csv, _dict):
        assert _csv is not None
        assert _dict is not None

        csv_fp = open(_csv, "wb")
        csv_writer = csv.writer(csv_fp)
        rows_written = 0
        logger.info("Writing {nb_obj:d} line(s) to {csv:s}...".format(
            nb_obj=len(_dict),
            csv=_csv
        ))
        for item_key in _dict.keys():
            item = _dict[item_key]
            if rows_written == 0:
                header_row = item.keys()
                csv_writer.writerow(header_row)
                rows_written += 1
            csv_writer.writerow(item.values())

        logger.info("{nb_obj:d} line(s) written to {csv:s}...".format(
            nb_obj=len(_dict),
            csv=_csv
        ))
        return rows_written
