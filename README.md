一个臭虫


2018年8月16日20:04:41
难度超出了我的预期,目前主要有如下比较严重问题:
1) 每个web页面下的深度太恐怖. 目前取出来的好几千个url全部在一个url下。
2) GNU 页面(目前只遍历这个页面)使用大量的'#'来当做标识符。如果遍历深度哪怕多一点点也会出现如下情况:
https://gcc.gnu.org/onlinedocs/gcc-8.2.0/gcc/DEC-Alpha-Options.html#DEC-Alpha-Optionsindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#Topindex.html#TopOption-Index.html#Option-Index  这个问题目前的想法是能不能找到每个页面的校验值, 如果再次遍历这个页面则跳过
3) 遍历时间太长, 一个页面的时间大约在1-3S之间，完全不能接受。考虑修改正则表达式优化。或者等以后抓取关键字的时候, 启用线程池。


