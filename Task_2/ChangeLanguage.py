from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, StaleElementReferenceException
import time

class ChangeLang:
    def __init__(self, onLeng):
        self.browser = webdriver.Chrome('../chromedriver.exe')
        self.onLeng = onLeng

    def change_leng(self):
        self.browser.get('https://coinmarketcap.com/')
        try:
            self.browser.find_elements_by_css_selector('.sc-10dhc7s-0.iFlDJJ>.Box-sc-16r8icm-0.jOvWhR')[1].click()
            self.browser.find_element_by_css_selector('.lbfhry-0.kgfbam').click()
            leng= self.leng_select()
            return leng

        except ElementNotInteractableException:
            self.browser.find_element_by_css_selector('.sc-10o4ja6-0.iwazsF').click()
            leng = self.leng_select()
            return leng

    def leng_select(self):
        self.lenguage = []
        lengs = self.browser.find_elements_by_css_selector('.cmc-language-picker__option')
        for leng in lengs:
            l = leng.text.split(' ')[0]
            if (l == self.onLeng):
                try:
                    self.lenguage.append(leng.text)
                    leng.click()
                    lenguage = self.test_changelang()
                    self.lenguage.append(lenguage)
                    return self.lenguage
                except StaleElementReferenceException:
                    self.lenguage = leng.text
                    lenguage = self.test_changelang()
                    self.lenguage.append(lenguage)
                    return self.lenguage
        return self.lenguage


    def test_changelang(self):
        time.sleep(8)
        crypto = self.browser.find_element_by_css_selector(
            '.Button__StyledButton-sc-1ejyco6-0.hXfoyj.quq9zv-1.dhtVSl').text
        price = self.browser.find_element_by_css_selector('.sc-9dqrx-0.inEvJB>.sc-9dqrx-1.gYhBqs>.Text-sc-1eb5slv-0.dVUklh').text
        currency = self.browser.find_element_by_css_selector('.Text-sc-1eb5slv-0.hVAibX.font_weight_500___2Lmmi').text[0]
        return (crypto, price, currency)

if __name__ == '__main__':
    change_leng = ChangeLang(onLeng = 'Русский')
    change_leng.change_leng()