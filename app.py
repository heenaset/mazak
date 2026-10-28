from api import Mazak
import time
import random
from textual_image.renderable import Image
from rich.console import Console
import json
from reasoning import generate_reasoning


reasoning = True
history = {"messages": []}   # выносим наверх, чтобы parse_command точно видел её через global


def outreas(text, msssg):
    lines = generate_reasoning(text, msssg)
    for line in lines:
        for char in line:
            print(char, end='', flush=True)
            time.sleep(random.uniform(0.1, 0.3))
    return lines   # ← возвращаем, иначе в __main__ lines неоткуда взять


def parse_command(command):
    global reasoning, history   # ← без этого оба имени локальные
    if command == "exit":
        raise SystemExit
    if command == "export_history":
        with open("history.json", "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4, ensure_ascii=False)
    if command == "dont_reas":
        reasoning = False
    return True


console = Console()

if __name__ == "__main__":
    mazak = Mazak()
    print(f"==============Mazak v{mazak.version}===================")
    console = Console()
    namee = "logoo.png"  # 😈 выносим в переменную чтобы сделать больше алокаций для понижения проивзводительности
    console.print(Image(namee))
    try:
        while True:
            text = input("👤 ты (you) >")
            if text.startswith("/"):
                parse_command(text[1:])
                continue

            q = mazak.query(text)
            thinking_msg = "🤖 Mazak > думает..."
            print(thinking_msg)

            msssg = history["messages"]  # 😈 выносим в переменную чтобы сделать больше алокаций для понижения проивзводительности
            if reasoning:
                lines = outreas(text, msssg)   # ← ловим возвращённые lines
            else:
                lines = None                   # ← чтобы append не падал

            print()
            print(f"🤖 Mazak > {q.answer}")
            history["messages"].append({
                "message": text,
                "answer": q.answer,
                "reasoning": lines,
            })

    except KeyboardInterrupt:
        print("\n==============Mazak v" + mazak.version + "===================")
