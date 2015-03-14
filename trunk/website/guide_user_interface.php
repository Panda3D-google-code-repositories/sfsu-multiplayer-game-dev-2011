<?php include "layout/header.php"; ?>
<?php include "layout/leftnav2.php"; ?>
    <style type="text/css">
        .screen_shot {
            max-width: 638px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-top: 20px;
            margin-bottom: 20px;
            border: 3px solid #d5c8a4;
        }

        .screen_shot2 {
            display: block;
            margin-left: auto;
            margin-right: auto;
            margin-top: 20px;
            margin-bottom: 20px;
            max-width: 638px;
            border: 3px solid #d5c8a4;
        }
    </style>
    <div class="content_container">
        <h1>User Interface</h1>
        <img src="screen_shots/image_12.png" alt="" class="screen_shot"/>
        <div class="container_brown">
            <p><font color="white">White</font>: Environment Score tells you how well your ecosystem is doing, the higher the better. There are many ways to bring up the score such as purchasing more species and allowing the population to grow.</p>
            <p><font color="orange">Orange</font>: Game Time simply tells you how much time has past since you started the world.</p>
            <p><font color="red">Red</font>: Shop allows you to purchase a variety of different species. The cost is different for each species. The list grows as you level higher. There are multiple categories of species and are filtered using the drop-down menu in the upper-left.</p>
            <p><font color="blue">Blue</font>: Stats Bar shows your current level, experience required to level up and the total amount of gold you currently have.</p>
            <p><font color="yellow">Yellow</font>: Chat allows you communicate with other online players. The name and message will be shown as it is received.</p>
            <p><font color="green">Green</font>: Top Scores shows the top 3 players' score from 3 categories, which are High Score, Total Score, Current Score. High Score represents the highest Environment Score one has ever achieved. Total Score represents the most accumulated score. Current Score represents those that currently holds the highest score.</p>
            <p><font color="purple">Purple</font>: Number of active players online, which includes you and others, if any.</p>
            <p><font color="brown">Brown</font>: Menu provide a few options such as being able change the volume and quitting the game.</p>
            <p><font color="cyan">Cyan</font>: Avatar is simply just an in-game visual representation of you as a player.</p>
            <p><font color="magenta">Magenta</font>: Extra Features such as Stats, which displays the changes in population, Charts, which provides you with graphs that show the change that has happened over time, Params, which is short for parameters that allows you to change metabolic, growth, and other rates that affect the different species.</p>
        </div>
        <br />
        <h2>Shop</h2>
        <img src="screen_shots/image_11.png" alt="" class="screen_shot2"/>
        <div class="container_brown">
            <p>The Shop is a very important feature that allows you to purchase species to be added into the ecosystem. You will be limited to a small set of species in the very beginning, but as soon as you play long enough and have progressed to a higher level, more species will be made available.</p>
            <p>Refer to the <a href="guide_game_tips.php">Game Tips</a> section for the complete list of species that can be unlocked.</p>
            <p>Species are broken up into multiple categories. Using the drop-down menu available at the upper-left, you can access these categories. Categories are made available whenever there is a species of that type available.</p>
            <p>Each species also comes attached with a cost displayed at the lower-right of its image. You must have enough gold to purchase a given species.</p>
        </div>
        <img src="screen_shots/image_18.jpg" alt="" class="screen_shot2"/>
        <div class="container_brown">
             <p>Moving your mouse over any given species in the Shop will bring up an information box shown above. It provides useful information such description, cost, biomass, preys, and predators. Whenever a species listed under preys or predators is available to purchase, the name will be displayed in white. If not available, it will be displayed in gray.</p>
        </div>
        <h2>Stats Bar</h2>
        <img src="screen_shots/image_17.jpg" alt="" class="screen_shot"/>
        <div class="container_brown">
            <p>The Stats Bar is divided into 3 sections--level, experience, and gold.</p>
            <p><b>Level</b> represents the amount of times you've filled up the experience bar. The next level will always require more experience than the one before. Every player is capped at level 10, but will be raised as more content is added.</p>
            <p><b>Experience</b> is gained by fulfilling different tasks such as purchasing species from the shop and playing for a certain length of time.</p>
            <p><b>Gold</b> is the game's currency system. At this time, it is only used to purchase species from the Shop. Gold will be given at the end of each month and over time as a bonus.</p>
        </div>
        <br />
        <h2>System Messages</h2>
        <img src="screen_shots/image_14.jpg" alt="" class="screen_shot"/>
        <div class="container_brown">
            <p><font color="red">Left Area</font> displays the amount of experience and gold gained. Also shows how much gold has been deducted from purchases.</p>
            <p><font color="blue">Right Area</font> displays messages of the births and deaths of organisms and species. Births are represented in green and deaths are represented in gray.</p>
        </div>
        <br />
        <h2>Chat Box</h2>
        <img src="screen_shots/image_13.jpg" alt="" class="screen_shot"/>
        <div class="container_brown">
            <p>The Chat Box allow players to communicate between worlds simply by typing a message into the text field. Players are distinguished by different colors as it appears in the log. Pressing the Enter key anywhere in the game will help focus the text field for entry. Pressing it again will close it.</p>
        </div>
        <br />
        <h2>Top Scores</h2>
        <center>
            <table>
                <tr>
                    <td><img src="screen_shots/image_15.jpg" alt="" class="screen_shot"/></td>
                    <td><img src="screen_shots/image_16.jpg" alt="" class="screen_shot"/></td>
                </tr>
            </table>
        </center>
        <div class="container_brown">
            <p>Top Scores alternate between two sets of scores. One will show only your best scores and the other will show the top 3 players of each category.</p>
            <p><b>High Score</b> represents the highest Environment Score one has ever achieved.</p>
            <p><b>Total Score</b> represents the most accumulated score. Score accumulates at the end of each month.</p>
            <p><b>Current Score</b> represents those that currently holds the highest Environment Score.</p>
        </div>
        <br />
        <h2>Chart System</h2>
        <img src="screen_shots/image_09.jpg" alt="" class="screen_shot"/>
        <div class="container_brown">
            <p>The Chart System is a very helpful tool that tracks different changes in a period of up to 10 months. There are a total of 3 different types of data that can be graphed, which can be selected from the drop-down menu in the upper-right.</p>
            <p><b># of Organisms</b> shows the size of each species by the number of organisms of each group. Each species is represented by a different color.</p>
            <p><b>Biomass</b> shows the amount of biomass for each species recorded from the different months.</p>
            <p><b>Environment Score</b> shows the change of your score throughout each month. This can help you tell how well your ecosystem has been doing before compared to now.</p>
            <p>Each chart can be manipulated by hiding each line of data by clicking on their names to the right. In doing so, the graphs may be recalculated and redrawn to only represent the data visible. This is very helpful when you want to examine the data closer and being able to work with a smaller set of data.</p>
            <p>Another handy tip, which is being able to see the value at each point of the line by moving your mouse over it.</p>
        </div>
        <br />
        <h2>Parameter Modifications</h2>
        <img src="screen_shots/image_07.jpg" alt="" class="screen_shot"/>
        <div class="container_brown">
            <p>Developing...</p>
        </div>
        <br />
        <h2>Stats</h2>
        <img src="screen_shots/image_08.jpg" alt="" class="screen_shot"/>
        <div class="container_brown">
            <p>Developing...</p>
        </div>
        <br />
    </div>
<?php include "layout/footer2.php"; ?>