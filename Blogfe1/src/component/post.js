import React from 'react';
import '../css/login.css'
import { observer } from 'mobx-react';
import 'antd/lib/message/style'
import {inject} from '../util'
import BlogService from '../service/blog';
import 'antd/lib/message/style'
import 'antd/lib/Card/style'

import { message,Card} from 'antd'

const service=new BlogService()

@inject({service}) //装饰器函数
@observer //使用mobx 的观察者 监控被观察者状态
export default class Post extends React.Component{
   constructor(props){
     super(props)
     let {id=3} =props.match.params;
     this.props.service.getPost(id)
   }

  render(){

    if(this.props.service.post){//render 中一定要使用这个被观察者 否则不会引起render 重绘
      console.log(this.props.service.post)
    }
    const{title,author,postdate,content} =this.props.service.post //结构post
    return ( 
    <Card
      title={title}
      bordered={true}
      style={{ width: 600 }}
    >
    <p>作者：{author} 发布时间：{new Date(postdate*1000).toLocaleDateString()}</p>
      <p>内容：{content}</p>

    </Card>
    );
  }
}
