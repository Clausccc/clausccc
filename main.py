from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os
from conf.config import *

# 存放保存的用户数据的路径，设置 Chrome 用户配置文件路径
user_data_dir = "C:\\ChromeProfile"  # 请根据你的系统修改路径
if not os.path.exists(user_data_dir):
    os.makedirs(user_data_dir)

# 设置 Chrome 选项
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# 初始化 Chrome 浏览器
driver = webdriver.Chrome(options=chrome_options)

try:
    # 打开目标网页
    print("脚本启动 >>> 打开补天网站")
    driver.get('https://www.butian.net/Loo/submit')

    # 若账号未登入，请开启该睡眠，并登入账号，登入账号后再注释代码
    # time.sleep(500)

    #等待网页加载完成
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
    print("URL 请求已发送，页面加载完成")

    # 等待并点击“提交漏洞”按钮
    print("等待提交漏洞按钮加载...")
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btnSub'))
    )
    submit_button.click()
    print("已点击提交漏洞按钮")

    # 等待表单加载
    print("等待漏洞类别选择框加载...")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'selCate'))
    )
    print("表单加载完成，开始填写内容...")

except Exception as e :
    print(f"error：{e}")
    os.exit()


try:
    if Vulnerability_id == '1':
        # “通用型”漏洞
        attribute_select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'attribute'))
        )
        attribute_select = Select(attribute_select_element)
        attribute_select.select_by_visible_text('通用型')
        print("已选择漏洞类型：通用型")
    
    elif Vulnerability_id == '2':
        # “事件型”漏洞
        attribute_select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'attribute'))
        )
        attribute_select = Select(attribute_select_element)
        attribute_select.select_by_visible_text('事件型')
        print("已选择漏洞类型：事件型")


        attribute_select_element_ = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'weight'))
        )
        attribute_select = Select(attribute_select_element_)
        options = attribute_select.options
        for option in options:
            if Vulnerability_weight in option.text:
                attribute_select.select_by_visible_text(option.text)
                print(f"已选择权重等级：权重={Vulnerability_weight}")
                break
        else:
            print("未找到权重对应选项，请重新选择：", [opt.text for opt in options])

    # 填写“厂商名称描述”
    company_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'company_name'))
    )
    company_name.clear()
    company_name.send_keys(Name_conpany)
    print("已填写厂商名称")

    
    # 填写“域名或ip”
    company_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'host'))
    )
    company_name.clear()
    company_name.send_keys(Name_Domain)
    print("已填写主域名")


    # 填写“简要描述”
    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'title'))
    )
    title.clear()
    title.send_keys(Name_title)
    print("已填写漏洞标题")

    # 填写漏洞类别
    selCate = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'selCate'))
    )
    WebDriverWait(driver, 10).until(
        lambda d: len(Select(selCate).options) > 1
    )
    selCate_select = Select(selCate)
    options_level = selCate_select.options
    for options_level in options:
        if Vulnerability_category in options_level.text:
            selCate_select.select_by_visible_text(option.text)
            print(f"已选择为漏洞等级为：{Vulnerability_Level}")
            break
    else:
        print("未找到‘信息传输’选项，可用选项：", [opt.text for opt in options])

    # 在第二个选项选择“信息泄露”类型
    lootype_select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'lootypesel2'))
    )
    WebDriverWait(driver, 10).until(
        lambda d: len(Select(lootype_select_element).options) > 1
    )
    lootype_select = Select(lootype_select_element)
    options = lootype_select.options
    for option in options:
        if Vulnerability_Type in option.text:
            lootype_select.select_by_visible_text(option.text)
            print("已选择信息泄露类型")
            break
    else:
        print("未找到‘信息泄露’选项，可用选项：", [opt.text for opt in options])

    # 漏洞等级选择
    level_select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'level'))
    )
    WebDriverWait(driver, 10).until(
        lambda d: len(Select(level_select_element).options) > 1
    )
    level_select = Select(level_select_element)
    level_select.select_by_visible_text(Vulnerability_Level)
    print(f"已选择漏洞等级：{Vulnerability_Level}")

    # 选择参与的活动“【2025专属SRC全年积分挑战赛】”
    active_select_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//select[@name="active_id"]'))  # 使用 XPATH 更精确
    )
    # 调试：检查元素类型
    tag_name = active_select_element.tag_name
    print(f"定位到的 active_id 元素类型: {tag_name}")
    if tag_name != 'select':
        raise Exception(f"预期元素为 <select>，实际为 <{tag_name}>")
    # 等待选项加载
    WebDriverWait(driver, 10).until(
        lambda d: len(Select(active_select_element).options) > 1
    )
    active_select = Select(active_select_element)
    # 调试：打印选项
    print("活动选项：", [opt.text for opt in active_select.options])
    if activities:
        active_select.select_by_visible_text(activities)
    else:
        pass
    print(f"已选择活动：{activities}")

    # 填写“简要描述”
    description = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'description'))
    )
    description.clear()
    description.send_keys(Name_description)
    print("已填写简要描述")

    # 填写“详细细节”（富文本编辑器）
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'detail'))
    )
    driver.execute_script(f'UE.getEditor("detail").setContent("{Name_detail}");')
    print("已填写详细细节")

    # 填写“修复方案”
    repair_suggest = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'repair_suggest'))
    )
    repair_suggest.clear()
    repair_suggest.send_keys(Name_repair)
    print("已填写修复方案")

    # 填写所属行业选项
    
    industry_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'industry1'))
    )
    WebDriverWait(driver, 10).until(
        lambda d: len(Select(industry_name).options) > 1
    )
    industry_select = Select(industry_name)
    options = industry_select.options
    available_options = [opt.text for opt in options]
    print(f"可选的所属行业选项：{available_options}")
    for option in options:
        if Name_Industry in option.text:
            industry_select.select_by_visible_text(option.text)
            print(f"已选择：{Name_Industry}")
            break
    else:
        print(f"未找到{Name_Industry}选项，可用选项：", [opt.text for opt in options])

    # 填写行业分类
    print("等待第二级行业分类加载...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'industry2'))
    )
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="industry2"]//input[@type="checkbox"]'))
    )
    print("第二级行业分类已加载")

    # 获取所有checkbox选项
    checkboxes = driver.find_elements(By.XPATH, '//*[@id="industry2"]//input[@type="checkbox"]')
    checkbox_labels = driver.find_elements(By.XPATH, '//*[@id="industry2"]//label')

    # 调试：打印所有可选行业
    available_options = [label.text for label in checkbox_labels]
    print("可选的第二级行业分类：", available_options)

    # 遍历并勾选目标子行业
    for checkbox, label in zip(checkboxes, checkbox_labels):
        if target_sub_industry in label.text:
            if not checkbox.is_selected():
                driver.execute_script("arguments[0].click();", checkbox)
                print(f"已勾选目标子行业：{target_sub_industry}")
            else:
                print(f"目标子行业 {target_sub_industry} 已勾选")
            break
    else:
        print(f"未找到目标子行业 '{target_sub_industry}'，可用选项：", available_options)





    # 等待操作完成
    time.sleep(2)
    print("所有操作完成")

    # 保持程序运行，直到手动关闭浏览器
    print("浏览器将保持打开状态，程序运行中... 关闭浏览器以结束程序")
    while True:
        try:
            driver.title
            time.sleep(1)
        except:
            print("检测到浏览器已关闭，程序即将退出")
            break

except Exception as e:
    print(f"发生错误: {str(e)}")
    print("程序将保持运行，直到手动关闭浏览器")
    while True:
        try:
            driver.title
            time.sleep(1)
        except:
            print("检测到浏览器已关闭，程序即将退出")
            break

finally:
    pass

print("程序已结束")