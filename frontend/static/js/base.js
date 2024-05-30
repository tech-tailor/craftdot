$( document ).ready(function() {
	$('#flashMessage').each(function(index, element) {
		setTimeout(() => {
				$(element).fadeOut('slow');
		}, 5000 * (index + 1)); // flash message to dissapear in 5sec
	
	})

});
