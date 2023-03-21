import json
import logging
import pandas as pd

log_data = []
logs = dict()

exer_id2knowledge_code = dict()
data = pd.read_excel(io = r"./data/Q.xls", sheet_name = 'Sheet1')
for row in data.values:
    if len(row) < 1:
        continue
    exer_id = int(row[0])
    if exer_id not in exer_id2knowledge_code:
        exer_id2knowledge_code[exer_id] = list()
    for idx, knowledge_code in enumerate(row[1:]):
        if knowledge_code > 0:
            exer_id2knowledge_code[exer_id].append(idx + 1)

print(exer_id2knowledge_code)

# exer_id2knowledge_code = dict()
# exer_id2knowledge_code[1] = [1]
# exer_id2knowledge_code[2] = [2]
# exer_id2knowledge_code[3] = [3]
# exer_id2knowledge_code[4] = [4]
# exer_id2knowledge_code[5] = [3, 7]
# exer_id2knowledge_code[6] = [3, 7]
# exer_id2knowledge_code[7] = [1, 2, 5]
# exer_id2knowledge_code[8] = [1, 2, 5]
# exer_id2knowledge_code[9] = [3, 4]
# exer_id2knowledge_code[10] = [3, 4, 6]
# exer_id2knowledge_code[11] = [1, 2, 3, 5, 7]
# exer_id2knowledge_code[12] = [1, 3, 4, 6, 7]
# exer_id2knowledge_code[13] = [1, 2, 3, 4, 6, 7]
# exer_id2knowledge_code[14] = [1, 2, 3, 4, 5, 6, 7]
# print(exer_id2knowledge_code)

with open('data/NeuralCD.json', encoding='utf8') as i_f:
        input_data = json.load(i_f)

        for item in input_data:
            if "user_id" not in item:
                logging.warn(f"no user_id in {item}")
                continue
            user_id = int(item["user_id"]) - 10000
            if "exer_id" not in item:
                logging.warn(f"no exer_id in {item}")
                continue
            exer_id = int(item["exer_id"])
            if "score" not in item:
                logging.warn(f"no score in {item}")
                continue
            score = float(item["score"])
            if "knowledge_code" not in item:
                logging.warn(f"no knowledge_code in {item}")
                continue
            # knowledge_code = int(item["knowledge_code"])
            if user_id not in logs:
                logs[user_id] = list()

            logs[user_id].append(dict({"exer_id" : exer_id, "score" : score, "knowledge_code" : exer_id2knowledge_code[exer_id], }))

for key, val in logs.items():
    log_data.append(dict({"user_id": key, "log_num": len(val), "logs": val}))

with open('data/trans.json', 'w', encoding='utf8') as o_f:
    json.dump(log_data, o_f, indent=4, ensure_ascii=False)
