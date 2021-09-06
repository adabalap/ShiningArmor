#!/bin/bash
export LC_ALL="C.UTF-8"
BASE_DIR=`pwd`


clean_up_stale_process() {
  # Clean up and stale process from previous run
	echo
	stale_process="Xvfb chromedriver"

	for i in $stale_process
	do
  		echo "`date`: Checking for ${i} stale process"
  		ps -ef | grep ${i} | grep -v grep

  		if [[ $? == 1 ]]
  		then
    			echo "`date`: No ${i} stale process found"
  		else
    			echo "`date`: Cleaning up ${i} stale process"
    			/usr/bin/pkill ${i}
    			sleep 5
  		fi
	done
}

main() {
	# Main function
	clean_up_stale_process
	return $?
}

# Setup the environment and run the program
cd ${BASE_DIR}
. ${BASE_DIR}/venv/bin/activate
main
deactivate
