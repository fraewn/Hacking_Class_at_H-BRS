#!/usr/bin/env bash

if [[ $# -ne 1 ]]; then
	echo "usage $0 path to ctf directory"
	exit 1
fi

ctf_name=$(basename $1)

container_tool=$(which docker 2>/dev/null)

if [[ -z $container_tool ]]; then
	container_tool=$(which podman 2>/dev/null)
fi

if [[ -z $container_tool ]]; then
	echo "you need docker or podman to run this script!"
	exit 1
fi
$container_tool run -d \
	--rm \
	-h ${ctf_name} \
	--name ${ctf_name} \
	-v $(pwd)/${ctf_name}:/ctf/work:Z \
	-p 23946:23946 \
	--cap-add=SYS_PTRACE \
	skysider/pwndocker

$container_tool exec -it ${ctf_name} /bin/bash
