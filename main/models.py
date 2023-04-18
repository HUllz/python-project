#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    nianling=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    shenfenzheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='身份证' )
    youxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    zhaopian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='照片' )
    money=models.FloatField   (  null=True, unique=False,default='0', verbose_name='余额' )
    '''
    zhanghao=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    nianling=Integer
    lianxidianhua=VARCHAR
    shenfenzheng=VARCHAR
    youxiang=VARCHAR
    zhaopian=VARCHAR
    money=Float
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class lingyangxinxi(BaseModel):
    __doc__ = u'''lingyangxinxi'''
    __tablename__ = 'lingyangxinxi'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dingdanbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='订单编号' )
    chongwumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物名称' )
    chongwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物类型' )
    pinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品种' )
    chongwutupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物图片' )
    chongwuxingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物性别' )
    chongwunianling=models.IntegerField  (  null=True, unique=False, verbose_name='宠物年龄' )
    youfei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮费' )
    lingyangriqi=models.DateField   (  null=True, unique=False, verbose_name='领养日期' )
    lingyangneirong=models.TextField   (  null=True, unique=False, verbose_name='领养内容' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    dingdanbianhao=VARCHAR
    chongwumingcheng=VARCHAR
    chongwuleixing=VARCHAR
    pinzhong=VARCHAR
    chongwutupian=VARCHAR
    chongwuxingbie=VARCHAR
    chongwunianling=Integer
    youfei=VARCHAR
    lingyangriqi=Date
    lingyangneirong=Text
    zhanghao=VARCHAR
    xingming=VARCHAR
    lianxidianhua=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    ispay=VARCHAR
    userid=BigInteger
    '''
    class Meta:
        db_table = 'lingyangxinxi'
        verbose_name = verbose_name_plural = '领养信息'
class chongwulingyang(BaseModel):
    __doc__ = u'''chongwulingyang'''
    __tablename__ = 'chongwulingyang'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    chongwumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物名称' )
    chongwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物类型' )
    pinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品种' )
    chongwutupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物图片' )
    chongwuxingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物性别' )
    chongwunianling=models.IntegerField  (  null=True, unique=False, verbose_name='宠物年龄' )
    chongwuzhongliang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物重量' )
    youfei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮费' )
    chongwujianjie=models.TextField   (  null=True, unique=False, verbose_name='宠物简介' )
    '''
    chongwumingcheng=VARCHAR
    chongwuleixing=VARCHAR
    pinzhong=VARCHAR
    chongwutupian=VARCHAR
    chongwuxingbie=VARCHAR
    chongwunianling=Integer
    chongwuzhongliang=VARCHAR
    youfei=VARCHAR
    chongwujianjie=Text
    '''
    class Meta:
        db_table = 'chongwulingyang'
        verbose_name = verbose_name_plural = '宠物领养'
class youfei(BaseModel):
    __doc__ = u'''youfei'''
    __tablename__ = 'youfei'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    chongwuzhongliang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物重量' )
    youfei=models.IntegerField  (  null=True, unique=False, verbose_name='邮费' )
    '''
    chongwuzhongliang=VARCHAR
    youfei=Integer
    '''
    class Meta:
        db_table = 'youfei'
        verbose_name = verbose_name_plural = '邮费'
class chongwushangcheng(BaseModel):
    __doc__ = u'''chongwushangcheng'''
    __tablename__ = 'chongwushangcheng'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    shangpinbianhao=models.CharField ( max_length=255, null=True,unique=True, verbose_name='商品编号' )
    chongwuyongpinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物用品名称' )
    leixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='类型' )
    tupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图片' )
    shiyongchongwu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='适用宠物' )
    yongtujianjie=models.TextField   (  null=True, unique=False, verbose_name='用途简介' )
    yongpinmiaoshu=models.TextField   (  null=True, unique=False, verbose_name='用品描述' )
    price=models.FloatField   ( null=False, unique=False, verbose_name='价格' )
    '''
    shangpinbianhao=VARCHAR
    chongwuyongpinmingcheng=VARCHAR
    leixing=VARCHAR
    tupian=VARCHAR
    shiyongchongwu=VARCHAR
    yongtujianjie=Text
    yongpinmiaoshu=Text
    price=Float
    '''
    class Meta:
        db_table = 'chongwushangcheng'
        verbose_name = verbose_name_plural = '宠物商城'
class lingyangchongwufabu(BaseModel):
    __doc__ = u'''lingyangchongwufabu'''
    __tablename__ = 'lingyangchongwufabu'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    chongwumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物名称' )
    chongwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物类型' )
    pinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品种' )
    chongwutupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物图片' )
    chongwuxingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物性别' )
    chongwunianling=models.IntegerField  (  null=True, unique=False, verbose_name='宠物年龄' )
    chongwuzhongliang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物重量' )
    youfei=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮费' )
    chongwushipin=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物视频' )
    zhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='账号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    chongwumingcheng=VARCHAR
    chongwuleixing=VARCHAR
    pinzhong=VARCHAR
    chongwutupian=VARCHAR
    chongwuxingbie=VARCHAR
    chongwunianling=Integer
    chongwuzhongliang=VARCHAR
    youfei=VARCHAR
    chongwushipin=VARCHAR
    zhanghao=VARCHAR
    xingming=VARCHAR
    userid=BigInteger
    '''
    class Meta:
        db_table = 'lingyangchongwufabu'
        verbose_name = verbose_name_plural = '领养宠物发布'
class huifangxinxi(BaseModel):
    __doc__ = u'''huifangxinxi'''
    __tablename__ = 'huifangxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    chongwumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物名称' )
    chongwuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物类型' )
    pinzhong=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品种' )
    chongwutupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物图片' )
    chongwuxingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物性别' )
    chongwunianling=models.IntegerField  (  null=True, unique=False, verbose_name='宠物年龄' )
    chongwuzhongliang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物重量' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    chongwuzhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='宠物状态' )
    shenghuozhuangkuang=models.TextField   (  null=True, unique=False, verbose_name='生活状况' )
    '''
    chongwumingcheng=VARCHAR
    chongwuleixing=VARCHAR
    pinzhong=VARCHAR
    chongwutupian=VARCHAR
    chongwuxingbie=VARCHAR
    chongwunianling=Integer
    chongwuzhongliang=VARCHAR
    xingming=VARCHAR
    chongwuzhuangtai=VARCHAR
    shenghuozhuangkuang=Text
    '''
    class Meta:
        db_table = 'huifangxinxi'
        verbose_name = verbose_name_plural = '回访信息'
class cart(BaseModel):
    __doc__ = u'''cart'''
    __tablename__ = 'cart'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='chongwushangcheng', verbose_name='商品表名' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    picture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='图片' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    price=models.FloatField   (  null=True, unique=False, verbose_name='单价' )
    discountprice=models.FloatField   (  null=True, unique=False, verbose_name='会员价' )
    '''
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=VARCHAR
    buynumber=Integer
    price=Float
    discountprice=Float
    '''
    class Meta:
        db_table = 'cart'
        verbose_name = verbose_name_plural = '购物车表'
class orders(BaseModel):
    __doc__ = u'''orders'''
    __tablename__ = 'orders'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    orderid=models.CharField ( max_length=255,null=False,unique=True, verbose_name='订单编号' )
    tablename=models.CharField ( max_length=255, null=True, unique=False,default='chongwushangcheng', verbose_name='商品表名' )
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    goodid=models.BigIntegerField  ( null=False, unique=False, verbose_name='商品id' )
    goodname=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品名称' )
    picture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品图片' )
    buynumber=models.IntegerField  ( null=False, unique=False, verbose_name='购买数量' )
    price=models.FloatField   ( null=False, unique=False,default='0', verbose_name='价格/积分' )
    discountprice=models.FloatField   (  null=True, unique=False,default='0', verbose_name='折扣价格' )
    total=models.FloatField   ( null=False, unique=False,default='0', verbose_name='总价格/总积分' )
    discounttotal=models.FloatField   (  null=True, unique=False,default='0', verbose_name='折扣总价格' )
    type=models.IntegerField  (  null=True, unique=False,default='1', verbose_name='支付类型' )
    status=models.CharField ( max_length=255, null=True, unique=False, verbose_name='状态' )
    address=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地址' )
    tel=models.CharField ( max_length=255, null=True, unique=False, verbose_name='电话' )
    consignee=models.CharField ( max_length=255, null=True, unique=False, verbose_name='收货人' )
    '''
    orderid=VARCHAR
    tablename=VARCHAR
    userid=BigInteger
    goodid=BigInteger
    goodname=VARCHAR
    picture=VARCHAR
    buynumber=Integer
    price=Float
    discountprice=Float
    total=Float
    discounttotal=Float
    type=Integer
    status=VARCHAR
    address=VARCHAR
    tel=VARCHAR
    consignee=VARCHAR
    '''
    class Meta:
        db_table = 'orders'
        verbose_name = verbose_name_plural = '订单'
class address(BaseModel):
    __doc__ = u'''address'''
    __tablename__ = 'address'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    address=models.CharField ( max_length=255,null=False, unique=False, verbose_name='地址' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='收货人' )
    phone=models.CharField ( max_length=255,null=False, unique=False, verbose_name='电话' )
    isdefault=models.CharField ( max_length=255,null=False, unique=False, verbose_name='是否默认地址[是/否]' )
    '''
    userid=BigInteger
    address=VARCHAR
    name=VARCHAR
    phone=VARCHAR
    isdefault=VARCHAR
    '''
    class Meta:
        db_table = 'address'
        verbose_name = verbose_name_plural = '地址'
