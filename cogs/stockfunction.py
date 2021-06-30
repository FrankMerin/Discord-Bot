import discord
from discord.ext import commands
import requests
import os


import urllib

from PIL import Image

from io import BytesIO
import io
from requests_html import AsyncHTMLSession
import re


stock_key = (os.environ.get('Stock_API'))

class StockFunction(commands.Cog):

    def __init__(self,client):
        self.client = client
        self.asession = AsyncHTMLSession()
        #self.chrome_options = webdriver.ChromeOptions()
        #self.chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        #self.chrome_options.add_argument("--headless")  
        #self.chrome_driver = "C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe" 
        
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('stocks enabled')

    
    async def getPrices(self, tk):
        try:
            tk = tk.replace('.','-')
            r = await self.asession.get(f'https://finance.yahoo.com/quote/{tk}')

            companyName = r.html.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1', first=True).text
            try:
                currentPrice = r.html.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]', first=True).text
            except:
                currentPrice = r.html.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/span[1]', first=True).text
            try:
                change = r.html.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]', first=True).text.split()
            except:
                change = r.html.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/span[2]', first=True).text.split()
            priceChange = change[0]
            percentChange = change[1]
            

            ### WARNING: BAD CODE HERE
            """ self.driver = webdriver.Chrome(self.chrome_driver, options=self.chrome_options)
            self.driver.get("https://www.tradingview.com/") 
            dropdownMenu = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/form/div/button')
            dropdownMenu.click()
            dropdownSelect = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/form/div/div/span[2]')
            dropdownSelect.click()
            searchinput = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/form/label/tv-autocomplete[2]/input')
            searchinput.send_keys(tk)
            searchinput.send_keys(Keys.RETURN)
            time.sleep(.3)
            companyName = self.driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[2]/div[1]/h1/div/div').get_attribute('innerHTML')
            price = self.driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[1]').text
            percentChange = self.driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[1]').text
            priceChange = self.driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/span[2]').text
            self.driver.quit() """
            return [companyName, currentPrice, priceChange, percentChange]
        except:
            return False

    async def getLogo(self, tk):
        try:
            

            r = await self.asession.get(f"https://www.google.com/search?q={tk}+stock")

            await r.html.arender()
            
            shortedHTML = str(r.text.split("FZylgf")[1])
            
            
            
            
            regex = re.findall("(data:image+/(?:jpeg|png)+;base64,.*?)';", str(shortedHTML))

            imgUri = (regex[0].split("\\")[0])

            uriWithoutSchema = imgUri.replace('data:image/png;base64,','').replace('data:image/jpeg;base64,','')

            lenOfLink = (len(uriWithoutSchema))

            
            return (imgUri + '='*((4-(lenOfLink % 4)) % 4)
)
            ### WARNING! BAD CODE BELOW
            """ self.driver = webdriver.Chrome(self.chrome_driver, options=self.chrome_options)
            self.driver.get(f"https://www.google.com/search?q={tk}+stock")
            images = self.driver.find_elements_by_tag_name('img')
            
            for image in images:
                if image.get_property('width') == 119:
                    response = (image.get_attribute('src'))
            self.driver.quit()
            
            return response """

        except:
            return os.getcwd()+"\\no-img.png"





    # stocks in USD
    @commands.command()
    async def tk(self, ctx, tk):
        try:  
            companyQuote = await self.getPrices(tk)
            
 
            stockpic = await self.getLogo(tk)
            stockcompany = companyQuote[0]
            stockprice = companyQuote[1]
            stockPriceChange = companyQuote[2]
            stockPercentChange = companyQuote[3]



            if "−" in stockPriceChange:
                sidecolor = discord.Color.red()
            else:
                sidecolor = discord.Color.green()

            
            embedstock = discord.Embed(
                color = sidecolor
            )

            if stockpic == os.getcwd()+"\\no-img.png":
                file = discord.File("no-img.png", filename="no-img.png") 
                embedstock.set_thumbnail(url = "attachment://no-img.png")
            else:
                response = urllib.request.urlopen(stockpic)
                imageBytes = response.file.read()
                imageStream = io.BytesIO(imageBytes)
                imageFile = Image.open(imageStream)
                with BytesIO() as image_binary:
                    imageFile.save(image_binary, 'PNG')
                    image_binary.seek(0)
                    file = discord.File(fp=image_binary, filename="logoFile.png")
                    embedstock.set_thumbnail(url = "attachment://logoFile.png")
                
            embedstock.add_field(name='**Company:**', value=stockcompany, inline=False)
            embedstock.add_field(name='**Price:**', value='$' + str(stockprice), inline=False)
            embedstock.add_field(name='**Price Change Today:**', value='$' + str(stockPriceChange), inline=False)
            embedstock.add_field(name='**Percent Change Today:**', value=stockPercentChange, inline=False)

            await ctx.send(embed=embedstock, file=file) 


        except:
            await ctx.send('Ticker Symbol Invalid')


    @commands.command()
    async def cr(self, ctx, cr):
        crToCapital = cr.upper()
        try:
            url = (f"https://financialmodelingprep.com/api/v3/quote/{crToCapital}USD?apikey={str(stock_key)}")
            data = requests.get(url).json()[0]
            cryptoName = data['name']
            cryptoPrice = data['price']
            cryptoMarketCap = data['marketCap']


            
            embedstock = discord.Embed(
                color = discord.Color.orange()
            )

            embedstock.add_field(name='**Coin:**', value=cryptoName, inline=False)
            embedstock.add_field(name='**Price:**', value='$' + "{:,}".format(cryptoPrice), inline=False)
            embedstock.add_field(name='**Market Cap**', value='$' + "{:,}".format(cryptoMarketCap), inline=False)
            

            await ctx.send(embed=embedstock)

        except IndexError:
            await ctx.send('Coin Symbol Invalid')


    

def setup(client):
    client.add_cog(StockFunction(client))