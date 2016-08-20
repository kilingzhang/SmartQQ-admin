// alert("slight");
function rule_list_fadeToggle(obj){

	var n = $(obj).attr('data-id');
	// alert(n);
	var i = "#keywords_rule_list_hd_"+n;
	// alert(i);
	$(i).fadeToggle();
	// $(i).fadeToggle("slow");

};