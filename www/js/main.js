// List of loaded recipes.
let recipeList = null;
// Currently selected recipy.
let currRecipe = null;
// Recipy select box.
const recipySelector = document.querySelector('#navSel');
// Ingredient serving slider.
const portionSlider = document.querySelector('#ingrServings');

/**
 * Event handler for recipy selection.
 * @param {*} evt 
 */
function recipeSelected(evt) {
    // Set current recipy.
    currRecipe = recipeList[recipySelector.value];
    // Set recipy info.
    document.querySelector('#infoImage').style.backgroundImage = "url('/img/"+currRecipe.image+"')";
    document.querySelector('#infoTitle').textContent = currRecipe.title;
    document.querySelector('#infoSummary').textContent = currRecipe.summary;
    document.querySelector('#infoDetails').innerHTML = currRecipe.details;
    document.querySelector('#infoSource').textContent = currRecipe.url;
    document.querySelector('.page-default').style.display='none';
    document.querySelector('#pageInfo').style.display='block';
    document.querySelector('#pageIngr').style.display='block';
    document.querySelector('#pageInstr').style.display='block';
    document.querySelector('#pageRev').style.display='block';
    document.querySelector('#ingrNum').textContent=currRecipe.num_default;
    document.querySelector('#ingrSuff').textContent=currRecipe.num_suffix;
    // Slider settings
    portionSlider.min = currRecipe.num_min; 
    portionSlider.max = currRecipe.num_max;
    portionSlider.value = currRecipe.num_default;
    // Add ingredients
    let ingrArr = new Array();
    let i = 0;
    currRecipe.ingredients.forEach(item => {
        let ingr = document.createElement('li');
        if(item.amount==0) {
            // Section
            ingr.className='ingr-sec';
            ingr.textContent = item.name;
        } else {
            // Ingredient with id
            ingr.innerHTML = item.name + ', <em><span id="ingr_'+(i)+'">'+item.amount+'</span> '+item.unit+'</em>';
        }
        i++;
        ingrArr.push(ingr);
    });
    document.querySelector('#ingrList').replaceChildren(...ingrArr);
    // Add instructions
    let instrArr = new Array();
    currRecipe.instructions.forEach(instr => {
        // Instruction list item.
        let li = document.createElement('li');
        li.innerHTML = instr.text;
        instrArr.push(li);
    });
    document.querySelector('#instrList').replaceChildren(...instrArr);
    // Add reviews
    setReviews();
}
/**
 * Fix how number is displayed.
 * @param {*} amount 
 * @returns fixed number
 */
function amountFix(amount) {
    let _amount = Number.parseFloat(amount.toPrecision(4));
    return _amount;
}
/**
 * Event handler for amount slider movement.
 * @param {*} evt 
 */
function calculateAmounts(evt) {
    let i = 0;
    // Scale relative to original value.
    const scale = portionSlider.value / currRecipe.num_default;
    document.querySelector('#ingrNum').textContent = portionSlider.value;
    currRecipe.ingredients.forEach(item => {
        if(item.amount != 0) {
            let amount = document.querySelector('#ingr_'+i);
            amount.textContent = amountFix(item.amount * scale);
        }
        i++;
    });
}
/**
 * Set reviews content as articles.
 */
function setReviews() {
    let revArr = new Array();
    currRecipe.reviews.forEach(rev => {
        let art = document.createElement('article');
        art.innerHTML = '<p class="rev-name">'+rev.name+'</p><p class="rev-rating" /><p class="rev-text">'+rev.text+'</p>'
        addStars(art.querySelector('.rev-rating'),false,rev.rating)
        revArr.push(art);
    });
    document.querySelector('#revList').replaceChildren(...revArr);
}
/**
 * Handle clicking on rating stars.
 * @param {*} evt 
 */
function handleRating(evt) {
    let rating = parseInt(evt.target.getAttribute('data-value'));
    let button = document.querySelector('#revRating button');
    let storedValue = document.querySelector('#rating');
    storedValue.value = rating;
    while(button != null) {
        let val = parseInt(button.getAttribute('data-value'));
        if(val <= rating) {
            button.classList.remove('st-empty');
            button.classList.add('st-filled');
        }
        else {
            button.classList.remove('st-filled');
            button.classList.add('st-empty');
        }
        button = button.nextElementSibling;
    }
}

/**
 * Handle posting of rating.
 * @param {*} evt 
 */
function handleSubmit(evt) {
    evt.preventDefault();
    const fdata = new FormData(evt.target);
    let data = new Object();
    fdata.forEach((value, key, parent) => {
        data[key] = value;
    })
    data.recipe_id = currRecipe.id;
    fetch('/review',{
        method:'POST',
        body:JSON.stringify(data),
        headers: {"Content-Type": "application/json"}
    }).then(
        resp => {
            if(resp.status != 200) {
                alert(resp.statusText);
            } else {
                resp.json().then(rev => {
                    currRecipe.reviews.push(rev);
                    setReviews();
                });
            }
        },
        alert
    ).catch(alert);
}
/**
 * Inject ratings stars into a container element.
 * @param {*} container Target container
 * @param {*} interacting True for interactive rating.
 * @param {*} rating Rating to display. 0=empty
 */
function addStars(container,interacting,rating) {
    for(let i=1; i<6; i++) {
        let bt = document.createElement('button');
        bt.type='button';
        bt.style.display='inline';
        if(i <= rating) bt.className="rt-bt st-filled";
        else bt.className="rt-bt st-empty";
        if(interacting===true) {
            bt.setAttribute('data-value',i);
            bt.onclick = handleRating;
        }
        container.appendChild(bt);
    }
}
/**
 * Handle recipe loading results from backend.
 * @param {*} recipes 
 */
function handleRecipes(recipes) {
    recipeList = recipes;
    let idx = 0;
    recipes.forEach(recipe => {
        let opt = document.createElement('option');
        opt.value = idx++;
        opt.textContent = recipe.title;
        recipySelector.append(opt);
    });

    recipySelector.addEventListener('change',recipeSelected);
    portionSlider.addEventListener('input',calculateAmounts);
    document.querySelector('form').addEventListener('submit', handleSubmit);

    let ratDiv = document.querySelector('#revRating');
    addStars(ratDiv,true,0);
}

/**
 * Initial call starts app by fetching recipes.
 */
fetch('/recipes')
    .then(resp => resp.json())
    .then(handleRecipes)
    .catch(alert);
