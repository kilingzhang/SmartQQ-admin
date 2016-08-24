// alert("slight");
function rule_list_fadeToggle(obj){

	var n = $(obj).attr('data-id');
	// alert(n);
	var i = "#keywords_rule_list_hd_"+n;
	// alert(i);
	$(i).fadeToggle();
	// $(i).fadeToggle("slow");

};

$(".reply-status").click(function(){
	
	var n = $(".reply-status").attr("data-status");
	// alert(n);
	if(n==0){
		$(".reply-status").attr("data-status",1);
		$(".reply-status").removeClass("btn-danger");
		$(".reply-status").addClass("btn-success");
		$(".reply-status").text("开启");
		$(".rule").hide();




	}else if(n==1){
		$(".reply-status").attr("data-status",0);
		$(".reply-status").removeClass("btn-success");
		$(".reply-status").addClass("btn-danger");
		$(".reply-status").text("停用");
		$(".rule").show();


	}
	

});


function rule_type(obj){
	// alert(obj);
	var n = $(obj).attr("data-type");
	// alert(n);
	var i = "."+n;
	var m = ".r_"+n;
	$(".rule-type").hide();
	$(".rule_type").removeClass("button-action");
	$(".rule_type").removeClass("button-primary");
	
	$(".rule_type").addClass("button-primary");

	$(m).removeClass("button-primary");
	$(m).addClass("button-action");

	// alert(i);
	// alert(i);
	$(i).show();
	// $(i).fadeToggle("slow");

};



$(".add-rule").click(function(){
	
	$("#Js_ruleItem_0").fadeToggle();

});
