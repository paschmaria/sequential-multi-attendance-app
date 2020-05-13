$(document).ready(function(){
    $('[data-toggle="offcanvas"]').click(function(){
        $("#navigation").toggleClass("hidden-xs");
    });

    let stateElement = document.querySelector("#state"); //select state field
    let lgaElement = document.querySelector("#lga");
    lgaElement.options[0] = new Option('Select LGA','');

    function populateStates() {
        stateElement.length=0;
        stateElement.options[0] = new Option('Select State','');
        stateElement.selectedIndex = 0;

        // update fields using data in lga_data.js
        data.map(res => {
            stateElement.options[stateElement.length] = new Option(res.state.name, res.state.name);
        });
    }

    function populateLGA(state) {
        lgaElement.length=0;
        lgaElement.options[0] = new Option('Select LGA','');
        lgaElement.selectedIndex = 0;
        let stateLGA = data.find(item => item.state.name === state).state.locals
        // update fields using data in lga_data.js
        stateLGA.map(res => {
            lgaElement.options[lgaElement.length] = new Option(res.name, res.name);
        });
    }

    populateStates();

    stateElement.onchange = function () {
        populateLGA(this.options[this.selectedIndex].value);
    }
 });