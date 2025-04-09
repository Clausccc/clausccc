## 补天漏洞信息自动填写工具 

## 工具简介
这是一个基于 Python 和 Selenium 的自动化工具，旨在简化网页表单的填写过程。有时候扫的漏洞太多，提交太慢，怕抢不过别人，那就直接让脚本帮你把基本信息全部填写完成。

工具刚开始开发，许多功能还不完善，目前只支持简单的信息输入，快速生成对应漏洞信息的输入


## 使用方法
Python 版本：Python 3.6 或更高。
Chrome 浏览器：确保系统中已安装 Google Chrome。

依赖安装：pip install selenium webdriver-manager

！！第一次使用请取消注释第29行代码，登入账号后，再取消注释！！

## 配置信息

打开conf下的config.py 根据对应的信息填写需要输入的数据

Name_company = "test1"  # 厂商名称

Name_Domain = "test2"   # 域名或IP

Vulnerability_category = "Web漏洞"  # 漏洞类别

Name_title = "test3"    # 漏洞标题

Vulnerability_id = "2"  # 漏洞选择（1为通用型，2为事件型）

Vulnerability_Type = "信息泄露"  # 漏洞类型

Vulnerability_weight = "0"  # 漏洞权重

Vulnerability_Level = "中危"  # 漏洞等级

activities = ""         # 参与活动（可选）

Name_description = "test4"  # 简要描述

Name_detail = "test5"   # 详细细节

Name_repair = "test6"   # 修复方案

Name_Industry = "信息传输"  # 所属行业（模糊匹配）

target_sub_industry = "软件和信息技术服务业"  # 目标子行业（模糊匹配）

