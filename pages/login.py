from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username_input = "//input[@placeholder='Username']"
        self.password_input = "//input[@placeholder='Password']"
        self.login_button = "//button[normalize-space()='Login']"

    def open_login_page(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
