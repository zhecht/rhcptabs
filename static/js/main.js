


var nav = new Vue({
  el: '#nav',
  data: {
    title: 'All'
  },
  methods: {
    
  }
});

var title = new Vue({
  el: '#title',
  data: {
    title: "All"
  }
});

function change_instrument(instrument) {
  if (instrument == "All") {
    $('.song a').show();
  } else if (instrument != "Guitar"){
    $('.song a').hide();
    $('.song a[class^='+instrument.toLowerCase()+']').show();
  } else {
    //guitar
    $('.song a').hide();
    $('.song a[class^=solo],.song a[class^=intro],.song a[class^=tab],.song a[class^=chords]').show();
  }
}

function change_nav(el) {
  el.addClass('active').siblings().removeClass('active');
  title.title = el.text();
}


$('nav a').click(function(){

  var el = $(this);
  change_nav(el);
  if (window.location['pathname'].search("album") != -1) {
    change_instrument(el.text());
  }
});

function click_link(album) {
  window.location.href = '/album/'+album+'?instrument='+title.title;
}

function openTabsWindow(URLtoOpen) {
  windowName='';
  windowFeatures='height=700,width=1000,top=50,left=150,toolbar=no,scrollbars=yes,resizable=yes,location=no,directories=no,status=no,menubar=no';
  newWindow=window.open(URLtoOpen, windowName, windowFeatures);
  newWindow.focus();
}