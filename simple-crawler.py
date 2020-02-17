from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import json

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')  

url = 'http://www.bmfbovespa.com.br/pt_br/produtos/listados-a-vista-e-derivativos/renda-variavel/empresas-listadas.htm'

chromeProfile = '/usr/local/bin/chromedriver'
driver = Chrome(chromeProfile, options=chrome_options)

driver.get(url)

time.sleep(5)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))


inputEmpresa = driver.find_element_by_id(
    'ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_txtNomeEmpresa_txtNomeEmpresa_text')

inputEmpresa.send_keys('petrobras')


buscarButton = driver.find_element_by_id(
    'ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_btnBuscar')

buscarButton.click()

time.sleep(3)
petrobrasTableLink = driver.find_element_by_xpath(
    '//*[@id="ctl00_contentPlaceHolderConteudo_BuscaNomeEmpresa1_grdEmpresa_ctl01"]/tbody/tr[2]/td[1]')

petrobrasTableLink.click()

time.sleep(3)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

ativoImobilizado = driver.find_element_by_xpath(
    '//*[@id="divDadosEconNovo"]/div[1]/table/tbody/tr[1]/td[2]').text
ativoTotal = driver.find_element_by_xpath(
    '//*[@id="divDadosEconNovo"]/div[1]/table/tbody/tr[2]/td[2]').text
patrimonioLiquido = driver.find_element_by_xpath(
    '//*[@id="divDadosEconNovo"]/div[1]/table/tbody/tr[3]/td[2]').text
patrimonioLiquidoCorretora = driver.find_element_by_xpath(
    '//*[@id="divDadosEconNovo"]/div[1]/table/tbody/tr[4]/td[2]').text

finalDict = {
    "ativo_imobilizado": ativoImobilizado,
    "ativo_total": ativoTotal,
    "patrimonio_liquido": patrimonioLiquido,
    "patrimonio_liquido_atribuido_a_corretora": patrimonioLiquidoCorretora
}
print(json.dumps(finalDict, indent=4))

driver.quit()