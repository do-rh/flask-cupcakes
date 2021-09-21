"use strict";

const API_URL = "http://localhost:5000/";

// Populates HTML with cupcake list from DB
async function getCupcakes(){

    let resp = await axios.get(`${API_URL}api/cupcakes`);
    $("#cupcake_list").empty();

    for (let cupcake of resp.data.cupcakes){
        $("#cupcake_list").append(`<li>
            <a href='/api/cupcakes/${cupcake.id}'>${cupcake.flavor}, Size: ${cupcake.size} </a>
            </li>`)
    }
}

// Handles click on form submit, adds a new cupcake to the DB and the HTML list
async function newCupcake(evt){
    evt.preventDefault();
    let resp = await axios.post(`${API_URL}api/cupcakes`, {
        flavor: $("#flavor").val(),
        size: $("#size").val(),
        rating: $("#rating").val(),
        image: $("#image").val()
    });
    getCupcakes();
}

getCupcakes();

$("#submit_button").on("submit", newCupcake);