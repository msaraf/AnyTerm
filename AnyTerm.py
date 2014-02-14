import sublime, sublime_plugin

class OpenTerminalCommand(sublime_plugin.WindowCommand):
    def run(self):
        print("Hello World")
