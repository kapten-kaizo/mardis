# Repo: https://github.com/kapten-kaizo/mardis
# Author: @Kang_Ehem
# Update at: 22 Jun 2024 18.42

import sys, re
from StringIO import StringIO
from uncompyle6.main import decompile

script_name = 'mardis'
version = "3.0"
mardis_error_decompile = "#mardis execution encountered an error!!!"

def try_decompile(code_obj):
	if isco(code_obj) == False:
		return code_obj
	paper = StringIO()
	try:
		decompile(None, code_obj, paper)
		return paper.getvalue()
	except Exception as err:
		return mardis_error_decompile

def save_code(file, string):
	open(file, "w").write(
		string
	)

def _parse(source):
	regex = re.findall("exec(.*)", source)
	amount = len(regex)
	if amount == 0:
		return 4, 0, 4
	_backup = source
	default = {}
	listv = []
	for i, value in enumerate(regex):
		listv.append("try:\n\tmardis_execute_list.append(mardis_execute%d)\nexcept Exception:\n\terr += 1" % (i))
		key = "exec" + value
		replace = "mardis_execute%d=%s" % (i, value)
		source = source.replace(key, replace)
	source += "\nerr = 0\nmardis_execute_list = []\n%s" % "\n".join(listv)
	exec(source)
	return mardis_execute_list

def isco(co):
	return hasattr(co, 'co_code')

def fn(x, iter=0):
	if x[-3:] == ".py":
		x = x[:-3]
	y = [x + ".py"]
	if iter:
		for i in range(1, iter):
			v = x + str(i) + ".py"
			y.append(v)
	return y

def view(xxx):
	try:
		return open(xxx).read()
	except Exception:
		print("file %s not found!" % xxx)
		exit()

def dis(filename, outfile):
	source_code = view(filename)
	layer = 0
	while True:
		if source_code.count("exec") != 0:
			try:
				codelist = _parse(source_code)
			except Exception:
				print('\n We got an unexpected error here, please check the `%s` file to find the cause of the error.' % outfile)
				save_code(
					outfile,
					source_code
				)
				break
			amount = len(codelist)
			suck = []
			err = 0
			if amount > 1:
				print('mardis layer%d:\n- get %s target to decompile. trying ...' % (layer, amount))
			else:
				xxx = codelist[0]
				if isco(xxx):
					print('mardis layer%d: try target %s' % (layer, str(codelist[0])))
				else:
					print('mardis layer%d: target is not a code type' % layer)
			for code_obj in codelist:
				execute = try_decompile(code_obj)
				if execute == mardis_error_decompile:
					err += 1
				else:
					suck.append(execute)
			amount = len(suck)
			if amount > 1:
				print('- total %d successfully decompiled' % len(suck))
				xyz = fn(outfile, iter=amount)
				for file, source in zip(xyz, suck):
					save_code(file, source)
				print('\ndecompilation results are saved to the following file\n- %s' % ('\n- '.join(xyz)))
				break
			else:
				if err > 0:
					print('\nthe decompilation process fails at this phase.')
					print('check the %s file to analyze errors' % outfile)
					save_code(outfile, source_code)
					break
				else:
					source_code = suck[0]
		else:
			if layer > 0:
				print('\nDecompilation was successful, with a total of %d layer. Results were saved to file `%s`' % (layer, outfile))
				save_code(outfile, source_code)
				break
			else:
				print('did not find code to decompile in file `%s`' % filename)
				break
		layer += 1

def main():
	outfile = "mardis_result.py"
	if len(sys.argv) < 2:
		print("Usage: %s [filename|output]" % script_name)
		print("\nfilename = the file you want to decompile ")
		print("output = For files that store decompilation results, the default is `%s`" % outfile)
		exit()
	else:
		if len(sys.argv) >= 3:
			outfile = sys.argv[2]
		dis(sys.argv[1], outfile)

if __name__ == "__main__":
	main()

