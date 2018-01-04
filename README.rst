==================
JSON-to-CSV Module
==================

This script reads JSON-structured data from a file or a URL to extract data and store it into a CSV file.

This program fulfills the following functions:

* Reads JSON data from a file
* Reads JSON data from a URL
* Write JSON data into a CSV file using Unicode

Requirements
============

JSON-to-CSV requires `unicodecsv` to function properly. This module can be installed by executing::

    pip install unicodecsv

or by using the `requirements.txt` file included with this project::

    pip install -r requirements.txt

Usage
=====

The JSON-to-CSV module can be used within other scripts by importing the module within your own code::

    from jsoncsv import JsonData

    url = "http://www.website.com/api/jsonresponse"
    csv = "out.csv"
    json = JsonData()
    data = json.read_url(url)
    json.write_dict_to_csv(csv, data["books"])

The code above will read the response from `http://www.website.com/api/jsonresponse` and return a dictionary
from the JSON data received. It will then save the "books" collection to the "out.csv" file. A simple script
is also provided that can perform the steps above from the command line::

    python.exe main.py -u http://www.website.com/api/jsonresponse -c out.csv -d Books

Each of the arguments available can be displayed using the `-h` switch::

    usage: main.py [-h] [-V] [-f INPUT_FILE] [-d DATA] -c OUTPUT_FILE
                   [-u INPUT_URL]

    Trasnfers data from JSON-structured data into a CSV file.

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -f INPUT_FILE, --file INPUT_FILE
                            Specifies a file containing JSON-formatted data to
                            extract from.
      -d DATA, --data DATA  Specifies which JSON element from the source should be
                            extracted.
      -c OUTPUT_FILE, --csv OUTPUT_FILE
                            Specifies the CSV filename data extracted will be
                            written to.
      -u INPUT_URL, --url INPUT_URL


Known Issues
============

Please report any bugs or requests that you have using the GitHub issue tracker.

Authors
=======

.. _DeepCode: https://www.deepcode.ca
