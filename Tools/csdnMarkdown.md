@[TOC](����д�Զ���Ŀ¼����)

# ��ӭʹ��Markdown�༭��

��ã� �������һ��ʹ�� **Markdown�༭��** ��չʾ�Ļ�ӭҳ���������ѧϰ���ʹ��Markdown�༭��, ������ϸ�Ķ���ƪ���£��˽�һ��Markdown�Ļ����﷨֪ʶ��

## �µĸı�

���Ƕ�Markdown�༭��������һЩ������չ���﷨֧�֣����˱�׼��Markdown�༭�����ܣ��������������¼����¹��ܣ�����������д���ͣ�
 1. **ȫ�µĽ������** ���������ȫ�µ�д�����飻
 2. �ڴ�������������ϲ���Ĵ��������ʽ��Markdown **������Ƭ��ʾѡ��ĸ�����ʽ** ����չʾ��
 3. ������ **ͼƬ��ק** ���ܣ�����Խ����ص�ͼƬֱ����ק���༭����ֱ��չʾ��
 4. ȫ�µ� **KaTeX��ѧ��ʽ** �﷨��
 5. ������֧��**����ͼ��mermaid�﷨[^1]** ���ܣ�
 6. ������ **����Ļ�༭** Markdown���¹��ܣ�
 7. ������ **����д��ģʽ��Ԥ��ģʽ�����д��ģʽ����������ͬ����������** �ȹ��ܣ����ܰ�ťλ�ڱ༭������Ԥ�������м䣻
 8. ������ **����б�** ���ܡ�
 [^1]: [mermaid�﷨˵��](https://mermaidjs.github.io/)

## ���ܿ�ݼ�

������<kbd>Ctrl/Command</kbd> + <kbd>Z</kbd>
������<kbd>Ctrl/Command</kbd> + <kbd>Y</kbd>
�Ӵ֣�<kbd>Ctrl/Command</kbd> + <kbd>B</kbd>
б�壺<kbd>Ctrl/Command</kbd> + <kbd>I</kbd>
���⣺<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>H</kbd>
�����б�<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>U</kbd>
�����б�<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd>
����б�<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>C</kbd>
������룺<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>K</kbd>
�������ӣ�<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>L</kbd>
����ͼƬ��<kbd>Ctrl/Command</kbd> + <kbd>Shift</kbd> + <kbd>G</kbd>
���ң�<kbd>Ctrl/Command</kbd> + <kbd>F</kbd>
�滻��<kbd>Ctrl/Command</kbd> + <kbd>G</kbd>

## ����Ĵ������⣬������Ŀ¼������

ֱ������1��<kbd>#</kbd>��������<kbd>space</kbd>�󣬽�����1�����⡣
����2��<kbd>#</kbd>��������<kbd>space</kbd>�󣬽�����2�����⡣
�Դ����ƣ�����֧��6�����⡣������ʹ��`TOC`�﷨������һ��������Ŀ¼��

## ��θı��ı�����ʽ

*ǿ���ı�* _ǿ���ı�_

**�Ӵ��ı�** __�Ӵ��ı�__

==����ı�==

~~ɾ���ı�~~

> �����ı�

H~2~O is��Һ�塣

2^10^ �������� 1024.

## ����������ͼƬ

����: [link](https://mp.csdn.net).

ͼƬ: ![Alt](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw)

���ߴ��ͼƬ: ![Alt](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw =30x30)

���е�ͼƬ: ![Alt](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw#pic_center)

���в��Ҵ��ߴ��ͼƬ: ![Alt](https://imgconvert.csdnimg.cn/aHR0cHM6Ly9hdmF0YXIuY3Nkbi5uZXQvNy83L0IvMV9yYWxmX2h4MTYzY29tLmpwZw#pic_center =30x30)

��Ȼ������Ϊ�����û����ӱ�ݣ�����������ͼƬ��ק���ܡ�

## ��β���һ��Ư���Ĵ���Ƭ

ȥ[��������](https://mp.csdn.net/configure)ҳ�棬ѡ��һ����ϲ���Ĵ���Ƭ������ʽ������չʾͬ�������� `����Ƭ`.
```javascript
// An highlighted block
var foo = 'bar';
```

## ����һ���ʺ�����б�

- ��Ŀ
  - ��Ŀ
    - ��Ŀ

1. ��Ŀ1
2. ��Ŀ2
3. ��Ŀ3

- [ ] �ƻ�����
- [x] �������

## ����һ�����
һ���򵥵ı������ô�����ģ�
��Ŀ     | Value
-------- | -----
����  | $1600
�ֻ�  | $12
����  | $1

### �趨���ݾ��С����󡢾���
ʹ��`:---------:`����
ʹ��`:----------`����
ʹ��`----------:`����
| ��һ��       | �ڶ���         | ������        |
|:-----------:| -------------:|:-------------|
| ��һ���ı����� | �ڶ����ı�����  | �������ı����� | 

### SmartyPants
SmartyPants��ASCII����ַ�ת��Ϊ�����ܡ�ӡˢ���HTMLʵ�塣���磺
|    TYPE   |ASCII                          |HTML                         
|----------------|-------------------------------|-----------------------------|
|Single backticks|`'Isn't this fun?'`            |'Isn't this fun?'            |
|Quotes          |`"Isn't this fun?"`            |"Isn't this fun?"            |
|Dashes          |`-- is en-dash, --- is em-dash`|-- is en-dash, --- is em-dash|

## ����һ���Զ����б�
Markdown
:  Text-to-HTML conversion tool

Authors
:  John
:  Luke

## ��δ���һ��ע��

һ������ע�ŵ��ı���[^2]

[^2]: ע�ŵĽ���

##  ע��Ҳ�Ǳز����ٵ�

Markdown���ı�ת��Ϊ HTML��

*[HTML]:   ���ı��������

## KaTeX��ѧ��ʽ

������ʹ����ȾLaTeX��ѧ���ʽ [KaTeX](https://khan.github.io/KaTeX/):

Gamma��ʽչʾ $\Gamma(n) = (n-1)!\quad\forall
n\in\mathbb N$ ��ͨ��ŷ������

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$

> ������ҵ�������ڵ���Ϣ **LaTeX** ��ѧ���ʽ[here][1].

## �µĸ���ͼ���ܣ��ḻ�������

```mermaid
gantt
        dateFormat  YYYY-MM-DD
        title Adding GANTT diagram functionality to mermaid
        section ��������
        �����               :done,    des1, 2014-01-06,2014-01-08
        ������               :active,  des2, 2014-01-09, 3d
        �ƻ�һ               :         des3, after des2, 5d
        �ƻ���               :         des4, after des3, 5d
```
- ���� **����ͼ** �﷨���ο� [���][2],

## UML ͼ��

����ʹ��UMLͼ�������Ⱦ�� [Mermaid](https://mermaidjs.github.io/). �������������һ������ͼ��

```mermaid
sequenceDiagram
���� ->> ����: ��ã�����, �����ô��?
����-->>����: �������ô�������壿
����--x ����: �Һܺã�лл!
����-x ����: �Һܺã�лл!
Note right of ����: �������˺ܳ�ʱ��, ����̫����<br/>���ʺϷ���һ��.

����-->>����: ����������...
����->>����: �ܺ�... ����, ����ô��?
```

�⽫����һ������ͼ��:

```mermaid
graph LR
A[������] -- ���� --> B((Բ))
A --> C(Բ�ǳ�����)
B --> D{����}
C --> D
```

- ���� **Mermaid** �﷨���ο� [���][3],

## FLowchart����ͼ

�������ɻ�֧��flowchart������ͼ��
```mermaid
flowchat
st=>start: ��ʼ
e=>end: ����
op=>operation: �ҵĲ���
cond=>condition: ȷ�ϣ�

st->op->cond
cond(yes)->e
cond(no)->op
```

- ���� **Flowchart����ͼ** �﷨���ο� [���][4].

## �����뵼��

###  ����
������볢��ʹ�ô˱༭��, ������ڴ�ƪ��������༭�����������һƪ���µ�д��, ���Ϸ��������ҵ� **���µ���** ������һ��.md�ļ�����.html�ļ����б��ر��档

### ����
����������һƪ��д����.md�ļ������Ϸ�����������ѡ���빦�ܽ��ж�Ӧ��չ�����ļ����룬
������Ĵ�����

 [1]: http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
 [2]: https://mermaidjs.github.io/
 [3]: https://mermaidjs.github.io/
 [4]: http://adrai.github.io/flowchart.js/