#!/bin/python
import os
os.system("pwd")
# exit(0)
base_dir = '/mnt/c/Users/Пользователь/Desktop/Git_repos/vkakids2024/rev-meduim-pdf_js/deploy/sourсe.js.411265f9.ARCHIVE'
for i in range(1, 1001):
    dir_path = os.path.join(base_dir, str(i))
    pdf_path = os.path.join(dir_path, 'task.pdf')
    # print(pdf_path)
    archive_name = os.path.join(dir_path, 'task.tar.gz')
    os.system(f"tar -xvzf {archive_name} -C {dir_path}")
    os.system(f'rm {archive_name}')


#/mnt/c/Users/Пользователь/Desktop/Git_repos/vkakids2024/rev-meduim-pdf_js/dev/source.js.411265f9.ARCHIVE/1

#/mnt/c/Users/Пользователь/Desktop/Git_repos/vkakids2024/rev-meduim-pdf_js/dev/source.js.411265f9.ARCHIVE/1
#
