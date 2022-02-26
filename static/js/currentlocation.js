document.getElementById("current").addEventListener("click", () => {
  navigator.geolocation.getCurrentPosition((loc) => {
    let lat = loc.coords.latitude;
    let lng = loc.coords.longitude;
    document.getElementById("lat").value = lat; //latitude
    document.getElementById("lng").value = lng; //longitude
  });
});

window.addEventListener("load", () => {
  document.getElementById("map").style.display = "none";
});

let i = true;
document.getElementById("choose").addEventListener("click", () => {
  console.log(i);
  if (i === false) {
    document.getElementById("map").style.display = "none";
    i = true;
  } else {
    document.getElementById("map").style.display = "block";
    i = false;
  }
});
