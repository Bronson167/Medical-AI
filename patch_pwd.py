# patch_pwd.py
import sys
import types

# Créer un faux module pwd pour Windows
if sys.platform == "win32":
    pwd = types.ModuleType('pwd')
    
    def getpwuid(uid=None):
        """Fake getpwuid function for Windows"""
        from collections import namedtuple
        import os
        
        # Structure simulée de passwd
        passwd_entry = namedtuple('passwd_entry', 
                                 ['pw_name', 'pw_passwd', 'pw_uid', 
                                  'pw_gid', 'pw_gecos', 'pw_dir', 'pw_shell'])
        
        username = os.environ.get('USERNAME', 'unknown')
        return passwd_entry(username, 'x', 1000, 1000, '', 
                           f'C:\\Users\\{username}', 'cmd.exe')
    
    pwd.getpwuid = getpwuid
    sys.modules['pwd'] = pwd
    print("✅ Patch applied: pwd module created for Windows")