<?php include "layout/header.php"; ?>
<?php include "layout/leftnav2.php"; ?>
    <style type="text/css">
        #search {
            margin-top: 30px;
            margin-bottom: 30px;
            text-align: center;
        }

        #search input {
            width: 200px;
        }

        #f_menu {
            padding-bottom: 20px;
        }

        #f_menu h2 {
            font-size: 14px;
        }

        #f_menu table {
            width: 100%;
        }

        #f_menu .type, .select {
            padding-left: 5px;
            padding-right: 5px;
            width: 1px;
        }

        #f_menu #sort, #show {
            text-align: right;
        }

        #j_menu {
            text-align: right;
        }
        
        .top {
            margin-bottom: 10px;
            margin-right: 10px;
            text-align: right;
        }

        .alpha_h {
            font-size: 18px;
        }

        .profile table {
            background-color: #FAEBD7;
            border-style: none solid solid none;
            width: 100%;
        }

        .profile table, td, th {
            border-color: #d5c8a4;
            border-width: 3px;
        }

        .profile td, th {
            border-style: solid none none solid;
            padding: 5px;
        }

        .name {
            font-size: 16px;
        }

        .species_img {
            height: 100px;
            width: 100px;
        }

        .species_img img {
            border: 3px solid #d5c8a4;
            display: block;
            height: 64px;
            margin-left: auto;
            margin-right: auto;
            width: 64px;
        }

        .stat {
            height: 25px;
            width: 200px;
        }

        .description, .prey, .predator {
            
        }
		.edit_button {
			float:right;
		}
        .div_empty {
            text-align: center;
        }
        
        .param_table table{
            background: #FAEBD7;
		    border: 3px solid #d5c8a4;
		    padding: 10px;
		    width : 100%;
		    display:block;
        }
        
        .param_stat {
            height: 25px;
            width: 400px;
            border: 1px solid #d5c8a4;
        }
        
    </style>
    <script type="text/javascript">
        function setFilter() {
            var filter_cat = document.getElementById("filter_cat").value;

            if (filter_cat == "resource") {
                $("#filter_class option").each(function() {
                    $(this).hide()
                });

                $("#filter_class option[value=" + "" + "]").show()
                $("#filter_class").val("").attr("selected", true);
            } else if (filter_cat != "plant") {
                $("#filter_class option").each(function() {
                    $(this).show()
                });

                if (filter_cat != "") {
                    $("#filter_class option[value=" + "producer" + "]").hide()

                    if ($("#filter_class").val() == "producer") {
                        $("#filter_class").val("").attr("selected", true);
                    }
                }
            } else if (filter_cat == "plant") {
                $("#filter_class option").each(function() {
                    $(this).hide()
                });

                $("#filter_class option[value=" + "producer" + "]").show()
                $("#filter_class").val("producer").attr("selected", true);
            }

            var filter_class = document.getElementById("filter_class").value;
            var filter_av = document.getElementById("filter_av").value;
            var filter_show = document.getElementById("filter_show").value;
            var filter_sort = document.getElementById("filter_sort").value;

            var query_string = "?cat=" + filter_cat + "&class=" + filter_class + "&av=" + filter_av + "&show=" + filter_show + "&sort=" + filter_sort;
            var url = "species_content.php" + query_string;
            createRequest("species_content", url);
        }

        $(function() {

<?php
    $con = mysql_connect("smurf.sfsu.edu", "BeastReality", "beastreality");
    $db = mysql_select_db("BeastRealityDB", $con);

    $result = mysql_query("SELECT `species_name` AS `name`
                           FROM (
                               SELECT `species_name`
                               FROM `animal_type`
                               WHERE `animal_type_id`
                               NOT IN (54, 58, 62, 76, 78, 79, 81, 84)

                               UNION

                               SELECT `species_name`
                               FROM `plant_type`
                               WHERE `plant_type_id`
                               NOT IN (1006)
                           ) AS `species`
                           ORDER BY `name`");

    $temp = "";
    $size = mysql_num_rows($result);
    for ($i = 0; $i < $size; $i++) {
        $row = mysql_fetch_assoc($result);
        $temp .= "\"" . $row['name'] . "\"";

        if ($i < $size - 1) {
            $temp .= ", ";
        }
    }

    echo "            var species = [$temp];";
?>
            $("#search_input").autocomplete({
                source: function(request, response) {
                    var matches = $.map(species, function(tag) {
                        if (tag.toUpperCase().indexOf(request.term.toUpperCase()) === 0) {
                            return tag;
                        }
                    });

                    response(matches);
                },

                select: function(event, ui) {
                    getSpecies(ui.item.value);
                }
            });
	});
    </script>
    <div class="content_container">
        <h1>Species</h1>

<?php
    echo "<div id=\"search\">
              <label for=\"search\">Search:</label>
              <input id=\"search_input\">
          </div>";
    echo "<div id=\"f_menu\" class=\"container_brown\">
              <h2>Search Filters</h2>
              <table>
                  <tr>
                      <td class=\"type\">Category:</td>
                      <td class=\"select\">
                          <select id=\"filter_cat\" onchange=\"setFilter()\">
                              <option value=\"\">All</option>
                              <option value=\"animal\">Animal</option>
                              <option value=\"animal_s\">Animal (Small)</option>
                              <option value=\"animal_l\">Animal (Large)</option>
                              <option value=\"bird\">Bird</option>
                              <option value=\"insect\">Insect</option>
                              <option value=\"plant\">Plant</option>
                              <option value=\"resource\">Resource</option>
                          </select>
                      </td>
                      <td class=\"type\">Available:</td>
                      <td class=\"select\">
                          <select id=\"filter_av\" onchange=\"setFilter()\">
                              <option value=\"\">All</option>
                              <option value=\"yes\">Yes</option>
                              <option value=\"no\">No</option>
                          </select>
                      </td>
                      <td id=\"sort\">
                          Sort By:
                          <select id=\"filter_sort\" onchange=\"setFilter()\">
                              <option value=\"name_asc\">Name A-Z</option>
                              <option value=\"name_desc\">Name Z-A</option>
                              <option value=\"species_asc\">Species ID: Low to High</option>
                              <option value=\"species_desc\">Species ID: High to Low</option>
                              <option value=\"node_asc\">Node ID: Low to High</option>
                              <option value=\"node_desc\">Node ID: High to Low</option>
                              <option value=\"price_asc\">Price: Low to High</option>
                              <option value=\"price_desc\">Price: High to Low</option>
                              <option value=\"biomass_asc\">Biomass: Low to High</option>
                              <option value=\"biomass_desc\">Biomass: High to Low</option>
                              <option value=\"available_asc\">Available: Low to High</option>
                              <option value=\"available_desc\">Available: High to Low</option>
                          </select>
                      </td>
                  </tr>
                  <tr>
                      <td class=\"type\">Class:</td>
                      <td class=\"select\">
                          <select id=\"filter_class\" onchange=\"setFilter()\">
                              <option value=\"\">All</option>
                              <option value=\"carnivore\">Carnivore</option>
                              <option value=\"herbivore\">Herbivore</option>
                              <option value=\"omnivore\">Omnivore</option>
                              <option value=\"producer\">Producer</option>
                          </select>
                      </td>
                      <td>
                      </td>
                      <td>
                      </td>
                      <td id=\"show\">
                          Show Only:
                          <select id=\"filter_show\" onchange=\"setFilter()\">
                              <option value=\"\">All</option>
    ";

    for ($i = 0; $i < 26; $i++) {
        $alpha = chr(ord("A") + $i);
        echo "                    <option value=\"$alpha\">$alpha</option>";
    }

    echo "
                          </select>
                      </td>
                  </tr>
              </table>
          </div>
          <br />
    ";

    echo "<div id=\"species_content\">";
    include "species_content.php";
    echo "</div>";
?>

    </div>
<?php include "layout/footer2.php"; ?>