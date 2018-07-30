// Off Canvas Menu
    /* Set the width of the side navigation to 250px and
    the left margin of the page content to 250px */
    function openNav() {
        $("#sideBarNav").css( 'width', '200px' );
        $("#main").css('margin-left', '200px' );
        $("#main").removeClass('container-fluid').addClass('container');
    }

    /* Set the width of the side navigation to 0 and 
    the left margin of the page content to 0 */
    function closeNav() {
        $("#sideBarNav").css( 'width', '0' );
        $("#main").css('margin-left', '0' );
        $("#main").removeClass('container').addClass('container-fluid');
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


// Example Form Submit Via Ajax
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
