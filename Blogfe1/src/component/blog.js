import React from 'react';
import ReactDom from 'react-dom';
import {Link,Redirect} from 'react-router-dom'
import '../css/login.css'
import { observer } from 'mobx-react';
import { Button,Form,Input} from 'antd'
import 'antd/lib/message/style'
import {inject} from '../util'
import BlogService from '../service/blog';
import TextArea from 'antd/lib/input/TextArea';
import FormItem from 'antd/lib/form/FormItem'
import 'antd/lib/message/style'
import 'antd/lib/form/style'
import 'antd/lib/input/style'
import 'antd/lib/button/style'
import { message} from 'antd'

const service=new BlogService()

@inject({service}) //装饰器函数
@observer //使用mobx 的观察者 监控被观察者状态
export default class Pub extends React.Component{
  //state={'ret':-1}
  handelClick(event){

    event.preventDefault();//阻止提交防止页面刷新
    let fm=event.target;
    console.log(fm)
     this.props.service.pub(fm[0].value,fm[1].value,this)
  }

  render(){

    if(this.props.service.errmsg){//render 中一定要使用这个被观察者 否则不会引起render 重绘
      message.info(this.props.service.errmsg,3,() => {
        this.props.service.errmsg=""
      })
    }
    return (
        <Form layout='vertacal' onSubmit={this.handelClick.bind(this)}>
          <FormItem
            label="标题"
          >
            <Input placeholder="标题" />
          </FormItem>
          <FormItem
            label="内容"
          >
            <TextArea rows={10} placeholder="内容" />
          </FormItem>
          <FormItem >
            <Button type="primary" htmlType="submit">提交</Button>
          </FormItem>
        </Form>);
  }
}
