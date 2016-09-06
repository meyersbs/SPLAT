#!/bin/sh

chmod +x /usr/local/lib/python3.5/site-packages/splat/base/splat_cli.py
echo 'alias splat="python3.5 /usr/local/lib/python3.5/site-packages/splat/base/splat_cli.py"' >> ~/.bashrc
echo 'alias splat="python3.5 /usr/local/lib/python3.5/site-packages/splat/base/splat_cli.py"' >> ~/.bash_profile
source ~/.bashrc
splat --info
#echo "Thank you for installing SPLAT! Documentation and example usage can be found here: https://github.com/meyersbs/SPLAT"