import git,shutil
import sys,os
git.Repo.clone_from(sys.argv[1],sys.argv[2])
for item in os.listdir(sys.argv[2]):
	if item.endswith(".py"):
		shutil.copy(sys.argv[2]+"\\"+item,sys.argv[3])
		