//= require vendor/jquery.js
//= require vendor/jquery.custom-scrollbar.js
//= require vendor/tooltipster.bundle.js
//= require vendor/fancybox/jquery.fancybox.js
//= require vendor/fancybox/helpers/jquery.fancybox-media.js
//= require !vendor/fancybox/helpers/jquery.fancybox-buttons.js
//= require !vendor/fancybox/helpers/jquery.fancybox-thumbs.js

//= require scripts/*.js

$(function() {

    var $B = $('body');

    $(".js-tooltip").tooltipster();

    function close_popup(popup) {
        popup.removeClass('_visible');
        setTimeout(function(){
            popup.removeClass('_show');
        }, 420);
    }

    $('#js-popupIndexText').on("click", function(event){
        event.preventDefault();

        var popup = $('#popupIndexText'),
            close = $(".popupText__close", popup)

        popup.addClass('_show');
        setTimeout(function(){
            popup.addClass('_visible');
        }, 20);


        close.on("click", function(event){
            event.preventDefault();
            close_popup(popup);

            close.off('click');
        });

    });



    $('.js-scroll').customScrollbar({
        hScroll: false,
        updateOnWindowResize: true
    });


    (function(){

        function closePopup(popup, close){
            $B.off('.popup');
            close.off('.popup');

            popup.removeClass('_visible');
            setTimeout(function(){
                popup.removeClass('_show');
            }, 310);

        }

        $('.js-open-popup').on('click', function(event){
            event.preventDefault();
            var popup = $($(this).data('popup'));

            if (popup.hasClass('_show')) { return; }

            if (!popup.length) { return; }
            var close = $(".popup__close", popup);

            popup.addClass('_show');
            setTimeout(function(){
                popup.addClass('_visible');
            }, 10);

            setTimeout(function(){
                close.on('click.popup', function(event){
                    event.preventDefault();
                    closePopup(popup, close);
                });
                $B.on('click.popup', function(event){
                    var $target = $(event.target);

                    if (!$target.closest('.popup').length) {
                        event.preventDefault();
                        closePopup(popup, close);
                        event.preventDefault();
                    }

                });
            }, 20)
        });
    }());


    (function(){
        var omen = $(".js-open-omen"),
            parent = omen.closest('.js-gif'),
            crnt = 0,
            items = $(".personageBird__textItem", parent);

        $('.personageBird__textClose', parent).on('click', function(event){
            event.preventDefault();
            parent.removeClass('_openOmen');
        });

        omen.on('click', function(){

            if (parent.hasClass('_openOmen')) {
                parent.removeClass('_openOmen');
            } else {
                var next;

                if (items.filter('._active').length) {
                    next = items.filter('._active').next();
                    items.filter('._active').removeClass('_active');
                    if (!next.length) {
                        next = items.eq(0);
                    }
                } else {
                    next = items.eq(0);
                }

                console.log(items);

                next.addClass('_active')
                parent.addClass('_openOmen');
            }
        });
    }());

});