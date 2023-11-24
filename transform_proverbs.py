import requests

def transform_proverb(proverb, index, total):
    # Only print the counter
    print(f"Processing {index}/{total}")
    api_key = "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"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "model": "gpt-4-1106-preview",
        "messages": [{
            "role": "system",
            "content": "Вы работаете в роли переводчика, который переформулирует поговорки в максимально бюрократический канцеляритный стиль. Пример: «Цыплят по осени считают» превратится в «Подсчет прироста домашней птицы производится после завершения сезона сельскохозяйственных работ»."
        }, {
            "role": "user",
            "content": f"Переформулируйте поговорку: '{proverb}'"
        }]
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    response_json = response.json()

    if response_json.get("choices"):
        transformed = response_json.get("choices")[0].get("message").get("content").strip()
        return transformed
    else:
        print(f"Error with proverb '{proverb}':", response_json)
        return None

# Reading proverbs from file
with open("proverbs1.txt", "r") as file:
    proverbs = [line.strip() for line in file if line.strip()]

total_proverbs = len(proverbs)
transformed_proverbs = [transform_proverb(proverb, index+1, total_proverbs) for index, proverb in enumerate(proverbs)]

# Writing result to file
with open("transformed_proverbs1.txt", "w") as file:
    for proverb in transformed_proverbs:
        file.write(proverb + "\n")
