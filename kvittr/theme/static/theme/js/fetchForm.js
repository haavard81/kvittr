$(document).ready(function()
		
		{
		
		//Attach a handler to the click event
		
		//of the link on the page:
		
		$('#fetch-signin-form').click(function()
		
		{
		
		//Target the div with id of result
		
		//and load the content from the specified url
		
		//and the specified div element into it:
		
		$('.modal-body').load('useraccounts/login .form-signin');
		
		});
		
		});