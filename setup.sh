#!/bin/sh

function check_matplotlib {
python - <<INSTALLED
try:
	import matplotlib
	print('y')
except ImportError:
	print('matplotlib is not installed!')
	print('n')
INSTALLED
}

if [ "$(uname)" == "Darwin" ]; then
	echo 'Detected Mac Operating System...'
	echo 'Unfortunately, Mac OS is not currently supported by CLAAP.'
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
	echo 'Detected Linux Operating System...'
	sudo apt-get update
	# PIP
	echo 'Installing pip...'
	sudo easy_install pip
	# NLTK
	echo 'Installing NLTK...'
	sudo pip install -U nltk
	echo 'Setting up NLTK...'
	sudo python setup.py
	# termcolor
	echo 'Installing termcolor...'
	sudo pip install termcolor
	STAT=$(check_matplotlib)
	if [[ $STAT == "n" ]]; then
		# matplotlib
		echo 'Downloading matplotlib...'
		sudo git clone git://github.com/matplotlib/matplotlib.git
		echo 'Building matplotlib dependencies...'
		sudo apt-get build-dep matplotlib
		echo 'Installing matplotlib...'
		cd matplotlib/
		sudo python setup.py install
		cd ..
		rmdir matplotlib/
	elif [[ $STAT == "y" ]]; then
		echo 'matplotlib is already installed!'
	else
		echo 'Unable to determine if matplotlib is installed...'
	fi
	echo 'Successfully Installed CLAAP Dependencies!'
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
	echo 'Detected Windows Operating System...'
	echo 'Unfortunately, MS Windows is not currently supported by CLAAP.'
else
	echo 'Unable to detect Operating System.'
fi
