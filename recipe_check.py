# urljoinを利用する場合はインポート
# from urllib.parse import urljoin
import requests
import bs4


def get_recipes_with_cookpad(food):
    '''
    cookpadからキーワード検索したレシピの、タイトルとURLの配列を返す
    '''

    base_url = "https://cookpad.com"
    search_url = f"{base_url}/search/{food}"

    res = requests.get(search_url)

    soup = bs4.BeautifulSoup(res.content, "html.parser")
    recipe_previews = soup.find_all(class_="recipe-preview")

    recipes = []
    for recipe_preview in recipe_previews:
        a_tag = recipe_preview.find(class_="recipe-title")
        recipes.append(
            {"title": a_tag.text, "url": f"{base_url}{a_tag.attrs['href']}"}
            # urljoinで「/」の有無を気にせず連結できる(URLの場合)
            # {"title": a_tag.text, "url": urljoin(res.url, a_tag.attrs["href"])}
        )

    return recipes


def main():
    food = "トマト"

    recipes = get_recipes_with_cookpad(food)

    for recipe in recipes:
        food_info = f'レシピ名 {recipe["title"]}, URL {recipe["url"]}'
        print(food_info)


if __name__ == "__main__":
    main()