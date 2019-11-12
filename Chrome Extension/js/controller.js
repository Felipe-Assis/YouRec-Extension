// This file executes server calls

function cont_handshake(){
	// Performs a test AJAX call to see if server is operative:
	$(function() {
        $.ajax({
            url: 'http://127.0.0.1:5000/handshake',
            type: 'POST',
            success: function(response) {
                //console.log(response);
            },
            error: function(error) {
                //console.log(error);
            }
        });
	});
}


// Fetches the next few words to be played by the service:
function cont_fetchData(resolve, reject, index){
	data = {index: index};
	$(function() {
		$.ajax({
			url: 'http://127.0.0.1:5000/words',
			type: 'POST',
			data: JSON.stringify(data, null, '\t'),
    		contentType: 'application/json;charset=UTF-8',
			success: function(response) {
				resolve(response);
			},
			error: function(error) {
				reject(error);
			}
		});
	});
}
