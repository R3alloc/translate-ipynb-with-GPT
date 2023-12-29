# translate-ipynb-with-GPT Usage Guide

#### English:
This script efficiently translates Markdown cells in a Jupyter Notebook from English to Chinese using OpenAI's GPT-3.5 model and asynchronous coroutines for improved efficiency. Steps:
1. Install `openai`, `nbformat`, and `tqdm` libraries.
2. Set OpenAI API key in the `client`.
3. Input the `.ipynb` file path for translation.
4. Script creates a translated copy, appending "_CN.ipynb" to the filename.
5. Run with `python3 script_name.py`, leveraging asyncio for concurrent translations.

#### 中文：
此脚本通过异步协程操作提高效率，使用 OpenAI 的 GPT-3.5 模型将 Jupyter 笔记本中的 Markdown 单元格从英文翻译成中文。使用步骤：
1. 安装 `openai`、`nbformat` 和 `tqdm` 库。
2. 在 `client` 中设置 OpenAI API 密钥。
3. 输入待翻译的 `.ipynb` 文件路径。
4. 脚本将创建一个翻译后的副本，文件名后加 "_CN.ipynb"。
5. 使用 `python3 translate_GPT_async.py` 运行脚本，利用 asyncio 进行并行翻译。
