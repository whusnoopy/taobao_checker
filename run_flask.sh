#!/bin/bash

PROJDIR=$( cd $(dirname $0) ; pwd -P )
cd ${PROJDIR}

PYTHON="${PROJDIR}/env/bin/python"

pid=$(pgrep -f "${PYTHON}")
if [ ${pid} ]; then
    kill ${pid}
fi

if [ $# -eq 0 ]; then
    nohup ${PYTHON} ./flask_server.py &
fi
