#!/data/data/com.termux/files/usr/bin/python2
# Created By KangEhem!
# Name    : mardis
# Version : 2.0
# Github  : github.com/kapten-kaizo
# Dont Forget To Follow my github profile:)
#--------------------------------------------------
# Merecode Tidak Akan Membuat anda Menjadi Hebat:v
#--------------------------------------------------
import os, sys, re, datetime
from base64 import b64decode as ajg
try:
    import uncompyle6
except Exception as i:
    exit(str(i))
rg = ajg(b'JXMKaW1wb3J0IHVuY29tcHlsZTYsIHN5cwpkZWYgZGVjb21waWxlKHZlcnNpb24sIGNvZGVfb2JqZWN0LCBpbyk6CiAgICB0cnk6CiAgICAgICAgdW5jb21weWxlNi5tYWluLmRlY29tcGlsZSh2ZXJzaW9uLCBjb2RlX29iamVjdCwgaW8pCiAgICBleGNlcHQ6IHByaW50KCJkZWNvbXBpbGUgZXJvcj8iKQppZiBoYXNhdHRyKHNzLCAiY29fY29kZSIpOgogICAgZGVjb21waWxlKDIuNywgc3MsIHN5cy5zdGRvdXQpCmVsc2U6IHByaW50KHNzKQ==')
im_kaizo = ajg(b'IyBEZWNvbXBpbGUgYnkgS2FuZ0VoZW06KQojIFRpbWUgU3VjY2VzIGRlY29tcGlsZSA6ICVzCiVzCiMgTWF1IE5nYXBhaW4gQ3VrPw==')
def rmbg(file_name):
    console = []
    read_source = open(file_name).read()
    for line in read_source.splitlines():
        if not line.startswith("#"):
            console.append(line)
    timestap = str(datetime.datetime.now())
    result_code = im_kaizo % (timestap, "\n".join(console))
    with open(file_name, mode='w') as save_dis:
        save_dis.write(result_code)
    exit("decompiling done!. saved to `%s`" % file_name)
save_code = None
ezx = lambda x,y: open(x,"w").write(y)
def dis(nama_file, output_file, ekse_file):
    max_line = 20
    r = open(nama_file).read()
    globals()["save_code"]=r
    line = len([r.splitlines()][0])
    '''
    if line > max_line:
        if os.path.exists(output_file):
            rmbg(nama_file)
        else: exit("decompile error! in file %s" % nama_file)'''
    if r.count("decompile eror?")!=0:
        if os.path.exists(output_file):
            ezx(output_file, save_code)
            exit("decompile error!. code saved to %s" % output_file)
        else: exit("decompile failed!")
    if r.count("exec")!=0:
        if len(re.findall("exec(.*)",r)) > 1:
            #new_code = "".join(["ss=", find_lines(r)])
            ezx(output_file, save_code)
            exit("decompile failed, exec count > 1. code saved to %s"%output_file)
        else: new_code = r.replace("".join(["exec",re.findall("exec(.*)",r)[0]]),"".join(["ss=",re.findall("exec(.*)",r)[0]]))
        try:
            exec(new_code)
        except Exception as i:
            ezx(output_file, save_code)
            exit("error ( %s ). code saved to %s"%output_file)
            #exit("decompile eror!. code saved to %s" % output_file)
        open(ekse_file,"w").write(rg % new_code)
        if hasattr(ss,"co_code"):
            print("%s: %s"%(name_of_file, str(ss)))
        else: print("%s: No compile mode!"%name_of_file)
        os.system("python2 %s > %s" % (ekse_file, output_file))
        if os.path.exists(ekse_file):
            os.unlink(ekse_file)
        dis(output_file, output_file, ekse_file)
    else:
        if os.path.exists(output_file):
            rmbg(output_file)
        else: exit("decompile failed!. not found `exec`")
if len(sys.argv) != 2:
    exit("usage: mardis [file]")
name_of_file = sys.argv[1]
output_name = "code.py"
ekse_name = "xcode.py"
try:
    dis(name_of_file, output_name, ekse_name)
except Exception as i:
    exit("Exception: %s"%str(i))
except (KeyboardInterrupt, EOFError):
    exit()

