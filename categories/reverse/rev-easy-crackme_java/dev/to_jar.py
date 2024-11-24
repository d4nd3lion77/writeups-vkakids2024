import os
import subprocess
import shutil

base_folder = "task.java.b1d2c96c.ARCHIVE"
for i in range(1, 1001):
    folder_path = os.path.join(base_folder, str(i))
    check_class_path = os.path.join(folder_path, "Check.class")
    jar_file_path = os.path.join(folder_path, "task.jar")
    manifest_path = os.path.join(folder_path, "MANIFEST.MF")
    if os.path.isfile(check_class_path):
        try:
            with open(manifest_path, "w") as manifest_file:
                manifest_file.write("Main-Class: Check\n")
            subprocess.run([
                "jar", "cmf", manifest_path, jar_file_path, "-C", folder_path, "Check.class"
            ], check=True)
            os.remove(check_class_path)
            os.remove(manifest_path)
        except subprocess.CalledProcessError:
            print(f"Ошибка при создании JAR файла в папке {folder_path}")
        except Exception as e:
            print(f"Ошибка: {e}")
    else:
        print(f"Check.class не найден в папке {folder_path}")
shutil.make_archive(base_folder, 'zip', base_folder)
