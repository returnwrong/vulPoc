import re
text = """<!DOCTYPE HTML >
<html>
  <head>
    <title>互联世界   物联未来</title>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=0.5, user-scalable=no">
        <link rel="stylesheet" href="css/main.css" />
        <!--<script type="text/javascript" src="js/checkIp.js"></script>  -->
        <script language="javascript" src="js/jquery-1.7.min.js"></script>
        <script type="text/javascript" src="js/jquery.blockUI.js"></script>
        <script type="text/javascript" src="js/publicCheck.js"></script>
        <script src="js/css_style.js"></script>

         <!--[if lt IE 9]>
　           　<script src="js/respond.min.js"></script>
 　　         <script src="js/html5shiv.min.js"></script>
   <![endif]-->
        <!--[if IE 7]>
<style>
        div#logo img{width:250px;}
        #menu_login{
                display:inline;
                margin-top:-50px;
                height:35px;
                line-height:35px;
                float: left;
                position:relative;
                }
                #menu_login li{
                        float:left;
                }
                #main{
                        margin-top:50px;
                }
                input{
                        width:160px;
                }
                .btn{border:0px solid #000;}
                input[type="radio"]{
                width:20px;
        }
        #text_l{
                        text-align:center;

                }
</style>
        <![endif]-->
        <!--[if IE 8]>
<style>
        div#logo img{width:250px;}
        #menu_login{
                display:inline;
                margin-top:-50px;
                height:35px;
                line-height:35px;
                float: left;
                position:relative;
                }
                #menu_login li{
                        float:left;
                }
                #main{
                        margin-top:50px;
                }
                #text_l{
                        text-align:center;

                }
                input{
                        width:160px;
                }
                input[type="radio"]{
                width:20px;
        }
</style>
<![endif]-->
  <style>
        #setIfPwd{padding:3px;height:44px;padding-right:3px ;}
        #main p{
                height:40px;
                line-height: 2em;
                margin-bottom: 15px;
        }
  .hinden{
        display: none;
        }
        #bug2{
                margin: 0 auto;
        }
        .right_position{ margin-left: 20px; }
        .left_position{ margin-right: 40px;}
        ul {
    list-style-type:none;
}
ul #li_admin {
    background-image:url(images/1.png);
    background-repeat:no-repeat;
    background-position:50px 34px;
    padding-left:0;
}
ul #li_wan {
    background-image:url(images/2.png);
    background-repeat:no-repeat;
    background-position:46px 32px;
    padding-left:0;
}
ul #li_wifi {
    background-image:url(images/3.png);
    background-repeat:no-repeat;
    background-position:50px 36px;
    padding-left:0;
}
ul #li_set {
    background-image:url(images/4.png);
    background-repeat:no-repeat;
    background-position:50px 34px;
    padding-left:0;
}
ul #li_exit {
    background-image:url(images/5.png);
    background-repeat:no-repeat;
    background-position:50px 33px;
    padding-left:0;
}
        .input_out{
        width:110px;
        height:40px;
        border:1px solid #0080CC;
        background-color:#FFFFFF;
        color: #0080CC;
        margin-left:10px;
        margin-right:10px;
        border-radius: 4px;
        font-size: 18px;
}
        .input_move{
        width:110px;
        height:40px;
        border:1px solid #0080CC;
        background-color:#0080CC;
        color: #FFFFFF;
        margin-left:10px;
        margin-right:10px;
        border-radius: 4px;
        font-size: 18px;
}

  </style>
 </head>
        <!-- end content -->
        <body>

                <div id='head'>
                <div id="logo"><img src="images/logo.png" alt="中移铁通路由"></div>
                <div id="menu_login">
                        <ul style="margin:0px;">
                                <!--<li  onclick="window.location='login.asp'" id="li_admin">管理员登录</li>-->                                <li onClick="window.location='index.asp'" id="li_wan">外网设置</li>
                                <li onClick="window.location='simple-index.asp'" class="actived" id="li_wifi"> 
无线设置<span class='menu_sj'></span></li>
                                <li onClick="window.location='status/status_network.asp'" id="li_set">高级设置</li>
                                <li onClick="window.location='login.asp'" id="li_exit">退出</li>
                        </ul>
                </div>
        </div>

        <div id="main" class="lg_600 md_62per sm_61per">
                <div >
                        <div align="center"><img src="images/wifi.png"></div>
                        <div align="center"><h4 class="lg_text_c md_text_l sm_text_l STYLE2" style="font-weight:bold">无线设置</h4></div>
                        <!--<hr style="height: 1px; background-color: #d3d1d2; width:210px;" align="left" class="lg_hidden"/>-->
                        <div align="center"><p class="mar_top_20 lg_w360">无线密码是设置在无线网络上的密码，建 
议设置一个高强度密码，使你的无线更安全。</p></div>
                </div>
                <br />
                <div class="contain_box" style="margin-left:2%">
                        <!--<form name="wanCfg" method="post" action="/goform/setSimple" onSubmit="return checkValue()" >-->
                        <form action="/goform/setSimpleIndex" name="setSimpleIndex"  method="post" onSubmit="return checkValue()">
                        <div class="left text_r w120 bold" style="margin:5px 0">
                                <p class="STYLE3">无线名称&nbsp;</p>
                                <p class="STYLE3">加密模式&nbsp;</p>
                                <p id="pwd_p1" class="hinden STYLE3">无线密码&nbsp;</p>
                                <p id="pwd_p2" class="hinden STYLE3"></p>
                                <p class="STYLE3">WIFI覆盖&nbsp;</p>
                        </div>
                        <div class="left">
                                <p>
                                <input type="text" class="lg_w330 md_w296 sm_w196 h44 border-radius" maxlength="32" name="ssid" id="ssidIndexId"
                                value="D201" onKeyUp="checkChineseAnd_w(this,this.value)" onBlur="checkChineseAnd_w(this,this.value)" />
                                </p>
                                <!--用户选择加密还是不加密-->
                                <p align="center">
                                        <select name="security_mode" size="1" class="lg_w330 md_w296 sm_w196 border-radius" style="height:42px" id="setIfPwd" onChange="ifhavepwd()">
                                        <option value="WPAPSKWPA2PSK">加密</option>
                                        <option value="OPEN" selected="selected">不加密</option>
                                  </select>
                                </p>
                                <!--加密 class为passwd的div显示  不加密 改为隐藏-->
                                <div class="passwd hinden">
                                        <p id="passWord_out_p">
                                        <input type="text"  class="lg_w330 md_w296 sm_w196 h44 border-radius" name="Pass_Phrase" id="passphrase" size="32" maxlength="32" onFocus="pwdFocus()">
                                        </p>
                                        <p align="center" class="lg_w330 md_w296 sm_w196 text_c" style="margin-left:-4%">密码长度8-32个字符，建议数字、字母、下划线组成</p>
                                </div>
                                <p align="center">
                                <select name="tx_power" class="lg_w330 md_w296 sm_w196 border-radius" style="height:42px" id="ping_select">
                                                                                    <option value="60" id="tx_power">单房</option>
                                                                                    <option value="80" id="tx_power">两房</option>

 <option value="100" id="tx_power">三房</option>

                                </select>
                                </p>
                                <br />
                                <p class="foot-bt" style="margin-right:9%">
                                        <!--<input  type="submit" class="input_out"  onMouseMove="this.className='input_move'" onMouseOut="this.className='input_out'" id="basicApply" value="确定">-->
                                        <button class="input_out" type="submit" id="success" onMouseMove="this.className='input_move'" onMouseOut="this.className='input_out'">确认</button>
                                                <input type="button" class="input_out"  onMouseMove="this.className='input_move'" onMouseOut="this.className='input_out'" id="basicCancel" onClick="basicReSet();" value="重设
">
                                </p>
                        </div>
                        </form>
                        <div class="clearfix"></div>
                </div>
        </div>

        <div id="footer" class="lg_600 md_90per sm_94per text_c">
                <img src="images/by_web.png" class="foot-img"/>
                <p id="foot-p">固件版本：2.0.002<br />帮助热线：4007-66-0632</p>
        </div>
 </body>
  <script type="text/javascript">
   $(document).ready(function(){
   var ifAndPwd = "WPAPSKWPA2PSK";
   if(ifAndPwd.indexOf(";")>=0){
     ifAndPwd = ifAndPwd.slice(0,ifAndPwd.indexOf(";"));
     }
   if("OPEN"!=ifAndPwd){
     //$("#setIfPwd").val("WPAPSKWPA2PSK");
         document.setSimpleIndex.security_mode.options.selectedIndex = 0;
     ifAndPwd ="23456789";
     if(null!=ifAndPwd&&""!=ifAndPwd){
    $("#passWord_out_p").html('<input type="password"  class="lg_w330 md_w296 sm_w196 h44 border-radius" name="Pass_Phrase" value="'
                               +ifAndPwd+'" id="passphrase" size="32" maxlength="32" >');
       }
   }
   ifhavepwd();
   ifAndPwd = "100";
   //ifAndPwd =100;
   if(ifAndPwd==60||ifAndPwd=="60"){
     //$("input[name='tx_power']:eq(0)").attr("checked",'checked');
         document.setSimpleIndex.tx_power.options.selectedIndex = 0;
   }else if(ifAndPwd==80||ifAndPwd=="80"){
     //$("input[name='tx_power']:eq(1)").attr("checked",'checked');
         document.setSimpleIndex.tx_power.options.selectedIndex = 1;
   }else{
     //$("input[name='tx_power']:eq(2)").attr("checked",'checked');
         document.setSimpleIndex.tx_power.options.selectedIndex = 2;
   }
  });

    //防浏览器表单填入，清空文本框
   function pwdFocus(){
    $("#passWord_out_p").html('<input type="password"  class="lg_w330 md_w296 sm_w196 h44 border-radius" name="Pass_Phrase" id="passphrase" size="32" maxlength="32" >');
    $("#passWord_out_p input").focus();
  }


   function ifhavepwd(){
    // var setIfPwd = $("#setIfPwd").val();
        var setIfPwd = document.getElementById("setIfPwd").value;
     if("WPAPSKWPA2PSK"==setIfPwd+""){
          $(".passwd,#pwd_p1,#pwd_p2").removeClass("hinden");
      }else if("OPEN"==setIfPwd+""){
          $(".passwd,#pwd_p1,#pwd_p2").addClass("hinden");
      }
   }
function switch_security_mode(it){
        var tempss = it;
        if( tempss != 'OPEN'){
        document.getElementById("div_wpa").style.display='block';
        }else{
        document.getElementById("div_wpa").style.display='none';
        }
  }

   function  checkValue(){
    var ssidIndexId = $("#ssidIndexId").val();
    var passphrase = $("#passphrase").val();
     var setIfPwd = $("#setIfPwd").val();
   if(""==ssidIndexId||null==ssidIndexId){
    alert("请输入无线名称!");
    return false;
   }
   if(!checkChineseAnd_w("",ssidIndexId)){
    alert("无线名称由数字，字母，中文，下划线组成！");
     return false;
   }

        if(checkChinese(document.getElementById("ssidIndexId")) && ssidIndexId.length>10){
                alert("含有中文的无线名称长度不能超过10个字符！");
                return false;
        }
   var newUN = "D201";
   var newPD = "23456789";
   if("OPEN"!=setIfPwd+""){
   if(""==passphrase||null==passphrase){
    alert("请输入无线密码！");
    return false;
    }

    if(passphrase.length<8||passphrase.length>32){
    alert("密码长度为8-32个字符！");
    return false;
    }

        var reg = /\W/g;//非(数字，字母，中文，下划线)
        var pattern = new RegExp(reg);
        var thisVal1 = passphrase.replace(pattern,"");
                        if(thisVal1.length != passphrase.length){
                           alert("密码只能包含数字、字母、下划线!");
                            $("#passphrase").select();
                                 return false;
                         }
          var retss = confirm("警告：修改无线设置将需要重新连接WIFI！是否继续？");
          if(!retss){ return false;}
   }else{
           var ret = confirm("警告：1.不加密存在安全风险！\n          2.修改无线设置将需要重新连接WIFI！  \n   
         是否继续？");
           if(!ret){ return false; }
        }
                $.blockUI({
                    message:'<image src="images/loading.gif" width="80" height="80"></image>',
                                        css:{
                                        width:"0px",
                                        height:"0px",
                                        marginLeft:"12.5%",
                                        marginTop:"-60px",
                                        border:'none',
                                opacity:"1"
                                        }
                 });
     setTimeout(function(){$.unblockUI();},10000);
   }

  //重设
function basicReSet(){
        var ifAndPwd = "WPAPSKWPA2PSK";
        document.setSimpleIndex.ssid.value="D201";
        document.getElementsByName("Pass_Phrase")[0].value="";

        //power
        var WifiPower='100';
        //alert(WifiPower);
        if(WifiPower<=60)
        {
                document.setSimpleIndex.tx_power.options.selectedIndex = 0;
        }
        else if(WifiPower<=80)
        {
                document.setSimpleIndex.tx_power.options.selectedIndex = 1;
        }
        else
        {
                document.setSimpleIndex.tx_power.options.selectedIndex = 2;
        }

}

</script>
</html>"""
pattern = re.compile(r'var\s+newPD\s+=\s+\"(\S+)\";')
result = pattern.findall(text)
print(result)