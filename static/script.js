$(document).ready(function(){
	$(".top-seller").on({
		mouseenter: function(){
			$(this).find(".hover-popup").css({height: "30%"})
		},
		mouseleave: function(){
			$(this).find(".hover-popup").css({height: "0%"})
		}
	})

	$(".top-seller").click(function(){
		window.location.href = "http://127.0.0.1:5000/product/" + $(this).data("id")
	})
	$(".navbar-brand").click(function(){
		window.location.href = "http://127.0.0.1:5000/"
	})
})