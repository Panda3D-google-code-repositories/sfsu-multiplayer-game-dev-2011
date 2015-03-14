<?php
    require_once("newDB.php");

    class Feedback {
        private $user_id;
        private $char_id;
        private $question_id;
        private $subject;
        private $message;
        private $rating;

        public function setuser_id($uid) {
            $this->user_id = $uid;
        }
        public function setchar_id($cid) {
            $this->char_id = $cid;
        }
        public function setquestion_id($qid) {
            $this->question_id = $qid;
        }
        public function setsubject($subj) {
            $this->subject = $subj;
        }
        public function setmessage($msg) {
            $this->message = $msg;
        }
        public function setrating($rate) {
            $this->rating = $rate;
        }

        public function getuser_id() {
            return $this->user_id;
        }
        public function getchar_id() {
            return $this->char_id;
        }
        public function getquestion_id() {
            return $this->question_id;
        }
        public function getsubject() {
            return $this->subject;
        }
        public function getmessage() {
            return $this->message;
        }
        public function getrating() {
            return $this->rating;
        }
    }

    class FeedbackController {
        /**
         * Constructor for question controller
         * @todo to be written
         * @return
         */
        public function __construct() {}

        /**
         * Returns an instantiation of a new question object.
         * @return Question instatiation of a question object
         */
        public static function getFeedback() {
            return new Feedback();
        }

        public static function getAllFeedbacks($qid) {
            $allFeedbackArr = getAllFeedbacks($qid);
            $allFeedbackObjArr = array();
            for ($i = 0; $i < sizeof($allFeedbackArr); $i++) {
                $fbObj = FeedbackController::getFeedback();
                $fbObj->setuser_id($allFeedbackArr[$i]['user_id']);
                $fbObj->setchar_id($allFeedbackArr[$i]['char_id']);
                $fbObj->setquestion_id($allFeedbackArr[$i]['question_id']);
                $fbObj->setsubject($allFeedbackArr[$i]['subject']);
                $fbObj->setmessage($allFeedbackArr[$i]['message']);
                $fbObj->setrating($allFeedbackArr[$i]['rating']);
                array_push($allFeedbackObjArr, $fbObj);
            }
            return $allFeedbackObjArr;
        }

        public static function create_feedback ($qid,$reviewer,$comment,$rating){
            create_feedback ($qid,$reviewer,$comment,$rating);
        }
    }
?>
