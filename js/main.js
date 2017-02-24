$(document).ready(function(){
	var path = window.location.pathname;
	var page = path.split('/').pop();
	$('nav > ul > li > a[href="'+page+'"]').parent().addClass('active');
});