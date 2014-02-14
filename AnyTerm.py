import sublime, sublime_plugin, subprocess

class AnyTerm():
    def run(self):
        self.at_server_list = open(sublime.packages_path() + '\\AnyTerm' + '\\servers.txt').read().splitlines()
        self.at_server_list = sorted(self.at_server_list, key=lambda s: s.lower())
        self.window.show_quick_panel(self.at_server_list, self.on_select)

    def on_select(self, selection):
        print("CLIENT: " + self.at_client)
        if selection >= 0:
            self.run_client(self.at_client, self.at_server_list[selection])

    def run_client(self, client, server):
        cmd = [client, server]
        subprocess.Popen(cmd)



class OpenTerminalCommand(sublime_plugin.WindowCommand, AnyTerm):
    def run(self):
        self.at_client = "C:\\Program Files\\VanDyke Software\\Clients\\SecureCRT.exe"
        AnyTerm.run(self)



class OpenFileTransferCommand(sublime_plugin.WindowCommand, AnyTerm):
    def run(self):
        self.at_client = "C:\\Program Files\\VanDyke Software\\Clients\\SecureFX.exe"
        AnyTerm.run(self)



