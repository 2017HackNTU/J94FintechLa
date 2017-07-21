var url = window.location.href;
function go(url) {
  window.open('.html'+'&'+url, '_blank');
  return url;
}
document.getElementById("url").innerHTML = go(url);
