# Repo: https://github.com/kapten-kaizo/mardis
# Author: @Kang_Ehem
# Update at: 17 January 2022 23.17
import os
import sys
import re
import datetime
import types
import base64
try:
    import uncompyle6
except Exception as i:
    exit(str(i))
script_name = 'mardis'
code_marshal = base64.b64decode('JXMKaW1wb3J0IHVuY29tcHlsZTYsIHN5cwpkZWYgZGVjb21waWxlKHZlcnNpb24sIGNvZGVfb2JqZWN0LCBpbyk6CiAgICB0cnk6CiAgICAgICAgdW5jb21weWxlNi5tYWluLmRlY29tcGlsZSh2ZXJzaW9uLCBjb2RlX29iamVjdCwgaW8pCiAgICBleGNlcHQ6IHByaW50KCJkZWNvbXBpbGUgZXJvcj8iKQppZiBoYXNhdHRyKHNzLCAiY29fY29kZSIpOgogICAgZGVjb21waWxlKDIuNywgc3MsIHN5cy5zdGRvdXQpCmVsc2U6IHByaW50KHNzKQ==')
have_code = base64.b64decode('IyBEZWNvbXBpbGUgYnkgTWFyZGlzIChUb29scyBCeSBLYXB0ZW4tS2Fpem8pCiMgVGltZSBTdWNjZXMgZGVjb21waWxlIDogJXMKJXMK')
def rmbg(file_name):
    r = open(file_name).read()
    console = [line for line in r.splitlines() if not line.startswith("#")]
    timestap = str(datetime.datetime.now())
    result_code = have_code % (timestap, "\n".join(console))
    with open(file_name, mode='w') as save_dis:
        save_dis.write(result_code)
    exit("decompiling done!. saved to `%s`" % file_name)
def simpen_cok(file, string, message):
    with open(file,"w") as indihome:
        indihome.write(string)
    exit(message)
find_string_exec = lambda master_key: master_key.replace("".join(["exec",re.findall("exec(.*)",master_key)[0]]),"".join(["ss=",re.findall("exec(.*)",master_key)[0]]))
def show_info(string):
    try:
        exec(string)
    except Exception as i:
        simpen_cok(sys.argv[1],save_code,"Exception: %s"%str(i))
    if type(ss) is types.CodeType:
        print("%s: %s"%(dah_lah, str(ss)))
    else:print("%s: No Compile Module given !!"%dah_lah)
def dis(nama_file, output_file, ekse_file):
    master_key = open(nama_file).read()
    line = len([master_key.splitlines()][0])
    if master_key.count("decompile eror?")!=0:
        if os.path.exists(output_file):
            simpen_cok(output_file,save_code,"%s: Decompile error!" % script_name)
        else:exit("%s: Decompile failed!" % script_name)
    globals()["save_code"]=master_key
    if master_key.count("exec")!=0:
        if len(re.findall("exec(.*)",master_key)) > 1:
            simpen_cok(output_file,save_code,"%s: Exec string is biggest!!" % script_name)
        else:new_code = find_string_exec(master_key)
        show_info(new_code)
        open(ekse_file,"w").write(code_marshal%new_code)
        os.system("python2 %s > %s" % (ekse_file, output_file))
        if os.path.exists(ekse_file):
            os.unlink(ekse_file)
        dis(output_file, output_file, ekse_file)
    else:
        if os.path.exists(output_file):
            rmbg(output_file)
        else:exit("%s: decompile failed!. not found `exec`" % nama_file)
class Type:
    def __init__(self,code):
        self.message=str(code)
        self.co_argcount = code.co_argcount
        self.co_nlocals = code.co_nlocals
        self.co_stacksize = code.co_stacksize
        self.co_flags = code.co_flags
        self.co_code = code.co_code
        self.co_consts = code.co_consts
        self.co_names = code.co_names
        self.co_varnames = code.co_varnames
        self.co_filename = code.co_filename
        self.co_name = code.co_name
        self.co_firstlineno = code.co_firstlineno
        self.co_lnotab = code.co_lnotab
        self.co_freevars = code.co_freevars
        self.co_cellvars = code.co_cellvars
    def myasm(co):
        return types.CodeType(co.co_argcount,co.co_nlocals,co.co_stacksize,co.co_flags,co.co_code,co.co_consts,co.co_names,co.co_varnames,co.co_filename,co.co_name,co.co_firstlineno,co.co_lnotab,co.co_freevars,co.co_cellvars)
    def __repr__(self):
        return self.message
    def __str__(self):
        return self.message
def main():
    if len(sys.argv) != 2:
        exit("usage: mardis file_name.py")
    globals()['dah_lah']=sys.argv[1]
    sys.argv=[dah_lah,"code.py",".master_key"]
    print("If You Get Error Decompile, Error code saved to %s"%sys.argv[1])
    dis(*sys.argv)
if __name__ == "__main__":
    main()
# Nyari Paan Lu Gan !!