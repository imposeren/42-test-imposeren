	$(function() {
		$( "#id_birth" ).datepicker({
			changeYear: true,
			changeMonth: true,
			minDate: '-110y',
			maxDate:'-6y',
			yearRange: '-110:+0',
			defaultDate: '-18y'});
	});