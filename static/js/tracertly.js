// Off Canvas Menu
/* Set the width of the side navigation to 250px and
   the left margin of the page content to 250px */
function openNav() {
    document.getElementById("sideBarNav").style.width = "200px";
    document.getElementById("main").style.marginLeft = "200px";
}

/* Set the width of the side navigation to 0 and 
   the left margin of the page content to 0 */
function closeNav() {
    document.getElementById("sideBarNav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
} 


//Card Text Item Attributes for expand and edit title
//Are hidden by default 
$('.cardTextMore').hide();
// and should be made visible on hover
$('.card-text').hover(
	function () {
		$(this).find('.cardTextMore').fadeIn(750);
	}, 
	function () {
		$(this).find('.cardTextMore').fadeOut(750);
	}
);