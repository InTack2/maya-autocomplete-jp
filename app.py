#!/usr/bin/env python3
import pprint
import re
import time
import random

import requests
from bs4 import BeautifulSoup

MAYA_VERSION = "2018"

BASE_HTML = "https://help.autodesk.com/cloudhelp/{}/JPN/Maya-Tech-Docs/CommandsPython/{}"
ROOT_HTML = BASE_HTML.format(MAYA_VERSION, "index_all.html")

EFFECTS_HTML = BASE_HTML.format(MAYA_VERSION, "cat_Effects.html")
ANIMATION_HTML = BASE_HTML.format(MAYA_VERSION, "cat_Animation.html")
WINDOWS_HTML = BASE_HTML.format(MAYA_VERSION, "cat_Windows.html")
GENERAL_HTML = BASE_HTML.format(MAYA_VERSION, "cat_General.html")
LANGUAGE_HTML = BASE_HTML.format(MAYA_VERSION, "cat_Language.html")
MODELING_HTML = BASE_HTML.format(MAYA_VERSION, "cat_Modeling.html")
RENDERING_HTML = BASE_HTML.format(MAYA_VERSION, "cat_Rendering.html")
SYSTEM_HTML = BASE_HTML.format(MAYA_VERSION, "cat_System.html")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
           }

FILE_CANDIDACY = [
    ["Windows", WINDOWS_HTML],
    ["System", SYSTEM_HTML],
    ["Rendering", RENDERING_HTML],
    ["Modeling", MODELING_HTML],
    ["Language", LANGUAGE_HTML],
    ["General", GENERAL_HTML],
    ["Animation", ANIMATION_HTML],
    ["Effects", EFFECTS_HTML]
]

CORRESPONDENCE_TABLE = [
    ["string\[\]", "Tuple[str]", "\"\""],
    ["int\[\]", "Tuple[int]", "\"\""],
    ["string", "str", "\"\""],
    ["boolean", "bool", "False"],
    ["Boolean", "bool", "False"],
    ["object(s*)", "str", "\"\""],
    ["node", "str", "\"\""],
    ["name", "str", "\"\""],
    ["target", "str", "\"\""],
    ["script", "str", "\"\""],
    ["int", "int", "1"],
    ["uint", "int", "1"],
    ["angle", "float", "1.0"],
    ["floatrange", "Tuple[float, float]", "tuple()"],
    ["timerange", "Tuple[float, float]", "tuple()"],
    ["float", "float", "1.0"],
    ["double", "float", "1.0"],
    ["time", "float", "1.0"],
    ["name", "str", "\"\""],
    ["linear", "float", "1.0"],
    ["STRING", "str", "\"\""],
    ["Int", "int", "1"],
    ["int64", "int", "1"],
    ["selectionItem", "str", "\"\""],
]

HEADER = """
from typing import Any, Container, Dict, Generic, Iterable, Iterator, List, Optional, Set, Tuple, TypeVar, Union, Text


"""

BASE_FUNCTION_FORMAT = """
def {function_name}({args_list}) -> {args_return_type}:
    \"\"\"
    {summary}



    -----------------------------------------

    Flags:

    -----------------------------------------
    {args_description}
    Return Value:
    {retrun_type}: {return_description}
    \"\"\"
    pass

    """

BASE_DESCRIPTION_ARGS = """
    {args_name} ({type}): {descripton}\n
    -----------------------------------------
"""

BASE_FILEPATH = "mayaSDK-{}/maya/cmds/{}.py"

ARGS_WORD = "{args_name}: {args_type} = {default_value}"


class FunctionData(object):
    def __init__(self, function_html_name):
        self.__soup = self.__get_function_soup_object(function_html_name)
        self.__text_block = self.__get_text_block()

        self.__title = self.__collect_function_title()
        self.__description = self.__collect_description()
        self.__retrun_type = self.__collect_return_type()
        self.__args_description_list, self.__args_list = self.__collect_args()
        self.__return_description = self.__collect_return_description()

    def __get_function_soup_object(self, html_name):
        """関数のsoupオブジェクトを取得する

        Args:
            html_name (str): html名

        Returns:
            [type]: [description]
        """
        res_sub_html = BASE_HTML.format(MAYA_VERSION, html_name)

        resuponse_html = requests.get(res_sub_html, headers=headers)
        soup = BeautifulSoup(resuponse_html.text, "html.parser")
        # soup = BeautifulSoup(open(res_sub_html, encoding="utf-8"), "html.parser")
        return soup

    def __collect_function_title(self):
        """関数のタイトルを取得する

        Args:
            soup ([type]): [description]

        Returns:
            [type]: [description]
        """
        title = self.__soup.find("h1").string
        title = title.replace(" ", "")

        return title

    def write_file(self, write_file):
        """ファイルに書き込む

        Args:
            search_html (str): htmlファイル
        """

        with open(write_file, "a", encoding="utf-8") as f:
            response_text = BASE_FUNCTION_FORMAT.format(function_name=self.__title, summary=self.__description, args_list=self.__args_list, args_return_type=self.__retrun_type, args_description=self.__args_description_list, retrun_type=self.__retrun_type, return_description=self.__return_description)
            f.write(response_text)

    def __collect_return_description(self):
        """戻り値の説明を収集する

        Returns:
            str: 戻り値の説明文
        """
        search_return_title_string = "戻り値"
        return_description_index = self.__find_startwith_index(self.__text_block, search_return_title_string, 1)

        return_description = self.__text_block[return_description_index]
        return return_description

    def __get_text_block(self):
        """htmlの文字ブロックを取得する
        """
        texts = self.__soup.get_text()
        lines = [line.strip() for line in texts.splitlines()]
        text_list = [_ for _ in lines if _ != ""]

        return text_list

    def __collect_description(self):
        """説明文を収集する

        Returns:
            str: 説明文
        """
        search_description_string = "{} は".format(self.__title)
        descripton_index = self.__find_startwith_index(self.__text_block, search_description_string, 1)
        descripton = self.__text_block[descripton_index]
        return descripton

    def __collect_return_type(self):
        after_string = self.__description
        function_return_type = None
        for _ in CORRESPONDENCE_TABLE:
            if self.__description.startswith(_[0]):
                after_string = after_string.replace(_[0], "")
                function_return_type = _[1]

        if not function_return_type:
            function_return_type = "None"

        return function_return_type

    def __collect_args(self):
        """引数を収集する

        # TODO: 現状引数と引数の説明文を一緒に取得している。分離する。
        """
        b_tag_list = self.__soup.find_all("tr", attrs={"bgcolor": "#EEEEEE"})
        b_tag_list_2 = [_.find_all("td") for _ in b_tag_list]

        args_description_tags = self.__soup.find_all("table", attrs={"width": "100%"})
        args_description_tags_2 = [_.find("tr").find_all("td") for _ in args_description_tags if _.find("td", attrs={"width": "5%"})]
        args_description_tags_3 = [_[1] for _ in args_description_tags_2 if _]
        args_description_tags_31 = []
        for args_value in args_description_tags_3:
            if args_value.string is None:
                args_description_tags_31.append(args_value.text)
            else:
                args_description_tags_31.append(args_value.string)
        args_description_tags_4 = [_.replace("\n", "") for _ in args_description_tags_31]
        args_description_tags_5 = [_.replace("\t", "") for _ in args_description_tags_4]
        args_description_tags_5 = [_.replace(" ", "") for _ in args_description_tags_5]

        args_array = []
        for i, b_tag in enumerate(b_tag_list_2):
            b_args_value = [_.find("b").string for _ in b_tag if _.find("a")][0]
            b_args_type = [_.find("i").string for _ in b_tag if _.find("i")][0]

            args_array.append([b_args_value, b_args_type, args_description_tags_5[i]])

        result_args_text = ""
        for args_text in args_array:
            result_args_text += BASE_DESCRIPTION_ARGS.format(args_name=args_text[0], type=args_text[1], descripton=args_text[2])

        args_word_list = []
        for args_text in args_array:
            args_type = self.__get_format_type_and_default_value(args_text[1])
            args_default_value = self.__get_default_value(args_type)

            args_word_list.append(ARGS_WORD.format(args_name=args_text[0], args_type=args_type, default_value=args_default_value))
        args_list = ",".join(args_word_list)

        return result_args_text, args_list

    def __find_startwith_index(self, array, search_word, offset):
        """配列の中から文字を見つける

        Args:
            array (list)): 検索に使う配列
            search_word (str)): 検索に使う文字列
            offset (int)): 見つけたindexのオフセット

        Returns:
            str: 配列内で見つかったindexのoffset後の値
        """
        for i, text in enumerate(array):
            if text.startswith(search_word):
                target_word = i + offset
                return target_word

    def __get_format_type_and_default_value(self, args_string):
        format_string = args_string
        if args_string.startswith("["):
            format_string = re.split(r"\[|,|\s|\]", format_string)
            format_string = "[{}]".format(", ".join([x for x in format_string if x]))
            format_string = "Tuple" + format_string

        for _ in CORRESPONDENCE_TABLE:
            format_string = re.sub(_[0], _[1], format_string)

        return format_string

    def __get_default_value(self, format_string):
        format_string = re.sub("Tuple\[", "tuple(", format_string)
        format_string = re.sub("\]", ")", format_string)

        for _ in CORRESPONDENCE_TABLE:
            format_string = re.sub(_[1], _[2], format_string)

        return format_string


def get_url_list(target_html):
    """リンクリストを取得する

    Returns:
        list: リンクリスト
    """
    response_html = requests.get(target_html, headers=headers)

    soup = BeautifulSoup(response_html.text, "html.parser")

    links = soup.find_all("a")
    links = [_.get("href") for _ in links]
    links = [_ for _ in links if _]
    format_links = [re.search(r"(?<=').*?(?=')", _).group() for _ in links]

    return format_links


def create_function_file(html_file_path, file_name):
    function_url_list = get_url_list(html_file_path)

    for function_url in function_url_list:
        time.sleep(random.randint(1, 3))
        try:
            function_data = FunctionData(function_url)
            function_data.write_file(BASE_FILEPATH.format(MAYA_VERSION, file_name))
        except Exception as e:
            print(e)
            print(file_name)


def add_headder(file_name):
    file_path = BASE_FILEPATH.format(file_name)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(HEADER)


if __name__ == "__main__":
    for file_set in FILE_CANDIDACY:
        file_name = file_set[0]
        target_html = file_set[1]

        add_headder(file_name)

        create_function_file(target_html, file_name)
