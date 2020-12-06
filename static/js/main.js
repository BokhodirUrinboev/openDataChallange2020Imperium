jQuery(function ($) {
        $(window).scroll(function fix_element() {
            $('.navbar').css(
                $(window).scrollTop() > 0
                    ? { 'background': 'rgba(255,255,255, .7)' }
                    : { 'background': 'transparent' }
            );
            return fix_element;
        }());
    });