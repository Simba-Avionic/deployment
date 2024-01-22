#!/bin/bash 
now=`date '+%Y_%m_%d_%H_%M_%S'`
echo $now
scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $3 "$2:/etc/simba/new/$4-$now.tar"

