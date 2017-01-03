#!/bin/bash

##########################################################
#							 #
# Template to remember the usage of some shell commands  #
#							 #
##########################################################


############# FOR EACH ####################

# List dirs
list_dirs()
{
	echo "List Dir $1"

	for f in `ls $1`
	do
		if [ -d $f ]
		then
			echo "$f (Dir)"
		else
			echo "$f (File)"
		fi
	done
}

#List process pid
list_process()
{
	echo "All pids from $1"

	for pid in $(ps aux | grep $1 | grep -v grep | awk '{print $2}')
	do 
		echo "$1 PID: $pid"
	done
}


############# AWK ############

#AWK Print 4 column (Ignore first line of stream)
#Obs: '<(command)' creates temp file with its content as output from command
test_awk()
{
	awk 'NR==1{next}{print $4}' <(echo -e "Should not be visible\n. . . Hello\n. . . World")
}


############### FOR ######################

# Use for to print 1 to 10
print_numbers()
{
	for(( i=1; i<=10; i++ ))
	do 
		echo $i
	done 
}


#############  CASE ###############

# Use case to select service options
fake_service()
{
	case $1 in
		start)
			echo "Starting fake service"
			;;
		stop)
			echo "Stopping fake service"
			;;
		*)
			echo "Correct Usage: fake_service [start|stop]"
			;;
	esac
}


########### CUT ######################
# Split word by ' '
split_word()
{
	echo "Sentence: $1"

	echo -n "First Two fields: "
	echo $1 | cut -d ' ' -f1-2

	echo -n "Last Two fields: "
	echo $1 | rev | cut -d ' ' -f1-2 | rev
}


######### FIND #################
# cat all files .conf inside dir
# Obs: Output is too large, so 1>&2 redirects output from stdout(1) to the same as stderr(2)
show_files()
{
	find $1 -type f -iname '*.conf' -exec cat {} \; 2>/dev/null 1>&2
}


###### KILL ##########
# Kill all process by name
kill_by_name()
{
	ps ax | grep $1 | grep -v grep | awk '{print $1}' | xargs kill -9
}

list_dirs $PWD
list_process chromium
test_awk
fake_service start
split_word "1 2 3 4 5 6 7 8 9 10"
show_files /etc
#kill_by_name "java"
