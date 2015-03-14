<?php
    require_once("newDB.php");
    class Question {
        private $id = "";
        private $question_type = "";
        private $question = "";
        private $correctanwser = "";
        private $option1 = "";
        private $option2 = "";
        private $option3 = "";
        private $option4 = "";
        private $hint = "";
        private $points = "";
        private $username = "";
        private $timelimit = "";
        private $is_validate = "";
        private $level = "";
        private $created_date = "";
        private $last_edit_date = "";
        private $course = "";
        private $topic = "";
        private $validator = "";

        public function get_id(){ return $this->id; }
        public function get_question_type(){ return $this->question_type; }
        public function get_question(){ return $this->question; }
        public function get_correctanwser(){ return $this->correctanwser; }
        public function get_option1(){ return $this->option1; }
        public function get_option2(){ return $this->option2; }
        public function get_option3(){ return $this->option3; }
        public function get_option4(){ return $this->option4; }
        public function get_hint(){ return $this->hint; }
        public function get_points(){ return $this->points; }
        public function get_username(){ return $this->username; }
        public function get_timelimit(){ return $this->timelimit; }
        public function get_is_validated(){ return $this->is_validate; }
        public function get_level(){ return $this->level; }
        public function get_created_date(){ return $this->created_date; }
        public function get_last_edit_date(){ return $this->last_edit_date; }
        public function get_course(){ return $this->course;}
        public function get_topic(){ return $this->topic; }
        public function get_validator(){ return $this->validator; }

        public function set_id($qid){ $this->id = $qid; }
        public function set_question_type($question_type){ $this->question_type = $question_type; }
        public function set_question($question){ $this->question = $question; }
        public function set_correctanwser($correctanwser){ $this->correctanwser = $correctanwser; }
        public function set_option1($option1){ $this->option1 = $option1; }
        public function set_option2($option2){ $this->option2 = $option2; }
        public function set_option3($option3){ $this->option3 = $option3; }
        public function set_option4($option4){ $this->option4 = $option4; }
        public function set_hint($hint){ $this->hint = $hint; }
        public function set_points($points){ $this->points = $points; }
        public function set_username($username){ $this->username = $username; }
        public function set_timelimit($timelimit){ $this->timelimit = $timelimit; }
        public function set_is_validated($is_validated){ $this->is_validate = $is_validated; }
        public function set_level($level){ $this->level = $level; }
        public function set_created_date($created_date){ $this->created_date = $created_date; }
        public function set_last_edit_date($last_edit_date){ $this->last_edit_date = $last_edit_date; }
        public function set_course($course){ $this->course = $course; }
        public function set_topic($topic){ $this->topic = $topic; }
        public function set_validator($validator){ $this->validator = $validator; }
    }

    class QuestionController {
        /**
        * Constructor for question controller
        * @todo to be written
        * @return
        */
        public function __construct(){}

        /**
        * Returns an instantiation of a new question object.
        * @return Question instatiation of a question object
        */
        public static function getQuestion(){ return new Question(); }

        /**
        * Gets a list of questions of a user.
        * The list is sorted by date.
        * @param int $userID user ID
        * @return array of Question objects sorted by date
        */
        public static function getUserQuestions($username) {
            $quesDataArr = getUserQuestions($username);
            $quesObjArr = array();
            for ($i = 0; $i < sizeof($quesDataArr); $i++) {
                $quesObj = QuestionController::getQuestion();
                $quesObj->set_id($quesDataArr[$i]['id']);
                $quesObj->set_question_type($quesDataArr[$i]['question_type']);
                $quesObj->set_question($quesDataArr[$i]['question']);
                $quesObj->set_correctanwser($quesDataArr[$i]['correctanswer']);
                $quesObj->set_option1($quesDataArr[$i]['option1']);
                $quesObj->set_option2($quesDataArr[$i]['option2']);
                $quesObj->set_option3($quesDataArr[$i]['option3']);
                $quesObj->set_option4($quesDataArr[$i]['option4']);
                $quesObj->set_hint($quesDataArr[$i]['hint']);
                $quesObj->set_points($quesDataArr[$i]['points']);
                $quesObj->set_username($quesDataArr[$i]['username']);
                $quesObj->set_timelimit($quesDataArr[$i]['timelimit']);
                $quesObj->set_is_validated($quesDataArr[$i]['is_validated']);
                $quesObj->set_level($quesDataArr[$i]['level']);
                $quesObj->set_created_date($quesDataArr[$i]['created_date']);
                $quesObj->set_last_edit_date($quesDataArr[$i]['last_edit_date']);
                $quesObj->set_course($quesDataArr[$i]['course']);
                $quesObj->set_topic($quesDataArr[$i]['topic']);
                $quesObj->set_validator($quesDataArr[$i]['validator']);
                array_push($quesObjArr, $quesObj);
            }
            return $quesObjArr;
        }

        public static function getUserPendingQuestions($userId) {
            $quesDataArr = getUserPendingQuestions($userId);
            $quesObjArr = array();
            for ($i = 0; $i < sizeof($quesDataArr); $i++) {
                $quesObj = QuestionController::getQuestion();
                $quesObj->set_id($quesDataArr[$i]['id']);
                $quesObj->set_question_type($quesDataArr[$i]['question_type']);
                $quesObj->set_question($quesDataArr[$i]['question']);
                $quesObj->set_correctanwser($quesDataArr[$i]['correctanswer']);
                $quesObj->set_option1($quesDataArr[$i]['option1']);
                $quesObj->set_option2($quesDataArr[$i]['option2']);
                $quesObj->set_option3($quesDataArr[$i]['option3']);
                $quesObj->set_option4($quesDataArr[$i]['option4']);
                $quesObj->set_hint($quesDataArr[$i]['hint']);
                $quesObj->set_points($quesDataArr[$i]['points']);
                $quesObj->set_username($quesDataArr[$i]['username']);
                $quesObj->set_timelimit($quesDataArr[$i]['timelimit']);
                $quesObj->set_is_validated($quesDataArr[$i]['is_validated']);
                $quesObj->set_level($quesDataArr[$i]['level']);
                $quesObj->set_created_date($quesDataArr[$i]['created_date']);
                $quesObj->set_last_edit_date($quesDataArr[$i]['last_edit_date']);
                $quesObj->set_course($quesDataArr[$i]['course']);
                $quesObj->set_topic($quesDataArr[$i]['topic']);
                $quesObj->set_validator($quesDataArr[$i]['validator']);
                array_push($quesObjArr, $quesObj);
            }
            return $quesObjArr;
        }

        public static function getUserRejectedQuestions($userId) {
            $quesDataArr = getUserRejectedQuestions($userId);
            $quesObjArr = array();
            for ($i = 0; $i < sizeof($quesDataArr); $i++) {
                $quesObj = QuestionController::getQuestion();
                $quesObj->set_id($quesDataArr[$i]['id']);
                $quesObj->set_question_type($quesDataArr[$i]['question_type']);
                $quesObj->set_question($quesDataArr[$i]['question']);
                $quesObj->set_correctanwser($quesDataArr[$i]['correctanswer']);
                $quesObj->set_option1($quesDataArr[$i]['option1']);
                $quesObj->set_option2($quesDataArr[$i]['option2']);
                $quesObj->set_option3($quesDataArr[$i]['option3']);
                $quesObj->set_option4($quesDataArr[$i]['option4']);
                $quesObj->set_hint($quesDataArr[$i]['hint']);
                $quesObj->set_points($quesDataArr[$i]['points']);
                $quesObj->set_username($quesDataArr[$i]['username']);
                $quesObj->set_timelimit($quesDataArr[$i]['timelimit']);
                $quesObj->set_is_validated($quesDataArr[$i]['is_validated']);
                $quesObj->set_level($quesDataArr[$i]['level']);
                $quesObj->set_created_date($quesDataArr[$i]['created_date']);
                $quesObj->set_last_edit_date($quesDataArr[$i]['last_edit_date']);
                $quesObj->set_course($quesDataArr[$i]['course']);
                $quesObj->set_topic($quesDataArr[$i]['topic']);
                $quesObj->set_validator($quesDataArr[$i]['validator']);
                array_push($quesObjArr, $quesObj);
            }
            return $quesObjArr;
        }

        public static function getUserApprovedQuestions($userId) {
            $quesDataArr = getUserApprovedQuestions($userId);
            $quesObjArr = array();
            for ($i = 0; $i < sizeof($quesDataArr); $i++) {
                $quesObj = QuestionController::getQuestion();
                $quesObj->set_id($quesDataArr[$i]['id']);
                $quesObj->set_question_type($quesDataArr[$i]['question_type']);
                $quesObj->set_question($quesDataArr[$i]['question']);
                $quesObj->set_correctanwser($quesDataArr[$i]['correctanswer']);
                $quesObj->set_option1($quesDataArr[$i]['option1']);
                $quesObj->set_option2($quesDataArr[$i]['option2']);
                $quesObj->set_option3($quesDataArr[$i]['option3']);
                $quesObj->set_option4($quesDataArr[$i]['option4']);
                $quesObj->set_hint($quesDataArr[$i]['hint']);
                $quesObj->set_points($quesDataArr[$i]['points']);
                $quesObj->set_username($quesDataArr[$i]['username']);
                $quesObj->set_timelimit($quesDataArr[$i]['timelimit']);
                $quesObj->set_is_validated($quesDataArr[$i]['is_validated']);
                $quesObj->set_level($quesDataArr[$i]['level']);
                $quesObj->set_created_date($quesDataArr[$i]['created_date']);
                $quesObj->set_last_edit_date($quesDataArr[$i]['last_edit_date']);
                $quesObj->set_course($quesDataArr[$i]['course']);
                $quesObj->set_topic($quesDataArr[$i]['topic']);
                $quesObj->set_validator($quesDataArr[$i]['validator']);
                array_push($quesObjArr, $quesObj);
            }
            return $quesObjArr;
        }

        public static function makeQuestion($question_type,$question,$correctanwser,$option1,$option2,$option3,$option4,$hint,$points,$username,$timelimit,$level,$course,$topic){
            $result= makeQuestion1($question_type,$question,$correctanwser,$option1,$option2,$option3,$option4,$hint,$points,$username,$timelimit,$level,$course,$topic);
            return $result;
        }

        public static function getThisQuestion1($quesID){
           $quesData=getThisQuestion($quesID);
           $quesObj = QuestionController::getQuestion();

               $quesObj->setQuestId($quesData['qid']);
               $quesObj->setUserId($quesData['uid']);
               //$quesObj->setCourseId($quesData['cid']);
               $quesObj->setQDate($quesData['date']);
               $quesObj->setVId($quesData['vid']);
               $quesObj->setVDate($quesData['vdate']);
               $quesObj->setQType($quesData['type']);
               $quesObj->setLevel($quesData['level']);
               $quesObj->setTitle($quesData['title']);
               $quesObj->setQuestion($quesData['question']);
               $quesObj->setStatus($quesData['status']);
               $quesObj->setGold($quesData['gold']);
               $quesObj->setFirst($quesData['first']);
               $quesObj->setSecond($quesData['second']);
               $quesObj->setThird($quesData['third']);
               $quesObj->setFourth($quesData['fourth']);
               $quesObj->setAnswer($quesData['answer']);
               $quesObj->setTime($quesData['timelimit']);
               //$quesObj->setTopic($quesData['topic']);
               $quesObj->setTid($quesData['tid']);

               return $quesObj;


   }

   public static function editQuestion($qid, $tid, $title, $level, $question, $gold, $first, $second, $third, $fourth, $answer, $timelimit){
       $type="";
       if($third !=""){
           $type="MC";
       }else{$type="TF" ;}

      if($third=="" || $third=="NULL"){
          $third="NULL";
      }
      if($fourth=="" || $fourth=="NULL"){
          $fourth="NULL";
      }

     $result= editQuestion($qid, $tid, $title, $type, $level, $question, $gold, $first, $second, $third, $fourth, $answer, $timelimit);

     return $result;
   }

   public static function getQuestionCourse($tid){
   //echo "tid is:". $tid ;
   $questionSid=getQuestionSid($tid);
   //echo "question sid is". $questionSid;
   $courseDataArr = getCourseSection($questionSid);
   //echo "course is: ". $courseDataArr;
   //$courseObj = CourseController::getCourse();
   //$courseObj->setSection($courseDataArr['section']);
   //$courseObj->setCId($courseDataArr['course']);
   $questionCourse=$courseDataArr['course']."-".$courseDataArr['section'];
   //echo "course & section is::".$questionCourse=$courseDataArr['course']."-".$courseDataArr['section'];
   //return $courseObj;
   return $questionCourse;
   }

   public static function getQuestionSID($tid){
       return $questionSid=getQuestionSid($tid);

   }

   public static function getQuestionTopic($tid){
   $questionTopic=getQuestionTopic($tid);
   return $questionTopic;

}
    /**
     * Gets a list of pending questions for the user.
     * The list is sorted by date.
     * @param $status
     * @return array of Question objects with status 'Pending' and sorted by date
     */

     public static function getPendingQuestions() {
		$pendingQuesArr = getPendingQuestions();
        $pendingQuesObjArr = array();

        for ($i = 0; $i < sizeof($pendingQuesArr); $i++) {
            $quesObj = QuestionController::getQuestion();

            $quesObj->setQuestId($pendingQuesArr[$i]['qid']);
			$quesObj->setQuestion($pendingQuesArr[$i]['question']);
            $quesObj->setLevel($pendingQuesArr[$i]['level']);
            $quesObj->setQType($pendingQuesArr[$i]['type']);
			$quesObj->setTime($pendingQuesArr[$i]['timelimit']);
            $quesObj->setQDate($pendingQuesArr[$i]['date']);
			$quesObj->setTid($pendingQuesArr[$i]['tid']);
			$quesObj->setUserId($pendingQuesArr[$i]['uid']);



            array_push($pendingQuesObjArr, $quesObj);
        }

        return $pendingQuesObjArr;

	}



	public static function approveQuestionV($vid,$ts,$qid,$uid) {
		$result=updateApprovedQuestionV($vid,$ts,$qid,$uid);
		return $result;
	}

	public static function rejectQuestionV($vid,$ts,$qid) {
		$result=updateRejectedQuestionV($vid,$ts,$qid);
		return $result;
	}

public static function getQuestionInfo($qid) {
    $quesDataArr= getQuestionInfo($qid);
    $questioninfoObj = array();
//    $size = sizeof($questioninfo);
//    echo "<script>alert($size );</script>";
    for ($i = 0; $i < sizeof($quesDataArr); $i++) {
        $quesObj = QuestionController::getQuestion();
//        $test = $quesDataArr[$i]['id'];
//        echo "$test";
//        $test = $quesDataArr[$i]['question_type'];
//        echo "$test";
        $quesObj->set_id($quesDataArr[$i]['id']);
        $quesObj->set_question_type($quesDataArr[$i]['question_type']);
        $quesObj->set_question($quesDataArr[$i]['question']);
        $quesObj->set_correctanwser($quesDataArr[$i]['correctanswer']);
        $quesObj->set_option1($quesDataArr[$i]['option1']);
        $quesObj->set_option2($quesDataArr[$i]['option2']);
        $quesObj->set_option3($quesDataArr[$i]['option3']);
        $quesObj->set_option4($quesDataArr[$i]['option4']);
        $quesObj->set_hint($quesDataArr[$i]['hint']);
        $quesObj->set_points($quesDataArr[$i]['points']);
        $quesObj->set_username($quesDataArr[$i]['username']);
        $quesObj->set_timelimit($quesDataArr[$i]['timelimit']);
        $quesObj->set_is_validated($quesDataArr[$i]['is_validated']);
        $quesObj->set_level($quesDataArr[$i]['level']);
        $quesObj->set_created_date($quesDataArr[$i]['created_date']);
        $quesObj->set_last_edit_date($quesDataArr[$i]['last_edit_date']);
        $quesObj->set_course($quesDataArr[$i]['course']);
        $quesObj->set_topic($quesDataArr[$i]['topic']);
        $quesObj->set_validator($quesDataArr[$i]['validator']);
        array_push($questioninfoObj, $quesObj);
        
    }
    return $questioninfoObj;
}

    public static function getQuestionsCL($course,$level)
	    {
	        $questioninfo = getQuestionsCL($course,$level);

			$questioninfoObj = array();

	        for ($i = 0; $i < sizeof($questioninfo); $i++) {
	            $quesObj = QuestionController::getQuestion();

	                        $quesObj->setQuestId($questioninfo[$i]['qid']);
				$quesObj->setQuestion($questioninfo[$i]['question']);
				$quesObj->setFirst($questioninfo[$i]['first']);
				$quesObj->setSecond($questioninfo[$i]['second']);
				$quesObj->setThird($questioninfo[$i]['third']);
				$quesObj->setFourth($questioninfo[$i]['fourth']);
				$quesObj->setAnswer($questioninfo[$i]['answer']);
				$quesObj->setGold($questioninfo[$i]['gold']);
				$quesObj->setQType($questioninfo[$i]['type']);
	                        $quesObj->setTime($questioninfo[$i]['timelimit']);
	            array_push($questioninfoObj, $quesObj);
	        }

	        return $questioninfoObj;

    }

    public static function updateQuestionLog($qid, $uid, $result) {
        $result = update_questionLog($qid, $uid, $result);
        return $result;
    }

    public static function getQuestionLog($uid) {
        $quesDataArr = get_questionLog($uid);
        return $quesDataArr;
    }

    public static function getFriendList($uid) {
        $quesDataArr = get_FriendsList($uid);
        return $quesDataArr;
    }
}
?>
