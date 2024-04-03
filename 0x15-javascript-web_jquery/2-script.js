/* color updated to red when tag is clicked */
$(() => {
  $('DIV#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
