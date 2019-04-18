import React from 'react';
import ReactDom from 'react-dom';
import {Link,Redirect} from 'react-router-dom'
import '../css/login.css'
import UserService from '../service/user';
import { observer } from 'mobx-react';
import {inject} from '../util'

const service=new UserService()

@inject({service}) //装饰器函数
@observer //使用mobx 的观察者 监控被观察者状态
export default class Reg extends React.Component{

  handelClick(event){
    event.preventDefault();//阻止提交防止页面刷新
    let fm=event.target.form;

    console.log(fm[0].value);
    console.log(fm[1].value);

     this.props.service.reg(fm[0].value,fm[1].value,fm[2].value)
  }
  render(){
      if(this.props.service.regin){
          return (<Redirect to="/"/>)
      }
    return (
        <div className="login-page">
        <div className="form">
          <form className="login-form">
            <input type="text" placeholder="姓名"/>
            <input type="text" placeholder="邮箱"/>
            <input type="password" placeholder="密码"/>
            <input type="password" placeholder="确认密码"/>
            <button onClick={this.handelClick.bind(this)}>注册</button>
            <p className="message">已有账号? <Link to="/login">请登陆</Link></p>
          </form>
        </div>
      </div>);
  }
}
