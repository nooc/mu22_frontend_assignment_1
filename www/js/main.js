let recipeList = null;
const recipySelector = document.querySelector('select.recipy-selector');
const recipyComments = document.querySelector('section.recipy-comments');

function recipeSelected(evt) {
    let recipy = recipeList[recipySelector.value];

    document.querySelector('.description-image').style.backgroundImage = '/img/'+recipy.image;
    document.querySelector('header h1').textContent = recipy.title;
    document.querySelector('header details summary').textContent = recipy.summary;
    document.querySelector('header details p').innerHTML = recipy.details;
    
    //recipyComments
}

function handleRecipes(recipes) {
    recipeList = recipes;
    let idx = 0;
    recipes.forEach(recipe => {
        let opt = document.createElement('option');
        opt.value = idx++;
        opt.textContent = recipe.title;
        recipySelector.append(opt);
    });

    recipySelector.addEventListener('change',recipeSelected)
}

fetch('/recipes')
    .then(resp => resp.json())
    .then(handleRecipes)
    .catch(alert);
