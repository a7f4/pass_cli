# -*- encoding: utf-8 -*-

"""
CLI interface for pass.

:Copyright: © 2019, Aleksandr Block.
:License: BSD (see /LICENSE).
"""

import os
import sys

import urwid as ui

__all__ = ('main', 'App')


# h/t Heiko Noordhof @hkoof
class FancyListBox(ui.ListBox):
    """A list box you can scroll in fancy ways."""

    def keypress(self, size, key):
        """Handle keypresses."""
        currentfocus = self.focus_position
        maxindex = len(self.body) - 1
        newfocus = None
        if key == 'home':
            newfocus = 0
        elif key == 'end':
            newfocus = maxindex
        elif key == 'k' and self._app.mode not in ('search', 'generate'):
            newfocus = currentfocus - 1
        elif key == 'j' and self._app.mode not in ('search', 'generate'):
            newfocus = currentfocus + 1
        if newfocus is not None:
            if newfocus < 0:
                newfocus = 0
            elif newfocus > maxindex:
                newfocus = maxindex
            self.set_focus(newfocus)
        return super(FancyListBox, self).keypress(size, key)

    def mouse_event(self, size, event, button, col, row, focus):
        """Handle scroll events."""
        currentfocus = self.focus_position
        newfocus = None
        maxindex = len(self.body) - 1

        if button == 4:
            newfocus = currentfocus - 3
        elif button == 5:
            newfocus = currentfocus + 3

        if newfocus is not None:
            if newfocus < 0:
                newfocus = 0
            elif newfocus > maxindex:
                newfocus = maxindex

            self.set_focus(newfocus)

        # handle clicks
        return super(FancyListBox, self).mouse_event(
            size, event, button, col, row, focus)


class App:
    def __init__(self, config):
        self.header = ui.AttrWrap(ui.Text(f"pass-cli v{pass_cli.__version__}"), 'header')
        listbox_content = ui.SimpleFocusListWalker([ui.Text('Loading')])
        self.box = FancyListBox(listbox_content)
        self.box._app = self

        column_data = [
            ui.Button('Help', self.help),
            ui.Button('Quit', self.quit),
        ]
        column_data = [ui.AttrWrap(i, 'footer', 'footer_reversed') for i in column_data]

        self.footer = ui.Columns(column_data)
        self.frame = ui.Frame(self.box, header=self.header,
                              footer=self.footer)

        self.loop = ui.MainLoop(self.frame)

    def help(self, originator):
        pass

    def quit(self, originator):
        """Quit the program."""
        raise ui.ExitMainLoop()

    def run(self):
        self.loop.run()


def main():
    App(pass_cli.config).run()


if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import pass_cli

    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("Bye!")
