import sqlite3
import time
from typing import Any, Callable, Optional

import cv2
import numpy as np
from arcaea_offline_ocr.phash_db import phash_opencv


def preprocess_char_icon(img_gray: np.ndarray):
    h, w = img_gray.shape[:2]
    img = cv2.fillPoly(
        img_gray,
        [
            np.array([[0, 0], [round(w / 2), 0], [0, round(h / 2)]], np.int32),
            np.array([[w, 0], [round(w / 2), 0], [w, round(h / 2)]], np.int32),
            np.array([[0, h], [round(w / 2), h], [0, round(h / 2)]], np.int32),
            np.array([[w, h], [round(w / 2), h], [w, round(h / 2)]], np.int32),
        ],
        (128),
    )
    return img


def build_image_phash_database(
    images: list[np.ndarray],
    labels: list[str],
    *,
    hash_size: int = 16,
    highfreq_factor: int = 4,
    progress_func: Optional[Callable[[int, int], Any]] = None,
):
    assert len(images) == len(labels)

    conn = sqlite3.connect(":memory:", check_same_thread=False)

    with conn:
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE properties (key TEXT, value TEXT)")
        cursor.executemany(
            "INSERT INTO properties VALUES (?, ?)",
            [
                ("hash_size", hash_size),
                ("highfreq_factor", highfreq_factor),
            ],
        )

        image_num = len(images)
        id_hashes = []
        for i, label, image in zip(range(image_num), labels, images):
            image_hash = phash_opencv(
                image,
                hash_size=hash_size,
                highfreq_factor=highfreq_factor,
            )
            image_hash_bytes = image_hash.flatten().tobytes()

            id_hashes.append([label, image_hash_bytes])
            if progress_func:
                progress_func(i + 1, image_num)

        hash_length = len(id_hashes[0][1])
        cursor.execute(f"CREATE TABLE hashes (id TEXT, hash BLOB({hash_length}))")

        cursor.executemany(
            "INSERT INTO hashes VALUES (?, ?)",
            id_hashes,
        )
        cursor.executemany(
            "INSERT INTO properties VALUES (?, ?)",
            [("built_timestamp", int(time.time()))],
        )
        conn.commit()

    return conn
