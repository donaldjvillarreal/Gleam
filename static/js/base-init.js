$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
    // Dashboards


    $('#sidebar-menu, #customize-menu').metisMenu({
        activeClass: 'open'
    });
    $('#sidebar-collapse-btn').on('click', function (event) {
        event.preventDefault();

        $("#app").toggleClass("sidebar-open");
    });

    $("#sidebar-overlay").on('click', function () {
        $("#app").removeClass("sidebar-open");
    });

    $('.nav-profile > li > a').on('click', function () {
        var $el = $(this).next();

        animate({
            name: 'flipInX',
            selector: $el
        });
    });
});