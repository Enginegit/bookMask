import requests

data1 = {
    'account':'',
    'code':'033FKC980LTBoD1Eek680OEy980FKC9Y',#变动数据
    'model':'53',
    'actionUnitId':'10000204', #变动数据
    'title': '口罩预约领取',
    'type': '0',
    'state': '1',
    'sysOrgId': '-1',
    'ispublic': 'N',
    'content': '口罩预约领取',
    'name': '雷小燕', #必填姓名
    'mobile': '15876316969', #必填手机
    'certType': 'SFZ',
    'certCode': '441882200311023320',   #必填身份证号
    'area': 'lianzhoustreet', #必填哪个区（县）
    'street': '丰阳镇', #哪条街（镇）
    'scene': '夏炉村委会水鸭塘村',    #具体地址
    'mailType':'1'
}

data2 = {
    'account':'',
    'code':'033FKC980LTBoD1Eek680OEy980FKC9Y',#变动数据
    'model':'53',
    'actionUnitId':'10000204', #变动数据
    'title': '口罩预约领取',
    'type': '0',
    'state': '1',
    'sysOrgId': '-1',
    'ispublic': 'N',
    'content': '口罩预约领取',
    'name': '李结清', #必填姓名
    'mobile': '13710832365', #必填手机
    'certType': 'SFZ',
    'certCode': '441825197410280048',   #必填身份证号
    'area': 'lianzhoustreet', #必填哪个区（县）
    'street': '丰阳镇', #哪条街（镇）
    'scene': '夏炉村委会水鸭塘村',    #具体地址
    'mailType':'1'
}

data3 = {
    'account':'',
    'code':'033FKC980LTBoD1Eek680OEy980FKC9Y',#变动数据
    'model':'53',
    'actionUnitId':'10000204', #变动数据
    'title': '口罩预约领取',
    'type': '0',
    'state': '1',
    'sysOrgId': '-1',
    'ispublic': 'N',
    'content': '口罩预约领取',
    'name': '吴昌灏', #必填姓名
    'mobile': '13192752697', #必填手机
    'certType': 'SFZ',
    'certCode': '44182520010712061X',   #必填身份证号
    'area': 'lianshanstreet', #必填哪个区（县）
    'street': '吉田镇', #哪条街（镇）
    'scene': '市场西街林苑',    #具体地址
    'mailType':'1'
}

data4 = {
    'account':'',
    'code':'033FKC980LTBoD1Eek680OEy980FKC9Y',#变动数据
    'model':'53',
    'actionUnitId':'10000204', #变动数据
    'title': '口罩预约领取',
    'type': '0',
    'state': '1',
    'sysOrgId': '-1',
    'ispublic': 'N',
    'content': '口罩预约领取',
    'name': '李柳清', #必填姓名
    'mobile': '13679547640', #必填手机
    'certType': 'SFZ',
    'certCode': '441825197608160068',   #必填身份证号
    'area': 'lianshanstreet', #必填哪个区（县）
    'street': '吉田镇', #哪条街（镇）
    'scene': '市场西街林苑',    #具体地址
    'mailType':'1'
}

data5 = {
    'account':'',
    'code':'033FKC980LTBoD1Eek680OEy980FKC9Y',#变动数据
    'model':'53',
    'actionUnitId':'10000204', #变动数据
    'title': '口罩预约领取',
    'type': '0',
    'state': '1',
    'sysOrgId': '-1',
    'ispublic': 'N',
    'content': '口罩预约领取',
    'name': '吴东俭', #必填姓名
    'mobile': '15992097683', #必填手机
    'certType': 'SFZ',
    'certCode': '441825197211210055',   #必填身份证号
    'area': 'lianshanstreet', #必填哪个区（县）
    'street': '吉田镇', #哪条街（镇）
    'scene': '市场西街林苑',    #具体地址
    'mailType':'1'
}

data6 = {
    'account':'',
    'code':'033FKC980LTBoD1Eek680OEy980FKC9Y',#变动数据
    'model':'53',
    'actionUnitId':'10000204', #变动数据
    'title': '口罩预约领取',
    'type': '0',
    'state': '1',
    'sysOrgId': '-1',
    'ispublic': 'N',
    'content': '口罩预约领取',
    'name': '雷国华', #必填姓名
    'mobile': '13535319874', #必填手机
    'certType': 'SFZ',
    'certCode': '441824197501267512',   #必填身份证号
    'area': 'lianzhoustreet', #必填哪个区（县）
    'street': '丰阳镇', #哪条街（镇）
    'scene': '夏炉村委会水鸭塘村',    #具体地址
    'mailType':'1'
}

data7 = {
    'account':'',
    'code':'033FKC980LTBoD1Eek680OEy980FKC9Y',#变动数据
    'model':'53',
    'actionUnitId':'10000204', #变动数据
    'title': '口罩预约领取',
    'type': '0',
    'state': '1',
    'sysOrgId': '-1',
    'ispublic': 'N',
    'content': '口罩预约领取',
    'name': '张玉婵', #必填姓名
    'mobile': '13726987912', #必填手机
    'certType': 'SFZ',
    'certCode': '441825198910180822',   #必填身份证号
    'area': 'lianshanstreet', #必填哪个区（县）
    'street': '吉田镇', #哪条街（镇）
    'scene': '民族度假村前台',    #具体地址
    'mailType':'1'
}

data8 = {
    'account':'',
    'code':'033FKC980LTBoD1Eek680OEy980FKC9Y',#变动数据
    'model':'53',
    'actionUnitId':'10000204', #变动数据
    'title': '口罩预约领取',
    'type': '0',
    'state': '1',
    'sysOrgId': '-1',
    'ispublic': 'N',
    'content': '口罩预约领取',
    'name': '李福财', #必填姓名
    'mobile': '15919287811', #必填手机
    'certType': 'SFZ',
    'certCode': '44020219810606091X',   #必填身份证号
    'area': 'lianshanstreet', #必填哪个区（县）
    'street': '吉田镇', #哪条街（镇）
    'scene': '民族度假村前台',    #具体地址
    'mailType':'1'
}

def post(data,uuid):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1278.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat','Referer':f'http://12345.gdqy.gov.cn/12345_weixinweb_kz//page/mask/maskForm.html?uuid={uuid}&code=033FKC980LTBoD1Eek680OEy980FKC9Y','Origin':'http://12345.gdqy.gov.cn',
'X-Requested-With':'XMLHttpRequest'

}
    url = f'http://12345.gdqy.gov.cn/12345_weixinweb_kz//order/doQyMaskSave.do?uuid={uuid}'
    response = requests.post(url=url,headers=headers,data=data)
    return response

def main1():
    print('请输入导入的数据名：')
    name = input()
    if name == 'data1':
       job(data1)
    elif name == 'data2':
       job(data2)
    elif name == 'data3':
       job(data3)
    elif name == 'data4':
       job(data4)
    elif name == 'data5':
       job(data5)
    elif name == 'data6':
       job(data6)
    elif name == 'data7':
       job(data7)
    elif name == 'data8':
       job(data8)

def job(data):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/4.0.1278.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2875.116 Safari/537.36 NetType/WIFI MicroMessenger/7.0.5 WindowsWechat','Referer':'http://12345.gdqy.gov.cn/12345_weixinweb_kz//page/mask/maskForm.html?code=033FKC980LTBoD1Eek680OEy980FKC9Y','Origin':'http://12345.gdqy.gov.cn',
'X-Requested-With':'XMLHttpRequest'

}

    while(True):
      try:
        re = requests.post(url='http://12345.gdqy.gov.cn/12345_weixinweb_kz//order/checkCount.do',headers=headers)
        if re.json()['code'] == 'success':
          uuid = re.json()['uuid']
          break
        else:
          print(re.json()['msg'])
      except:
        print('连接失败')
    print('获取uuid成功')
    while(True):
      try:
        res = post(data,uuid)
        print("{}{}{}".format(data['name'],res.json()['code'], res.json()['msg']))
      except:
        print('发包失败')


if __name__ == '__main__':
    main1()