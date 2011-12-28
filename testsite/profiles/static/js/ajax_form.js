function setupAjaxForm(form_id){
    var form = '#' + form_id;
    var form_message = '#message';

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
		disableAll(false);
		if(json.errors) {
			$.each(json.errors,function(fieldname,errmsgs) {
			    id = "#id_" + fieldname;
			    for (var i=0; i<errmsgs.length; i++){
			        $(id).after('<div class="error" id="' + fieldname + '_error">' + errmsgs[i] + '</div>');
			    }
			});
		}
		$(form_message).removeClass().addClass(json.type).html(json.message+". Redirecting in 2 seconds").fadeIn('slow');
                setTimeout('window.location.href=window.location.href', 2000);
        }
    };
    $(form).ajaxForm(options);
};

function cloneMore(selector, type) {
    var newElement = $(selector+":last").clone(true);
//    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    var total = $(selector).length;
    console.log(total);
    newid = newElement.attr('id').replace('-' + (total-1),'-' + total);
    console.log(newElement.attr('id'))
    console.log(newid)
    newElement.attr({'id': newid});
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });
    newElement.find('a').each(function() {
        $(this).attr('href', "javascript:cloneLess('tr.clonable', 'contact_set', 'tr#" + newid + "');");
    });

    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector+":last").after(newElement);
};

function cloneLess(selector, type, subselector) {
    var oldElement = $(selector);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    //var total = $(selector).length;
    total--;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(subselector).remove();
};


$(document).ready(function() {
    new setupAjaxForm('edit-profile');
});
