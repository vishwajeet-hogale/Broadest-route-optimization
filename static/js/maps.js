// // Making a map and tiles
// // Setting a higher initial zoom to make effect more obvious
// var lat = document.currentScript.getAttribute("lat");
// var long = document.currentScript.getAttribute("long");
// var origin = document.currentScript.getAttribute("origin");
// var dest = document.currentScript.getAttribute("dest");

// console.log(lat, long, origin, dest);

// var box = document.getElementById("box");

// async function getAdd(lat, long) {
//   url =
//     "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=" +
//     lat +
//     "&lon=" +
//     long;
//   const response = await fetch(url);
//   const data = await response.json();
//   roadname = data["display_name"];
//   return roadname;
// }
const locationsDetails = [
  {
    address:
      "NICE Peripheral Ring Road, Gattigerepalya, Hemmigepura, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560074, India",
    nodeName: "1",
  },
  {
    address:
      "Banashankari 6th Stage - 7th Block, Hemmigepura, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560074, India",
    nodeName: "2",
  },
  {
    address:
      "Banashankari 6th Stage - 3rd Block, Hemmigepura, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560109, India",
    nodeName: "3",
  },
  {
    address:
      "NICE Expressway, Banashankari 6th Stage - 7th Block, Hemmigepura, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560098, India",
    nodeName: "4",
  },
  {
    address:
      "Ganakkal, Hemmigepura, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560098, India",
    nodeName: "5",
  },
  {
    address:
      "Channasandra, Dr. Vishnuvardhan Road, Channasandra, Rajarajeshwari Nagar, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560098, India",
    nodeName: "6",
  },
  {
    address:
      "Dr. Vishnuvardhan Road, AGS Layout, Rajarajeshwari Nagar, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560098, India",
    nodeName: "7",
  },
  {
    address:
      "80 Feet Road, AGS Layout, Rajarajeshwari Nagar, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560098, India",
    nodeName: "8",
  },
  {
    address:
      "NICE Expressway, AGS Layout, Uttarahalli, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 570061, India",
    nodeName: "9",
  },
  {
    address:
      "Kenchenahalli Main Road, Srinivasapura, Rajarajeshwari Nagar, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560098, India",
    nodeName: "10",
  },
  {
    address:
      "80 Feet Road, AGS Layout, Rajarajeshwari Nagar, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560098, India",
    nodeName: "11",
  },
  {
    address:
      "80 Feet Road, AGS Layout, Rajarajeshwari Nagar, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560098, India",
    nodeName: "12",
  },
  {
    address:
      "Kanakapura Road, Bangalore South, Bengaluru Urban District, Karnataka, 560109, India",
    nodeName: "13",
  },
  {
    address:
      "Kanakapura Road, Thalaghattapura, Hemmigepura, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560109, India",
    nodeName: "14",
  },
  {
    address:
      "NICE Peripheral Ring Road, Anjanapura, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560108, India",
    nodeName: "15",
  },
  {
    address:
      "Anjanapura, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560108, India",
    nodeName: "16",
  },
  {
    address:
      "Bannerghatta Road, Gottigere, Gottigere Ward, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560083, India",
    nodeName: "17",
  },
  {
    address:
      "Bannerghatta Road, Gottigere, Gottigere Ward, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560083, India",
    nodeName: "18",
  },
  {
    address:
      "Bannerghatta Road, Gottigere, Gottigere Ward, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560083, India",
    nodeName: "19",
  },
  {
    address:
      "Konanakunte, Anjanapura, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560062, India",
    nodeName: "20",
  },
  {
    address:
      "Sri Nidhi Medicals, 3, Anjanapura 60 Feet Road, Thippasandra, Anjanapura, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560062, India",
    nodeName: "21",
  },
  {
    address:
      "Vajrahalli, Hemmigepura, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560062, India",
    nodeName: "22",
  },
  {
    address:
      "Jambu Savari Dinne Bus Bay, Amruth Nagar Main Road, Kothnur, Gottigere Ward, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560083, India",
    nodeName: "23",
  },
  {
    address:
      "Amruth Nagar Main Road, Kothnur, Gottigere Ward, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560083, India",
    nodeName: "24",
  },
  {
    address:
      "Kothnur Main Road, Navodaya Nagar, Gottigere Ward, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560083, India",
    nodeName: "25",
  },
  {
    address:
      "1st Cross Road, Sri Guru Raghavendra Nagar, Puttenahalli Ward, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560078, India",
    nodeName: "26",
  },
  {
    address:
      "Eshwara Layout, Konanakunte, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560082, India",
    nodeName: "27",
  },
  {
    address:
      "6 C Cross Road, Srinidhi Layout, Anjanapura, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560082, India",
    nodeName: "28",
  },
  {
    address:
      "PNB Layout, Vasanthapura, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560082, India",
    nodeName: "29",
  },
  {
    address:
      "Kanakapura Road, Vasanthapura, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560082, India",
    nodeName: "30",
  },
  {
    address:
      "Kanakapura Road, Thalaghattapura, Hemmigepura, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560109, India",
    nodeName: "31",
  },
  {
    address:
      "80 Feet Road, Subramanyapura, Uttarahalli, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560062, India",
    nodeName: "32",
  },
  {
    address:
      "80 Feet Road, Banashankari 6th Stage - 1st Block, Uttarahalli, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560098, India",
    nodeName: "33",
  },
  {
    address:
      "80 Feet Road, Banashankari 6th Stage - 2nd Block, Hemmigepura, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560098, India",
    nodeName: "34",
  },
  {
    address:
      "St. Martha's Hospital, Dr. Vishnuvardhan Road, AGS Layout, Uttarahalli, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560061, India",
    nodeName: "35",
  },
  {
    address:
      "Subramanyapura Main Road, Subramanyapura, Uttarahalli, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560111, India",
    nodeName: "36",
  },
  {
    address:
      "Pipeline Vasanthapura, Konanakunte-Uttarahalli Road, Vasanthapura, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560111, India",
    nodeName: "37",
  },
  {
    address:
      "AGS Layout, Uttarahalli, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 570061, India",
    nodeName: "38",
  },
  {
    address:
      "80 Feet Road, Anjanapura, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560108, India",
    nodeName: "39",
  },
  {
    address:
      "Holiday Village Road, Bangalore South, Bengaluru Urban District, Karnataka, 560109, India",
    nodeName: "40",
  },
  {
    address:
      "Kanakapura Road, Thalaghattapura, Hemmigepura, Rajarajeshwari Nagar Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560109, India",
    nodeName: "41",
  },
  {
    address:
      "Holy Spirit School ICSE, Bannerghatta Road, Nobo Nagar, Begur, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560083, India",
    nodeName: "42",
  },
  {
    address:
      "BDA 80 Feet Road, Arekere, Arakere, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560076, India",
    nodeName: "43",
  },
  {
    address:
      "Reliance Mart, Arekere Mico Layout Main Road, Govinda Reddy Layout, Puttenahalli Ward, Bommanahalli Zone, Bengaluru, Bangalore South, Bengaluru Urban District, Karnataka, 560076, India",
    nodeName: "44",
  },
];
// async function getISS(o_lat, o_long, d_lat, d_long) {
//   url =
//     "https://api.tomtom.com/routing/1/calculateRoute/" +
//     o_lat +
//     "," +
//     o_long +
//     ":" +
//     d_lat +
//     "," +
//     d_long +
//     "/json?key=mHywp1xqUaq62ROfTAuCRKtxjTYA0Zak&routeType=shortest";
//   const response = await fetch(url);
//   const data = await response.json();
//   console.log(data);
//   avg = data["routes"][0]["summary"]["lengthInMeters"];
//   time_sec = data["routes"][0]["summary"]["travelTimeInSeconds"];
//   list = [avg, time_sec];
//   return list;
// }

// const mymap = L.map("issMap").setView(origin, 13);
// const attribution =
//   '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';

// const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
// const tiles = L.tileLayer(tileUrl, { attribution });

// tiles.addTo(mymap);
// const marker = L.marker(origin);
// marker.addTo(mymap);
// marker.bindPopup("Origin").openPopup();

// const marker1 = L.marker(dest);
// marker1.addTo(mymap);
// marker1.bindPopup("Destination").openPopup();
// var i = 0;
// console.log(long.length);
// for (i = 0; i < lat.length; i++) {
//   const circle = L.circle([lat[i], long[i]], {
//     color: "yellow",
//     fillColor: "yellow",
//     fillOpacity: 0.5,
//     radius: 35,
//   });
//   circle.addTo(mymap);
// }

// const issIcon = L.icon({
//   iconUrl: "{{url_for('static',filename='images/amb.png')}}",
//   iconSize: [50, 32],
//   iconAnchor: [25, 16],
// });
// let marker3 = L.marker(origin, { icon: issIcon }).addTo(mymap);

// let yo = [];

// var i = 0,
//   x = 0;
// a = setInterval(function () {
//   mymap.removeLayer(marker3);
//   marker3 = L.marker([lat[i], long[i]], { icon: issIcon });
//   marker3.addTo(mymap);

//   const circle2 = L.circle([lat[i], long[i]], {
//     color: "black",
//     fillColor: "yellow",
//     fillOpacity: 0.5,
//     radius: 2,
//   });
//   circle2.addTo(mymap);
//   i++;
// }, 300);

function onSubmit(event) {
  event.preventDefault();

  var source = document.getElementById("source").value;
  var destination = document.getElementById("destination").value;
  document.getElementById("result").innerHTML =
    "<h2>Planning route from " + source + " to " + destination + "...</h2>";
}
