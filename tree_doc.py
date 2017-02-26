# -*- coding: utf-8 -*-

from sixpad import window as win
import qc6paddlgs


class TreeDoc:
    def __init__(self, mul):
        self.mul = mul
        self.value = qc6paddlgs.TreeViewDialog.open(
            title = 'Arborescence du document',
            #hint = 'Text d'aide',
            # If modal is set to True,, tree is a window. 
            modal = True,
            #modal = False,
            multiple = False,
            editable = False,
            #okButtonText = '',
            #cancelButtonText = '',
            callback = self.fill_tree)
        
    def fill_tree(self, tree):
        """Callback function call when opening tree dialog"""
        root = tree.root
        # Parse all document line by line
        h1 = root.appendChild('Mathieu', 'Barbe',selected=False, expanded=False)
        h11 = h1.appendChild('Raph', 'Barbe',selected=False, expanded=False)
        h1.insertBefore(h11, 'test', 'value')



TreeDoc('test mul')