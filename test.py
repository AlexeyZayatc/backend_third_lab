from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
import math

#f_template = open('test_template.html','r', encoding ='utf-8-sig')
#html = f_template.read()
#f_template.close()

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('task2_template.html');

def f(x):
    return math.sin(x)

def y(x):
    return math.cos(x)

template.globals['f']=f
template.globals['y']=y

N = 10
a = 0
b = 2*math.pi

step =(b-a)/N

myList = []


for i in range(N+1):
    myList.append({
        "x":round(a,3),
        "f(x)": round(f(a),3),
        "y(x)": round(y(a),3)
        })
    a+=step
    pass

first_row = 1
last_row = 12



result_html=template.render(values=myList, firstRow=first_row, lastRow=last_row)

#создадим файл для HTML-страницы
f = open('task2.html', 'w', encoding ='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
