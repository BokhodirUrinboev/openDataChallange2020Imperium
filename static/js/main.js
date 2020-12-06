jQuery(function ($) {
    $(window).scroll(function fix_element() {
        $('.navbar').css(
            $(window).scrollTop() > 0
                ? {'background': 'rgba(255,255,255, .7)'}
                : {'background': 'transparent'}
        );
        return fix_element;
    }());
});

$(document).ready(function () {
    $('#regions').change(function () {
        var unselectedValues = $(this).find('option:not(:selected)').map(function () {
            return this.value;
        }).get();

        console.log(unselectedValues);
    });
    $('#submit').on('click', function () {
    })
})