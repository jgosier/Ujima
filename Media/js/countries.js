

$(document).ready(function () {
	
    $('img.country').click(function () {
	$('div.countries').slideToggle('medium');
    });
	$('img.topic').click(function () {
	$('div.topics').slideToggle('medium');
    });
	




	$("#filter").keyup(function () {
    var filter = $(this).val(), count = 0;
    $(".filtered em.ts").each(function () {
        if ($(this).text().search(new RegExp(filter, "i")) < 0) {
            $(this).addClass("hidden");
        } else {
            $(this).removeClass("hidden");
            count++;
        }
    });
   
});
});




































