// <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js" > </script>

// <script>
//     var note ;
//     var comment;
//     function getCookie(c_name)
// 	{
// 	    if (document.cookie.length > 0)
// 	    {
// 	        c_start = document.cookie.indexOf(c_name + "=");
// 	        if (c_start != -1)
// 	        {
// 	            c_start = c_start + c_name.length + 1;
// 	            c_end = document.cookie.indexOf(";", c_start);
// 	            if (c_end == -1) c_end = document.cookie.length;
// 	            return unescape(document.cookie.substring(c_start,c_end));
// 	        }
// 	    }
// 	    return "";
// 	 }

// 	function onSuccess(data, status, xhr)
// 	{
// 		// with our success handler, we're just logging the data...
// 		console.log(data, status, xhr);
// 		// but you can do something with it if you like - the JSON is deserialised into an object
// 		console.log(String(data.value).toUpperCase());
// 	//	$("#div1").text("value form ajax: " + String(data.value));
// 		// alert ("ajax successful");
// 		if (data == 'note'){
// 			var li = '<li class="list-group-item">' + note + '</li>';
// 			$('#my_notes').prepend(li);

// 		}
		
// 		if (data == 'comment') {
// 			var li = '<li class="list-group-item">' + comment + '</li>';
// 			$('#pre_comment').append(li);


// 		}

// 	}


// 	$(document).ready(function(){

// 		$(function () {
// 		    $.ajaxSetup({
// 		        headers: { "X-CSRFToken": getCookie("csrftoken") }
// 		    });
// 		});
				

// 		$("#bAddNote").click(function(){	

// 			note = $('#note').val();
// 			var reading_content_id = $('#reading_content_id').val();
// 			// alert (reading_content_id);
// 			if (note.length > 0) {
// 				 $.post('/readingmaterial/ajax/addnote/', { 'note'  : note, 'reading_content_id' : reading_content_id}, onSuccess);

// 			} else {
// 				alert ("To make a note write something in the note box");
// 			}
		  
		    
	  		
// 		});


// 		$("#bAddComment").click(function(){	

// 			comment = $('#comment').val();
// 			var reading_content_id = $('#reading_content_id').val();
// 		//	alert (comment)
// 			if (comment.length > 0) {
// 				 $.post('/readingmaterial/ajax/addcomment/', { 'comment'  : comment, 'postId' : reading_content_id}, onSuccess);

// 			} else {
// 				alert ("To make a comment write something in the comment box");
// 			}			  
	  		
// 		});

// 	});

	
    
// </script>
