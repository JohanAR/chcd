#
# chain cd
#

CHCD_SCRIPT="${0:h}/chcd.py"

function chcd
{
  cd $($CHCD_SCRIPT "$1")
}

chcd "$@"

