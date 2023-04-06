import os
import pandas as pd
from fuzzywuzzy import fuzz
from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor
import importlib

# 模块级常量
FILE_NAME = os.path.join(os.path.dirname(__file__), 'info.xlsx')
SCORE_THRESHOLD = 50
DEFAULT_LIMIT = 5


@lru_cache(maxsize=1)
def read_excel():
    return pd.read_excel(FILE_NAME)


df = read_excel()


@lru_cache(maxsize=128)
def fuzzy_match(describe):
    scores = []
    for _, row in df.iterrows():
        score = fuzz.partial_ratio(describe, row['describe'])
        if score >= SCORE_THRESHOLD:
            scores.append((row, score))
    return scores


def get_method(describe: str, limit: int = DEFAULT_LIMIT) -> pd.DataFrame:
    """
    获取与描述模糊匹配的方法列表，并让用户选择需要的方法。

    Args:
        describe: 用户提供的描述
        limit: 返回的匹配项数量，默认为5

    Returns:
        返回方法执行的结果，数据类型为pandas.DataFrame
    """
    try:
        matches = []
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(fuzzy_match, describe)]
            for future in futures:
                matches.extend(future.result())
        matches = sorted(matches, key=lambda x: x[1], reverse=True)[:limit]

        if len(matches) == 0:
            print(f"没有找到与'{describe}'相关的方法。")
            return pd.DataFrame()

        print("以下是与您提供的描述匹配的方法列表：")
        for i, match in enumerate(matches):
            print(f"{i+1}\t{match[0]['describe']}")
        selected = input("请选择您需要的方法：")
        method_name = matches[int(selected) - 1][0]['method']
        ppshare = importlib.import_module('PPshare')
        method = getattr(ppshare, method_name)
        result = method()
        if not isinstance(result, pd.DataFrame):
            raise ValueError(f"{method_name}方法的返回值不是DataFrame。")
        return result
    except FileNotFoundError:
        print(f"找不到文件'{FILE_NAME}'。")
    except KeyError:
        print(f"文件'{FILE_NAME}'不包含所需的列。")
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == '__main__':
    DF = get_method('GDP')
    print(DF)
