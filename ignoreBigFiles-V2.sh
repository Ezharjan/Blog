#!/bin/bash

echo "automatically ignoring large files"
find . -size 1M | sed 's|^\./||g' >> .gitignore
cat .gitignore | sort | uniq > .gitignore

git diff --exit-code .gitignore
exit_status=$?
if [ $exit_status -eq 1 ]
then
    set +e
    for i in `cat .gitignore`
    do
    set +e
        git rm --cached $i
    done

    git add .gitignore
    git commit .gitignore --no-verify -m"ignoring large files"

    echo "ignored new large files"
fi
