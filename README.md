# 1688 Supplier Research

1688 supplier research and factory screening tool.

## Project Goal

用于搜索、整理和筛选 1688 厂家信息，重点寻找适合 OEM / ODM 合作的供应商。

## Supplier Fields

计划采集以下信息：

- 店铺名称
- 企业主体
- 成立时间
- 详细地址
- 主营产品
- 主营品牌
- 厂家资质
- OEM / ODM 能力
- 厂房面积
- 是否入驻工厂
- 店铺链接
- 最新成交指标
- 联系状态
- 供应商评级
- 最后更新时间

## Workflow

1. 输入产品关键词
2. 设置目标地区
3. 设置最大采集页数
4. 搜索供应商
5. 整理厂家信息
6. 对供应商进行初步评级
7. 导出 Excel
8. 人工筛选并联系厂家

## Project Structure

- `config.py`：关键词、地区、页数等参数设置
- `supplier_scraper.py`：主程序
- `requirements.txt`：Python 依赖库
- `output/`：以后用于保存导出的 Excel 文件

## Current Status

目前为项目初始版本，已完成基础项目结构。

下一步计划：

- 增加供应商数据采集逻辑
- 增加字段清洗
- 增加供应商评级
- 增加 Excel 导出
- 增加筛选功能
