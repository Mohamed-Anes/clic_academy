/* Constants */
import { all_results, results_container } from "./search.js";

const RESULTS_PER_PAGE = 100;
const page_select = document.getElementById("page-select");
var num_of_pages;

const SEARCH_RESULTS = "searchResults"; // ID of element to display search results
const PAGINATE = "paginate"; // ID of element to display pagination results

function pagination(total_results) {
  console.log("total_results : " + total_results);
  // Determine the length of the array to be returned, which is the total
  // results divided by the number of results per page.
  const length = Math.ceil(total_results / RESULTS_PER_PAGE);
  num_of_pages = length;

  // Fill up a new array with the range numbers
  // using Array.from() with a mapping function.
  let full_array = Array.from(Array(length), (x, index) => index + 1);

  //adding the pages to the page select
  page_select.hidden = false;
  full_array.forEach((element) => {
    let temp_element = document.createElement("option");
    temp_element.value = element;
    temp_element.innerText = element;
    page_select.appendChild(temp_element);
  });

  page_select.value = 1;
}

page_select.addEventListener("change", (event) => {
  // calculate first and last element indices
  let first_element = (page_select.value - 1) * RESULTS_PER_PAGE;
  let last_element = first_element + RESULTS_PER_PAGE - 1;
  if (last_element >= all_results.length) {
    last_element = all_results.length - 1;
  }
  // delete page elements
  results_container.innerHTML = "";
  // add new page elements
  var temp_element;

  for (let i = first_element; i <= last_element; i++) {
    temp_element = document.createElement("a");
    temp_element.setAttribute("href", all_results[i].id);
    temp_element.innerText = all_results[i].word;
    results_container.appendChild(temp_element);
  }
});

const prv_slct = document.getElementById("previous-page");
const nxt_slct = document.getElementById("next-page");

prv_slct.addEventListener("click", (event) => {
  let temp = parseInt(page_select.value) - 1;
  nxt_slct.disabled = false;
  page_select.value = temp;
  page_select.dispatchEvent(new Event("change"));
  if (temp == 1) {
    prv_slct.disabled = true;
    return;
  }
});

nxt_slct.addEventListener("click", (event) => {
  let temp = parseInt(page_select.value) + 1;
  prv_slct.disabled = false;
  page_select.value = temp;
  page_select.dispatchEvent(new Event("change"));
  if (temp == num_of_pages) {
    nxt_slct.disabled = true;
    return;
  }
});

export { pagination, page_select };
