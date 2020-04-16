PYENV_HOME=$WORKSPACE/.sample1/
if [ –d $PYENV_HOME ]; then
   rm –rf $PYENV_HOME
fi

virtualenv —no–site–packages $PYENV_HOME
. $PYENV_HOME/bin/activate
pip install –r envs/req.txt
