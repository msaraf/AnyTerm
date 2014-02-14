import sublime, sublime_plugin, subprocess

class AnyTerm():
    @staticmethod
    def get_setting(key):
        # Figure out where we are at
        at_plugin_dir = __name__.split('.')[0]
        at_plugin_home = sublime.packages_path() + '\\' + at_plugin_dir + '\\'
        # Try and get the setting out of Default.settings, otherwise reuturn built-in default
        settings = sublime.load_settings('Default.settings')
        value = settings.get(key)
        if key == 'at_terminal':
            return value if len(value) > 0 else (at_plugin_home + 'putty.exe')
        elif key == 'at_filexfer':
            return value if len(value) > 0 else (at_plugin_home + 'psftp.exe')
        elif key == 'at_server_list' :
            return value if len(value) > 0 else (at_plugin_home + 'servers.default.txt')
        else :
            print ("ERROR: get_setting, unknown key.")
            return None

    def run(self):
        self.at_server_list = open(self.get_setting('at_server_list')).read().splitlines()
        self.at_server_list = sorted(self.at_server_list, key=lambda s: s.lower())
        self.window.show_quick_panel(self.at_server_list, self.on_select)

    def on_select(self, selection):
        if selection >= 0:
            self.run_client(self.at_client, self.at_server_list[selection])

    def run_client(self, client, server):
        cmd = [client, server]
        subprocess.Popen(cmd)



class OpenTerminalCommand(sublime_plugin.WindowCommand, AnyTerm):
    def run(self):
        self.at_client = AnyTerm.get_setting('at_terminal')
        AnyTerm.run(self)



class OpenFileTransferCommand(sublime_plugin.WindowCommand, AnyTerm):
    def run(self):
        self.at_client = AnyTerm.get_setting('at_filexfer')
        AnyTerm.run(self)

