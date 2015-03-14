<?PHP
    session_start();
    require_once('user.php');
//    require_once('course.php');
    require_once('question.php');
    if(session_is_registered('userinfo')) {
        $serializedUser = $_SESSION['userinfo'];
        $userinfo1 = unserialize($serializedUser);
        $uname = $userinfo1->getUserName();
    }
?>
<?PHP
    $gold=0;

    $choice= $_POST['correct_answer'];
    switch($choice) {
        case 1:   $answer="first";  break;
        case 2:   $answer="second"; break;
        case 3:   $answer="third";  break;
        case 4:   $answer="fourth"; break;
        default:  break;
    }

    $level = 0;
    switch($_POST['level']) {
        case 'Easy':    $level=1;   break;
        case 'Medium':  $level=2;   break;
        case 'Hard':    $level=3;   break;
    }

    $course = (string)$_POST['course'];
    $scale = (int)substr($course, 4, 1);
    
    $gold = $scale * 10 + $level*10;

    $getType = $_POST['type'];
    switch($getType){
        case "Multiple Choice":     $type="MC"; break;
        case "True/False":          $type="TF"; break;
    }


//    $sid=CourseController::getSid($course,1);
//    $tid=CourseController::getTid($_POST['level'], $sid, $_POST['topic']);

    echo "question_type: ".$type."<br />";
    echo "question: ".$_POST['question']."<br />";
    echo "correctanwser: ".$_POST['correct_answer']."<br />";
    echo "option1: ".$_POST['first']."<br />";
    echo "option2: ".$_POST['second']."<br />";
    echo "option3: ".$_POST['third']."<br />";
    echo "option4: ".$_POST['fourth']."<br />";
    echo "hint: ".$_POST['hint']."<br />";
    echo "points: ".$gold."<br />";
    echo "username: ".$uname."<br />";
    echo "timelimit: ".$_POST['time']."<br />";
    echo "level: ".$level."<br />";
    echo "course: ".$_POST['course']."<br />";
    echo "topic: ".$_POST['topic']."<br />";

    $result = QuestionController::makeQuestion($type,$_POST['question'],$_POST['correct_answer'],$_POST['first'],$_POST['second'],$_POST['third'],$_POST['fourth'],$_POST['hint'],$gold,$uname,$_POST['time'],$level,$_POST['course'],$_POST['topic']);

    if ($result!= -1){
        echo "<meta http-equiv='refresh' content='0; url=../store_submitQuestionProcessed.php?result=1'>";
    } else {
        echo "<meta http-equiv='refresh' content='0; url=../store_submitQuestionProcessed.php?result=0'>";
    }
?>