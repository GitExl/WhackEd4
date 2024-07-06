import re

subs = re.compile(r'wx\.Size\(.+?\)')

with open('src/whacked4/ui/windows.py', 'r') as f:
    lines = f.readlines()

with open('src/whacked4/ui/windows.py', 'w') as f:
    for line in lines:
        if line.startswith('		wx.MDIParentFrame.__init__'):
            pass
        elif line.startswith('		wx.MDIChildFrame.__init__') or line.startswith('		wx.Dialog.__init__'):
            line = subs.sub(r'parent.FromDIP( \g<0> )', line)
        else:
            line = subs.sub(r'self.FromDIP( \g<0> )', line)

        f.write(line)
