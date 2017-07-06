#!/usr/bin/env python

""" Provides an interface to view and update configuration settings. """

__author__ = "Benjamin S. Meyers"
__copyright__ = "Copyright 2015-2017, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__version__ = "1.0.0"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "ben@splat-library.org"
__status__ = "Development"

#### IMPORTS ###################################################################
import json
import multiprocessing
import os
import re

from splat import FIXES_EN, LOGGER, SUPPORTED_LANGS
from splat.corpora import StopWords


class Configuration(object):
    def __init__(self, name):
        """
        Instantiate a Configuration object with the default settings.

        :param name: a name for this configuration
        :type name: str
        """
        self.name = name

        self._language = "English"
        self._threads = 1
        self._recalculate = True
        self._serialize = True

        self._punctuation = [".", ",", "!", "?", ":", ";"]
        self._quotes = ["\"", "'", "`"]
        self._symbols = ["@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "=",
                         "|", "\\", "/", "~"]
        self._brackets = ["(", ")", "[", "]", "{", "}", "<", ">"]
        self._stopwords = StopWords(self._language.lower())
        self._token_fixes = dict()
        if self._language.lower() in ['english']:
            self._token_fixes = FIXES_EN

        self._fix_tokens = False

        self._strip_punctuation = False
        self._strip_quotes = False
        self._strip_symbols = False
        self._strip_brackets = False
        self._strip_stopwords = False
        
        self._split_punctuation = True
        self._split_quotes = False
        self._split_symbols = False
        self._split_brackets = False
        self._split_apostrophes = False
        
        self._case = "preserve"

        self._parser = "Berkeley"
        self._corenlp_url = None

    #### IMPORT/EXPORT ####
    def import_config(self, filename):
        """
        Load an existing configuration.

        :param filename:
        :type filename: str
        :return:
        """
        self.load(filename)

    def export_config(self):
        """
        Save the current configuration.
        
        :return: 
        """
        self.dump()

    #### CONFIGURATION NAME ####
    def _get_name(self):
        """
        Get the current value of self.name.
        
        :return: str
        """
        LOGGER.get("'name': '{0}'".format(self.name))
        return self.name

    def _set_name(self, n):
        """
        Update the value of self.name.
        
        :param n:
        :type n: str
        :return: 
        """
        self.name = n
        LOGGER.set("'name': '{0}'".format(self.name))

    name = property(fget=_get_name, fset=_set_name,
                    doc="The name of the current configuration.")

    #### LANGUAGE ####
    def _get_language(self):
        """
        Get the current value of self._language.

        :return: str
        """
        LOGGER.get("'language': '{0}'".format(self._language))
        return self._language

    def _set_language(self, l, update_stopwords=True):
        """
        Update the value of self._language.

        :param l: the name of a supported natural language
        :type l: str
        :param update_stopwords:
        :type update_stopwords: bool
        :return:
        """
        if l.lower() in SUPPORTED_LANGS:
            self._language = l.lower()
            LOGGER.set("'language': '{0}'".format(self._language))
            if update_stopwords:
                self._set_stopwords(self._language.lower())
        else:
            LOGGER.warn(
                "The value of 'language' must be one of the following: {0}."
                .format(str(SUPPORTED_LANGS)))

    language = property(fget=_get_language, fset=_set_language,
                        doc="The natural language associated with the current "
                            "configuration of SPLAT.")

    #### THREADS ####
    def _get_threads(self):
        """
        Get the current value of self._threads.

        :return: int
        """
        LOGGER.get("'threads': '{0}'".format(self._threads))
        return self._threads

    def _set_threads(self, t):
        """
        Update the value of self._threads.

        :param t: number of threads
        :type t: int
        :return:
        """
        if t <= multiprocessing.cpu_count():
            self._threads = t
            LOGGER.set("'threads': '{0}'".format(self._threads))            
        else:
            LOGGER.warn(
                "Your current system only has {0} cores available.".format(
                    multiprocessing.cpu_count()))

    threads = property(fget=_get_threads, fset=_set_threads,
                       doc="The number of threads to use for functions that "
                           "support multithreading.")

    #### RECALCULATE ####
    def _get_recalculate(self):
        """
        Get the current value of self._recalculate.

        :return: bool
        """
        LOGGER.get("'recalculate': '{0}'".format(self._recalculate))
        return self._recalculate
    
    def _set_recalculate(self, r):
        """
        Update the value of self._recalculate.

        :param r:
        :type r: bool
        :return:
        """
        if type(r) == bool:
            self._recalculate = r
            LOGGER.set("'recalculate': '{0}'".format(self._recalculate))
        else:
            LOGGER.warn(
                "'recalculate' must be of type bool, not {0}.".format(type(r)))

    recalculate = property(fget=_get_recalculate, fset=_set_recalculate,
                           doc="If 'True', features will be recalculated each "
                               "time they are accessed.")
    
    #### SERIALIZE ####
    def _get_serialize(self):
        """
        Get the current value of self._serialize.

        :return: bool
        """
        LOGGER.get("'serialize': '{0}'".format(self._serialize))
        return self._serialize
    
    def _set_serialize(self, s):
        """
        Update the value of self._serialize.

        :param s:
        :type s: bool
        :return:
        """
        if type(s) == bool:
            self._serialize = s
            LOGGER.set("'serialize': '{0}'.".format(self._serialize))
        else:
            LOGGER.warn(
                "'serialize' must be of type bool, not {0}.".format(type(s)))

    serialize = property(fget=_get_serialize, fset=_set_serialize,
                         doc="If 'True', SPLAT objects will be serialized and "
                             "saved to disk for access later.")
    
    #### PUNCTUATION ####
    def _get_punctuation(self):
        """
        Get the current value of self._punctuation.

        :return: list
        """
        LOGGER.get("'punctuation: '{0}'".format(self._punctuation))
        return self._punctuation
    
    def _set_punctuation(self, p):
        """
        Update the value of self._punctuation.

        :param p: punctuation characters
        :type p: list
        :return:
        """
        self._punctuation = p
        LOGGER.set("'punctuation': '{0}".format(self._punctuation))

    punctuation = property(fget=_get_punctuation, fset=_set_punctuation,
                           doc="A list of characters that the current "
                               "configuration is treating as punctuation.")
    
    #### QUOTES ####
    def _get_quotes(self):
        """
        Get the current value of self._quotes.

        :return: list
        """
        LOGGER.get("'quotes: '{0}'".format(self._quotes))
        return self._quotes
    
    def _set_quotes(self, q):
        """
        Update the value of self._quotes.

        :param q: quote characters
        :type q: list
        :return:
        """
        self._quotes = q
        LOGGER.set("'quotes': '{0}".format(self._quotes))
        
    quotes = property(fget=_get_quotes, fset=_set_quotes,
                      doc="A list of characters that the current configuration "
                          "is treating as quotes.")
    
    #### SYMBOLS ####
    def _get_symbols(self):
        """
        Get the current value of self._symbols.

        :return: list
        """
        LOGGER.get("'symbols: '{0}'".format(self._symbols))
        return self._symbols
    
    def _set_symbols(self, s):
        """
        Update the value of self._symbols.

        :param s: symbol characters
        :type s: list
        :return:
        """
        self._symbols = s
        LOGGER.set("'symbols': '{0}".format(self._symbols))

    symbols = property(fget=_get_symbols, fset=_set_symbols,
                       doc="A list of characters that the current configuration"
                           " is treating as symbols (special characters).")
    
    #### BRACKETS ####
    def _get_brackets(self):
        """
        Get the current value of self._brackets.

        :return: list
        """
        LOGGER.get("'brackets: '{0}'".format(self._brackets))
        return self._brackets
    
    def _set_brackets(self, b):
        """
        Update the value of self._brackets.

        :param b: bracket characters
        :type b: list
        :return:
        """
        self._brackets = b
        LOGGER.set("'brackets': '{0}".format(self._brackets))

    brackets = property(fget=_get_brackets, fset=_set_brackets,
                        doc="A list of characters that the current "
                            "configuration is treating as brackets.")

    #### STOPWORDS ####
    def _get_stopwords(self):
        """
        Get the current value of self._stopwords.

        :return: list
        """
        LOGGER.get("'stopwords: '{0}'".format(self._stopwords))
        return self._stopwords

    def _set_stopwords(self, s):
        """
        Update the value of self._stopwords.

        :param s: stopwords
        :type s: list
        :return:
        """
        self._stopwords = StopWords(s)
        LOGGER.set("'stopwords': '{0}".format(self._stopwords))

    stopwords = property(fget=_get_stopwords, fset=_set_stopwords,
                         doc="A list of words that the current configuration is"
                             " treating as stopwords.\n\nStopwords are common "
                             "words within a language that are typically "
                             "ignored for certain calculations, such as "
                             "type-token-ratio.")
    
    #### TOKEN FIXES ####
    def _get_token_fixes(self):
        """
        Get the current value of self._token_fixes.

        :return: dict
        """
        LOGGER.get("'token_fixes: '{0}'".format(self._token_fixes))
        return self._token_fixes

    def _set_token_fixes(self, t):
        """
        Update the value of self._token_fixes.

        :param t: token_fixes
        :type t: dict
        :return:
        """
        if type(t) == dict:
            types = [str(type(y)) for y in list(t.keys()) + list(t.values())]
            if list(set(types)) == ['str']:
                self._token_fixes = t
                LOGGER.set("'token_fixes': '{0}".format(self._token_fixes))
            else:
                LOGGER.error("Input dict has malformed keys and/or values.")
        else:
            LOGGER.warn("'token_fixes' must be of type 'dict', not '{0}'."
                        .format(type(t)))

    token_fixes = property(fget=_get_token_fixes, fset=_set_token_fixes,
                         doc="A dictionary of token keys and replacement values"
                             " to be used when the 'fix_tokens' property is "
                             "'True'.")
    
    #### FIX TOKENS ####
    def _get_fix_tokens(self):
        """
        Get the current value of self._fix_tokens.
        
        :return: bool 
        """
        if self._language.lower() not in ['english']:
            LOGGER.warn("The property 'fix_tokens' has not been implemented for"
                        " the '{0}' language yet. In order to use this "
                        "functionality, you must set the 'token_fixes' "
                        "property.".format(self._language))
        LOGGER.get("'fix_tokens': {0}".format(self._fix_tokens))
        return self._fix_tokens
    
    def _set_fix_tokens(self, f):
        """
        Update the value of self._fix_tokens.
        
        :param f:
        :type f: bool
        :return: 
        """
        if self._language.lower() not in SUPPORTED_LANGS:
            LOGGER.warn("The property 'fix_tokens' has not been implemented for"
                        " the '{0}' language yet. In order to use this "
                        "functionality, you must set the 'token_fixes' "
                        "property.".format(self._language))
        if type(f) == bool:
            self._fix_tokens = f
            LOGGER.set("'fix_tokens': {0}".format(self._fix_tokens))
        else:
            LOGGER.warn("'fix_tokens' must be of type bool, not {0}."
                        .format(type(f)))
        
    fix_tokens = property(fget=_get_fix_tokens, fset=_set_fix_tokens,
                          doc="If 'True' (and supported), the 'token_fixes' "
                              "property will be used to replace specified "
                              "tokens with predefined values.")

    #### STRIP PUNCTUATION ####
    def _get_strip_punctuation(self):
        """
        Get the current value of self._strip_punctuation.

        :return: bool
        """
        LOGGER.get("'strip_punctuation': '{0}'".format(self._strip_punctuation))
        return self._strip_punctuation
    
    def _set_strip_punctuation(self, p):
        """
        Update the value of self._strip_punctuation.

        :param p:
        :type p: bool
        :return:
        """
        if type(p) == bool:
            self._strip_punctuation = p
            LOGGER.set("'strip_punctuation': '{0}'"
                       .format(self._strip_punctuation))
        else:
            LOGGER.warn("'strip_punctuation' must be of type bool, not {0}."
                        .format(type(p)))

    strip_punctuation = property(fget=_get_strip_punctuation,
                                 fset=_set_strip_punctuation,
                                 doc="If 'True', punctuation will be removed "
                                     "during preprocessing.\n\nPunctuation is "
                                     "defined in the 'punctuation' property.")

    #### STRIP QUOTES ####
    def _get_strip_quotes(self):
        """
        Get the current value of self._strip_quotes.

        :return: bool
        """
        LOGGER.get("'strip_quotes': '{0}'".format(self._strip_quotes))
        return self._strip_quotes
    
    def _set_strip_quotes(self, q):
        """
        Update the value of self._strip_quotes.

        :param q:
        :type q: bool
        :return:
        """
        if type(q) == bool:
            self._strip_quotes = q
            LOGGER.set("'strip_quotes': '{0}'".format(self._strip_quotes))
        else:
            LOGGER.warn("'strip_quotes' must be of type bool, not {0}."
                        .format(type(q)))

    strip_quotes = property(fget=_get_strip_quotes, fset=_set_strip_quotes,
                            doc="If 'True', quotes will be removed during "
                                "preprocessing.\n\nQuotes are defined in the "
                                "'quotes' property.")
    
    #### STRIP SYMBOLS ####
    def _get_strip_symbols(self):
        """
        Get the current value of self._strip_symbols.

        :return: bool
        """
        LOGGER.get("'strip_symbols': '{0}'".format(self._strip_symbols))
        return self._strip_symbols
    
    def _set_strip_symbols(self, s):
        """
        Update the value of self._strip_symbols.

        :param s:
        :type s: bool
        :return:
        """
        if type(s) == bool:
            self._strip_symbols = s
            LOGGER.set("'strip_symbols': '{0}'".format(self._strip_symbols))
        else:
            LOGGER.warn("'strip_symbols' must be of type bool, not {0}."
                        .format(type(s)))

    strip_symbols = property(fget=_get_strip_symbols, fset=_set_strip_symbols,
                             doc="If 'True', symbols will be removed during "
                                 "preprocessing.\n\nSymbols are defined in the "
                                 "'symbols' property.")
    
    #### STRIP BRACKETS ####
    def _get_strip_brackets(self):
        """
        Get the current value of self._strip_brackets.

        :return: bool
        """
        LOGGER.get("'strip_brackets': '{0}'".format(self._strip_brackets))
        return self._strip_brackets
    
    def _set_strip_brackets(self, b):
        """
        Update the value of self._strip_brackets.

        :param b:
        :type b: bool
        :return:
        """
        if type(b) == bool:
            self._strip_brackets = b
            LOGGER.set("'strip_brackets': '{0}'".format(self._strip_brackets))
        else:
            LOGGER.warn("'strip_brackets' must be of type bool, not {0}."
                        .format(type(b)))

    strip_brackets = property(fget=_get_strip_brackets,
                              fset=_set_strip_brackets,
                              doc="If 'True', brackets will be removed during "
                                  "preprocessing.\n\nBrackets are defined in "
                                  "the 'brackets' property.")

    #### STRIP STOPWORDS ####
    def _get_strip_stopwords(self):
        """
        Get the current value of self._strip_stopwords.

        :return: bool
        """
        LOGGER.get("'strip_stopwords': '{0}'".format(self._strip_stopwords))
        return self._strip_stopwords

    def _set_strip_stopwords(self, s):
        """
        Update the value of self._strip_stopwords.

        :param s:
        :type s: bool
        :return:
        """
        if type(s) == bool:
            self._strip_stopwords = s
            LOGGER.set("'strip_stopwords': '{0}'".format(self._strip_stopwords))
        else:
            LOGGER.warn("'strip_stopwords' must be of type bool, not {0}."
                        .format(type(s)))

    strip_stopwords = property(fget=_get_strip_stopwords,
                              fset=_set_strip_stopwords,
                              doc="If 'True', stopwords will be removed during "
                                  "preprocessing.\n\nStopwords are defined in "
                                  "the 'stopwords' property.")
    
    #### SPLIT PUNCTUATION ####
    def _get_split_punctuation(self):
        """
        Get the current value of self._split_punctuation.

        :return: bool
        """
        LOGGER.get("'split_punctuation': '{0}'".format(self._split_punctuation))
        return self._split_punctuation
    
    def _set_split_punctuation(self, p):
        """
        Update the value of self._split_punctuation.

        :param p:
        :type p: bool
        :return:
        """
        if type(p) == bool:
            self._split_punctuation = p
            LOGGER.set("'split_punctuation': '{0}'"
                       .format(self._split_punctuation))
        else:
            LOGGER.warn("'split_punctuation' must be of type bool, not {0}."
                        .format(type(p)))

    split_punctuation = property(fget=_get_split_punctuation,
                                 fset=_set_split_punctuation,
                                 doc="If 'True', punctuation will be treated "
                                     "as separate tokens during tokenization."
                                     "\n\nIf the 'strip_punctuation' property "
                                     "is 'True', this setting is ignored.")

    #### SPLIT QUOTES ####
    def _get_split_quotes(self):
        """
        Get the current value of self._split_quotes.

        :return: bool
        """
        LOGGER.get("'split_quotes': '{0}'".format(self._split_quotes))
        return self._split_quotes
    
    def _set_split_quotes(self, q):
        """
        Update the value of self._split_quotes.

        :param q:
        :type q: bool
        :return:
        """
        if type(q) == bool:
            self._split_quotes = q
            LOGGER.set("'split_quotes': '{0}'".format(self._split_quotes))
        else:
            LOGGER.warn("'split_quotes' must be of type bool, not {0}."
                        .format(type(q)))

    split_quotes = property(fget=_get_split_quotes, fset=_set_split_quotes,
                            doc="If 'True', quotes will be treated as separate "
                                "tokens during tokenization.\n\nIf the "
                                "'strip_quotes' property is 'True', this "
                                "setting is ignored.")
    
    #### SPLIT SYMBOLS ####
    def _get_split_symbols(self):
        """
        Get the current value of self._split_symbols.

        :return: bool
        """
        LOGGER.get("'split_symbols': '{0}'".format(self._split_symbols))
        return self._split_symbols
    
    def _set_split_symbols(self, s):
        """
        Update the value of self._split_symbols.

        :param s:
        :type s: bool
        :return:
        """
        if type(s) == bool:
            self._split_symbols = s
            LOGGER.set("'split_symbols': '{0}'".format(self._split_symbols))
        else:
            LOGGER.warn("'split_symbols' must be of type bool, not {0}."
                        .format(type(s)))

    split_symbols = property(fget=_get_split_symbols, fset=_set_split_symbols,
                             doc="If 'True', symbols will be treated as "
                                 "separate tokens during tokenization.\n\n"
                                 "If the 'strip_symbols' property is 'True', "
                                 "this setting is ignored.")
    
    #### SPLIT BRACKETS ####
    def _get_split_brackets(self):
        """
        Get the current value of self._split_brackets.

        :return: bool
        """
        LOGGER.get("'split_brackets': '{0}'".format(self._split_brackets))
        return self._split_brackets
    
    def _set_split_brackets(self, b):
        """
        Update the value of self._split_brackets.

        :param b:
        :type b: bool
        :return:
        """
        if type(b) == bool:
            self._split_brackets = b
            LOGGER.set("'split_brackets': '{0}'".format(self._split_brackets))
        else:
            LOGGER.warn("'split_brackets' must be of type bool, not {0}."
                        .format(type(b)))

    split_brackets = property(fget=_get_split_brackets,
                              fset=_set_split_brackets,
                              doc="If 'True', brackets will be treated as "
                                  "separate tokens during tokenization.\n\n"
                                  "If the 'strip_brackets' property is 'True', "
                                  "this setting is ignored.")

    #### SPLIT APOSTROPHES ####
    def _get_split_apostrophes(self):
        """
        Get the current value of self._split_apostrophes.

        :return: bool
        """
        LOGGER.get("'split_apostrophes': '{0}'".format(self._split_apostrophes))
        return self._split_apostrophes
    
    def _set_split_apostrophes(self, a):
        """
        Update the value of self._split_apostrophes.

        :param a:
        :type a: bool
        :return:
        """
        if type(a) == bool:
            self._split_apostrophes = a
            LOGGER.set("'split_apostrophes': '{0}'".format(self._split_apostrophes))
        else:
            LOGGER.warn("'split_apostrophes' must be of type bool, not {0}."
                        .format(type(a)))

    split_apostrophes = property(fget=_get_split_apostrophes,
                              fset=_set_split_apostrophes,
                              doc="If 'True', apostrophes will be treated as "
                                  "separate tokens during tokenization.")                                

    #### CASE ####
    def _get_case(self):
        """
        Get the current value of self._case

        :return: str
        """
        LOGGER.get("'case': '{0]'".format(self._case))
        return self._case

    def _set_case(self, c):
        """
        Update the value of self._case.

        :param c: one of 'preserve', 'lower', or 'upper'
        :type: str
        :return:
        """
        if c not in ['preserve', 'lower', 'upper']:
            LOGGER.warn("'case' must be one of the following: 'preserve', "
                        "'lower', 'upper'.")
        else:
            self._case = c
            LOGGER.set("'case': '{0}'".format(self._case))

    case = property(fget=_get_case, fset=_set_case,
                    doc="If 'lower' or 'upper', the original text will be "
                        "converted to all lowercase or uppercase, respectively,"
                        " during preprocessing.")

    #### PARSER ####
    def _get_parser(self):
        """
        Get the current value of self._default_parser.

        :return: str
        """
        LOGGER.get("'default_parser': '{0]'".format(self._parser))
        return self._parser

    def _set_parser(self, d):
        """
        Update the value of self._default_parser.

        :param d: one of 'CoreNLP' or 'Berkeley'
        :type d: str
        :return:
        """
        if d not in ['CoreNLP', 'Berkeley']:
            LOGGER.warn("'default_parser' must be one of the following: "
                        "'CoreNLP', or 'Berkeley'.")
        else:
            self._parser = d
            LOGGER.set("'default_parser': '{0}'".format(self._parser))

    parser = property(fget=_get_parser, fset=_set_parser,
                      doc="The parser to be used by the current configuration."
                          "\n\nIf 'CoreNLP', the 'corenlp_url' property must be"
                          " set.")

    def get_corenlp_url(self):
        """
        Get the current value of self._corenlp_url.
        
        :return: 
        """
        LOGGER.get("'corenlp_url': '{0}'".format(self._corenlp_url))
        return self._corenlp_url

    def set_corenlp_url(self, url):
        """
        Update the value of self._corenlp_url.
        
        :param url:
        :type url: str
        :return: 
        """
        if not re.match(r'https?://', url):
            url = 'http://' + url

        self._corenlp_url = url
        LOGGER.set("'corenlp_url': '{0}'".format(self._corenlp_url))

    corenlp_url = property(fget=get_corenlp_url, fset=set_corenlp_url,
                           doc="The URL of a running CoreNLP server.")

    #### SERIALIZATION ####
    def dump(self):
        """
        Serialize the current Configuration object and save to disk.
        
        :return: 
        """
        if os.path.exists(self.name + ".splat.conf"):
            response = ""
            prompt = True
            while prompt:
                response = input("Configuration '{0}' already exists in the "
                                 "current directory. Would you like to replace"
                                 " it? (Yn) "
                                 .format(self.name + ".splat.conf"))
                if response in ['yes', 'Yes', 'y', 'Y', 'no', 'No', 'n', 'No']:
                    prompt = False
                else:
                    print("Sorry, I don't know what '{0}' means.\n"
                          .format(response))

            if response in ['yes', 'Yes', 'y', 'Y']:
                json.dump(self.__dict__, self.name + ".splat.conf")
                LOGGER.out("Exported configuration '{0}' to disk in current "
                           "directory as '{0}.splat.conf'.".format(self.name))
            else:
                LOGGER.warn("Exporting of Configuration '{0}' has been aborted."
                            .format(self.name))
        else:
            json.dump(self.__dict__, self.name + ".splat.conf")
            LOGGER.out("Exported configuration '{0}' to disk in current "
                       "directory as '{0}.splat.conf'.".format(self.name))

    def load(self, filename):
        """
        De-Serialize the Configuration object with the given filename.

        :param filename:
        :type filename: str
        :return: 
        """
        if not os.path.exists(filename):
            LOGGER.warn("Importing configuration failed. '{0}' does not exist."
                        .format(filename))
        else:
            self.__dict__ = json.load(filename)
            LOGGER.out("Imported configuration '{0}' from file '{1}. "
                       .format(self.name, filename))
