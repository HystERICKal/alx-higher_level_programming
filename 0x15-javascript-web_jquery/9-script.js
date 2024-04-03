/* fetch and display */
$(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
    $('DIV#hello').text(data.hello);
    console.log(data);
  });
});
