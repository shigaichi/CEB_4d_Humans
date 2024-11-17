import logging
import shutil
import os
import datetime
import json

import numpy as np


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


def get_addon_logger():
    """
    他のモジュールで利用するための公開
    """
    return logger


def safe_copyfile(src: str, dst: str):
    """
    ファイルをコピーする前に、コピー先のファイルをバックアップします。
    """
    if os.path.exists(dst):
        # バックアップファイル名を作成
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dst = f"{dst}_backup_{timestamp}"
        shutil.move(dst, backup_dst)  # 元のファイルをバックアップ
        logger.info(f"Backup created: {backup_dst}")

    # ファイルをコピー
    shutil.copyfile(src, dst)
    logger.info(f"File copied from {src} to {dst}")


def save_to_json(data, file_path: str):
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, default=custom_serializer, indent=4)
        logger.info(f"Data saved to {file_path}")
    except TypeError as e:
        logger.error(f"Could not serialize data: {e}")


def custom_serializer(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()  # ndarray をリストに変換
    raise TypeError(f"Type {type(obj)} is not JSON serializable")
