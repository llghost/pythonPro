import React from 'react';
import ReactDom from 'react-dom';
import {Route,Link,BrowserRouter as Router} from 'react-router-dom';
import Login from './component/login';
import Reg from './component/reg' ;
import Pub from './component/blog' ;
import L from './component/list' ;
import Post from './component/post' ;
import './css/menu.css';
import { Menu, Icon,LocaleProvider } from 'antd';
import { Layout } from 'antd';
import 'antd/lib/menu/style';
import 'antd/lib/icon/style'
import zh_CN from 'antd/lib/locale-provider/zh_CN';

const {
  Header, Footer, Content,
} = Layout;

const Home = () =>(  //特别注意这里是 小括号
  <div>
    <h2></h2>
  </div>
);

const About = () =>(
  <div>
    <h2> 关于</h2>
  </div>
);

class Root extends React.Component{
  render(){
    return (
    <Router>  

        <Layout>
          <Header>        
            <Menu mode="horizontal" theme='dark'>
            <Menu.Item key="home">
              <Icon type="home" /><Link to='/'>主页</Link>
            </Menu.Item>
            <Menu.Item key="login">
              <Icon type="login" /><Link to='/login'>登陆</Link>
            </Menu.Item>
            <Menu.Item key="reg">
              <Icon /><Link to='/reg'>注册</Link>
            </Menu.Item>
            <Menu.Item key="bar">
              <Icon type="bars"/><Link to='/Pub'>发布博文</Link>
            </Menu.Item>
            <Menu.Item key="list">
              <Icon type="bars"/><Link to='/List'>文章列表</Link>
            </Menu.Item>
            <Menu.Item key="about">
              <Icon /><Link to='/about'>关于</Link>
            </Menu.Item>
          </Menu></Header>
          <Content style={{ padding: '8px 50px' }}>
          <div style={{ background:'#fff',padding:24,minHeight:280}}>
            <Route path="/about" component={About} />
            <Route path="/" component={Home} />
            <Route path="/login" component={Login} />
            <Route path="/reg" component={Reg} />
            <Route path="/Pub" component={Pub} />
            <Route path="/List" component={L} />
            <Route path="/post/:id" component={Post} />
            </div>
            </Content>

          <Footer style={{ textAlign: 'center' }}>
         BLOG ©2018 Created by GHOST
      </Footer>
        </Layout>



    </Router>);
  }
}


ReactDom.render(<LocaleProvider locale={zh_CN}><Root /></LocaleProvider> ,document.getElementById('root'))
