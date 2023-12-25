#PyTestdeki decoratorleri araştırarak oluşturduğunuz notları bir "ReadMe" dosyası olarak githubda paylaşınız.
#Bir önceki ödevde yazdığınız tüm testleri PyTest uyumlu hale getiriniz.
#Kullandığımız SauceDemo sitesinde kendi belirlediğiniz en az "3" test case daha yazınız.
#En az 1 testiniz parametrize fonksiyonu ile en az 3 farklı veriyle test edilmelidir.

""" PyTest- Decorators
PyTest, Python'da kullanılan, yazılan programları test eden bir test çerçevesidir. 
PyTest'in en önemli özelliği hata ayıklayıcı olarak kullanılmasıdır. 
Python'da decorator'lar, işlevleri veya testleri genişletmek, 
işlevleri işaretlemek veya testlerin davranışını değiştirmek için kullanılan özel işaretçi nitelikleridir.
Pytest'te sık kullanılan decorator'lar şunlardır: 
@pytest.fixture: Bu, testler arasında durum paylaşımını sağlayan ve gerekli kaynakları testlere sağlayan fixture'ları tanımlar.
@pytest.mark.parametrize: Aynı test fonksiyonunu farklı girişlerle tekrar tekrar çalıştırmanıza olanak tanır, böylece testlerinizi çeşitli senaryolarla kontrol edebilirsiniz. 
@pytest.mark.skip: Belirli bir testin atlanmasını sağlar. Örneğin, henüz hazır olmayan veya geçici olarak kullanılmayan testleri işaretlemek için kullanılır. 
@pytest.mark.xfail: Beklenen başarısız test durumlarını işaretlemek için kullanılır. Yani, testin başarısız olmasını beklediğinizi belirtir. 
Bu decorator'lar, testlerinizi işaretlemek, düzenlemek veya davranışlarını değiştirmek için kullanılır. 
Pytest'te kullanıldıklarında testlerinizi daha esnek ve organize etmenizi daha kolay hale getirirler. """



from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
import pytest

class Test_work:
    def setup_method(self):  
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()
    def teardown_method(self):
        self.driver.quit()
        

#-Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def test_free_user(self):
        loginButton =self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3') 
        assert errorMessage.text =="Epic sadface: Username is required"

        
#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    
    def test_passPasword(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))       
        usernameInput.send_keys("standard_user") 
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput.send_keys("")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        assert errorMessage.text =="Epic sadface: Password is required"
        
#Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_locked_out(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("locked_out_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage =self. driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        
#-Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde 
#kullanıcı "/inventory.html" sayfasına gönderilmelidir. 
#Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def test_successfull_login(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))       
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID , "login-button")
        loginButton.click()
        listOfElement = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert listOfElement and len(listOfElement) == 6
#1.Case: Başarılı ödeme işlemi 
    def test_successful_pay(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))       
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID , "login-button")
        loginButton.click() 
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart.click()
        shopping_cart_container = self.driver.find_element(By.ID, "shopping_cart_container")
        shopping_cart_container.click()
        checkout = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "checkout")))
        checkout.click()
        first_name = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))       
        first_name.send_keys("esra")
        last_name = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"last-name")))       
        last_name.send_keys("çınar")
        zip_postal_code = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"postal-code")))       
        zip_postal_code.send_keys("34696")
        continue_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "continue")))
        continue_button.click()
        self.driver.execute_script("window.scrollTo(0,300)")
        finish = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "finish")))
        finish.click()
        thank_you= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"complete-header")))
        assert thank_you.text == "Thank you for your order!"
#2.Case: Başarılı Login İşlemi
    @pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),("visual_user", "secret_sauce"),("problem_user", "secret_sauce")])
    def test_valid_login(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        inventory_page_title = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert inventory_page_title.text == "Products"

#3.case: Belli bir fonksiyonun test fonksiyonunun çalıştırılmasını engellemek için"bu test henüz hazır değil."
    @pytest.mark.skip(reason="this test is not ready yet")
    def test_notready_yet(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))       
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID , "login-button")
        loginButton.click() 
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart.click()
#4.case: 



    







""" #kullanıcı ürün ekledikten sonra satın alma/ödeme sayfasına geçmelidir.
#kullanıcı first_name'i ve Zip/Postal Code'u doldurabilmeli, last_name'e veri girememelidir.
problem user girmeli
    def test_checkout_information(self):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))       
        usernameInput.send_keys("standard_user")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password"))) 
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID , "login-button")
        loginButton.click()
        self.driver.execute_script("window.scrollTo(0,500)") 
        addToCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")))
        addToCart.click()
        remove = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='remove-test.allthethings()-t-shirt-(red)']")))
        testResult = remove.text == "Remove"
        #scrollBar'ı yukarı kaydır.0 değer girildi.
        self.driver.execute_script("window.scrollTo(0,0)") 
        #sepete git.tıkla.
        shopping_cart_container = self.driver.find_element(By.ID, "shopping_cart_container")
        shopping_cart_container.click()

        #yeni bir sayfa açıldığını continue shopping ile gör.
        continue_shopping = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"continue-shopping"))) 
        continue_shopping.send_keys("Continue Shopping")


        #checkout ile ödeme sayfasına geç.
        checkout = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "checkout")))
        checkout.click()
        first_name = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"first-name")))       
        first_name.send_keys("esra")
 """

















