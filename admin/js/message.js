// alert("slight");
$("#add-msg").click(function(){
	
	var n = $("#mes-tr").attr("data-id");
	// alert(n);
	n = parseInt(n)+1;
	var html = "<tr data-id='"+n+"' id='mes-tr'><td><div class='num_logo'><img src='http://www.jq22.com/demo/jQuery-szmjs20151201/img/img.png' alt=' class='img-rounded'>&nbsp;&nbsp;&nbsp;&nbsp;行行行：啦啦啦啦啦测试"+n+"！</div></td></tr>";
	if(html){
		$("#mes-tb").prepend(html);
		$("#mes-tr").hide();
		$("#mes-tr").fadeToggle();


	}else{
		alert("No");
	}
	
	
});

function msg_type(obj){
	// alert(obj);
	var type = $(obj).attr("data-type");
	// alert(type);
	var i = "."+type+"-type";
	// alert(i);
	$(".msg-type").removeClass("button-action");
	$(i).addClass("button-action");
	$(".msg-type").removeClass("button-action");
	$(i).addClass("button-action");
	if(type=='user'){
		$(".status-font").removeClass("icon-group");
		$(".status-font").addClass("icon-user");
	}else if(type=='group'){
		$(".status-font").removeClass("icon-user");
		$(".status-font").addClass("icon-group");
	}

};

