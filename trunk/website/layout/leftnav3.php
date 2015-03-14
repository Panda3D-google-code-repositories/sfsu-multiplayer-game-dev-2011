    <script type="text/javascript">
        function initMenus() {
            $.each($('ul.menu'), function(){
                    $('#' + this.id + '.expandfirst ul:first').show();
            });
            $('ul.menu li a').click(
                function() {
                    var checkElement = $(this).next();
                    var parent = this.parentNode.parentNode.id;

                    if($('#' + parent).hasClass('noaccordion')) {
                        $(this).next().slideToggle('normal');
                        return false;
                    }
                    if((checkElement.is('ul')) && (checkElement.is(':visible'))) {
                        if($('#' + parent).hasClass('collapsible')) {
                            $('#' + parent + ' ul:visible').slideUp('normal');
                        }
                        return false;
                    }
                    if((checkElement.is('ul')) && (!checkElement.is(':visible'))) {
                        $('#' + parent + ' ul:visible').slideUp('normal');
                        checkElement.slideDown('normal');
                        return false;
                    }
                }
            );
        }
        $(document).ready(function() {initMenus();});
    </script>

    <style type="text/css">
        ul.menu, ul.menu ul {
          list-style-type:none;
          margin: 0px 0px 0px 0px;
          padding: 0px;
          width: 194px;
        }

        ul.menu a {
          display: block;
          text-decoration: none;
        }

        ul.menu li {
          width:  auto;
        }

        ul.menu li a {
          background: #996633;
          color: #FFF;
          padding: 5px;
        }

        ul.menu li a:hover {
            background: #d5c8a4;
        }

        ul.menu li ul li a {
          background: #FDF5E6;
          color: #000;
          padding-left: 20px;
        }

        ul.menu li ul li a:hover {
          background: #d5c8a4;
          border-left: 5px #875a01 solid;
          padding-left: 15px;
        }
    </style>

    <body>
        <div id="navleft">
            <div class ="menu_container_brown">
                <ul id="menu1" class="menu noaccordion expandfirst">
                    <li>
                        <a href="#">Downloads</a>
                        <ul>
                            <li><a href="download_game_client.php">Game Client</a></li>
                            <li><a href="download_screen_shots.php">Images</a></li>
                            <li><a href="download_videos.php">Videos</a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
