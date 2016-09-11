# -*- coding:utf-8 -*-
"""Functions to go to item"""

from item import *

class Goto():
    def __init__(self, sp, regex_compiled):
        self.regex_compiled = regex_compiled
        self.sp = sp
        
    def next_item(self, item_type):
        """Go to the next item
        item_type: int
        return true if item found or false if not.
        """
        
        # Get current line (+1  fixe 6pad++ bug)
        line = self.sp.window.curPage.curLine+1
        # test each line
        
        while line < self.sp.window.curPage.lineCount:
            line_text = self.sp.window.curPage.line(line)
            line += 1
            # test this line with regex
            if self.regex_compiled[item_type].match(line_text):
                # regex found item, go to this line
                self.sp.window.curPage.curLine = line
                # say this line heading 
                self.sp.say(line_text, True)
                return True
            # end if
        # end while
        # Item not found, bip and return False
        self.sp.window.messageBeep(0)
        return False
        # end def
        