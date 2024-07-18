# Introduction to Python

<br>

## What is Python?

Made by Guido van Rossum in 1991, Python is a general-purpose, high-level programming language that emphasises code readability that consistently ranks as one of the most popular programming languages for beginners and professionals alike.

<br>

## What can you do with Python?

- Data analysis
- Data visualisation
  - Example [Uber Ridesharing in NYC Visualisation built with Streamlit](https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/main)
  - See the [streamlit gallery](https://streamlit.io/gallery) for more examples, although you can create visualisation dashboards with many other librarires.
- Statistics and machine learning
- Web development
    - Built with django web framework: [The National Geographic website](https://www.nationalgeographic.com/)
- Automation or scripting of everyday tasks

<br>

## Why Python?

- It has simple syntax that mimics natural language
  - This makes Python **beginner-friendly** and easy to read.
- Its open source
  - This means Python is free to use, built and supported by the developer community, without any corporate interest.
- It has a large and active online community supporting and extending Python to suit many usecases
  - This makes Python a very **stable** language.
  - This makes Python very **versatile** (Python has a large array of useful modules and libraries that add functionality)
  - This also makes it very **easy to find support** for learning and for troubleshooting online.
  - Python is a **popular**, **in-demand** professional skill.
- Python is a **high-level** language
  - This combined with its simple syntax means that it takes less code to make big projects a reality.
  - Althought this can come at the cost of performance for certain tasks
- Python is a **multi-paradigm** language
  - This means you have the ability to code in multiple ways and doesn't box you into one programming paradigm.
- Here is the [2023 Stack Overflow Developer survey](https://survey.stackoverflow.co/2023/#technology-most-popular-technologies).

<br>

### What do you think this code below does?


```Python
consultants = {
    "Ada": {"homework_done": True},
    "Marie": {"homework_done": True},
    "Linus": {"homework_done": False},
    "Guido": {"homework_done": True},
}

for consultant_name, info in consultants.items():
    if info["homework_done"] is False:
        print(f"""
        Dear {consultant_name}, 
        Please remember to hand in your git homework.
        Many thanks,
        Gareth
        """
        )
```

---
## Hello World
### Hello World in Python
```Python
print("hello world")
```

### Hello World in Java

```java
public class myfirstclass {
    public static void main(String[] args){
        System.out.println("Hello World!")
    }
}
```