import React from 'react';
import ReactDom from 'react-dom';
import {Link,Redirect} from 'react-router-dom'
import '../css/login.css'
import UserService from '../service/user';
import { observer } from 'mobx-react';
import { message} from 'antd'
import 'antd/lib/message/style'
import {inject} from '../util'


const service=new UserService()

// export default class Login extends React.Component{
//   render(){
      
//       return <_Login service={userservice} />
//   }
// }
@inject({service}) //装饰器函数
@observer //使用mobx 的观察者 监控被观察者状态
//class _Login extends React.Component{
export default class Login extends React.Component{
  //state={'ret':-1}
  handelClick(event){
    event.preventDefault();//阻止提交防止页面刷新
    let fm=event.target.form;
     this.props.service.login(fm[0].value,fm[1].value,this)
  }

  render(){
    //主动判断状态是否被修改过  不推荐
    // if(this.state.ret!=-1){
    //   return (<Redirect to="/about"/>)
    // }
    if(this.props.service.errmsg){//render 中一定要使用这个被观察者 否则不会引起render 重绘
      message.info(this.props.service.errmsg,3,() => {
        this.props.service.errmsg=""
      })
    }
    if(this.props.service.loginin){//render 中一定要使用这个被观察者 否则不会引起render 重绘
      return (<Redirect to="/about"/>)
    }
    return (
        <div className="login-page">
        <div className="form">
          <form className="login-form">
            <input type="text" placeholder="用户名" />
            <input type="password" placeholder="密码"/>
            <button onClick={this.handelClick.bind(this)}>登陆</button>
            <p className="message">还没注册? <Link to="/reg">注册</Link></p>
          </form>
        </div>
      </div>);
  }
}
