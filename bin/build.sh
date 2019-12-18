#!/usr/bin/env bash

ME=$(basename $0)
BASE=$(readlink -f $(dirname $0)/..)

VENV_DIR=${VENV_DIR:-$BASE/venv}

$VENV_DIR/bin/pyinstaller -F -n normalizer $BASE/app/app.py --hidden-import=queue --paths=$BASE/app --onefile;

distfolder=normalizer
distpath=${BASE}/${distfolder}
[[ -d ${distpath} ]] || mkdir -p ${distpath}
cp $BASE/dist/normalizer ${distpath}/normalizer
distfilename=${BASE}/normalizer.tar.gz

tar -cvzf $distfilename -C $BASE ./$distfolder

rm -rf build dist normalizer.spec $distpath

echo
echo " *************************************** "
echo " ${distfilename} distribution file created... "
echo

