# -*- coding:utf-8 -*-
"""Functions to go to item"""

from item import *

class Goto():
    def __init__(self, sp, regex_compiled):
        self.regex_compiled = regex_compiled
        self.sp = sp
        
    # end def
    
    def next_item(self, item_type):
        """Go to the next item
        item_type: int
        return true if item found or false if not.
        """
        
        # Get current line, note that  first line is 0
        line = self.sp.window.curPage.curLine
        # First test with next line
        line += 1
        
        # test each line
        while line < self.sp.window.curPage.lineCount:
            # Fetch text on this line.
            line_text = self.sp.window.curPage.line(line)
            # test this line with regex
            if self.regex_compiled[item_type].match(line_text):
                # regex found item, go to this line
                self.sp.window.curPage.curLine = line
                # say this line heading 
                self.sp.say(line_text, True)
                return True
            # end if
            # increment line for next loop
            line += 1
        # end while
        # Item not found, bip and return False
        self.sp.window.messageBeep(0)
        return False
        
    # end def
    
    def previous_item(self, item_type):
        """Go to the previous item
        item_type: int
        return true if item found or false if not.
        """
        
        # Get current line, note that line number start from 0. 
        line = self.sp.window.curPage.curLine
        # First test on the previous line
        line -= 1
        
        # test each line
        while line >= 0:
            line_text = self.sp.window.curPage.line(line)
            # test this line with regex
            if self.regex_compiled[item_type].match(line_text):
                # regex found item, go to this line
                self.sp.window.curPage.curLine = line
                # say this line heading 
                self.sp.say(line_text, True)
                return True
            # end if
            # Decrement line number to test previous line
            line -= 1
        # end while
        # Item not found, making bip and return False
        self.sp.window.messageBeep(0)
        return False
    # end def
    
# end class
