// Making a map and tiles
// Setting a higher initial zoom to make effect more obvious
var lat = document.currentScript.getAttribute("lat");
var long = document.currentScript.getAttribute("long");
var origin = document.currentScript.getAttribute("origin");
var dest = document.currentScript.getAttribute("dest");

console.log(lat, long, origin, dest);

var box = document.getElementById("box");

async function getAdd(lat, long) {
  url =
    "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=" +
    lat +
    "&lon=" +
    long;
  const response = await fetch(url);
  const data = await response.json();
  roadname = data["display_name"];
  return roadname;
}

async function getISS(o_lat, o_long, d_lat, d_long) {
  url =
    "https://api.tomtom.com/routing/1/calculateRoute/" +
    o_lat +
    "," +
    o_long +
    ":" +
    d_lat +
    "," +
    d_long +
    "/json?key=mHywp1xqUaq62ROfTAuCRKtxjTYA0Zak&routeType=shortest";
  const response = await fetch(url);
  const data = await response.json();
  console.log(data);
  avg = data["routes"][0]["summary"]["lengthInMeters"];
  time_sec = data["routes"][0]["summary"]["travelTimeInSeconds"];
  list = [avg, time_sec];
  return list;
}

const mymap = L.map("issMap").setView(origin, 13);
const attribution =
  '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';

const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const tiles = L.tileLayer(tileUrl, { attribution });

tiles.addTo(mymap);
const marker = L.marker(origin);
marker.addTo(mymap);
marker.bindPopup("Origin").openPopup();

const marker1 = L.marker(dest);
marker1.addTo(mymap);
marker1.bindPopup("Destination").openPopup();
var i = 0;
console.log(long.length);
for (i = 0; i < lat.length; i++) {
  const circle = L.circle([lat[i], long[i]], {
    color: "yellow",
    fillColor: "yellow",
    fillOpacity: 0.5,
    radius: 35,
  });
  circle.addTo(mymap);
}

const issIcon = L.icon({
  iconUrl: "{{url_for('static',filename='images/amb.png')}}",
  iconSize: [50, 32],
  iconAnchor: [25, 16],
});
let marker3 = L.marker(origin, { icon: issIcon }).addTo(mymap);

let yo = [];

var i = 0,
  x = 0;
a = setInterval(function () {
  mymap.removeLayer(marker3);
  marker3 = L.marker([lat[i], long[i]], { icon: issIcon });
  marker3.addTo(mymap);

  const circle2 = L.circle([lat[i], long[i]], {
    color: "black",
    fillColor: "yellow",
    fillOpacity: 0.5,
    radius: 2,
  });
  circle2.addTo(mymap);
  i++;
}, 300);
