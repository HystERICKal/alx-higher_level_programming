/* fetch n' print language dependent Hello sayer */
$(() => {
  $('INPUT#btn_translate').click(() => {
    const lang_code = $('INPUT#language_code').val();
    const the_link = 'https://fourtonfish.com/hellosalut/?lang=' + lang_code;
    $.get(the_link, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
