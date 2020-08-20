const names = ['Joe', 'Sue', 'Frank', 'Franz'];

const name_list = document.getElementById("name_list");

function addNamesToDOM(names) {
    names.forEach(name => {
        const element = document.createElement("div");
        element.innerHTML = name;
        name_list.appendChild(element);
    });
}

function addFilteredNamesToDOM() {
    const search_term = input_box.value;
    filtered_names = names.filter(name => {
        return name.toLowerCase().includes(search_term.toLocaleLowerCase());
    });
    name_list.innerHTML = '';
    addNamesToDOM(filtered_names);
}

document.addEventListener("DOMContentLoaded", addNamesToDOM(names));

let filtered_names = [];
const input_box = document.getElementById("input_box");
const filter_button = document.getElementById("filter_names");

filter_button.addEventListener('click', addFilteredNamesToDOM);

input_box.addEventListener('keyup', () => {
    const search_term = input_box.value.toLowerCase();
    filtered_names = names.filter(name => {
        return name.toLocaleLowerCase().includes(search_term);
    });
    name_list.innerHTML = '';
    addNamesToDOM(filtered_names);
});

const reverse_button = document.getElementById("reverse");

reverse_button.addEventListener("click", () => {
    names.reverse();
    const search_term = input_box.value.toLowerCase();
    filtered_names = names.filter(name => {
        return name.toLocaleLowerCase().includes(search_term);
    });
    name_list.innerHTML = '';
    addNamesToDOM(filtered_names);
});

const random_number_btn = document.getElementById("random_number_btn");
const random_number = document.getElementById("random_number");
