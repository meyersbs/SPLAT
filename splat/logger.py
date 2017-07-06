#!/usr/bin/env python

""" This module formats messages with colors and/or identifiers. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers", "Nuthan Munaiah"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
import sys

from pkg_resources import resource_filename
from termcolor import cprint
from time import gmtime, strftime

#### GLOBALS ###################################################################
LOG = resource_filename('splat', 'log.splat')


class Logger(object):
    """ A collection of functions for printing formatted messages. """
    def __init__(self):
        """ Instantiate a Logger object. """
        self._pretty_log = list()
        self._clean_log = list()

    def _get_time(self):
        """
        Get a formatted str representing the current date and time.

        :return: str
        """
        return self._time_str(gmtime())

    @staticmethod
    def _time_str(time_str):
        """
        Format the given time_str into a human-readable str.

        :param time_str:
        :type time_str: time Object

        :return: str
        """
        return strftime("%Y-%m-%d %H:%M:%S", time_str)

    def print_log(self):
        """
        Print the log file for the current process/shell.

        :return:
        """
        for line in self._pretty_log:
            cprint(line[0], line[1], sys.stdout)

    @staticmethod
    def history():
        """
        Print the entire contents of the LOG file.

        :return:
        """
        with open(LOG, 'r') as f:
            for line in f.readlines():
                if '[DBG]' in line:
                    cprint(line, 'blue', file=sys.stdout)
                elif '[INF]' in line:
                    cprint(line, 'white', file=sys.stdout)
                elif '[WRN]' in line:
                    cprint(line, 'yellow', file=sys.stdout)
                elif '[ERR]' in line:
                    cprint(line, 'red', file=sys.stdout)
                elif '[OUT]' in line:
                    cprint(line, 'green', file=sys.stdout)
                elif '[GET]' in line:
                    cprint(line, 'magenta', file=sys.stdout)
                elif '[SET]' in line:
                    cprint(line, 'orange', file=sys.stdout)
                else:
                    print(line)

    def save_log(self):
        """
        Append each element in self._clean_log to the LOG file.

        :return:
        """
        with open(LOG, 'a+') as f:
            for line in self._clean_log:
                f.write(line)

    def debug(self, message):
        """
        Print a formatted version of the given message.

        Prepend the given message with the current date/time and the debug
        identifier. The prefix will be of the form: [(date/time) DBG]. The
        formatted message will be blue and print to sys.stdout.

        :param message: a message to format
        :type message: str
        :return:
        """
        message = '\r[({0}) DBG] {1}'.format(self._get_time(), message)
        self._clean_log.append(message)
        self._pretty_log.append([message, 'blue'])
        cprint(message, 'blue', file=sys.stdout)

    def info(self, message):
        """
        Print a formatted version of the given message.

        Prepend the given message with the current date/time and the info
        identifier. The prefix will be of the form: [(date/time) INF]. The
        formatted message will be white and print to sys.stdout.

        :param message: a message to format
        :type message: str
        :return:
        """
        message = '\r[({0}) INF] {1}'.format(self._get_time(), message)
        self._clean_log.append(message)
        self._pretty_log.append([message, 'white'])
        cprint(message, 'white', file=sys.stdout)

    def warn(self, message):
        """
        Print a formatted version of the given message.

        Prepend the given message with the current date/time and the warn
        identifier. The prefix will be of the form: [(date/time) WRN]. The
        formatted message will be yellow and print to sys.stderr.

        :param message: a message to format
        :type message: str
        :return:
        """
        message = '\r[({0}) WRN] {1}'.format(self._get_time(), message)
        self._clean_log.append(message)
        self._pretty_log.append([message, 'yellow'])
        cprint(message, 'yellow', file=sys.stderr)

    def error(self, message):
        """
        Print a formatted version of the given message.

        Prepend the given message with the current date/time and the error
        identifier. The prefix will be of the form: [(date/time) ERR]. The
        formatted message will be red and print to sys.stderr.

        :param message: a message to format
        :type message: str
        :return:
        """
        message = '\r[({0}) ERR] {1}'.format(self._get_time(), message)
        self._clean_log.append(message)
        self._pretty_log.append([message, 'red'])
        cprint(message, 'red', file=sys.stderr)

    def out(self, message):
        """
        Print a formatted version of the given message.

        Prepend the given message with the current date/time and the out
        identifier. The prefix will be of the form: [(date/time) OUT]. The
        formatted message will be green and print to sys.stdout.

        :param message: a message to format
        :type message: str
        :return:
        """
        message = '\r[({0}) OUT] {1}'.format(self._get_time(), message)
        self._clean_log.append(message)
        self._pretty_log.append([message, 'green'])
        cprint(message, 'green', file=sys.stdout)

    def get(self, message):
        """
        Print a formatted version of the given message.

        Prepend the given message with the current date/time and the get
        identifier. The prefix will be of the form: [(date/time) GET]. The
        formatted message will be magenta and print to sys.stdout.

        :param message: a message to format
        :type message: str
        :return:
        """
        message = '\r[({0}) GET] {1}'.format(self._get_time(), message)
        self._clean_log.append(message)
        self._pretty_log.append([message, 'magenta'])
        cprint(message, 'magenta', file=sys.stdout)

    def set(self, message):
        """
        Print a formatted version of the given message.

        Prepend the given message with the current date/time and the set
        identifier. The prefix will be of the form: [(date/time) SET]. The
        formatted message will be orange and print to sys.stdout.

        :param message: a message to format
        :type message: str
        :return:
        """
        message = '\r[({0}) SET] {1}'.format(self._get_time(), message)
        self._clean_log.append(message)
        self._pretty_log.append([message, 'orange'])
        cprint(message, 'orange', file=sys.stdout)
