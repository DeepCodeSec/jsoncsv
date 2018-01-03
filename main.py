#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) DeepCode 2017, All Rights Reserved

All information contained herein is, and remains the property of DeepCode
and is provided to authorized clients Dissemination of this information
or reproduction of this material is strictly forbidden unless prior written
permission is obtained from DeepCode.
"""

from __future__ import print_function

import sys
import argparse
import logging

from jsoncsv import metadata
from jsoncsv import JsonData

logger = logging.getLogger(__name__)

def extract_json_from_url_to_csv(_url, _csv, _key):
    json = JsonData()
    data = json.read_url(_url)
    lines_written = 0
    if _key in data:
        data_to_save = data[_key]
        lines_written = json.write_dict_to_csv(_csv=_csv, _dict=data_to_save)
    else:
        logger.error("Could not find '{data:s}' in JSON data read from '{u:s}'.".format(
            data=_key,
            u=_url,
        ))

    if lines_written == 0:
        logger.error("No lines written to {csv:s}.".format(csv=_csv))

def extract_json_from_file_to_csv(_file, _csv, _key):
    pass

def main(argv):
    """Program entry point.

    :param argv: command-line arguments
    :type argv: :class:`list`
    """

    logging.basicConfig(format="[%(asctime)s]-%(levelname)s: %(message)s", level=logging.INFO)

    author_strings = []
    for name, email in zip(metadata.authors, metadata.emails):
        author_strings.append('Author: {0} <{1}>'.format(name, email))

    epilog = '''
{project} {version}

{authors}
URL: <{url}>
'''.format(
        project=metadata.project,
        version=metadata.version,
        authors='\n'.join(author_strings),
        url=metadata.url)

    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=metadata.description,
        epilog=epilog)
    arg_parser.add_argument(
        '-V', '--version',
        action='version',
        version='{0} {1}'.format(metadata.project, metadata.version))
    arg_parser.add_argument(
        '-f', '--file',
        dest='input_file',
        help="Specifies a file containing JSON-formatted data to extract from.")
    arg_parser.add_argument(
        '-d', '--data',
        dest='data',
        help="Specifies which JSON element from the source should be extracted.")
    arg_parser.add_argument(
        '-c', '--csv',
        dest='output_file',
        required=True,
        help="Specifies the CSV filename data extracted will be written to.")
    arg_parser.add_argument(
        '-u', '--url',
        dest='input_url')
    args = arg_parser.parse_args(args=argv[1:])

    print(epilog)

    if args.input_url is not None:
        input_url = args.input_url
        output_file = args.output_file
        keys = args.data
        extract_json_from_url_to_csv(
            _url=input_url,
            _csv=output_file,
            _key=keys
        )
    elif args.input_file is not None:
        input_file = args.input_file
        output_file = args.output_file
        keys = args.data
        extract_json_from_file_to_csv(
            _file=input_file,
            _csv=output_file,
            _key=keys
        )
    else:
        logger.error("No file or URL specified.")
        return 1

    return 0


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()
