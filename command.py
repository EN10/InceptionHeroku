import subprocess
 
p = subprocess.Popen(["python", "classify_image.py"], stdout=subprocess.PIPE)
output, err = p.communicate()

print output

# http://blog.nuventure.in/2014/09/04/executing-bash-commands-via-python