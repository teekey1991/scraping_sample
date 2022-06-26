import bs4
import requests


def main():
    food = "とまと"
    recipes = find_recipe(food)
    print(recipes)

def find_recipe(food):
    base_url = "https://cookpad.com"

    res = requests.get(f"{base_url}/search/{food}")

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # classがrecipe-previewの要素を取得
    recipe_previews = soup.find_all(class_="recipe-preview")

    # recipe-previewsからタイトルとURLを取得
    recipes = []
    for recipe_preview in recipe_previews:
        a_tag = recipe_preview.find("a", class_="recipe-title")
        recipes.append({"title": a_tag.text, "url": f"{base_url}{a_tag.attrs['href']}"})
    return recipes


if __name__ == "__main__":
    main()
