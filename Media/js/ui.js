$(document).ready(function (){
jQuery("ul.tabs").tabs2("div.panes > div");


});

//the status of overlay box
var isOpen = false;
//function to display the box
function showOverlayBox() {
	//if box is not set to open then don't do anything
	if( isOpen == false ) return;
	// set the properties of the overlay box, the left and top positions
	$('.overlayBox').css({
		display:'block',
		left:( $(window).width() - $('.overlayBox').width() )/2,
		top:( $(window).height() - $('.overlayBox').height() )/2 -20,
		position:'absolute'
	});
	// set the window background for the overlay. i.e the body becomes darker
	$('.bgCover').css({
		display:'block',
		width: $(window).width(),
		height:$(window).height()
	});
}
function doOverlayOpen() {
	//set status to open
	isOpen = true;
	showOverlayBox();
	$('.bgCover').css({opacity:0}).animate( {opacity:0.5, backgroundColor:'#000'} );
	// dont follow the link : so return false.
	return false;
}
function doOverlayClose() {
	//set status to closed
	isOpen = false;
	$('.overlayBox').css( 'display', 'none' );
	// now animate the background to fade out to opacity 0
	// and then hide it after the animation is complete.
	$('.bgCover').animate( {opacity:0}, null, null, function() { $(this).hide(); } );
}
// if window is resized then reposition the overlay box
$(window).bind('resize',showOverlayBox);
// activate when the link with class launchLink is clicked
$('a.launchLink').click( doOverlayOpen );
// close it when closeLink is clicked
$('a.closeLink').click( doOverlayClose );
