import streamlit as st



st.set_page_config(
    page_title="Smart Recipe Finder",
    page_icon="🍳",
    layout="centered"
)

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(BASE_DIR, "style.css")

with open(CSS_PATH, encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )



recipes = {
    "Sandwich": {
        "ingredients": ["bread", "tomato", "onion", "cheese"],
        "time": "10 minutes",
        "image": "images/sandwich.jpg",
        "steps": [
            "Take two slices of bread.",
            "Add tomato, onion and cheese.",
            "Toast the sandwich on a pan.",
            "Serve hot."
        ]
    },

    "Pasta": {
        "ingredients": ["pasta", "tomato", "onion", "garlic"],
        "time": "20 minutes",
        "image": "images/pasta.jpg",
        "steps": [
            "Boil the pasta.",
            "Cook onion, tomato and garlic in a pan.",
            "Add the boiled pasta.",
            "Mix well and serve."
        ]
    },

    "Poha": {
        "ingredients": ["poha", "onion", "potato", "peanuts"],
        "time": "15 minutes",
        "image": "images/poha.jpg",
        "steps": [
            "Wash the poha and keep it aside.",
            "Cook onion and potato in a pan.",
            "Add poha and peanuts.",
            "Mix everything and cook for a few minutes."
        ]
    },

    "Fried Rice": {
        "ingredients": ["rice", "carrot", "onion", "peas"],
        "time": "15 minutes",
        "image": "images/fried_rice.jpg",
        "steps": [
            "Heat oil in a pan.",
            "Add onion, carrot and peas.",
            "Add cooked rice.",
            "Mix well and serve hot."
        ]
    },

    "Pizza": {
        "ingredients": ["bread", "tomato", "onion", "cheese"],
        "time": "15 minutes",
        "image": "images/pizza.jpg",
        "steps": [
            "Take a bread slice as the base.",
            "Add tomato, onion and chbanana", "milk", "honeese.",
            "Cook it on a pan until the cheese melts.",
            "Serve hot."
        ]
    },

    "Salad": {
        "ingredients": ["tomato", "onion", "carrot", "cucumber"],
        "time": "10 minutes",
        "image": "images/salad.jpg",
        "steps": [
            "Wash all vegetables.",
            "Cut tomato, onion, carrot and cucumber.",
            "Mix all vegetables in a bowl.",
            "Add salt and lemon according to taste."
        ]
    },

    "Burger": {
            "ingredients": ["bun", "onion", "tomato", "sauce", "patty"],
        "time":"5 minutes",
        "image":"images/burger.jpg",
        "steps":[
            "Wash the vegetables.",
            "Cut the tomato and onion.",
            "Place the tomato, onion, patty and sauce on the bottom bun.",
            "Put the other half of the bun on top."
        ]
    },

    "Omelette": {
        "ingredients": ["eggs", "onion", "tomato", "cheese"],
        "time": "10 minutes",
        "image": "images/omelette.jpg",
        "steps": ["Beat the eggs.", "Chop the onion and tomato.", "Cook the eggs and vegetables in a pan.", "Add cheese, fold and serve."]
    },

    "Pancakes": {
        "ingredients": ["flour", "milk", "eggs", "sugar"],
        "time": "20 minutes",
        "image": "images/pancakes.jpg",
        "steps": ["Mix flour and sugar.", "Whisk in milk and eggs.", "Pour batter into a hot pan.", "Flip when bubbles form and cook until golden."]
    },

    "Grilled Cheese": {
        "ingredients": ["bread", "cheese", "butter"],
        "time": "10 minutes",
        "image": "images/grilled_cheese.jpg",
        "steps": ["Butter one side of each bread slice.", "Add cheese between the unbuttered sides.", "Toast in a pan until golden on both sides.", "Serve warm."]
    },

    "Vegetable Soup": {
        "ingredients": ["carrot", "onion", "potato", "peas"],
        "time": "30 minutes",
        "image": "images/vegetable_soup.jpg",
        "steps": ["Chop the vegetables.", "Cook onion in a pot until soft.", "Add the other vegetables and water.", "Simmer until tender and serve."]
    },

    "Banana Smoothie": {
        "ingredients": ["banana", "milk", "honey"],
        "time": "5 minutes",
        "image": "images/banana_smoothie.jpg",
        "steps": ["Peel and slice the banana.", "Add banana, milk and honey to a blender.", "Blend until smooth.", "Pour into a glass and serve."]
    }

}




st.markdown(
    """
    <div class="header">
        <div class="emoji">🍳</div>
        <h1>Smart Recipe Finder</h1>
        <p>Find delicious recipes using the ingredients you already have.</p>
    </div>
    """,
    unsafe_allow_html=True
)




st.markdown(
    '<div class="section-title">🥕 What ingredients do you have?</div>',
    unsafe_allow_html=True
)

ingredients_input = st.text_input(
    "",
    placeholder="Example: bread, tomato, onion",
    key="ingredients"
)

find_button = st.button("🔍 Find My Recipes")




if find_button:

    if ingredients_input.strip() == "":
        st.warning("Please enter at least one ingredient.")

    else:

        user_ingredients = {
            item.strip().lower()
            for item in ingredients_input.split(",")
            if item.strip()
        }

        matching_recipes = []

        for recipe_name, recipe in recipes.items():
            recipe_ingredients = {
                ingredient.strip().lower()
                for ingredient in recipe["ingredients"]
            }

            if user_ingredients.issubset(recipe_ingredients):
                matching_recipes.append(recipe_name)

     

        if matching_recipes:

            st.markdown(
                f'<div class="result-title">✨ {len(matching_recipes)} recipe(s) found!</div>',
                unsafe_allow_html=True
            )

            for recipe_name in matching_recipes:

                recipe = recipes[recipe_name]

                st.markdown(
                    f"""
                    <div class="recipe-card">
                        <h2>🍽️ {recipe_name}</h2>
                        <p>⏱️ Cooking time: {recipe["time"]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.image(
                    recipe["image"],
                    use_container_width=True
                )

                st.markdown("### 🥕 Ingredients")

                ingredients_text = " • ".join(
                    ingredient.title()
                    for ingredient in recipe["ingredients"]
                )

                st.write(ingredients_text)

                st.markdown("### 👩‍🍳 How to make it")

                for number, step in enumerate(recipe["steps"], 1):
                    st.write(f"**Step {number}:** {step}")

                st.divider()

        else:

            st.error(
                "😕 No exact recipe found with these ingredients."
            )

            st.info(
                "Try adding more ingredients. Example: bread, tomato, onion, cheese"
            )




st.markdown(
    """
    <div class="footer">
        Made with ❤️ using Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)




