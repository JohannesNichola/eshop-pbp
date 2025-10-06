from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from django.contrib.auth.models import User
from main.models import Products


class ProductsFunctionalTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Buka Chrome sekali buat semua test
        cls.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        # Tutup Chrome setelah selesai semua test
        cls.browser.quit()

    def setUp(self):
        # Bikin user dummy
        self.test_user = User.objects.create_user(
            username="testadmin",
            password="testpassword"
        )

    def tearDown(self):
        # Reset browser di antara test
        self.browser.delete_all_cookies()
        self.browser.execute_script("window.localStorage.clear();")
        self.browser.execute_script("window.sessionStorage.clear();")
        self.browser.get("about:blank")

    def login_user(self):
        """Helper login"""
        self.browser.get(f"{self.live_server_url}/login/")
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys("testadmin")
        password_input.send_keys("testpassword")
        password_input.submit()

    def test_login_page(self):
        self.login_user()

        wait = WebDriverWait(self.browser, 30)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Offside!")  # sesuai show_main

        logout_link = self.browser.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        self.assertTrue(logout_link.is_displayed())

    def test_register_page(self):
        self.browser.get(f"{self.live_server_url}/register/")

        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Register")

        username_input = self.browser.find_element(By.NAME, "username")
        password1_input = self.browser.find_element(By.NAME, "password1")
        password2_input = self.browser.find_element(By.NAME, "password2")

        username_input.send_keys("newuser")
        password1_input.send_keys("complexpass123")
        password2_input.send_keys("complexpass123")
        password2_input.submit()

        wait = WebDriverWait(self.browser, 30)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        login_h1 = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(login_h1.text, "Login")

    def test_create_products(self):
        self.login_user()

        wait = WebDriverWait(self.browser, 10)
        add_button = wait.until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Add Products"))
        )
        add_button.click()

        name_input = self.browser.find_element(By.NAME, "name")
        price_input = self.browser.find_element(By.NAME, "price")
        description_input = self.browser.find_element(By.NAME, "description")
        thumbnail_input = self.browser.find_element(By.NAME, "thumbnail")
        category_input = self.browser.find_element(By.NAME, "category")
        featured_checkbox = self.browser.find_element(By.NAME, "is_featured")

        name_input.send_keys("Test Sepatu")
        price_input.send_keys("200000")
        description_input.send_keys("Sepatu bola kualitas premium")
        thumbnail_input.send_keys("https://example.com/sepatu.jpg")
        category_input.send_keys("Olahraga")
        featured_checkbox.click()

        name_input.submit()

        wait.until(lambda driver: "Test Sepatu" in driver.page_source)
        self.assertIn("Test Sepatu", self.browser.page_source)

    def test_products_detail(self):
        self.login_user()

        product = Products.objects.create(
            name="Sepatu",
            price=100000,
            description="Sepatu bola",
            thumbnail="https://example.com/sepatu.jpg",
            category="Olahraga",
            is_featured=True,
            user=self.test_user
        )

        self.browser.get(f"{self.live_server_url}/products/{product.id}/")

        self.assertIn("Sepatu", self.browser.page_source)
        self.assertIn("100000", self.browser.page_source)
        self.assertIn("Sepatu bola", self.browser.page_source)
        self.assertIn("Olahraga", self.browser.page_source)

    def test_logout(self):
        self.login_user()

        logout_button = self.browser.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
        logout_button.click()

        wait = WebDriverWait(self.browser, 30)
        wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Login"))
        h1_element = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1_element.text, "Login")

    def test_filter_main_page(self):
        Products.objects.create(
            name="Produk Saya",
            price=150000,
            description="Produk milik testadmin",
            thumbnail="https://example.com/milik.jpg",
            category="Olahraga",
            user=self.test_user
        )

        other_user = User.objects.create_user(username="other", password="otherpass")
        Products.objects.create(
            name="Produk Lain",
            price=200000,
            description="Produk milik user lain",
            thumbnail="https://example.com/lain.jpg",
            category="Elektronik",
            user=other_user
        )

        self.login_user()

        # All
        self.browser.get(f"{self.live_server_url}/?filter=all")
        self.assertIn("Produk Saya", self.browser.page_source)
        self.assertIn("Produk Lain", self.browser.page_source)

        # My
        self.browser.get(f"{self.live_server_url}/?filter=my")
        self.assertIn("Produk Saya", self.browser.page_source)
        self.assertNotIn("Produk Lain", self.browser.page_source)
