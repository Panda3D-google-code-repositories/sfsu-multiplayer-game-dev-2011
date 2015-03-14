<?php
    $con=mysql_connect("localhost", "deBuggerUser", "deBugger") or die("Query failed with error: ".mysql_error());
    mysql_select_db("deBuggerUser") or die("Query failed with error: ".mysql_error());


    function create_user ($fname,$lname,$uname,$email,$password){
        $fname = mysql_real_escape_string($fname);
        $lname = mysql_real_escape_string($lname);
        $uname = mysql_real_escape_string($uname);
        $email = mysql_real_escape_string($email);
        $password = mysql_real_escape_string($password);
        $password = md5($password);
        mysql_query("INSERT INTO user(first_name,last_name,username,email,password) VALUES ('" . $fname
            . "', '" .$lname."','".$uname."','".$email ."','" . $password ."')");
    }

    function get_user_id_by_username($username) {
        $username = mysql_real_escape_string($username);
        $result = mysql_query("SELECT user_id FROM user WHERE username = '"
            . $username . "'");
        if (mysql_num_rows($result) > 0)
            return mysql_result($result, 0);
        else
            return null;
    }

    function get_user_id_by_username_password($username,$password) {
        $uname= mysql_real_escape_string($username);
        $password = md5($password);
        $result = mysql_query("SELECT user_id FROM user WHERE username = '"
            . $username . "' AND password='".$password."'");
        if (mysql_num_rows($result) > 0)
            return mysql_result($result, 0);
        else
            return null;
    }

    function obtain_user($username){
        $sql = "SELECT * FROM user WHERE username='".$username."'";
        $result = mysql_query($sql) or die("Query failed with error: ".mysql_error());
        return( mysql_fetch_array($result));
    }

    function get_questionLog($uid) {
        $sql = "SELECT * FROM question_log WHERE user_id='".$uid."'";
        $result = mysql_query($sql);
        return $result;
    }

    function getQuestionInfo($id) {
	$sql = "SELECT * FROM questions WHERE id='".$id."'";
        $result = mysql_query($sql) or die("Query failed with error: ".mysql_error());
        $resultArr = array();
        while ($row = mysql_fetch_array($result)) {
            array_push($resultArr, $row);
        }
        return $resultArr;
    }

    function getAllFeedbacks($qid) {
	$sql = "SELECT * FROM comment_log WHERE question_id='".$qid."'";
	$result = mysql_query($sql) or die("Query failed with error: ".mysql_error());
	$resultArr = array();
	while ($row = mysql_fetch_array($result)) {
            array_push($resultArr, $row);
        }
        sort($resultArr);
        return $resultArr;
    }

    #Given a user_id, return username.
    function get_username_by_user_id($user_id) {
        $sql = "SELECT username FROM user WHERE user_id =".$user_id;
        $result = mysql_query($sql) or die("Query failed with error: ".mysql_error());
        $username = mysql_fetch_row($result);
        $username1 = $username[0];
        return $username1;
    }

    function makeQuestion1($question_type,$question,$correctanwser,$option1,$option2,$option3,$option4,$hint,$points,$username,$timelimit,$level,$course,$topic){
        $addTime = date("Y-m-d");
        $sql = "INSERT INTO questions(question_type, question, correctanswer, option1, option2, option3, option4, hint, points, username, timelimit, level, created_date, course, topic)
                VALUES ('".question_type."', '".$question."', '".$correctanwser."', '".$option1."', '".$option2."', '".$option3."', '".$option4."', '".$hint."', '".$points."', '".$username."', '".$timelimit."', '".$level."', '".$addTime."', '".$course."', '".$topic."')";
          if (mysql_query($sql)) {
            return mysql_insert_id();
        } else {
            return -1;
        }
    }

    function getUserQuestions($username) {
        $sql = "SELECT * FROM questions WHERE username='".$username."' ORDER BY id DESC";
        $result = mysql_query($sql);
        $resultArr = array();
        while ($row = mysql_fetch_array($result)) {
            array_push($resultArr, $row);
        }
        return $resultArr;
    }

    /**
     *
     * @param <type> $userID
     * @return <type>
     * returns the array of rows of pending questions of a particular user.
     *
     * function to be used in viewquestions.php
     */
    function getUserPendingQuestions($username){
        $sql = "SELECT * FROM questions WHERE username='".$username."' AND is_validate=0 ORDER BY id DESC";
        $result = mysql_query($sql);
        $resultArr = array();
        while ($row = mysql_fetch_array($result)) {
            array_push($resultArr, $row);
        }
        return $resultArr;
    }

    function getUserRejectedQuestions($userID){
        $sql = "SELECT * FROM questions WHERE username='".$username."' AND status=3 ORDER BY id DESC";
        $result = mysql_query($sql);
        $resultArr = array();
        while ($row = mysql_fetch_array($result)) {
            array_push($resultArr, $row);
        }
        return $resultArr;
    }

    function getUserApprovedQuestions($userID){
        $sql = "SELECT * FROM QuestionBank WHERE uid='".$userID."' AND status='Approved' ORDER BY qid DESC";
        $result = mysql_query($sql);
        $resultArr = array();
        while ($row = mysql_fetch_array($result)) {
            array_push($resultArr, $row);
        }
            return $resultArr;
    }
?>
