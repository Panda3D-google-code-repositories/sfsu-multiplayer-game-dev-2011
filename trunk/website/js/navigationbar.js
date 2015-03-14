// Navigation Bar drop down menu javascript
var timeout	= 200;
var closetimer	= 0;
var ddmenuitem	= 0;

// open hidden layer
function mopen(id)
{
    // cancel close timer
    mcancelclosetime();
    // close old layer
    mclose();

    // get new layer and show it
    ddmenuitem = document.getElementById(id);
    ddmenuitem.style.visibility = 'visible';
}
// close showed layer
function mclose()
{
    if(ddmenuitem) ddmenuitem.style.visibility = 'hidden';
}

function mtoggle(id) {
    if (ddmenuitem) {
        if (ddmenuitem.style.visibility == 'hidden') {
            mopen(id);
        } else {
            mclose();
        }
    } else {
        mopen(id);
    }
}

// go close timer
function mclosetime()
{
	closetimer = window.setTimeout(mclose, timeout);
}

// cancel close timer
function mcancelclosetime()
{
	if(closetimer)
	{
		window.clearTimeout(closetimer);
		closetimer = null;
	}
}

// close layer when click-out
//document.onclick = mclose;
