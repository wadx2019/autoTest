import os,sys
"""python自动化评测，命令行参数一clone的python文件所在的文件夹，
命令行参数二测试数据文件位置，输出为与原python文件同名的json文件"""
def _main(_input_file,_exec_file,_output_file):
	"""参数一输入文件位置，参数二代码文件位置，参数三输出文件位置"""
	_stdintmp=sys.stdin
	_stdouttmp=sys.stdout
	with open(_input_file,'r') as input_file:
		for _lines in input_file.readlines():
			_temp=open("_tmp.txt",'w')
			_temp.write(_lines)
			_temp.close()
			sys.stdin=open("_tmp.txt",'r')
			with open(_output_file,'a+') as sys.stdout:
				_pyexec=open(_exec_file,'r')
				_pycontent=_pyexec.readlines()
				exec("".join(_pycontent))
				_pyexec.close()
			sys.stdin.close()
			sys.stdin=_stdintmp
			sys.stdout=_stdouttmp
			os.remove("_tmp.txt")

def _find_file():
	"""过滤文件下的python文件，返回其位置列表"""
	path_list=[]
	for item in os.listdir():
		if item.endswith(".py"):
			path_list.append(item)
	return path_list

os.chdir(sys.argv[1])
_lp=_find_file()
for _f in _lp:
	_f_name,_=os.path.splitext(_f)
	_main(sys.argv[2],_f,_f_name+".json")



