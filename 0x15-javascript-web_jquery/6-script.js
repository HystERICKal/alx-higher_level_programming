/* text updated when tag is clicked */
$(() => {
  $('DIV#update_header').click(() => {
    $('header').text('New Header!!!');
  });
});
