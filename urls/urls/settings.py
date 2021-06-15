# Scrapy settings for urls project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'urls'

SPIDER_MODULES = ['urls.spiders']
NEWSPIDER_MODULE = 'urls.spiders'

# ipaddrset
DOWNLOADER_MIDDLEWARES = {
    'urls.middlewares.ProxyMiddleware': 543,
}


PROXIES=[
'223.8.216.150:4256','110.247.112.157:4245','175.21.125.219:4254','101.74.146.227:4245','123.101.67.194:4210','36.57.87.49:4248','1.70.80.223:4256','60.20.193.113:4215','175.146.215.224:4256','114.98.148.31:4245','182.128.44.205:4264','183.166.162.47:4248','42.56.238.125:4275','175.21.99.186:4254','58.252.195.137:4210','110.247.118.113:4245','60.9.218.193:4245','114.104.128.50:4248','171.90.56.35:4243','122.188.243.68:4245','221.9.19.212:4254','221.203.148.178:4280','139.208.105.101:4220','27.152.192.148:4268','114.104.129.185:4248','42.84.165.230:4286','171.12.40.214:4210','114.99.3.73:4224','42.86.81.43:4250','115.209.121.13:4256','1.70.80.95:4256','220.179.219.124:4276','175.174.139.169:4215','183.166.132.74:4248','113.237.4.68:4256','218.88.246.17:4263','182.145.28.11:4210','58.255.199.198:4210','175.21.99.126:4254','114.104.139.16:4248','123.160.69.43:4230','183.95.149.5:4234','120.15.174.43:4245','183.166.139.71:4248','101.26.195.52:4245','183.92.254.86:4245','27.152.195.244:4268','123.8.95.150:4210','112.91.78.60:4245','171.90.56.88:4243','119.7.144.25:4278','223.215.1.168:4245','113.237.241.39:4280','223.215.182.242:4220','110.18.155.229:4234','175.19.66.72:4254','58.19.80.222:4245','139.208.106.244:4220','183.92.12.101:4230','42.84.169.249:4286','221.203.148.217:4250','223.8.207.30:4256','60.185.151.84:4256','114.99.23.235:4276','123.188.116.6:4245','1.31.97.169:4245','114.104.129.46:4248','182.128.45.250:4264','221.201.202.236:4215','175.146.208.170:4256','111.72.138.5:4221','175.149.63.94:4275','140.255.202.25:4210','110.90.220.252:4245','222.213.136.222:4263','10.33.53.111:4245','114.104.143.30:4248','117.69.179.141:4284','118.118.201.3:4210','60.185.200.34:4256','58.243.28.34:4270','163.179.204.62:4210','123.160.69.23:4210','175.21.120.143:4254','114.104.128.5:4248','119.249.41.92:4256','171.13.137.165:4230','120.15.173.194:4245','121.207.92.14:4268','183.92.255.78:4245','183.94.90.210:4234','114.99.10.59:4224','175.23.220.71:4256','117.63.133.189:4276','61.53.13.247:4210','117.70.35.35:4220','42.176.132.238:4230','110.18.152.238:4234','119.7.144.120:4278','60.169.56.255:4245'

]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'urls (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
# LOG_LEVEL='WARNING'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
}


# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'urls.middlewares.UrlsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'urls.middlewares.UrlsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'urls.pipelines.UrlsPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
