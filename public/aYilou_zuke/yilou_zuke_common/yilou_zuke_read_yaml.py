# -*- coding: UTF-8 -*-
import yaml
import os
import logging.config
base_path='..yilou_zuke_common\yilou_zuke_config\YiLou_zufang.yaml'
log_path=r'd:\Python_study\PYREQUESTS\config\logging.conf'
logging.config.fileConfig(log_path)
logger=logging.getLogger()

class Read_Yaml_Config(object):
    def get_peizhi_(self,name,yaml_ming,huanjing=1):
        ''''''
        if huanjing==1:
            name=name+'_test'
            yaml_path = os.path.dirname(os.path.dirname(__file__))
            yaml_path = yaml_path + '/yilou_zuke_config/' + yaml_ming
            # logging.info(yaml_path)

            try:
                if name != None:
                    with open(yaml_path, 'r', encoding='utf-8') as stream:
                        shuju_name = yaml.load(stream)
                        shuju = shuju_name[name]
                        # logging.info(shuju)
                        stream.close()
                    return shuju
            except:
                print('name is not Null')

        if huanjing==2:
            name=name+'_beta'
            yaml_path = os.path.dirname(os.path.dirname(__file__))
            yaml_path = yaml_path + '/yilou_zuke_config/' + yaml_ming
            # logging.info(yaml_path)

            try:
                if name != None:
                    with open(yaml_path, 'r', encoding='utf-8') as stream:
                        shuju_name = yaml.load(stream)
                        shuju = shuju_name[name]
                        # logging.info(shuju)
                        stream.close()
                    return shuju
            except:
                print('name is not Null')
    def get_peizhi(self,name,yaml_ming):
        '''
        #获取yaml配置
        :param name:父类名 
        :return: 
        '''
        yaml_path = os.path.dirname(os.path.dirname(__file__))
        yaml_path = yaml_path + '/yilou_zuke_config/' + yaml_ming
        #logging.info(yaml_path)

        try:
            if name!=None:
                logging.info('name is %s'%name)
        except :
            print('name is not Null')
        else:
            with open(yaml_path,'r',encoding='utf-8') as stream:
                shuju_name=yaml.load(stream)
                shuju=shuju_name[name]
                #logging.info(shuju)
                stream.close()
            return shuju

    def write_yaml(self,yaml_name,yaml_zhi,yaml_ming):
        '''
        写入yaml
        :param yaml_name: 子类名
        :param yaml_zhi: 子类值
        :param yaml_ming: 写入文件名
        :return: 
        '''
        yaml_path=os.path.dirname(os.path.dirname(__file__))
        yaml_path=yaml_path+'/yilou_zuke_config//'+yaml_ming
        logging.info(yaml_path)
        C=open(yaml_path,'r',encoding='utf-8')
        shuju_name=yaml.load(C)#获取yaml父类值

        with open(yaml_path,'w',encoding='utf-8') as F:
            shuju_name[yaml_name]=yaml_zhi#写入值
            yaml.dump(shuju_name,F)
            logging.info('write %s is %s'%(yaml_zhi,yaml_name))
if __name__ == '__main__':
    data_peizhi=Read_Yaml_Config()
    data=data_peizhi.get_peizhi(name='Login',yaml_ming='yilou_zufang.yaml')
    print(data)