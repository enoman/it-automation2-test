# Copyright 2022 NEC Corporation#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from flask import g
import os
"""
  Ansible共通モジュール
"""


def getMovementAnsibleCnfUploadDirPath():
    """
      Movement一覧 ansible.cfgファイル FileUploadColumnディレクトリバスを取得する。
      基本コンソールのMovement一覧の項目に対応したディレクトリにファイルが収まっている
      Arguments:
        なし
      Returns:
         Movement一覧 ansible.cfgファイル ディレクトリバスを取得
    """
    return "{}{}/{}/uploadfiles/10202/Ansible_cfg".format(os.environ["PYTHONPATH"], g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))



def getRolePackageContentUploadDirPath():
    """
      ロールパッケージ管理FileUploadColumnディレクトリバスを取得する。
      Arguments:
        なし
      Returns:
        ロールパッケージ管理FileUploadColumnディレクトリバス
    """
    return "{}{}/{}/uploadfiles/20404/zip_format_role_package_file".format(os.environ["PYTHONPATH"], g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))

def getFileContentUploadDirPath():
    """
      ファイル管理FileUploadColumnディレクトリバスを取得する。
      Arguments:
        なし
      Returns:
        ファイル管理FileUploadColumnディレクトリバスを取得
    """
    return "{}{}/{}/uploadfiles/20105/files".format(os.environ["PYTHONPATH"], g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))

def getTemplateContentUploadDirPath():
    """
      テンプレート管理FileUploadColumnディレクトリバスを取得する。
      Arguments:
        なし
      Returns:
        テンプレート管理FileUploadColumnディレクトリバス
    """
    return "{}{}/{}/uploadfiles/20106/template_files".format(os.environ["PYTHONPATH"], g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))

def getDeviceListSSHPrivateKeyUploadDirPath():
    """
      機器一覧ssh秘密鍵ファイルディレクトリバスを取得する。
      Arguments:
        なし
      Returns:
        機器一覧ssh秘密鍵ファイルディレクトリバスを取得
    """
    return "{}{}/{}/uploadfiles/20101/ssh_private_key_file".format(os.environ["PYTHONPATH"], g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))

def getDeviceListServerCertificateUploadDirPath():
    """
      機器一覧サーバー証明書ディレクトリバスを取得する。
      Arguments:
        なし
      Returns:
        機器一覧サーバー証明書ディレクトリバスを取得
    """
    return "{}{}/{}/uploadfiles/20101/server_certificate".format(os.environ["PYTHONPATH"], g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))

def getAnsibleIFSSHPrivateKeyUploadDirPath():
    """
      Ansibleインターフェースssh秘密鍵ファイルディレクトリバスを取得する。
      Arguments:
        なし
      Returns:
        Ansibleインターフェースssh秘密鍵ファイルディレクトリバス
    """
    return "{}{}/{}/uploadfiles/20102/ssh_private_key_file".format(os.environ["PYTHONPATH"], g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))

def getAACListSSHPrivateKeyUploadDirPath():
    """
      AACホスト一覧ssh秘密鍵ファイルディレクトリバスを取得する。
      Arguments:
        なし
      Returns:
        AACホスト一覧ssh秘密鍵ファイルディレクトリバス
    """
    return "{}{}/{}/uploadfiles/20103/ssh_private_key_file".format(os.environ["PYTHONPATH"], g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))

def getLegayRoleExecutPopulatedDataUploadDirPath():
    """
      作業管理投入データディレクトリバスを取得する。
      Arguments:
        なし
      Returns:
        作業管理投入データディレクトリバス
    """
    return "{}{}/{}/uploadfiles/20414/populated_data".format(os.environ["PYTHONPATH"], g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))

def getLegayRoleExecutResultDataUploadDirPath():
    """
      作業管理結果データディレクトリバスを取得する。
      Arguments:
        なし
      Returns:
        作業管理結果データディレクトリバス
    """
    return "{}{}/{}/uploadfiles/20414/result_data".format(os.environ["PYTHONPATH"], g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))

def to_str(bstr):
    """
      byte型をstr型に変換
      Arguments:
        bstr: byte型
      Returns:
        str型に変換したデータ
    """
    if isinstance(bstr, bytes):
        toStr = bstr.decode('utf-8')
    else:
        toStr = bstr
    return toStr
  
  
def get_AnsibleDriverTmpPath():
    """
      Ansible用tmpバスを取得する。
      Arguments:
        なし
      Returns:
        Ansible用tmpバス
    """
    return getDataRelayStorageDir() + "/tmp/driver/ansible"
  
  
def getFileupLoadColumnPath(menuid, Column):
    """
      FileUploadColumnのパスを取得する。
      Arguments:
        menuid: メニューID
        Column: カラム名
      Returns:
        Ansible用tmpバス
    """
    return getDataRelayStorageDir() + "/uploadfiles/{}/{}".format(menuid, Column)


def get_AnsibleDriverShellPath():
    """
      Ansible用shell格納バスを取得する。
      Arguments:
        なし
      Returns:
        Ansible用shell格納バス
    """
    return "{}common_libs/ansible_driver/shells".format(os.environ["PYTHONPATH"])
 

def getDataRelayStorageDir():
    return "/{}/{}/{}".format("storage", g.get('ORGANIZATION_ID'), g.get('WORKSPACE_ID'))
  

def getInputDataTempDir(EcecuteNo, DriverName):
    """
      Ansible Gitリポジトリ用 tmpバスを取得する。
      Arguments:
        EcecuteNo: 作業番号
        DriverName: オケストレータID  vg_tower_driver_name
      Returns:
        Ansible Gitリポジトリ用 tmpバス
    """
    ary = {}
    basePath = get_AnsibleDriverTmpPath()
    ary["BASE_DIR"] = basePath
    tgtPath = basePath + "/{}_{}".format(DriverName, EcecuteNo)
    ary["DIR_NAME"] = tgtPath
    return ary
