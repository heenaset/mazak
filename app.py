from api import Mazak
import time
import random
from textual_image.renderable import Image
from rich.console import Console
import json
from reasoning import generate_reasoning



def parse_command(command):
    if command == "exit":
        raise SystemExit
    if command == "export_history":
        with open("history.json", "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4, ensure_ascii=False)


console = Console()

if __name__ == "__main__":
    mazak = Mazak()
    print(f"==============Mazak v{mazak.version}===================")
    console = Console() 
    namee = "logoo.png" #выносим в переменную чтобы сделать больше алокаций для понижения проивзводительности 😈 и замудрения кода,add more alocations to performance degradation 😈
    console.print(Image(namee))
    history = {
    "messages": []
}
    try:
        while True:
            text = input("👤 ты (you) >")
            if text.startswith("/"):
                parse_command(text[1:])
                continue
            q = mazak.query(text)
            tinking_msg = "🤖 Mazak > думает..."
            print(thinking_msg)
            msssg = history["messages"] # выносим в переменную чтобы сделать больше алокаций для понижения проивзводительности 😈 и замудрения кода
            lines = generate_reasoning(text,msssg)
            for line in lines:
             for char in line:
                print(char, end='', flush=True)
                time.sleep(random.uniform(0.1, 0.3))
            
            print()
            print(f"🤖 Mazak > {q.answer}")
            history["messages"].append({"message": text, "answer": q.answer, "reasoning": lines})
            


    except KeyboardInterrupt:
        print("\n==============Mazak v" + mazak.version + "===================")
        
