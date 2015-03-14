#!/bin/sh

build=GameServer-$(date +"%m-%d-%y")
sfsu="http://sfsu-multiplayer-game-dev-2011.googlecode.com/svn/trunk/serverTeam/serverTest0914"

# Remove the previous GameServer so we can build a new one.
#rm GameServer*.jar

mkdir -p $build/{build,dist,lib,src}/

svn checkout $sfsu/src/@490 $build/src
svn checkout $sfsu/lib/@490 $build/lib/

cd $build/

javac -classpath lib/commons-dbcp-1.4.jar:lib/commons-logging.jar:lib/commons-pool-1.5.6.jar:lib/org.springframework.beans-3.0.0.RELEASE.jar:lib/org.springframework.core-3.0.0.RELEASE.jar src/*.java src/business/*.java src/com/*.java src/configuration/*.java src/dao/*.java src/gameDB/*.java src/metadata/*.java src/model/*.java src/networking/{request,response}/*.java src/utility/*.java src/worldManager/gameEngine/*.java src/worldManager/gameEngine/species/*.java src/worldManager/gameManager/*.java src/worldManager/gameManager/speciesType/*.java
#javac -classpath lib/commons-dbcp-1.4.jar:lib/commons-logging.jar:lib/commons-pool-1.5.6.jar:lib/org.springframework.beans-3.0.0.RELEASE.jar:lib/org.springframework.core-3.0.0.RELEASE.jar src/*.java src/business/*.java src/com/*.java src/configuration/*.java src/dataAccessLayer/*.java src/metadata/*.java src/model/*.java src/networking/{request,response}/*.java src/utility/*.java src/worldManager/gameEngine/*.java src/worldManager/gameEngine/species/*.java src/worldManager/gameManager/*.java src/worldManager/gameManager/speciesType/*.java

#jar -cvfm $build.jar src/manifest.mf src/*.class src/business/*.class src/com/*.class src/configuration/*.class src/dataAccessLayer/*.class src/metadata/*.class src/model/*.class src/networking/{request,response}/*.class src/utility/*.class src/worldManager/gameEngine/*.class src/worldManager/gameEngine/species/*.class src/worldManager/gameManager/*.class src/worldManager/gameManager/speciesType/*.class

echo $?

#mv $build.jar ../

cd -

#rm -rf $build/
#rm -rf $sfsu/

#java -jar $build.jar &> GameServer.log &
