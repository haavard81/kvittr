

$(document).ready(function(){

    $(".likes_link").click(function(event) {
        event.preventDefault();
        var post_id = $(this).data("postid");
        var likes_elm_id = "#id-likes-" + post_id;

        $.ajax({
            url: /posts/ + post_id + "/add_likes"
        })
        .done(function(data){
            var likes_updated = data['likes_updated'];
            $(likes_elm_id).html(likes_updated);
        });

    });   

});

