from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_engeto_kontakt_email(page):

    #načtení webové stránky
    page.goto("https://engeto.cz/")

    #potvrzení cookies
    page.locator("#cookiescript_reject").click()
    
    #klik na kontakty
    page.get_by_role("link", name="Kontakt", exact=True).click()

    #vymezení konkrétního místa na stránce
    page.locator("block-contact-box[href='mailto:info@engeto.com']")

    #kontaktní email je viditelný
    expect(page.get_by_role("heading", name="info@engeto.com")).to_be_visible(timeout=10000)

    