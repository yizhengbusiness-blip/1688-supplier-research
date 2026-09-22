"""将供应商记录导出为固定字段顺序的 Excel 工作簿。"""

from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any, Union

import pandas as pd

from config import OUTPUT_FILE
from supplier_fields import SUPPLIER_FIELDS


def export_suppliers_to_excel(
    suppliers: Iterable[Mapping[str, Any]],
    output_file: Union[str, Path] = OUTPUT_FILE,
) -> Path:
    """导出中文字段字典，返回文件路径；同名文件将被覆盖。

    缺失字段留空，空输入仍输出表头。未知字段会报错，以避免拼写
    错误导致数据丢失。字符串按文本保存，不作为 Excel 公式执行。
    """
    output_path = Path(output_file)
    if output_path.suffix.lower() != ".xlsx":
        raise ValueError("输出文件必须使用 .xlsx 扩展名")

    records = []
    for index, supplier in enumerate(suppliers, start=1):
        if not isinstance(supplier, Mapping):
            raise TypeError(f"第 {index} 条供应商记录必须是字典或 Mapping")
        unknown = set(supplier) - set(SUPPLIER_FIELDS)
        if unknown:
            raise ValueError(f"第 {index} 条供应商记录包含未知字段：{unknown}")
        records.append(dict(supplier))

    frame = pd.DataFrame(records, columns=list(SUPPLIER_FIELDS))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        frame.to_excel(writer, sheet_name="供应商", index=False)
        worksheet = writer.sheets["供应商"]
        worksheet.freeze_panes = "A2"
        worksheet.auto_filter.ref = worksheet.dimensions
        for row in worksheet.iter_rows(min_row=2):
            for cell in row:
                if cell.data_type == "f":
                    cell.data_type = "s"
    return output_path
