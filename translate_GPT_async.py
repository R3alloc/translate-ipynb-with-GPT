import nbformat
import openai
import os
import asyncio
# from openai import OpenAI
from openai import AsyncOpenAI
from tqdm import tqdm

client = AsyncOpenAI(api_key='XXX') 
input_filepath = './XXX.ipynb'
output_filepath = input_filepath.replace('.ipynb', '_CN.ipynb')

async def translate_text(text):
    chat_completion = await client.chat.completions.create(
        messages=[
            {"role": "user", "content": "Translate the following English text to Chinese: {}".format(text)}
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

async def translate_notebook(input_file, output_file):
    # Load the notebook
    with open(input_file, 'r', encoding='utf-8') as file:
        notebook = nbformat.read(file, as_version=4)

    # Create translation tasks for each Markdown cell
    translation_tasks = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            task = asyncio.create_task(translate_text(cell['source']))
            translation_tasks.append(task)
    
    # Wait for all translation tasks to complete
    translated_texts = await asyncio.gather(*translation_tasks)
    
    # # 创建翻译任务
    # translation_tasks = [translate_text(cell['source']) for cell in notebook['cells'] if cell['cell_type'] == 'markdown']

    # # 使用 tqdm 显示进度
    # for i, completed_task in enumerate(tqdm(asyncio.as_completed(translation_tasks), total=len(translation_tasks), desc="Translating")):
    #     translated_text = await completed_task
    #     # 找到对应的 Markdown 单元格并分配翻译文本
    #     # 注意：这里假设单元格的顺序和任务的顺序是一致的
    #     markdown_cells = [c for c in notebook['cells'] if c['cell_type'] == 'markdown']
    #     markdown_cells[i]['source'] = translated_text
        

    # Assign translated texts to cells
    for cell, translated_text in zip([c for c in notebook['cells'] if c['cell_type'] == 'markdown'], translated_texts):
        cell['source'] = translated_text

    # Write the translated notebook to a new file
    with open(output_file, 'w', encoding='utf-8') as file:
        nbformat.write(notebook, file)

if __name__ == "__main__":
    asyncio.run(translate_notebook(input_filepath, output_filepath))
