import time
from login import login
from monitor import check_stock
from purchase import purchase

if __name__ == "__main__":
    print("开始登录...")
    cookies = login()
    
    sku_id = "100012043978"  # 替换为目标商品的 SKU ID
    print(f"监控商品 {sku_id} 的库存状态...")
    
    while True:
        try:
            if check_stock(sku_id, cookies):
                print("商品有货，开始抢购...")
                purchase(sku_id, cookies)
                break
            else:
                print("无货，继续监控...")
            time.sleep(1)  # 每秒检查一次库存
        except Exception as e:
            print("发生异常:", e)
            time.sleep(5)  # 异常处理后稍作等待
