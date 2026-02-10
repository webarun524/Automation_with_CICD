from pages.login import LoginPage

def test_login(page):
    login_page = LoginPage(page)

    login_page.open_login_page()
    login_page.login("Admin", "admin123")
    page.wait_for_load_state("networkidle")

