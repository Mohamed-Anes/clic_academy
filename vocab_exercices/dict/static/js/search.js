// For pagination
import { pagination, page_select } from "./pagination.js";

// Search box elements
const srch_start = document.getElementById("start");
const srch_end = document.getElementById("end");
const srch_btn = document.getElementById("search-button");
const srch_inpt = document.getElementById("search-input");
const srch_lem = document.getElementById("lem");
const srch_mot = document.getElementById("mot");
var results_container = document.getElementById("searchResults");

// Controls for the search options
srch_start.addEventListener("change", (event) => {
  srch_end.min = srch_start.value;
});

srch_end.addEventListener("change", (event) => {
  srch_start.max = srch_end.value;
});

var all_results;

// Sending the search parameters
srch_btn.addEventListener("click", (event) => {
  var lem_mot;
  if (srch_lem.checked) {
    lem_mot = srch_lem.value;
  } else {
    lem_mot = srch_mot.value;
  }
  const srch_parameters = {
    query: srch_inpt.value,
    range_strt: srch_start.value,
    range_end: srch_end.value,
    lem_mot: lem_mot,
  };

  console.log(srch_parameters);

  // Sending the fetch request
  fetch("/search", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(srch_parameters),
  })
    .then((response) => response.text())
    .then((data) => {
      // Handle the received data
      data = JSON.parse(data);
      console.log(data);
      all_results = data.results;

      // // delete previous search results
      // results_container.innerHTML = "";

      // var temp_element;
      // data.results.forEach((element) => {
      //   temp_element = document.createElement("a");
      //   temp_element.setAttribute("href", element.id);
      //   temp_element.innerText = element.word;
      //   results_container.appendChild(temp_element);
      // });

      // buildPagination(data.length);
      console.log(data.results.length);

      pagination(data.results.length);
      page_select.dispatchEvent(new Event("change"));

      // Update the webpage content with the received data
      // document.getElementById('reload-content').innerHTML = data;
    })
    .catch((error) => {
      // Handle any errors
      console.error(error);
    });
});

export { all_results, results_container };
