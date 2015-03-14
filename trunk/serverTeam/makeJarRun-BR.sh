#!/bin/sh

build=GameServer-$(date +"%m-%d-%y")
sfsu="sfsu-multiplayer-game-dev-2011-read-only"

# Remove the previous GameServer so we can build a new one.
rm GameServer*.jar

svn checkout http://sfsu-multiplayer-game-dev-2011.googlecode.com/svn/trunk/ $sfsu

mkdir $build

# Move source to a temp directory.
mv $sfsu/serverTeam/serverTest*/src/* $build/
mv $sfsu/serverTeam/serverTest*/manifest.mf $build/
mv $sfsu/serverTeam/serverTest*/lib/ $build/

cd $build/
mkdir core
mv Game{Client,Server}.java core/

javac -classpath lib/commons-dbcp-1.4.jar:lib/commons-logging.jar:lib/commons-pool-1.5.6.jar:lib/org.springframework.beans-3.0.0.RELEASE.jar:lib/org.springframework.core-3.0.0.RELEASE.jar core/*.java business/*.java com/*.java configuration/*.java gameDB/*.java metadata/*.java model/*.java networking/{request,response}/*.java utility/*.java worldManager/game{Engine,Manager}/*.java

jar -cvfm GameServer.jar manifest.mf core/*.java business/*.java com/*.java configuration/*.java gameDB/*.java metadata/*.java model/*.java networking/{request,response}/*.java utility/*.java worldManager/game{Engine,Manager}/*.java

echo $?

#rm {core,business,com,configuration,gameDB,metadata,model,networking,utility}/*.class
mv GameServer.jar ../

cd -

rm -rf $build/
rm -rf $sfsu/

java -jar GameServer
