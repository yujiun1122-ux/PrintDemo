# Python Print Examples

이 문서는 Python에서 **기본 출력, f-string, format, % 포맷팅, 여러 옵션** 등을 사용하는 예제를 정리한 것입니다.

---

## 1. 변수 선언

```python
name = "YJW"
age = 20
score = 70
```

---

## 2. 기본 출력

```python
print("Hello, Python!")
```

출력:
```
Hello, Python!
```

---

## 3. 여러 값 출력 (콤마로 구분 → 자동 띄어쓰기)

```python
print("Name:", name, "Age:", age, "Score:", score)
```

출력:
```
Name: YJW Age: 20 Score: 70
```

---

## 4. f-string (Python 3.6+)

```python
print(f"My name is {name}, I am {age} years old, score: {score}")
```

출력:
```
My name is YJW, I am 20 years old, score: 70
```

---

## 5. `format()` 함수

```python
print("My name is {}, I am {} years old, score: {}".format(name, age, score))
print("My name is {0}, age {1}, score {2}".format(name, age, score))
print("Score with 2 decimals: {:.2f}".format(score))
```

출력:
```
My name is YJW, I am 20 years old, score: 70
My name is YJW, age 20, score 70
Score with 2 decimals: 70.00
```

---

## 6. % 포맷팅 (C 스타일, 옛날 방식)

```python
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))
```

출력:
```
Name: YJW, Age: 20, Score: 70.0
```

---

## 7. 여러 줄 출력 (줄바꿈 포함)

```python
print("This is line 1\nThis is line 2")
```

출력:
```
This is line 1
This is line 2
```

---

## 8. `end` 옵션 (줄바꿈 대신 다른 문자로 종료)

```python
print("Hello", end=" ")
print("World!")
```

출력:
```
Hello World!
```

---

## 9. `sep` 옵션 (기본값은 공백)

```python
print("2025", "09", "23", sep="-")
```

출력:
```
2025-09-23
```

---

## 10. 딕셔너리/리스트 같이 출력

```python
data = {"name": name, "age": age, "score": score}
print("Data:", data)
```

출력:
```
Data: {'name': 'YJW', 'age': 20, 'score': 70}
```

---

## 11. f-string 내 계산/함수 사용

```python
print(f"Next year age: {age + 1}")
print(f"Score (rounded): {round(score)}")
```

출력:
```
Next year age: 21
Score (rounded): 70
```

---

## 12. 멀티라인 f-string

```python
print(f"""
Student Info:
- Name : {name}
- Age  : {age}
- Score: {score:.2f}
""")
```

출력:
```
Student Info:
- Name : YJW
- Age  : 20
- Score: 70.00
```