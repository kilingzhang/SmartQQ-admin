<?php
		include  './conn/conn.php';
		
		mysql_set_charset("utf8");
		//设置字符集，没有测试是否必须。科普：微信服务器采用utf8，所以MySql数据库字符集是utf8_general_ci。
		$keyword= $object->Content;
		//获取关键字    	$rs = mysql_query("select * from guanjiancihuifu where keywords='$keyword'",$link);//查询数据        $info = mysql_fetch_array($rs);//将查询到的数据填充到数组        if(!$rs)        {        	$content="词库中没有这个词，查询失败！/nBy阿凡舟舟";           //$rs为空        }        else        {       //获取查询到的结果；[]内的为数据表列名        	$type = $info[type];              //回复消息类型——text，image，voice，video，music，news        	$contentStr = $info[content];        //文本消息                	$Title = $info[title];        	$Description = $info[description];//单图文消息        	$PicUrl = $info[picurl];        	$Url = $info[url];                	$MusicUrl = $info[musicurl];     //音乐消息        	$HQMusicUrl = $info[hqmusicurl];                switch ($type)//这里我设置一列为type，借以区分回复消息的类型        {            case "text":                $content = $contentStr;        //文本消息                break;            case "news":                      //这里的news仅代表单图文                $content = array();                $content[] = array("Title"=>$Title,  "Description"=>$Description, "PicUrl"=>$PicUrl, "Url" =>$Url);                break;           /*  case "多图文":                //多图文还没有实现                $content = array();                $content[] = array("Title"=>"多图文1标题", "Description"=>"", "PicUrl"=>"http://discuz.comli.com/weixin/weather/icon/cartoon.jpg", "Url" =>"http://m.cnblogs.com/?u=txw1958");                $content[] = array("Title"=>"多图文2标题", "Description"=>"", "PicUrl"=>"http://d.hiphotos.bdimg.com/wisegame/pic/item/f3529822720e0cf3ac9f1ada0846f21fbe09aaa3.jpg", "Url" =>"http://m.cnblogs.com/?u=txw1958");                $content[] = array("Title"=>"多图文3标题", "Description"=>"", "PicUrl"=>"http://g.hiphotos.bdimg.com/wisegame/pic/item/18cb0a46f21fbe090d338acc6a600c338644adfd.jpg", "Url" =>"http://m.cnblogs.com/?u=txw1958");                break; */            case "music":                $content = array("Title"=>$Title, "Description"=>$Description, "MusicUrl"=>$MusicUrl, "HQMusicUrl"=>$HQMusicUrl);                break;            default:                $content = "该关键词还没有收录词库。请从菜单获取信息/n/n".date("Y-m-d H:i:s",time())."/nBy阿凡舟舟";                break;        }//switch        	mysql_close($link);        }//else        if(is_array($content)){//TODO 如果发过来的是图片链接或音乐链接。。。            if (isset($content[0]['PicUrl'])){                $result = $this->transmitNews($object, $content);            }else if (isset($content['MusicUrl'])){                $result = $this->transmitMusic($object, $content);            }        }else{            $result = $this->transmitText($object, $content);        }        return $result;    }