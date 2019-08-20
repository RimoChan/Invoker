import os
import tempfile


f = tempfile.NamedTemporaryFile(delete=False)
b = 'import os;os.system(\'\""./python36/python\"" -m invoker.py\');os.system("pause")'.encode('utf8')
f.write(b)
f.close()
os.system(f'pyinstaller {f.name} --name invoker.exe --distpath ./ -F -i ./html/Invoke_icon.ico')
