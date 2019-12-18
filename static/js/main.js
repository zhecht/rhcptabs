function click_link(album) {
  window.location.href = '/album/'+album;
}

function openTabsWindow(url) {
  windowFeatures = 'height=700,width=1000,top=50,left=150,toolbar=no,scrollbars=yes,resizable=yes,location=no,directories=no,status=no,menubar=no';
  newWindow = window.open(url, '', windowFeatures);
  newWindow.focus();
}