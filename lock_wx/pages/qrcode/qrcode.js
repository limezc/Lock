import QR from '../../utils/qrcode.js'
var util = require('../../utils/util.js')
const app = getApp()

Page({
  data: {
    setInter: '',
    expireTime: 60,  //过期时间，这里设置为20秒
    qrcode:'',
  },
  onLoad: function (options) {
    var that = this
    var size = that.setCanvasSize();//动态设置画布大小
    // wx.request({
    //   url: 'https://www.wyt.cloud/wx_auth/qrcode',
    //   method: "POST",//指定请求方式，默认get
    //   header: { "Cookie": app.globalData.cookie },
    //   success: function (res) {
    //     if (res.data.info == "success") {
    //       app.globalData.data = res.data.url
    //       QR.api.draw(app.globalData.data, "mycanvas", size.w, size.h)
    //     } else {
    //       wx.showToast({
    //         title: '权限不足',
    //         icon: 'fail',
    //         duration: 1000,
    //         mask: true
    //       })
    //     }
    //   },
    // })
    var url = "https://www.wyt.cloud/wx_auth/qrcode"
    var data = null
    util.requestFun(url, data).then((res) => {
      return util.requestFun(url, data);
      //Promise队列实现异步函数顺序执行
    }).catch((res) => {
      console.log('错误' + res)
    }).then((res) => {
      if (res.data.info == "success") {
        app.globalData.data = res.data.url
        QR.api.draw(app.globalData.data, "mycanvas", size.w, size.h)
      } else {
        wx.showToast({
          title: '权限不足',
          icon: 'fail',
          duration: 1000,
          mask: true
          })
        }
      that.setData({ qrcode: app.globalData.data })
      console.log(app.globalData.data);
    }).catch((res) => {
      console.log('错误' + res)
    })
  },
  onShow:function(){
    var that=this
    var size = that.setCanvasSize();//动态设置画布大小
    that.data.setInter = setInterval(function () {
      // wx.request({
      //   url: 'https://www.wyt.cloud/wx_auth/qrcode',
      //   method: "POST",//指定请求方式，默认get
      //   header: { "Cookie": app.globalData.cookie },
      //   success: function (res) {
      //     if (res.data.info == "success") {
      //       app.globalData.data = res.data.url
      //       QR.api.draw(app.globalData.data, "mycanvas", size.w, size.h)
      //     } else {
      //       wx.showToast({
      //         title: '权限不足',
      //         icon: 'fail',
      //         duration: 1000,
      //         mask: true
      //       })
      //     }
      //   },
      // })
      var url = "https://www.wyt.cloud/wx_auth/qrcode"
      var data = null
      util.requestFun(url, data).then((res) => {
        return util.requestFun(url, data);
        //Promise队列实现异步函数顺序执行
      }).catch((res) => {
        console.log('错误' + res)
      }).then((res) => {
        if (res.data.info == "success") {
          app.globalData.data = res.data.url
          QR.api.draw(app.globalData.data, "mycanvas", size.w, size.h)
        } else {
          wx.showToast({
            title: '权限不足',
            icon: 'fail',
            duration: 1000,
            mask: true
          })
        }
        that.setData({ qrcode: app.globalData.data })
        console.log(app.globalData.data);
      }).catch((res) => {
        console.log('错误' + res)
      })
    }, 2000);
  },
  //适配不同屏幕大小的canvas
  setCanvasSize: function () {
    var size = {};
    try {
      var res = wx.getSystemInfoSync();
      var scale = 750 / 300;//不同屏幕下canvas的适配比例；设计稿是750宽
      var width = res.windowWidth / scale;
      var height = width;//canvas画布为正方形
      size.w = width;
      size.h = height;
    } catch (e) {
      console.log("获取设备信息失败" + e);
    }
    return size;
  },

  // 生成二维码
  createQrCode: function (canvasId, cavW, cavH) {
      let url = app.globalData.opt
      //调用插件中的draw方法，绘制二维码图片
      QR.api.draw(url, canvasId, cavW, cavH);
  },

  // 手动刷新一次，先清除定时器，再重新开启一个定时器
  manuRefresh: function () {
    let that = this
    clearInterval(that.data.setInter)
    that.autoRefresh()
  },
})