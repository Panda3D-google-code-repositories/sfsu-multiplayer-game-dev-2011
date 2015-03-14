#!/bin/bash

pid=$(ps aux | grep 'java -jar GameServer-11-07-11.jar' | grep -v 'grep' | awk '{print $2}')

grep -i 'NullPointerException' GameServer-11-07-11.log

if [ $(echo $?) eq 0 ] then
    java -jar GameServer-11-07-11.jar &> GameServer-11-07-11.log

ps aux | grep 'java -jar GameServer-11-07-11.jar' | grep -v 'grep'

if [ $(echo $?) eq 0 ] then
    kill -9 $pid
    java -jar GameServer-11-07-11.jar &> GameServer-11-07-11.log
