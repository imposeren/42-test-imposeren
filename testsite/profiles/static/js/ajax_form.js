function setupAjaxForm(form_id){
    var form = '#' + form_id;
    var form_message = form + '-message';

    var disableAll = function(val){
	var f = document.getElementById(form_id);
	var inputs = f.getElementsByTagName("input");
	for(var i = 0; i < inputs.length; i++){
		inputs[i].readOnly = val;
	};
	var inputs = f.getElementsByTagName("textarea");
	for(var i = 0; i < inputs.length; i++){
		inputs[i].readOnly = val;
	};
    };

    var enableAll = function(val){
	var f = document.getElementById(form_id);
	var inputs = f.getElementsByTagName("input");
	for(var i = 0; i < inputs.length; i++){
		inputs[i].removeAttribute("readonly",0);
	};
	var inputs = f.getElementsByTagName("textarea");
	for(var i = 0; i < inputs.length; i++){
		inputs[i].removeAttribute("readonly",0);
	};
    };

    $(form).ajaxSend(function(){
        $(form_message).removeClass().addClass('loading').html('Uploading...').fadeIn();
    });

    var options = {
        dataType:  'json',
        beforeSubmit: function(){
            disableAll(true);
        },
        success: function(json){
		$(form_message).hide();
		$(form_message).removeClass().addClass(json.result).html(json.result).fadeIn('slow');
		disableAll(false);
		if(json.errors) {
			$(form_message).removeClass().addClass(json.result).html(json.errors).fadeIn('slow')
		}

        }
    };
    $(form).ajaxForm(options);
}

$(document).ready(function() {
    new setupAjaxForm('edit-profile');
});
