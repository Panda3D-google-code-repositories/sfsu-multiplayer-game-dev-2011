function getSpecies(name) {

    //Change these values to style your modal popup
    var source = "get_species.php?name=" + name;
    var width = 685;
    var align = "center";
    var top = 100;
    var padding = 10;
    var backgroundColor = "#FDF5E6";
    var borderColor = "#D5C8A4";
    var borderWeight = 4;
    var borderRadius = 5;
    var fadeOutTime = 300;
    var disableColor = "#666666";
    var disableOpacity = 40;
    var loadingImage = "js/lib/loading.gif";

    //This method initialises the modal popup
    modalPopup( align,
        top,
        width,
        padding,
        disableColor,
        disableOpacity,
        backgroundColor,
        borderColor,
        borderWeight,
        borderRadius,
        fadeOutTime,
        source,
        loadingImage );	

    //This method hides the popup when the escape key is pressed
    $(document).keyup(function(e) {
        if (e.keyCode == 27) {
            closePopup(fadeOutTime);
        }
    });

}