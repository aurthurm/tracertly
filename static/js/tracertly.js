// Off Canvas Menu
    /* Set the width of the side navigation to 250px and
    the left margin of the page content to 250px */
    function openNav() {
        document.getElementById("sideBarNav").style.width = "200px";
        document.getElementById("main").style.marginLeft = "200px";
    }

    /* Set the width of the side navigation to 0 and 
    the left margin of the page content to 0 */
    function closeNav() {
        document.getElementById("sideBarNav").style.width = "0";
        document.getElementById("main").style.marginLeft = "0";
    } 


//Card Text Item Attributes for expand and edit title
    //Are hidden by default 
    $('.cardTextMore').hide();
    // and should be made visible on hover
    $('.card-text').hover(
        function () {
            $(this).find('.cardTextMore').fadeIn(750);
        }, 
        function () {
            $(this).find('.cardTextMore').fadeOut(750);
        }
    );

// Enable Django CSRF-ready AJAX Calls
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


// Form Submit Via Ajax
    $(document).ready(function(){
        var $myForm = $('.formclassgoeshere')
        $myForm.submit(function(event){
            event.preventDefault()
            var $formData = $(this).serialize()
            var $thisURL = $myForm.attr('data-url')
            $.ajax({
                method: "POST",
                url: $thisURL,
                data: $formData,
                success: handleFormSuccess,
                error: handleFormError,
            })
        })

        function handleFormSuccess(data, textStatus, jqXHR){
            console.log(data)
            console.log(textStatus)
            console.log(jqXHR)
            $myForm[0].reset(); // reset form data
        }

        function handleFormError(jqXHR, textStatus, errorThrown){
            console.log(jqXHR)
            console.log(textStatus)
            console.log(errorThrown)
        }
    })

// CommentForm Submit Via Ajax
    $(document).on('submit', '#itemcommentform4', function(e){
        e.preventDefault();
        var $myForm = $('#itemcommentform4');
        $.ajax({
            type: "POST",
            url: $myForm.attr('data-url') || window.location.href,
            data: {
                comment:$("#comment").val(),
            },
            success: function(){

            }
        });

    });

    $(document).ready(function(){
        var $myForm = $('#itemcommentform')
        $myForm.submit(function(event){
            event.preventDefault()
            var $formData = $(this).serialize()
            var $thisURL = $myForm.attr('data-url') || window.location.href // or set your own url
            $.ajax({
                method: "POST",
                url: $thisURL,
                data: $formData,
                success: handleFormSuccess,
                error: handleFormError,
            })
        })

        function handleFormSuccess(data, textStatus, jqXHR){
            console.log(data)
            console.log(textStatus)
            console.log(jqXHR)
            $myForm[0].reset(); // reset form data
        }

        function handleFormError(jqXHR, textStatus, errorThrown){
            console.log(jqXHR)
            console.log(textStatus)
            console.log(errorThrown)
        }
    })



    // $(document).on("submit", "#pony_form", function(e) {
    //     e.preventDefault();
    //     var self = $(this),
    //         url = self.attr("action"),
    //         ajax_req = $.ajax({
    //             url: url,
    //             type: "POST",
    //             data: {
    //                 name: self.find("#id_name").val()
    //             },
    //             success: function(data, textStatus, jqXHR) {
    //                 django_message("Pony saved successfully.", "success");
    //             },
    //             error: functior(data, textStatus, jqXHR) {
    //                 var errors = $.parseJSON(data.responseText);
    //                 $.each(errors, function(index, value) {
    //                     if (index === "__all__") {
    //                         django_message(value[0], "error");
    //                     } else {
    //                         apply_form_field_error(index, value);
    //                     }
    //                 });
    //             }
    //         });
    // });