<?php

$type = $_GET['type'];
$user_id = $_GET['user_id'];
$q_value = $_GET['value'];
$q_question_id = $_GET['question_id'];

$con = mysql_connect("thecity.sfsu.edu", "deBuggerUser", "deBugger");
$db = mysql_select_db('deBuggerUser', $con);

if ($type == '' && $user_id == '' && $q_value == '' && $q_question_id == '') {
    $result = mysql_query("SELECT * FROM `user` WHERE `user_id` >= 350 ORDER BY `last_name`");

    echo "
        <html>
        <head>
        <script type='text/javascript'>
        function setView(type) {
            var type_lists = document.getElementsByName('type_list');

            for each(var type_list in type_lists) {
                type_list.value = type;
                getGameData(type, type_list.id);
            }
        }

        function getGameData(type, user_id) {
            var xmlhttp;

            if (window.XMLHttpRequest) {
                xmlhttp = new XMLHttpRequest();
            }

            xmlhttp.onreadystatechange = function() {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                    document.getElementById('data_' + user_id).innerHTML = xmlhttp.responseText;
                }
            }

            var query_string = '?type=' + type + '&user_id=' + user_id;
            xmlhttp.open('GET', 'activity.php' + query_string, true);
            xmlhttp.send();
        }

        function getQuestion(value, question_id) {
            var xmlhttp;

            if (window.XMLHttpRequest) {
                xmlhttp = new XMLHttpRequest();
            }

            xmlhttp.onreadystatechange = function() {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                    document.getElementById('question_' + question_id).innerHTML = xmlhttp.responseText;
                }
            }

            var query_string = '?value=' + value + '&question_id=' + question_id;
            xmlhttp.open('GET', 'activity.php' + query_string, true);
            xmlhttp.send();
        }
        </script>
        </head>
        <body>
        <table width='768' cellspacing='1'>
            <tr id='main'>
                <td width=125>
                    <select onchange='setView(value)'>
                        <option value=''>Hide</option>
                        <option value='tpd'>Time Spent</option>
                        <option value='bh'>Bug Hunting</option>
                        <option value='td'>Top Down</option>
                        <option value='code'>Coding</option>
                        <option value='var'>Variables</option>
                    </select>
                </td>
                <td><i>Rank</i></td>
                <td><i>Name</i></td>
                <td><i>Student ID</i></td>
                <td><i>Level</i></td>
                <td><i>Hours</i></td>
                <td><i>Last Activity</i></td>
                <td><i>Online</i></td>
            </tr>";

    while ($row = mysql_fetch_assoc($result)) {
        $user_id = $row['user_id'];
        $name = $row['last_name'] . ', ' . $row['first_name'];
        $student_id = $row['student_id'];
        $online = $row['online'];
        $time = round($row['play_time'] / 360, 2);
        $last_login = date('m-d-Y', strtotime($row['last_login']));
        $last_logout = date('m-d-Y', strtotime($row['last_logout']));

        if ($online == 0) {
            $online = 'No';
        } else {
            $online = 'Yes';
        }

        $last_activity = '-';

        if (strcmp($last_logout, "01-01-1970") == 0) {
            $last_activity = '-';
        } else {
            if ($last_login > $last_logout) {
                $last_activity = $last_login;
            } else {
                $last_activity = $last_logout;
            }
        }

        $result3 = mysql_query("SELECT * FROM `character` WHERE `user_id` = $user_id");

        $char_id = 0;
        if ($row3 = mysql_fetch_assoc($result3)) {
            $char_id = $row3['char_id'];
            $char_name = $row3['name'];
            $char_level = $row3['level'];
        }

        $result4 = mysql_query("SELECT * FROM `leaderboard` WHERE `char_id` = $char_id");

        if ($row4 = mysql_fetch_assoc($result4)) {
            $rank = $row4['rank'];
        }

        echo "
            <tr>
                <td>
                    <select id=$user_id name='type_list' onchange='getGameData(value, $user_id)'>
                        <option value=''>Hide</option>
                        <option value='tpd'>Time Spent</option>
                        <option value='bh'>Bug Hunting</option>
                        <option value='code'>Coding</option>
                        <option value='td'>Top Down</option>
                        <option value='var'>Variables</option>
                    </select>
                </td>
                <td>$rank</td>
                <td>$name <br /> [ $char_name ]</td>
                <td>$student_id</td>
                <td>$char_level</td>
                <td>$time</td>
                <td>$last_activity</td>
                <td>$online</td>
            </tr>
            <tr>
                <td colspan='8' id='data_$user_id' />
            </tr>";
    }

    echo "</table>";

    echo "<table width='320' border='1' cellpadding='3'>
              <tr>
                  <td colspan='1' align='center'><i>Comments</i></td>
              </tr>";

    $result = mysql_query("SELECT * FROM `comment_log` c JOIN `user` u ON c.`user_id` = u.`user_id` ORDER BY `question_id`");
    
    $question_id = -1;
    
    while ($row = mysql_fetch_assoc($result)) {
        $q_id = $row['question_id'];

        if ($q_id != $question_id) {
            $question_id = $q_id;

            echo "    <tr>
                          <td align='center'>
                              <select id=$question_id name='question_list' onchange='getQuestion(value, $question_id)'>
                                  <option value=''>Hide Question</option>
                                  <option value='show'>Show Question</option>
                              </select>
                              <div id='question_$question_id' />
                          </td>
                      </tr>";
        }

        $first_name = $row['first_name'];
        $last_name = $row['last_name'];
        $subject = $row['subject'];
        $message = $row['message'];
        $rating = $row['rating'];
        $create_time = $row['create_time'];

        echo "    <tr>
                      <td>
                          Name: $first_name $last_name <br />
                          Subject: $subject <br />
                          Date: $create_time <br />
                          Message: $message <br />
                          $rating Stars
                      </td>
                  </tr>";
    }

    echo "</table>";

    echo "</body>
          </html>";
} else if ($type != '' && $user_id != '') {
    if ($type != '') {
        $con = mysql_connect("thecity.sfsu.edu", "deBuggerUser", "deBugger");
        $db = mysql_select_db('deBuggerUser', $con);

        $result = mysql_query("SELECT * FROM `character` WHERE `user_id` = $user_id");

        $char_id = 0;
        if ($row = mysql_fetch_assoc($result)) {
            $char_id = $row['char_id'];
        }

        if ($type == 'tpd') {
            $result = mysql_query("SELECT * FROM `user_log_tpd` WHERE `user_id` = $user_id");

            if (mysql_num_rows($result) > 0) {
                echo "
                <br />
                <table width='640' border='1' cellpadding='3'>
                <tr>
                    <td><i>Week (Hours)</i></td>
                    <td><i>Sun</i></td>
                    <td><i>Mon</i></td>
                    <td><i>Tue</i></td>
                    <td><i>Wed</i></td>
                    <td><i>Thu</i></td>
                    <td><i>Fri</i></td>
                    <td><i>Sat</i></td>
                    <td><i>Daily Average</i></td>
                </tr>
            ";

                while ($row = mysql_fetch_assoc($result)) {
                    $week = date("m-d-Y", strtotime($row['date_start']));
                    $day_0 = round($row['day_0'] / 360, 2);
                    $day_1 = round($row['day_1'] / 360, 2);
                    $day_2 = round($row['day_2'] / 360, 2);
                    $day_3 = round($row['day_3'] / 360, 2);
                    $day_4 = round($row['day_4'] / 360, 2);
                    $day_5 = round($row['day_5'] / 360, 2);
                    $day_6 = round($row['day_6'] / 360, 2);
                    $d_avg = round(($day_0 + $day_1 + $day_2 + $day_3 + $day_4 + $day_5 + $day_6) / 7, 2);

                    echo "
                    <tr>
                        <td>$week</td>
                        <td>$day_0</td>
                        <td>$day_1</td>
                        <td>$day_2</td>
                        <td>$day_3</td>
                        <td>$day_4</td>
                        <td>$day_5</td>
                        <td>$day_6</td>
                        <td>$d_avg</td>
                    </tr>
                ";
                }

                echo "
                    </table>
                    <br />
                ";
            } else {
                echo "
                    <i>No Record</i>
                ";
            }
        } else if ($type == 'bh') {
            $result = mysql_query("SELECT * FROM `leaderboard` WHERE `char_id` = $char_id");

            if ($row = mysql_fetch_assoc($result)) {
                $correct = $row['correct'];
                $wrong = $row['wrong'];
                $grade = $row['grade'];

                if ($grade == 0) {
                    $grade = '-';
                } else {
                    $grade = $grade * 100 . '%';
                }
            }

            if ($correct + $wrong > 0) {
                echo "
                <br />
                <table border='1' cellpadding='3'>
                <tr>
                    <td colspan='3' align='center'>Overall</td>
                </tr>
                <tr>
                    <td><i>Q. Correct</i></td>
                    <td><i>Q. Wrong</i></td>
                    <td><i>Grade</i></td>
                </tr>
                <tr>
                    <td>$correct</td>
                    <td>$wrong</td>
                    <td>$grade</td>
                </tr>
                </table>
                <br />
            ";
            } else {
                echo "
                    <i>No Record</i>
                ";
            }
            
            $result = mysql_query("SELECT * FROM `statistics` WHERE `char_id` = $char_id");

            if ($row = mysql_fetch_assoc($result)) {
                for ($i = 1; $i <= 10; $i++) {
                    if ($i == 7) {
                        continue;
                    }

                    $correct = $row['ch' . $i . '_correct'];
                    $wrong = $row['ch' . $i . '_wrong'];

                    if ($correct + $wrong > 0) {
                        if ($wrong == 0) {
                            $ratio = round($correct, 2);
                        } else {
                            $ratio = round($correct / $wrong, 2);
                        }

                        $grade = round($correct / ($correct + $wrong), 3);

                        if ($grade == 0) {
                            $grade = '-';
                        } else {
                            $grade = $grade * 100 . '%';
                        }

                        echo "
                        <table border='1' cellpadding='3'>
                        <tr>
                            <td colspan='4' align='center'>Chapter $i</td>
                        </tr>
                        <tr>
                            <td><i>Q. Correct</i></td>
                            <td><i>Q. Wrong</i></td>
                            <td><i>Ratio</i></td>
                            <td><i>Grade</i></td>
                        </tr>
                        <tr>
                            <td>$correct</td>
                            <td>$wrong</td>
                            <td>$ratio</td>
                            <td>$grade</td>
                        </tr>
                        </table>
                        <br />
                    ";
                    }
                }
            }
        } else if ($type == 'code') {
            $result = mysql_query("SELECT * FROM `code_log` WHERE `char_list` = $char_id");

            if (mysql_num_rows($result) > 0) {
                echo "
                <br />
                <table border='1' cellpadding='3'>
                <tr>
                    <td><i>Game No.</i></td>
                    <td><i>Level No.</i></td>
                    <td><i>Question ID</i></td>
                    <td><i>Check Type</i></td>
                    <td><i>Success</i></td>
                    <td><i>Seconds</i></td>
                </tr>
            ";

                while ($row = mysql_fetch_assoc($result)) {
                    $session_id = $row['session_id'];

                    $result2 = mysql_query("SELECT *, TIME_TO_SEC(TIMEDIFF(`time_end`, `time_start`)) AS time FROM `code_log_level` WHERE `session_id` = $session_id AND `order` != ''");

                    while ($row2 = mysql_fetch_assoc($result2)) {
                        $level = $row2['level'];
                        $question_id = $row2['question_id'];
                        $check_type = $row2['check_type'];

                        if ($check_type == 0) {
                            $check_type = 'Regular';
                        } else {
                            $check_type = 'Compile';
                        }

                        $status = $row2['status'];

                        if ($status == 1) {
                            $status = 'Yes';
                        } else {
                            $status = 'No';
                        }

                        $time = $row2['time'];

                        echo "
                        <tr>
                            <td>$session_id</td>
                            <td>$level</td>
                            <td>$question_id</td>
                            <td>$check_type</td>
                            <td>$status</td>
                            <td>$time</td>
                        </tr>
                    ";
                    }
                }
                echo "
                    </table>
                    <br />
                ";
            } else {
                echo "
                    <i>No Record</i> 
                ";
            }
        } else if ($type == 'td') {
            $result = mysql_query("SELECT * FROM `td_log` WHERE `char_list` = $char_id");

            if (mysql_num_rows($result) > 0) {
                echo "
                   <br />
                   <table border='1' cellpadding='3'>
                   <tr>
                       <td><i>Game No.</i></td>
                       <td><i>Level No.</i></td>
                       <td><i>Question ID</i></td>
                       <td><i>Success</i></td>
                       <td><i>Seconds</i></td>
                   </tr>
                   ";

                while ($row = mysql_fetch_assoc($result)) {
                    $session_id = $row['session_id'];

                    $result2 = mysql_query("SELECT *, TIME_TO_SEC(TIMEDIFF(`time_end`, `time_start`)) AS time FROM `td_log_level` WHERE `session_id` = $session_id AND `status` != 0");

                    while ($row2 = mysql_fetch_assoc($result2)) {
                        $level = $row2['level'];
                        $question_id = $row2['question_id'];

                        $status = $row2['status'];

                        if ($status == 1) {
                            $status = 'Yes';
                        } else if ($status == 2) {
                            $status = 'No';
                        }

                        $time = $row2['time'];

                        echo "
                        <tr>
                            <td>$session_id</td>
                            <td>$level</td>
                            <td>$question_id</td>
                            <td>$status</td>
                            <td>$time</td>
                        </tr>
                    ";
                    }
                }
                echo "
                    </table>
                    <br />
                ";
            } else {
                echo "
                    <i>No Record</i> 
                ";
            }
        } else if ($type == 'var') {
            $result = mysql_query("SELECT * FROM `var_log` WHERE `char_list` = $char_id");

            if (mysql_num_rows($result) > 0) {
                echo "
                <br />
                <table border='1' cellpadding='3'>
                <tr>
                    <td><i>Game No.</i></td>
                    <td><i>Level No.</i></td>
                    <td><i>Last Step No.</i></td>
                    <td><i>Question ID</i></td>
                    <td><i>Success</i></td>
                    <td><i>Seconds</i></td>
                </tr>
                ";

                while ($row = mysql_fetch_assoc($result)) {
                    $session_id = $row['session_id'];

                    $result2 = mysql_query("SELECT *, TIME_TO_SEC(TIMEDIFF(`time_end`, `time_start`)) AS time FROM `var_log_level` WHERE `session_id` = $session_id AND `status` != 0");

                    while ($row2 = mysql_fetch_assoc($result2)) {
                        $level = $row2['level'];
                        $step_num = $row2['step_num'] + 1;
                        $question_id = $row2['question_id'];

                        $status = $row2['status'];

                        if ($status == 1) {
                            $status = 'Yes';
                        } else if ($status == 2) {
                            $status = 'No';
                        } else if ($status == 3) {
                            $status = 'No';
                        }

                        $time = $row2['time'];

                        echo "
                        <tr>
                            <td>$session_id</td>
                            <td>$level</td>
                            <td>$step_num</td>
                            <td>$question_id</td>
                            <td>$status</td>
                            <td>$time</td>
                        </tr>
                    ";
                    }
                }
                echo "
                    </table>
                    <br />
                ";
            } else {
                echo "
                    <i>No Record</i>             
                ";
            }
        }
    } else {
        echo "";
    }
} else if ($q_value != '' && $q_question_id != '') {
    if ($q_value == 'show') {
        $result = mysql_query("SELECT * FROM `questions` WHERE `question_id` = $q_question_id");

        if ($row = mysql_fetch_assoc($result)) {
            $question = $row['question'];

            echo "<br/ >
                  $question";
        }
    }
}
?>
