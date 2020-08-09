import $ from 'jquery';

$(document).ready(function(){
    $(".collapse-arrow-container").click(function(){
        $(this).find(".collapse-arrow").toggleClass("active")
    });
});