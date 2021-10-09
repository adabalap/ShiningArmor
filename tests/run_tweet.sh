#!/bin/bash
export LC_ALL="C.UTF-8"
BASE_DIR="${HOME}/Source/ShiningArmor/tests"
# Need to store the last index in a file
RR_FILE="/tmp/rr.tmp"
# Create an array with multiples cities
TAGS=("perl" "computers" "linux" "linuxcookie" "literature" "science" "poems" "startrek" "wisdom" "work")

round_robin(){
    ARRAY=("$@")
    COUNT=$(cat $RR_FILE)

    for ITEM in ${#ARRAY[@]}; do
        HASH_TAG="${ARRAY[$COUNT]}"
        COUNT=$((COUNT+1))
        echo $COUNT > $RR_FILE

        if [[ $COUNT -ge ${#ARRAY[@]} ]]; then
            COUNT=0
            # Update file for the next run
            echo $COUNT > $RR_FILE
        fi
    done
}

cd ${BASE_DIR}
. ${BASE_DIR}/venv/bin/activate

if [ ! -f $RR_FILE ]; then
  touch $RR_FILE
fi

# Using round robin function for tweet hash tags
round_robin ${TAGS[@]}

python  test_tweet.py \
        -t ./tokens.json \
        -d ${HOME}/Source/sqlite3/testDB.db \
        -s ./sql_stmts.json \
        -ht ${HASH_TAG}

deactivate
