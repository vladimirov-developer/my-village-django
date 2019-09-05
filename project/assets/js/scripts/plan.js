$(function() {
    var plan = $("#js-plan");

    if (!plan.length) { return; }


    window.initPlan = function(data){

        if (data.reserved) {
            for (var i = 0; i < data.reserved.length; i++) {
                var id = data.reserved[i];
                $('#' + data.reserved[i], plan).attr('class', 'area_reserved');
            }
        }

        if (data.sold) {
            for (var i = 0; i < data.sold.length; i++) {
                var id = data.sold[i];

                $('#' + data.sold[i], plan).attr('class', 'area_sold');
            }
        }
    }


    var urlTmpl = plan.data('url'),
        popup = $('#landTextPopup'),
        close = $(".js-close", popup),
        cntn = $(".landText__container", popup),
        isEvent = false;

    close.on('click', function(event){
        event.preventDefault();
        isEvent = true;

        popup.removeClass('_visible');

        setTimeout(function(){
            popup.removeClass('_show _ready');
            isEvent = false;
        }, 400);
    });

    plan.on('click', '.area', function(event){
        event.preventDefault();
        if (isEvent) { return; }
        isEvent = true;
        var $this = $(this),
            id = $this.attr('id');
        
        popup.removeClass('_ready');
        popup.addClass('_loadContent _show');
        setTimeout(function(){
            popup.addClass('_visible');
        }, 10);

        $.ajax({
            url: urlTmpl.replace('<%id%>', id),
            type: 'get',
            success: function(data) {
                cntn.html(data);
                setTimeout(function(){
                    $('.js-scroll', cntn).customScrollbar({
                        hScroll: false
                    });
                    isEvent = false;
                    popup.removeClass('_loadContent');
                    popup.addClass('_ready');
                }, 800);
            }
        });
    });





    // var id = 500;

    // $('#main polygon').on('click', function(){
    //     console.log(id);
    //     $(this).attr('class', 'oooook');
    //     $(this).attr('id', 'id' + id);
    //     id++;
    // });
});