# 1688 Supplier Research

1688 supplier research and factory screening tool.

## Project Goal

用于搜索、整理和筛选 1688 厂家信息，重点寻找适合 OEM / ODM 合作的供应商。

## Supplier Fields

供应商记录统一使用 `supplier_fields.py` 中的 `SUPPLIER_FIELDS`，以下顺序也用于 Excel 表头：

- 店铺名称
- 企业主体
- 成立时间
- 详细地址
- 主营产品
- 主营品牌
- 厂家资质
- OEM/ODM
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
- `supplier_fields.py`：15 个供应商字段及固定导出顺序
- `export_excel.py`：使用 pandas 和 openpyxl 导出供应商 Excel
- `requirements.txt`：Python 依赖库
- `output/`：默认 Excel 输出目录，导出时自动创建

## Current Status

目前已完成基础项目结构、供应商字段定义和独立的 Excel 导出函数。
采集主程序仍是骨架，尚未自动调用导出函数。

下一步计划：

- 增加供应商数据采集逻辑
- 增加字段清洗
- 增加供应商评级
- 增加筛选功能

## Excel Export

安装依赖（Python 3.9+）：

```bash
python -m pip install -r requirements.txt
```

在项目根目录运行以下 Python 示例：

```python
from export_excel import export_suppliers_to_excel

suppliers = [
    {
        "店铺名称": "示例包材厂",
        "企业主体": "示例包材有限公司",
        "主营产品": "香水瓶",
        "OEM/ODM": "支持 OEM / ODM",
        "厂房面积": 1200,
        "是否入驻工厂": True,
        "联系状态": "未联系",
        "供应商评级": "待评级",
        "最后更新时间": "2026-09-22",
    }
]
output_path = export_suppliers_to_excel(suppliers)
print(f"已导出：{output_path}")

# 也可指定路径，或用空列表生成仅包含表头的模板：
# export_suppliers_to_excel([], "output/supplier_template.xlsx")
```

- 输入为中文字段字典的可迭代对象，每条字典表示一家供应商。
- 默认路径来自 `config.OUTPUT_FILE`（`output/suppliers.xlsx`），相对路径基于当前工作目录。
- 输出必须为 `.xlsx`；父目录自动创建，同名文件会被覆盖。
- 工作表名为“供应商”，包含固定的 15 列，不输出 DataFrame 索引；冻结表头并启用筛选。
- 缺失字段留空，未知字段报错；字段名须精确匹配，例如 `OEM/ODM`。
- 字符串按文本写入，包括以 `=` 开头的内容；数字和布尔值保留对应类型。
- 导出函数不负责采集、评级或自动填充更新时间，这些值由调用方提供。
