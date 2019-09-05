$(function() {
    var gif = $(".js-gif");



    function startAnimate(block, parent, index) {
        var width = block.data('width'),
            quantity = block.data('quantity') - 1,
            speed = block.data('speed'),
            cycle = block.data('cycle') - 1,
            i = 0,
            crnt_cycle = 0;

        setTimeout(function(){
            parent.addClass('_animation');
            block.addClass('_animation');
        }, speed);

        var interval = setInterval(function(){
            if (i > quantity) {
                i = 0;
                crnt_cycle++;
            }
            if (crnt_cycle > cycle) {
                clearInterval(interval);
                parent.removeClass('_animation');
                block.removeClass('_animation');
                return;
            }

            block.css({
                'background-position': (width * i * -1) + 'px 0'
            });

            i++;

        }, speed);


        if (parent.hasClass('js-gif-click')) {
            parent.off('.anim').on('click.anim', function(event){
                event.preventDefault();
                if (index == 0) { return; }
                clearInterval(interval);
                parent.removeClass('_animation');
                block.removeClass('_animation');
            });
        }
    }



    gif.each(function(){
        var $this = $(this),
            crnt = 0,
            anim = false,
            items = $('.js-gif-item', $this),
            quantity = items.length - 1,
            start = true,
            time1 = setTimeout(function(){}, 0),
            time2 = setTimeout(function(){}, 0),
            time3 = setTimeout(function(){}, 0);


        function inter(immediately) {
            var t = Math.floor((Math.random() * 20000) + 1);

            if (t < 15000) {
                t = 15000;
            }

            if (start) {
                t = 2000;
                start = false;
            }

            if (crnt > quantity) {
                crnt = 0;
            }

            if (immediately) {
                t = 0;
            }

            time1 = setTimeout(function(){
                var next = items.eq(crnt);

                anim = true;
                startAnimate(items.eq(crnt), $this, crnt);

                var duration = next.data('speed') * (next.data('quantity')) * next.data('cycle') + next.data('speed');

                time2 = setTimeout(function(){
                    crnt++;
                    anim = false;
                    inter();
                }, duration);
            }, t);
        }

        var delay = $this.data('delay') || 1000

        time3 = setTimeout(function(){
            inter();
        }, delay);


        if ($this.hasClass('js-gif-click')) {
            $this.on('click', function(event){
                event.preventDefault();
                if (anim && crnt == 0) { return; }
                clearTimeout(time1);
                clearTimeout(time2);
                clearTimeout(time3);

                setTimeout(function(){
                    $this.removeClass('_animation');
                    items.removeClass('_animation');
                    crnt = 0;
                    start = false;
                    inter(true);
                }, 10);
            });
        }

    });
});