// Forked from https://github.com/ctiml/campaign-finance.g0v.ctiml.tw
$(document).ready(function(){

  var shadow = function() {
    $('#ans-shadow').offset($('#ans').position());
  }
  $(window).resize(function(){
    shadow();
  });
  shadow();

  var submitAnswer = function(e) {
    if (e !== undefined) {
      e.preventDefault();
    }

    var ans = $('#txt').val();
    var p = $('.cell-info').data('p');

    var url = 'submit.php';
    $.post(url, { p: p, cont: ans }, function(e) { console.log(e); });
    getRandomImage();
  };

  var getRandomImage = function() {
    $('#img').html("");
    $('#txt').val("").focus();

    $.get('random.php', function(e){
      var p = e['p'];
      $('.cell-info').data({p: p});
      $('#img').html('<img src="http://ckhis.ck.tp.edu.tw/~ljm/amis/'+p+'.jpg">');
      $('#txt').val(e['cont']).focus();
      /*
      var content = '';
      for(var i in e) {
        content += '<input type="checkbox" name="'+e[i]['p']+'_'+e[i]['line']+'">' + '('+e[i]['line']+') ' + e[i]['ans'] + '<br>\n';
      }
      $('#txt').html(content);
      */
    });
  };
  getRandomImage();

  $('#submit').click(submitAnswer);
});
