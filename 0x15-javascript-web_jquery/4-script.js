/* color updated to red when tag is clicked */
$(() => {
  $('DIV#toggle_header').click(() => {
    $('header').toggleClass('red green');
  });
});
