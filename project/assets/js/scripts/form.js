$(function() {
    
    var isEvent = false;

    $('.js-form-ajax').on('submit', 'form', function(event){
        event.preventDefault();
        if (isEvent) { return; }
        isEvent = true;
        var $form = $(this),
            $parent = $form.closest('.js-form-ajax'),
            $container = $(".form__container", $parent);

        $parent.addClass('_loading');

        $container.css({
            'min-height': $container.innerHeight()
        });

        $.ajax({
            url: $form.attr('action'),
            type: $form.prop('method'),
            data: $form.serialize(),
            success: function(data) {
                if (data == 'Success auth') {
                    window.location.replace('/accounts/profile/');
                } else {
                    setTimeout(function(){
                        $container.html(data);
                        isEvent = false;
                        $parent.removeClass('_loading');
                    }, 800);
                }
            }
        });
    });
});