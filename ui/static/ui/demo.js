// Comments

// // variable types
// let i;
// const j;
// alert
// arrays
const names = ['Joe', 'Sue', 'Frank', 'Franz'];
// document object
// get by id

const names_list = document.getElementById("names_list");

function appendToDOM(names) {
    const search_term = document.getElementById("search_term").value.toLowerCase();
    const filtered_list = names.filter(name => {
        return name.toLocaleLowerCase().includes(search_term);
    });
    names_list.innerHTML = "";
    filtered_list.forEach(function (name) {


//    Create a new div element
        const div = document.createElement("div");
//    Assign that element's innerHtml to the value from the array
        div.innerHTML = name;
//    Append the new div element to our names_list
        names_list.appendChild(div);
    })
}

document.addEventListener('DOMContentLoaded', appendToDOM(names));

// Create a list of names on the page

// Search by button
const filter_text_btn = document.getElementById("filter_text");
filter_text_btn.addEventListener("click", function () {
    console.log("works");
    // Filter our names list for any name with a substring of our search term
    const search_term = document.getElementById("search_term").value;
    const filtered_list = names.filter(name => {
        return name.includes(search_term);
    })
    // clear our names_list
    names_list.innerHTML = "";
    // Append children from filtered_list
    appendToDOM(filtered_list);
});

const search_box = document.getElementById("search_term");
search_box.addEventListener("keyup", function () {
    console.log("works");
    // Filter our names list for any name with a substring of our search term
    const search_term = document.getElementById("search_term").value.toLowerCase();
    const filtered_list = names.filter(name => {
        return name.toLocaleLowerCase().includes(search_term);
    })
    // clear our names_list
    names_list.innerHTML = "";
    // Append children from filtered_list
    appendToDOM(filtered_list);
});

const reverse_element = document.getElementById("reverse");
reverse_element.addEventListener('click', () => {
    names.reverse()
    names_list.innerHTML = "";
    appendToDOM(names);
});
// Search by typing
// Search case insenstive
// Reverse order
// Ajax

const random_number_element = document.getElementById("random_number");
const random = document.getElementById("random");
random.addEventListener("click", () => {
    axios.get("/random")
        .then(function(response){
            const random_number = response.data.random_number;
            random_number_element.innerHTML = random_number;
        })
})