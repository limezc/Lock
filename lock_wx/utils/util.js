const app = getApp()
const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return [year, month, day].map(formatNumber).join('/') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

function requestFun(url_i, data_i) {
  var data = new Promise(function (resolve, reject) {
    wx.request({
      url: url_i,
      method: "POST",
      data: data_i,
      header: { "Cookie": app.globalData.cookie },
      success: function (res) {
        resolve(res)
      },
      fail: function (res) {
        reject("系统异常，请重试！")
      },
      complete: function (res) {
        wx.hideLoading()
      },
    })
  });
  return data;
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : '0' + n
}

module.exports = {
  formatTime: formatTime,
  requestFun: requestFun
}
