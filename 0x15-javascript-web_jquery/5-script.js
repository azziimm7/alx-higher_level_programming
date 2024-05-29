// Js script that adds a <li> element to a list

$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
