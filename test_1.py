
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_obchodni_podminky_page(page):

    #načtení webové stránky
    page.goto("https://www.engeto.cz")

    #potvrzení cookies
    page.get_by_role("button", name="Souhlasím jen s nezbytnými").click()
    
    #kliknutí na obchodní podmínky
    page.get_by_text("Obchodní podmínky", exact=True).click()

    #očekávám viditelný odpovídající nadpis stránky
    expect(page.get_by_role("heading", name="Všeobecné obchodní podmínky")).to_be_visible()

    