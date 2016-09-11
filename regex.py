# -*- coding: utf-8 -*-
"""Regex methods to find item into text"""

import re

from item import *

# Regex definition #
# devra être viré

regex_def = {
HEAD:'^#+ '

    #"regClsPython": "^[ \t]*class[^\\w\

    #"regFuncPython": "^[ \t]*def[^\\w\\d_].*?:.*",

    #"regClsAndFuncPython": "^[ \t]*((?:class|def)[^\\w\\d_].*?:.*$)"

} # end regex dico


def get_regex(markup_type):

    return regex_def

# end def


def compile_regex(regex):

     # creating dico for compiled regex
     regex_compiled = {}
     for item, regexText in regex.items():
         regex_compiled[item] = re.compile(regexText, re.MULTILINE)
     # end for
     return regex_compiled
# end def