var url = window.location.href;
function go(url) {
  window.open('localhost:9487/test.html', '_blank');
  return url;
}
document.getElementById("url").innerHTML = go(url);
