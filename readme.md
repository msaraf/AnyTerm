# ** AnyTerm **

### ** Installation **

#### ** Clone from GitHub  **
    git clone https://github.com/msaraf/AnyTerm.git

### ** Usage **

`Default.settings` by default:  
- at_terminal : Runs ${PLUGIN_HOME}/putty.exe [servername]  
- at_filexfer : Runs ${PLUGIN_HOME}/psftp.exe [servername]  
- at_server_list : ${PLUGIN_HOME}/servers.default.txt provides the list of servers to pick from  

`Default.sublime-keymap` by default binds:  
- ["ctrl+shift+t"] to launch a terminal  
- ["ctrl+alt+t"] to launch file transfer  

### ** Todo **
- Use default settings instead of hard coded paths
- Create default servers.default.txt
- Test with putty and psftp
- Finish readme {Install, Usage}

### ** License **

All of AnyTerm is licensed under the MIT License.

Copyright (c) 2014 Mike Saraf &lt;<github@mikesaraf.com>&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
