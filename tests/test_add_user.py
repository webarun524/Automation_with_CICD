from pages.login import LoginPage


def test_add_user(page):
    login_page = LoginPage(page)

    login_page.open_login_page()
    login_page.login("Admin", "admin123")

    login_page.add_user()