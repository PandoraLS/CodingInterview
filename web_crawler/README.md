## pythontools

### get_html.py
* get_html(url, code='utf-8')
* get_html_with_proxies(url, code='utf-8', proxies=None)
* get_html_with_header(url, code='utf-8', header=None)
* get_redirect_url_and_html(url, code='utf-8')

### text_process.py
* full2half(s), 全角转半角
* clean(s)
* to_unicode(s)

### date_process.py
* days_between(T_begin, T_end)
* calu_begin_date(T_now, before_days)
* parse_time(t)

### filetree.py
```
参数格式1：python filetree.py src_dir             # 将src_dir的目录树输出到终端
参数格式2：python filetree.py src_dir dest_file   # 将src_dir的目录树输出到dest_file
示例：     python filetree.py C:\Desktop D:\filetree.txt
路径不含空格
```

### logger.py
程序片段, 同时输出到控制台和文件中
