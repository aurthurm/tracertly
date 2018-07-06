
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