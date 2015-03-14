<?php
    require_once("newDB.php");
    class User{
        private $user_id = "";
        private $username = "";
        private $student_id = "";
        private $first_name = "";
        private $last_name = "";
        private $gender = "";
        private $email = "";
        private $level = "";
        private $online = "";
        private $play_time = "";
        private $last_login = "";
        private $last_logout = "";
        private $last_ip = "";
        private $create_time = "";
        private $course = "";
        private $user_type = "";
        private $birthday = "";
        private $isBanned = "";
        private $picture_path = "";

        public function set_user_id($user_id){ $this->user_id = $user_id;}
        public function set_username($username){ $this->username = $username;}
        public function set_student_id($student_id){ $this->student_id = $student_id;}
        public function set_first_name($first_name){ $this->first_name = $first_name;}
        public function set_last_name($last_name){ $this->last_name = $last_name;}
        public function set_gender($gender){ $this->gender = $gender;}
        public function set_email($email){ $this->email = $email;}
        public function set_level($level){ $this->level = $level;}
        public function set_online($online){ $this->online = $online;}
        public function set_play_time($play_time){ $this->play_time = $play_time;}
        public function set_last_login($last_login){ $this->last_login = $last_login;}
        public function set_last_logout($last_logout){ $this->last_logout = $last_logout;}
        public function set_last_ip($last_ip){ $this->last_ip = $last_ip;}
        public function set_create_time($create_time){ $this->create_time = $create_time;}
        public function set_course($course){ $this->course = $course;}
        public function set_user_type($user_type){ $this->user_type = $user_type;}
        public function set_birthday($birthday){ $this->birthday = $birthday;}
        public function set_isBanned($isBanned){ $this->isBanned = $isBanned;}
        public function set_picture_path($picture_path){ $this->picture_path = $picture_path;}

        public function get_user_id(){ return $this->user_id;}
        public function get_username(){ return $this->username;}
        public function get_student_id(){ return $this->student_id;}
        public function get_first_name(){ return $this->first_name;}
        public function get_last_name(){ return $this->last_name;}
        public function get_gender(){ return $this->gender;}
        public function get_email(){ return $this->email;}
        public function get_level(){ return $this->level;}
        public function get_online(){ return $this->online;}
        public function get_play_time(){ return $this->play_time;}
        public function get_last_login(){ return $this->last_login;}
        public function get_last_logout(){ return $this->last_logout;}
        public function get_last_ip(){ return $this->last_ip;}
        public function get_create_time(){ return $this->create_time;}
        public function get_course(){ return $this->course;}
        public function get_user_type(){ return $this->user_type;}
        public function get_birthday(){ return $this->birthday;}
        public function get_isBanned(){ return $this->isBanned;}
        public function get_picture_path(){ return $this->picture_path;}
    }

    class UserController {
        public function __construct() {}
        public static function getUser() { return new User();}
        public static function create_user ($fname,$lname,$uname,$email,$password){
            create_user ($fname,$lname,$uname,$email,$password);
        }
        public static function obtain_user($username) {
            $userInfo = obtain_user($uname);
            $myUser = UserController::getUser();
            $myUser->set_user_id($userinfo['user_id']);
            $myUser->set_username($userinfo['username']);
            $myUser->set_student_id($userinfo['student_id']);
            $myUser->set_first_name($userinfo['first_name']);
            $myUser->set_last_name($userinfo['last_name']);
            $myUser->set_gender($userinfo['gender']);
            $myUser->set_email($userinfo['email']);
            $myUser->set_level($userinfo['level']);
            $myUser->set_online($userinfo['online']);
            $myUser->set_play_time($userinfo['play_time']);
            $myUser->set_last_login($userinfo['last_login']);
            $myUser->set_last_logout($userinfo['last_logout']);
            $myUser->set_last_ip($userinfo['last_ip']);
            $myUser->set_create_time($userinfo['create_time']);
            $myUser->set_course($userinfo['course']);
            $myUser->set_user_type($userinfo['user_type']);
            $myUser->set_birthday($userinfo['birthday']);
            $myUser->set_isBanned($userinfo['isBanned']);
            $myUser->set_picture_path($userinfo['picture_path']);
            return $myUser;
        }
        public static function get_user_id_by_username($username) {
            return (get_user_id_by_username($username));
        }
        public static function get_user_id_by_username_password($username,$password) {
            return (get_user_id_by_username_password($username,$password));
        }
        public static function get_username_by_user_id($user_id) {
            $username = get_username_by_user_id($user_id);
            return $username;
        }
    }
?>
