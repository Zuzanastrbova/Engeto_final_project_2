from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_engeto_testing_akademie_color_nadpis_proplacení(page):
    #načtení webové stránky
    page.goto("https://engeto.cz/")

    #potvrzení cookies
    page.locator("#cookiescript_reject").click(timeout=30000)
    
    #klik na přehled IT kurzů
    page.locator(".block-button[href='/prehled-kurzu/']").click(timeout=30000)
    
    #klik na oblast testing akademie
    page.locator(".card[href='https://engeto.cz/testovani-softwaru/']").click(timeout=30000)

    #vymezení konkrétního bloku na stránce
    page.locator(".h3=block-a-block")

    #sledovaný nadpis v daném bloku má odpovídající barvu
    expect(page.get_by_role("heading", name="Nech si proplatit 82 % ceny kurzu!")).to_have_css("color","rgb(192, 1, 240)")

