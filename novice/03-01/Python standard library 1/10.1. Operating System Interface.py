# import os
# print(os.getcwd())

# os.chdir('/server/accesslogs')   # Change current working directory
# print(os.system('mkdir today'))

# import os
# print(dir(os))
# print(help(os))

import shutil
print(shutil.copyfile('data.db', 'archive.db'))
print(shutil.move('/build/executables', 'installdir'))