import openai
import sys
from openai import OpenAI
from Getdata import getdata_from_database
client = OpenAI()
sys.stdout.reconfigure(encoding='utf-8')
# openai.api_key = 'sk-xxxx'#

def get_ai_response(prompt):
    prompt = prompt.encode('utf-8').decode('utf-8')

    response = client.chat.completions.create(
        # model="gpt-4o-mini-2024-07-18",#gpt-3.5-turbo-instruct #GPT for answer question
        messages=[
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": preprocess_input(prompt)}
        ],
        max_tokens=2560,
        
    )   
    return response.choices[0].message.content
def get_ai_response_sql(prompt):
    prompt = prompt.encode('utf-8').decode('utf-8')
    # print(prompt)
    response = client.chat.completions.create(
        # model="ft:gpt-4o-mini-2024-07-18:xxx",#gpt-3.5-turbo-instruct #GPT for translation sql code
        messages=[
            {"role": "system", "content": "I am a helpful assistant here to provide you with all the information you need."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2560,
        
    )   
    results = response.choices[0].message.content.encode('utf-8').decode('utf-8')
    print(results)
    return response.choices[0].message.content.encode('utf-8').decode('utf-8')
def preprocess_input(input):
    input = input.encode("utf-8").decode('utf-8')
    if "接下來" in input:
        query_part,instruction_part = input.split("接下來",1)
        query_part = get_ai_response_sql(query_part)
        # print(query_part+"-0--------------------------")
        query_part = getdata_from_database(query_part)
        print(query_part)
        print(instruction_part)
        print(query_part+instruction_part)
        print("-----------here")
        return query_part+instruction_part
    else:
        input = get_ai_response_sql(input)
        # print(input)
        return getdata_from_database(input)


# ft:gpt-3.5-turbo-1106:personal:test1:AalFldC3
#從museumexhibits資料表找支援影像辨識模型為N的所有展品是什麼？接下來請以年分做排序