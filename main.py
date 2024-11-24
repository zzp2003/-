import time
from login import login
from monitor import check_stock
from purchase import purchase

if __name__ == "__main__":
    cookies = login()
    sku_id = "100012043978"  # 替换为目标商品ID
    while True:
        if check_stock(sku_id, cookies):
            purchase(sku_id, cookies)
            break
        time.sleep(1)  # 监控间隔1秒
