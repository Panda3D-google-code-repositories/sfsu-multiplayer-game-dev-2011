BEGIN TRANSACTION;
CREATE TABLE avatar (avatar_id INTEGER PRIMARY KEY, avatar_file TEXT);
INSERT INTO avatar VALUES(1,'ralph/ralph');
INSERT INTO avatar VALUES(2,'rockstar/rockstar');
INSERT INTO avatar VALUES(3,'males/male1/male');
INSERT INTO avatar VALUES(4,'males/male2/male');
INSERT INTO avatar VALUES(5,'males/male3/male');
INSERT INTO avatar VALUES(6,'males/male4/male');
INSERT INTO avatar VALUES(7,'males/male5/male');
INSERT INTO avatar VALUES(8,'females/ralphSister/eve');
CREATE TABLE bug (bug_id INTEGER PRIMARY KEY, bug_file TEXT);
INSERT INTO bug VALUES(1,'panda/panda');
INSERT INTO bug VALUES(2,'bug1/bug1');
CREATE TABLE game (game_id INTEGER PRIMARY KEY, name TEXT, version TEXT);
INSERT INTO game VALUES(1,'Board Game',1.00);
INSERT INTO game VALUES(2,'Survival',1.00);
INSERT INTO game VALUES(3,'Coding',1.00);
INSERT INTO game VALUES(4,'Top Down',1.00);
INSERT INTO game VALUES(5,'Variables',1.00);
CREATE TABLE item (item_id INTEGER PRIMARY KEY, item_name TEXT, item_description BLOB, item_file TEXT);
INSERT INTO item VALUES(1,'Small HP Potion','Restores 25 HP','');
INSERT INTO item VALUES(2,'Medium HP Potion','Restores 50 HP','');
INSERT INTO item VALUES(3,'Large HP Potion','Restores 100 HP','');
INSERT INTO item VALUES(4,'Mega HP Potion','Restores 50% HP','');
INSERT INTO item VALUES(5,'Hint Card J-1','Reveals hint for a single question.

Only usable in battle.
Used for topic, Java Chapter 1.','');
INSERT INTO item VALUES(6,'Hint Card J-2','Reveals hint for a single question.

Only usable in battle.
Used for topic, Java Chapter 2.','');
INSERT INTO item VALUES(7,'Hint Card J-3','Reveals hint for a single question.

Only usable in battle.
Used for topic, Java Chapter 3.','');
INSERT INTO item VALUES(8,'Hint Card J-4','Reveals hint for a single question.

Only usable in battle.
Used for topic, Java Chapter 4.','');
INSERT INTO item VALUES(9,'Hint Card J-5','Reveals hint for a single question.

Only usable in battle.
Used for topic, Java Chapter 5.','');
INSERT INTO item VALUES(10,'Hint Card J-6','Reveals hint for a single question.

Only usable in battle.
Used for topic, Java Chapter 6.','');
INSERT INTO item VALUES(11,'Hint Card J-7','Reveals hint for a single question.

Only usable in battle.
Used for topic, Java Chapter 7.','');
INSERT INTO item VALUES(12,'Hint Card J-8','Reveals hint for a single question.

Only usable in battle.
Used for topic, Java Chapter 8.','');
INSERT INTO item VALUES(13,'Hint Card J-9','Reveals hint for a single question.

Only usable in battle.
Used for topic, Java Chapter 9.','');
INSERT INTO item VALUES(14,'Hint Card J-10','Reveals hint for a single question.

Only usable in battle.
Used for topic, Java Chapter 10.','');
INSERT INTO item VALUES(15,'Wooden Stick','Attack Power 2-4

Requires Level 1','');
INSERT INTO item VALUES(16,'Plastic Ruler','Attack Power 6-9

Requires Level 4','');
INSERT INTO item VALUES(17,'Beard','Max HP +5

Requires Level 3','');
INSERT INTO item VALUES(18,'Ring','Max HP +30

Requires Level 10','');
INSERT INTO item VALUES(19,'Cardboard Shield','Defense +2

Requires Level 12','');
INSERT INTO item VALUES(20,'Cotton Shirt','Defense +1

Requires Level 3','');
INSERT INTO item VALUES(21,'Cotton Shorts','Defense +1

Requires Level 4','');
INSERT INTO item VALUES(22,'Sharp Ruler','Attack Power 16-21

Requires Level 11','');
INSERT INTO item VALUES(23,'Metal Rod','Attack Power 24-33

Requires Level 16','');
INSERT INTO item VALUES(24,'Cap','Defense +1
Max HP +10

Requires Level 5','');
INSERT INTO item VALUES(25,'Wooden Shield','Defense +5

Requires level 22','');
INSERT INTO item VALUES(26,'Old Book','Attack Power 12-15

Requires Level 6','');
INSERT INTO item VALUES(27,'Red Shirt','Defense +3

Requires Level 5','');
INSERT INTO item VALUES(28,'Slippers','Defense +1

Requires Level 5','');
INSERT INTO item VALUES(29,'Blue Shirt','Defense +3

Requires Level 5','');
INSERT INTO item VALUES(30,'Green Shirt','Defense +5

Requires Level 10','');
INSERT INTO item VALUES(31,'Pink Shirt','Defense +5

Requires Level 10','');
INSERT INTO item VALUES(32,'Short Sword','Attack Power 28-42

Requires Level 21','');
INSERT INTO item VALUES(33,'Club','Attack Power 45-48

Requires Level 26','');
INSERT INTO item VALUES(34,'Haste Shirt','Move Speed +0.05

Requires Level 8','');
INSERT INTO item VALUES(35,'Durable Shirt','Max HP +2%

Requires Level 8','');
INSERT INTO item VALUES(36,'Time Shirt','Attack Time +0.5 sec

Requires Level 8','');
INSERT INTO item VALUES(37,'210 Shirt','Move Speed +0.2
Max HP +10%

Requires Level 8','');
INSERT INTO item VALUES(38,'213 Shirt','Attack Time +2 sec

Requires Level 8','');
INSERT INTO item VALUES(39,'413 Shirt','Max HP +15%
Attack Time +1 sec

Requires Level 8','');
INSERT INTO item VALUES(40,'1337 Shirt','Defense +5
Max HP +25%
Attack Time +4 sec
Move Speed +0.3

Requires Level 8','');
INSERT INTO item VALUES(41,'Black Jeans','Defense +2

Requires Level 6','');
INSERT INTO item VALUES(42,'Red Jeans','Defense +3

Requires Level 11','');
INSERT INTO item VALUES(43,'White Jeans','Defense +3

Requires Level 11','');
INSERT INTO item VALUES(44,'Blue Jeans','Defense +2

Requires Level 6','');
INSERT INTO item VALUES(45,'Trousers','Defense +4

Requires Level 16','');
INSERT INTO item VALUES(46,'Boots','Defense +3

Requires Level 15','');
INSERT INTO item VALUES(47,'Shoes','Defense +2

Requires Level 10','');
INSERT INTO item VALUES(48,'Jacket','Defense +8

Requires Level 15','');
INSERT INTO item VALUES(49,'Haste Jeans','Move Speed +0.05

Requires Level 8','');
INSERT INTO item VALUES(50,'Durable Jeans','Max HP +2%

Requires Level 8','');
INSERT INTO item VALUES(51,'Time Jeans','Attack Time +0.5 sec

Requires Level 8','');
INSERT INTO item VALUES(52,'Leather Jeans','Max HP +10%
Move Speed -0.15

Requires Level 8','');
INSERT INTO item VALUES(53,'Shorts','Move Speed +0.2
Max HP -12%

Requires Level 8','');
INSERT INTO item VALUES(54,'Reading Glasses','Attack Time +0.5 sec

Requires Level 14','');
INSERT INTO item VALUES(55,'Frameless Glasses','Move Speed +0.1

Requires Level 14','');
INSERT INTO item VALUES(56,'Sunglasses','Max HP +2%

Requires Level 14','');
INSERT INTO item VALUES(57,'Aviators','Max HP +3%
Move Speed +0.15

Requires Level 14','');
INSERT INTO item VALUES(58,'Party Glasses','Move Speed +0.2

Requires Level 14','');
INSERT INTO item VALUES(59,'Big Glasses','Attack Time +1 sec

Requires Level 14','');
INSERT INTO item VALUES(60,'Future Glasses','Max HP +10%
Move Speed +0.3
Attack Time +2 sec

Requires Level 14','');
INSERT INTO item VALUES(61,'Sturdy Belt','Max HP +3%

Requires Level 20','');
INSERT INTO item VALUES(62,'Light Belt','Move Speed +0.2

Requires Level 20','');
INSERT INTO item VALUES(63,'New Belt','Attack Time +1 sec

Requires Level 20','');
INSERT INTO item VALUES(64,'Leather Belt','Max HP +10%
Attack Time -2 sec

Requires Level 20','');
INSERT INTO item VALUES(65,'Magical Belt','Max HP +8%
Move Speed +0.1
Attack Time +1 sec

Requires Level 20','');
INSERT INTO item VALUES(66,'White Shoes','Max HP +3%
Attack Time +1.5 sec

Requires Level 28','');
INSERT INTO item VALUES(67,'Black Shoes','Move Speed +0.2
Attack Time +1 sec

Requires Level 28','');
INSERT INTO item VALUES(68,'Dragon Shoes','Max HP +15%
Move Speed +0.25

Requires Level 28','');
INSERT INTO item VALUES(69,'Magical Shoes','Max HP +20%
Attack Time +1.5 sec

Requires Level 28','');
INSERT INTO item VALUES(70,'210 Shoes','Max HP +20%
Move Speed + 0.15
Attack Time +2 sec

Requires Level 28','');
INSERT INTO item VALUES(71,'213 Shoes','Move Speed +0.5

Requires Level 28','');
INSERT INTO item VALUES(72,'413 Shoes','Max HP +25%
Move Speed +0.2
Attack Time +2.5 sec

Requires Level 28','');
INSERT INTO item VALUES(73,'1337 Shoes','Defense +5
Max HP +30%
Move Speed +0.25
Attack Time +4 sec

Requires Level 28','');
INSERT INTO item VALUES(74,'Baseball Hat','Attack Time +1.5 sec

Requires Level 35','');
INSERT INTO item VALUES(75,'Gentleman''s Hat','Max HP +10%

Requires Level 35','');
INSERT INTO item VALUES(76,'Cowboy Hat','Move Speed +0.15

Requires Level 35','');
INSERT INTO item VALUES(77,'Magician''s Hat','Max HP +15%
Move Speed +0.1

Requires Level 35','');
INSERT INTO item VALUES(78,'210 Hat','Max HP +15%
Move Speed +0.1
Attack Time +1.5 sec

Requires Level 35','');
INSERT INTO item VALUES(79,'213 Hat','Max HP +30%

Requires Level 35','');
INSERT INTO item VALUES(80,'413 Hat','Max HP +20%
Move Speed +0.15
Attack Time +2 sec

Requires Level 35','');
INSERT INTO item VALUES(81,'1337 Hat','Defense +5
Max HP +25%
Move Speed +0.4
Attack Time +2.5 sec

Requires Level 35','');
INSERT INTO item VALUES(82,'Eliminator Scroll Lv. 1','One of the choices will be eliminated.

Only usable in battle.
Must have at least 2 available choices.','');
INSERT INTO item VALUES(83,'Mystery Box','Receive one random item','mystery.png');
INSERT INTO item VALUES(84,'Leather Armor','Defense +12

Requires Level 20','');
INSERT INTO item VALUES(85,'Leather Pants','Defense +5

Requires Level 21','');
INSERT INTO item VALUES(86,'Leather Shoes','Defense +4

Requires Level 20','');
INSERT INTO item VALUES(87,'Hard Leather Armor','Defense +15

Requires Level 25','');
INSERT INTO item VALUES(88,'Hard Leather Pants','Defense +6

Requires Level 26','');
INSERT INTO item VALUES(89,'Hard Leather Shoes','Defense +5

Requires Level 25','');
INSERT INTO item VALUES(90,'Long Sword','Attack Power 50-60

Requires Level 31','');
INSERT INTO item VALUES(91,'Axe','Attack Power 56-64

Requires Level 36','');
INSERT INTO item VALUES(92,'Magical Blade','Attack Power 65-75

Requires Level 41','');
INSERT INTO item VALUES(93,'Flaming Sword','Attack Power 72-90

Requires Level 46','');
INSERT INTO item VALUES(94,'Wooden Armor','Defense +18

Requires Level 30','');
INSERT INTO item VALUES(95,'Wooden Leg Guards','Defense +8

Requires Level 31','');
INSERT INTO item VALUES(96,'Wooden Boots','Defense +7

Requires Level 30','');
INSERT INTO item VALUES(97,'Chainmail','Defense +23

Requires Level 35','');
INSERT INTO item VALUES(98,'Chainmail Pants','Defense +10

Requires Level 36','');
INSERT INTO item VALUES(99,'Chainmail Boots','Defense +9

Requires Level 35','');
INSERT INTO item VALUES(100,'Light Plate Armor','Defense +26

Requires Level 40','');
INSERT INTO item VALUES(101,'Light Plate Pants','Defense +12

Requires Level 41','');
INSERT INTO item VALUES(102,'Light Plate Boots','Defense +10

Requires Level 40','');
INSERT INTO item VALUES(103,'Plate Armor','Defense +32

Requires Level 45','');
INSERT INTO item VALUES(104,'Plate Pants','Defense +15

Requires Level 46','');
INSERT INTO item VALUES(105,'Plate Boots','Defense +12

Requires Level 45','');
CREATE TABLE map (map_id INTEGER PRIMARY KEY, map_name TEXT, map_bgm TEXT);
INSERT INTO map VALUES(1,'The Table','02.ogg');
INSERT INTO map VALUES(2,'Chapter 1 Level','03.ogg');
INSERT INTO map VALUES(3,'Chapter 1 Dungeon','03.ogg');
INSERT INTO map VALUES(4,'Chapter 2 Level','03.ogg');
INSERT INTO map VALUES(5,'Chapter 3 Level','03.ogg');
INSERT INTO map VALUES(6,'Chapter 4 Level','03.ogg');
INSERT INTO map VALUES(7,'Chapter 5 Level','03.ogg');
INSERT INTO map VALUES(8,'Chapter 6 Level','03.ogg');
INSERT INTO map VALUES(9,'Chapter 8 Level','03.ogg');
INSERT INTO map VALUES(10,'Chapter 9 Level','03.ogg');
INSERT INTO map VALUES(11,'Chapter 10 Level','03.ogg');
INSERT INTO map VALUES(12,'Space','03.ogg');
INSERT INTO map VALUES(13,'Blank Level','03.ogg');
CREATE TABLE map_object (object_id INTEGER PRIMARY KEY, object_file TEXT);
INSERT INTO map_object VALUES(1,'resistor_green/resistor_green');
INSERT INTO map_object VALUES(2,'resistor_red/resistor_red');
INSERT INTO map_object VALUES(3,'harddrive/harddrive');
INSERT INTO map_object VALUES(4,'wire_blue/wire_blue');
INSERT INTO map_object VALUES(5,'wire_red/wire_red');
INSERT INTO map_object VALUES(6,'wire_green/wire_green');
CREATE TABLE map_type (map_type_id INTEGER PRIMARY KEY, map_file TEXT);
INSERT INTO map_type VALUES(1,'mainScene/mainScene');
INSERT INTO map_type VALUES(2,'easyLevelScene/easyLevelScene');
INSERT INTO map_type VALUES(3,'dungeonEasyScene/dungeonEasyScene');
INSERT INTO map_type VALUES(4,'easyLevelSpace/easyLevelSpace');
INSERT INTO map_type VALUES(5,'blank_level/blank_level');
CREATE TABLE msg (msg_id INTEGER PRIMARY KEY, msg_text TEXT);
INSERT INTO msg VALUES(1,'You have received %s [ %d ]');
INSERT INTO msg VALUES(2,'You have received %d Bytes');
INSERT INTO msg VALUES(3,'You have used %s [ %d ]');
INSERT INTO msg VALUES(4,'Not implemented');
INSERT INTO msg VALUES(5,'You cannot whisper to yourself');
INSERT INTO msg VALUES(6,'You have equipped %s [ %d ]');
INSERT INTO msg VALUES(7,'You have unequipped %s [ %d ]');
INSERT INTO msg VALUES(8,'You have removed %s [ %d ]');
INSERT INTO msg VALUES(9,'%s has been added to your friends list');
INSERT INTO msg VALUES(10,'%s has rejected your friend invite');
INSERT INTO msg VALUES(11,'%s has been removed from your friends list');
INSERT INTO msg VALUES(12,'%s is not on your friends list');
INSERT INTO msg VALUES(13,'%s is offline');
INSERT INTO msg VALUES(14,'%s is unavailable');
INSERT INTO msg VALUES(15,'Sent %s a friend invite');
INSERT INTO msg VALUES(16,'Your inventory is full');
INSERT INTO msg VALUES(17,'You do not meet the level requirement');
INSERT INTO msg VALUES(18,'No description');
INSERT INTO msg VALUES(19,'Sent %s a party invite');
INSERT INTO msg VALUES(20,'Party name, %s,  is unavailable');
INSERT INTO msg VALUES(21,'%s is already in a party');
INSERT INTO msg VALUES(22,'You are not the party leader');
INSERT INTO msg VALUES(23,'%s has rejected your party invite');
INSERT INTO msg VALUES(24,'%s has joined the party');
INSERT INTO msg VALUES(25,'%s has left the party');
INSERT INTO msg VALUES(26,'You have left the party');
INSERT INTO msg VALUES(27,'%s has become the new party leader');
INSERT INTO msg VALUES(28,'Party has been disbanded');
INSERT INTO msg VALUES(29,'Party is full');
INSERT INTO msg VALUES(30,'You are not in a party');
INSERT INTO msg VALUES(31,'Party member must be online');
INSERT INTO msg VALUES(32,'%s has entered the game');
INSERT INTO msg VALUES(33,'%s has left the game');
INSERT INTO msg VALUES(34,'You have become the party leader');
INSERT INTO msg VALUES(35,'You do not meet the requirements');
INSERT INTO msg VALUES(36,'You have eliminated one of the choices');
INSERT INTO msg VALUES(37,'%s has eliminated one of the choices');
INSERT INTO msg VALUES(38,'You have successfully answered the question');
INSERT INTO msg VALUES(39,'You have failed to answer the question. Please try again...');
INSERT INTO msg VALUES(40,'%s has failed to answer the question');
INSERT INTO msg VALUES(41,'%s has successfully answered the question');
INSERT INTO msg VALUES(42,'You have failed to use the item');
INSERT INTO msg VALUES(43,'You''ve been disconnected');
INSERT INTO msg VALUES(44,'You''ve been disconnected by a user from another location');
INSERT INTO msg VALUES(45,'Could not connect to server. Please try again later.');
INSERT INTO msg VALUES(46,'You are dead!');
INSERT INTO msg VALUES(47,'Username is not available');
INSERT INTO msg VALUES(48,'Character name is not available');
INSERT INTO msg VALUES(49,'Registration Complete!');
INSERT INTO msg VALUES(50,'First Name Required');
INSERT INTO msg VALUES(51,'Last Name Required');
INSERT INTO msg VALUES(52,'Student ID Required');
INSERT INTO msg VALUES(53,'Student ID has to be of length 9');
INSERT INTO msg VALUES(54,'Student ID has to be a number');
INSERT INTO msg VALUES(55,'Username Required');
INSERT INTO msg VALUES(56,'Username must not contain spaces');
INSERT INTO msg VALUES(57,'Password Required');
INSERT INTO msg VALUES(58,'Passwords do not match');
INSERT INTO msg VALUES(59,'E-Mail Required');
INSERT INTO msg VALUES(60,'Invalid E-Mail');
INSERT INTO msg VALUES(61,'Character Name Required');
INSERT INTO msg VALUES(62,'Character Name must not contain spaces');
INSERT INTO msg VALUES(63,'Do you want to join %s''s party?');
INSERT INTO msg VALUES(64,'Do you want to be %s''s friend?');
INSERT INTO msg VALUES(65,'Friend already exists');
INSERT INTO msg VALUES(66,'You cannot add yourself');
INSERT INTO msg VALUES(67,'Can not use white spaces');
INSERT INTO msg VALUES(68,'Login Failed!');
INSERT INTO msg VALUES(69,'The account is being used. To continue, you need to log in again.');
INSERT INTO msg VALUES(70,'Getting Ready...');
INSERT INTO msg VALUES(71,'Game Start!');
INSERT INTO msg VALUES(72,'%s''s turn');
INSERT INTO msg VALUES(73,'%s has run out of time!');
INSERT INTO msg VALUES(74,'You''ve run out of time!');
INSERT INTO msg VALUES(75,'You have failed to answer the question');
INSERT INTO msg VALUES(76,'%s is the winner! Try harder next time!');
INSERT INTO msg VALUES(77,'You are the winner!');
INSERT INTO msg VALUES(78,'%s has rolled %d');
INSERT INTO msg VALUES(79,'You''ve rolled %d');
INSERT INTO msg VALUES(80,'Your turn');
INSERT INTO msg VALUES(81,'Your client needs to be updated to run this game.');
INSERT INTO msg VALUES(82,'You''ve gained %s experience points');
INSERT INTO msg VALUES(83,'%s is ready');
INSERT INTO msg VALUES(84,'Dice has rolled %d');
INSERT INTO msg VALUES(85,'Leaving in...');
INSERT INTO msg VALUES(86,'Starting in...');
INSERT INTO msg VALUES(87,'You''ve just leveled up to %d!');
INSERT INTO msg VALUES(88,'Sent %s a trade request');
INSERT INTO msg VALUES(89,'%s has rejected your trade request');
INSERT INTO msg VALUES(90,'%s has accepted your trade request');
INSERT INTO msg VALUES(91,'%s is busy');
INSERT INTO msg VALUES(92,'%s has canceled trade');
INSERT INTO msg VALUES(93,'Trade Complete!');
INSERT INTO msg VALUES(94,'%s has canceled trade request');
INSERT INTO msg VALUES(95,'You are already trading with %s');
INSERT INTO msg VALUES(96,'Do you accept %s''s trade request?');
INSERT INTO msg VALUES(97,'You have accepted %s''s trade request');
INSERT INTO msg VALUES(98,'You have rejected %s''s trade request');
INSERT INTO msg VALUES(99,'You have canceled trade');
INSERT INTO msg VALUES(100,'You have confirmed trade');
INSERT INTO msg VALUES(101,'%s has confirmed trade');
INSERT INTO msg VALUES(102,'Trade Failed!');
INSERT INTO msg VALUES(103,'%s does not have enough space');
INSERT INTO msg VALUES(104,'You do not have enough space');
INSERT INTO msg VALUES(105,'Your feedback is greatly appreciated!');
INSERT INTO msg VALUES(106,'Feedback Received');
INSERT INTO msg VALUES(107,'Feedback Failed');
INSERT INTO msg VALUES(108,'Received %d Bytes');
INSERT INTO msg VALUES(109,'Received %d Experience');
INSERT INTO msg VALUES(110,'Received %s [ %d ]');
INSERT INTO msg VALUES(111,'Subject Required');
INSERT INTO msg VALUES(112,'Message Required');
INSERT INTO msg VALUES(113,'Rating Required');
INSERT INTO msg VALUES(114,'Thanks for your purchase!');
INSERT INTO msg VALUES(115,'You do not have enough Bytes');
INSERT INTO msg VALUES(116,'You have recovered %d health');
INSERT INTO msg VALUES(117,'You have lost %d health');
INSERT INTO msg VALUES(118,'Sent %s a duel request');
INSERT INTO msg VALUES(119,'%s has accepted your duel request');
INSERT INTO msg VALUES(120,'%s has rejected your duel request');
INSERT INTO msg VALUES(121,'You have accepted %s''s duel request');
INSERT INTO msg VALUES(122,'You have rejected %s''s duel request');
INSERT INTO msg VALUES(123,'%s wants to challenge you in a %s duel. Do you accept?');
INSERT INTO msg VALUES(124,'%s has won the duel against %s');
INSERT INTO msg VALUES(125,'You have won the duel against %s');
INSERT INTO msg VALUES(126,'You have lost the duel against %s');
INSERT INTO msg VALUES(127,'You are already dueling with %s');
INSERT INTO msg VALUES(128,'%s is already dueling');
INSERT INTO msg VALUES(129,'%s has won the duel against %s');
INSERT INTO msg VALUES(130,'The duel has ended with a draw');
INSERT INTO msg VALUES(131,'The duel between %s and %s has ended with a draw');
INSERT INTO msg VALUES(132,'You''re already dueling');
INSERT INTO msg VALUES(133,'You need to be level 10 to duel');
INSERT INTO msg VALUES(134,'%s needs to be at least level 10 to duel');
CREATE TABLE npc (npc_id INTEGER PRIMARY KEY, npc_file TEXT);
INSERT INTO npc VALUES(1,'sphere/sphere');
INSERT INTO npc VALUES(2,'females/ralphSister/eve');
INSERT INTO npc VALUES(3,'ralph/ralph');
CREATE TABLE skill (skill_id INTEGER PRIMARY KEY, skill_name TEXT, skill_description BLOB, skill_file TEXT);
CREATE TABLE space_item (item_id INTEGER PRIMARY KEY, item_name TEXT, item_description TEXT, item_file TEXT);
INSERT INTO space_item VALUES(1,'Green Resistor',NULL,'resistor_green.png');
INSERT INTO space_item VALUES(2,'Red Resistor',NULL,'resistor_red.png');
INSERT INTO space_item VALUES(3,'Hard Drive',NULL,'harddrive.png');
INSERT INTO space_item VALUES(4,'Blue Wire',NULL,'wire_blue.png');
INSERT INTO space_item VALUES(5,'Red Wire',NULL,'wire_red.png');
INSERT INTO space_item VALUES(6,'Green Wire',NULL,'wire_green.png');
CREATE TABLE tip (tip_id INTEGER PRIMARY KEY, tip_text TEXT);
INSERT INTO tip VALUES(1,'Did you know you can quickly access chat by using the [Enter] key?');
INSERT INTO tip VALUES(2,'You can jump into the air simply by using the [Space Bar]');
INSERT INTO tip VALUES(3,'By performing a [Right-Click] on other characters, you can access a list of extra options');
INSERT INTO tip VALUES(4,'Holding down [Right-Click] while moving the mouse allows you to control the camera');
INSERT INTO tip VALUES(5,'Creating a hotkey is easy by dragging an item from the inventory to the hotkey bar');
INSERT INTO tip VALUES(6,'You can use an item by double-clicking on it');
INSERT INTO tip VALUES(7,'To remove an item from you inventory, just drag it outside of the window');
INSERT INTO tip VALUES(8,'To remove a hotkey, just drag it outside of the hotkey bar');
INSERT INTO tip VALUES(9,'Did you know you can review any questions you''ve answered in the Question Log?');
INSERT INTO tip VALUES(10,'You can easily view your friends by pressing [Ctrl+F]');
INSERT INTO tip VALUES(11,'You can hide the chat box by using [Ctrl+C]');
INSERT INTO tip VALUES(12,'Need more viewing space? You can easily hide the items at the left of your screen');
INSERT INTO tip VALUES(13,'Experience can be received by playing a board game with a party');
INSERT INTO tip VALUES(14,'Just [Right-Click] on another character to create a party');
INSERT INTO tip VALUES(15,'Want to trade items? Just [Right-Click] on a player and select [Trade]');
INSERT INTO tip VALUES(16,'You can leave the game by pressing [ESC] and select [Quit Game]');
INSERT INTO tip VALUES(17,'To leave a board game, just hit [ESC] and select [Leave Mode]');
INSERT INTO tip VALUES(18,'For whatever reasons, you can hide the mini-map by pressing [Ctrl+M]');
INSERT INTO tip VALUES(19,'Try to familiarize yourself with the buttons at the lower right to access certain features');
INSERT INTO tip VALUES(20,'Did you know you can shout across all maps by selecting [World Chat]?');
INSERT INTO tip VALUES(21,'You can quickly shout a message by adding [ ! ] in front of your message');
INSERT INTO tip VALUES(22,'Your Party Leader''s name is highlighted in yellow at the left of your screen');
INSERT INTO tip VALUES(23,'Remember that only Party Leader can invite other players to your party');
INSERT INTO tip VALUES(24,'You can quickly access your equipments by pressing [Ctrl+E]');
INSERT INTO tip VALUES(25,'You can just press [Enter] to send your message without the need to click [Send]');
INSERT INTO tip VALUES(26,'Need more gold? Keep defeating more bugs!');
INSERT INTO tip VALUES(27,'Did you know you can easily access your Question Log by pressing [Ctrl+Q]?');
INSERT INTO tip VALUES(28,'You can whisper your messages by typing /<Name> <Message>');
INSERT INTO tip VALUES(29,'By selecting [Reconnect] in the quit menu, you will be brought back to Login');
INSERT INTO tip VALUES(30,'To remove a friend, just [Right-Click] on their name and select [Remove]');
INSERT INTO tip VALUES(31,'Something wrong with a question? Just let us know using the Question Log');
INSERT INTO tip VALUES(32,'Boss Bugs may contain more than one question!');
INSERT INTO tip VALUES(33,'Leveling up gives you a slight boost in Health Points');
INSERT INTO tip VALUES(34,'You can find several different items by defeating bugs');
INSERT INTO tip VALUES(35,'Did you know you can change Party Leader in the party window?');
INSERT INTO tip VALUES(36,'To access a few extra party options, just press [Ctrl+P]');
INSERT INTO tip VALUES(37,'You can always run away from bugs if you''re low on Health Points');
INSERT INTO tip VALUES(38,'Are you having fun in deBugger?');
INSERT INTO tip VALUES(39,'You can move faster by finding equipments that enhance your move speed');
INSERT INTO tip VALUES(40,'You can take a closer look at your character by scrolling your [Mouse Wheel]');
INSERT INTO tip VALUES(41,'You can move your character by using the [W, A, S, D] keys');
INSERT INTO tip VALUES(42,'You can move your character by using the [Arrow] keys');
INSERT INTO tip VALUES(43,'You can move your character by using the [Left-Click]');
INSERT INTO tip VALUES(44,'Did you know you can just press [1-7] keys to use your hotkeys?');
INSERT INTO tip VALUES(45,'If you are having issues with the game, you should contact your instructor');
INSERT INTO tip VALUES(46,'Check our website at http://thecity.sfsu.edu/~debugger/ for the latest updates!');
INSERT INTO tip VALUES(47,'Interested in working on this game? Let us know!');
CREATE TABLE view (view_id INTEGER PRIMARY KEY, view_file TEXT, view_color TEXT);
INSERT INTO view VALUES(1,'random','0.93,0.05,0.45');
INSERT INTO view VALUES(2,'random','0.03,0.06,0.67');
INSERT INTO view VALUES(3,'random','0.8,0.73,0.75');
INSERT INTO view VALUES(4,'random','0.28,0.94,0.88');
INSERT INTO view VALUES(5,'random','0.9,0.08,0.47');
INSERT INTO view VALUES(6,'random','0.0,0.38,0.8');
INSERT INTO view VALUES(7,'random','0.56,0.39,0.38');
INSERT INTO view VALUES(8,'random','1.0,0.85,0.77');
INSERT INTO view VALUES(9,'random','0.92,0.69,0.03');
INSERT INTO view VALUES(10,'random','0.16,0.39,0.46');
INSERT INTO view VALUES(11,'random','0.76,0.63,0.37');
INSERT INTO view VALUES(12,'random','0.87,0.42,0.09');
INSERT INTO view VALUES(13,'random','0.14,0.84,0.48');
INSERT INTO view VALUES(14,'random','0.64,0.98,0.55');
INSERT INTO view VALUES(15,'random','0.66,0.14,0.08');
INSERT INTO view VALUES(16,'random','0.15,0.09,0.04');
INSERT INTO view VALUES(17,'random','0.3,0.8,0.3');
INSERT INTO view VALUES(18,'random','0.09,0.05,0.64');
INSERT INTO view VALUES(19,'random','0.94,0.2,0.01');
INSERT INTO view VALUES(20,'random','0.46,0.87,0.43');
INSERT INTO view VALUES(21,'random','0.99,0.03,0.5');
INSERT INTO view VALUES(22,'random','0.52,0.78,0.39');
INSERT INTO view VALUES(23,'random','0.23,0.65,0.92');
INSERT INTO view VALUES(24,'random','0.13,0.04,0.39');
INSERT INTO view VALUES(25,'random','0.01,0.8,0.88');
INSERT INTO view VALUES(26,'random','0.53,0.7,0.45');
INSERT INTO view VALUES(27,'random','0.56,0.24,0.97');
INSERT INTO view VALUES(28,'random','0.64,0.49,0.23');
INSERT INTO view VALUES(29,'random','0.89,0.25,0.25');
INSERT INTO view VALUES(30,'random','0.53,0.95,0.96');
INSERT INTO view VALUES(31,'random','0.16,0.13,0.53');
INSERT INTO view VALUES(32,'random','0.09,0.51,0.63');
INSERT INTO view VALUES(33,'random','0.1,0.67,0.62');
INSERT INTO view VALUES(34,'random','0.12,0.47,0.52');
INSERT INTO view VALUES(35,'random','0.54,0.99,0.96');
INSERT INTO view VALUES(36,'random','0.64,0.49,0.63');
INSERT INTO view VALUES(37,'random','0.8,0.36,0.38');
INSERT INTO view VALUES(38,'random','0.54,0.46,0.22');
INSERT INTO view VALUES(39,'random','0.07,0.55,0.8');
INSERT INTO view VALUES(40,'random','0.64,0.15,0.65');
INSERT INTO view VALUES(41,'random','0.37,0.12,0.68');
INSERT INTO view VALUES(42,'random','0.28,0.81,0.53');
INSERT INTO view VALUES(43,'random','0.62,0.38,0.77');
INSERT INTO view VALUES(44,'random','0.86,0.34,0.24');
INSERT INTO view VALUES(45,'random','0.74,0.45,0.98');
INSERT INTO view VALUES(46,'random','0.63,0.46,0.25');
INSERT INTO view VALUES(47,'random','0.04,0.26,0.79');
INSERT INTO view VALUES(48,'random','0.81,0.39,0.1');
INSERT INTO view VALUES(49,'random','0.29,0.89,0.93');
INSERT INTO view VALUES(50,'random','0.05,0.88,0.71');
INSERT INTO view VALUES(51,'random','0.78,0.12,0.06');
INSERT INTO view VALUES(52,'random','0.55,0.49,0.98');
INSERT INTO view VALUES(53,'random','0.66,1.0,0.98');
INSERT INTO view VALUES(54,'random','0.06,0.97,0.46');
INSERT INTO view VALUES(55,'random','0.38,0.24,0.73');
INSERT INTO view VALUES(56,'random','0.6,0.4,0.5');
COMMIT;
